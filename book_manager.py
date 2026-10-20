from mongodb_connect import get_db

db = get_db()
books = db["books"]

# 1. 图书评分排行（降序取前 5）
def top_books():
    print("\n--- 评分前 5 的图书 ---")
    # 投影仅输出书名和评分，按评分降序，取前5
    result = books.find({}, {"_id": 0, "title": 1, "rating": 1}).sort("rating", -1).limit(5)
    for b in result:
        print(f"书名: {b.get('title')} | 评分: {b.get('rating')}")

# 2. 模糊查询（正则表达式匹配书名）
def search_book():
    keyword = input("请输入书名关键词: ")
    print(f"\n--- 包含 '{keyword}' 的图书 ---")
    # $regex 正则匹配，$options: "i" 忽略大小写
    result = books.find({"title": {"$regex": keyword, "$options": "i"}}, {"_id": 0, "title": 1, "price": 1})
    count = 0
    for b in result:
        print(f"书名: {b.get('title')} | 价格: {b.get('price')}")
        count += 1
    if count == 0:
        print("[提示] 未找到相关图书。")

# 3. 新增图书（输入各项基本信息）
def add_book():
    isbn = input("请输入 ISBN: ")
    title = input("请输入书名: ")
    author = input("请输入作者: ")
    publisher = input("请输入出版社: ")
    category = input("请输入类别 (如 计算机/文学): ")
    price = float(input("请输入价格: "))
    stock = int(input("请输入库存: "))
    rating = float(input("请输入评分 (0-5): "))
    
    # 组装文档结构
    doc = {
        "isbn": isbn, "title": title, "author": author,
        "publisher": publisher, "category": category,
        "price": price, "stock": stock, "rating": rating,
        "tags": [], "publish_date": None, "borrow_count": 0
    }
    # 插入单条文档
    res = books.insert_one(doc)
    print(f"[成功] 成功新增 1 本图书。")

# 4. 修改库存（$inc 实现数值增减）
def update_stock():
    isbn = input("请输入要修改库存的图书 ISBN: ")
    num = int(input("请输入库存变动值 (减少输入负数，如 -5): "))
    # 使用 $inc 操作符对 stock 字段进行数学加减
    res = books.update_one({"isbn": isbn}, {"$inc": {"stock": num}})
    print(f"[成功] 成功修改 {res.modified_count} 本图书的库存。")

# 5. 删除图书（根据 ISBN 删除单条）
def delete_book():
    isbn = input("请输入要删除的图书 ISBN: ")
    res = books.delete_one({"isbn": isbn})
    if res.deleted_count > 0:
        print(f"[成功] 成功删除 1 本图书。")
    else:
        print("[提示] 未找到该 ISBN 的图书。")