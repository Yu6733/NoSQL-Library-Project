from mongodb_connect import get_db

db = get_db()
readers = db["readers"]

# 1. 查看所有读者基本信息
def list_readers():
    print("\n--- 读者列表 ---")
    result = readers.find({}, {"_id": 0, "name": 1, "college": 1})
    for r in result:
        print(f"姓名: {r.get('name')} | 学院: {r.get('college')}")

# 2. 按学院统计读者人数（聚合分组）
def count_by_college():
    print("\n--- 各学院读者人数统计 ---")
    # 聚合管道：先按学院分组，再按人数降序
    pipeline = [
        {"$group": {"_id": "$college", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    result = readers.aggregate(pipeline)
    for r in result:
        print(f"学院: {r.get('_id')} | 人数: {r.get('count')}")

# 3. 读者等级分布（distinct 去重 + 计数）
def level_distribution():
    print("\n--- 读者等级分布 ---")
    # 先用 distinct 找出所有不重复的等级
    levels = readers.distinct("level")
    for lv in levels:
        # 逐个统计各等级人数
        c = readers.count_documents({"level": lv})
        print(f"等级: {lv} | 人数: {c}")