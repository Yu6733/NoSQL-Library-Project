from mongodb_connect import get_db
from datetime import datetime

db = get_db()
borrows = db["borrow_logs"]

# 1. 借阅登记（新增一条借阅流水记录）
def borrow_book():
    card = input("请输入读者证号 (如 R20240001): ")
    isbn = input("请输入图书 ISBN: ")
    
    # 组装借阅记录，自动获取当前时间作为借阅时间
    doc = {
        "borrow_date": datetime.now(),
        "reader_card": card,
        "book_isbn": isbn,
        "status": "借出"
    }
    res = borrows.insert_one(doc)
    print(f"[成功] 借阅成功，记录 ID: {res.inserted_id}")

# 2. 归还处理（更新状态并记录归还时间）
def return_book():
    card = input("请输入读者证号: ")
    isbn = input("请输入图书 ISBN: ")
    
    # 找到该读者借出这本书且状态为“借出”的记录，将其改为“已归还”
    res = borrows.update_one(
        {"reader_card": card, "book_isbn": isbn, "status": "借出"},
        {"$set": {"status": "已归还", "return_date": datetime.now()}}
    )
    if res.modified_count > 0:
        print("[成功] 归还成功。")
    else:
        print("[提示] 未找到该读者借出此书的未归还记录。")

# 3. 查询逾期记录（筛选 status 为“逾期”的数据）
def query_overdue():
    print("\n--- 逾期记录 ---")
    result = borrows.find({"status": "逾期"})
    count = 0
    for r in result:
        print(f"读者: {r.get('reader_card')} | 图书: {r.get('book_isbn')} | 状态: {r.get('status')}")
        count += 1
    if count == 0:
        print("[提示] 暂无逾期记录。")