from pymongo import MongoClient

# 连接 MongoDB 数据库的公共模块
def get_db():
    # 使用读写账号连接，authSource=admin 指定认证库
    uri = "mongodb://libWriter:Writer123@localhost:27017/library?authSource=admin"
    client = MongoClient(uri)
    # 返回 library 数据库对象
    return client["library"]

if __name__ == "__main__":
    # 本地测试连接是否成功
    try:
        db = get_db()
        db.command("ping")
        print("[成功] 成功连接到 MongoDB 数据库！")
    except Exception as e:
        print("[错误] 连接失败，错误信息：", e)