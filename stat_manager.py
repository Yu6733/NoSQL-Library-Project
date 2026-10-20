from mongodb_connect import get_db

db = get_db()
books = db["books"]
borrows = db["borrow_logs"]

# 1. 分类统计报表（按类别分组，求和与平均值）
def category_stats():
    print("\n--- 分类统计报表 ---")
    # 按 category 分组，计算库存总和($sum)、价格平均($avg)、图书数量
    pipeline = [
        {"$group": {
            "_id": "$category",
            "total_stock": {"$sum": "$stock"},
            "avg_price": {"$avg": "$price"},
            "book_count": {"$sum": 1}
        }},
        {"$sort": {"total_stock": -1}}
    ]
    result = books.aggregate(pipeline)
    for r in result:
        print(f"类别: {r.get('_id')} | 库存总量: {r.get('total_stock')} | 平均价格: {round(r.get('avg_price'), 2)} | 图书数: {r.get('book_count')}")

# 2. 借阅趋势分析（按年份格式化日期并分组）
def borrow_trend():
    print("\n--- 借阅趋势分析 (按年份) ---")
    # 使用 $dateToString 将 borrow_date 格式化为 "%Y年"
    pipeline = [
        {"$group": {
            "_id": {"$dateToString": {"format": "%Y年", "date": "$borrow_date"}},
            "count": {"$sum": 1}
        }},
        {"$sort": {"_id": 1}}
    ]
    result = borrows.aggregate(pipeline)
    for r in result:
        print(f"时间: {r.get('_id')} | 借阅量: {r.get('count')}")

# 3. 畅销榜（按 borrow_count 借阅次数排序）
def best_sellers():
    print("\n--- 畅销榜前 5 名 ---")
    # 按借阅次数降序，取前5，只显示书名和次数
    pipeline = [
        {"$sort": {"borrow_count": -1}},
        {"$limit": 5},
        {"$project": {"_id": 0, "title": 1, "borrow_count": 1}}
    ]
    result = books.aggregate(pipeline)
    for r in result:
        print(f"书名: {r.get('title')} | 借阅次数: {r.get('borrow_count')}")