# 导入各个功能模块
from book_manager import top_books, search_book, add_book, update_stock, delete_book
from reader_manager import list_readers, count_by_college, level_distribution
from borrow_manager import borrow_book, return_book, query_overdue
from stat_manager import category_stats, borrow_trend, best_sellers
from mongodb_connect import get_db

# 打印主菜单
def show_menu():
    print("\n" + "="*30)
    print(" 图书情报检索与统计平台")
    print("="*30)
    print("1. 图书评分排行")
    print("2. 模糊查询图书")
    print("3. 新增图书")
    print("4. 修改图书库存")
    print("5. 删除图书")
    print("6. 查看读者列表")
    print("7. 统计各学院人数")
    print("8. 统计读者等级分布")
    print("9. 借阅登记")
    print("10. 归还处理")
    print("11. 查询逾期记录")
    print("12. 分类统计报表")
    print("13. 借阅趋势分析")
    print("14. 畅销榜前 5 名")
    print("0. 退出系统")
    print("="*30)

# 主程序入口
def main():
    # 启动时尝试连接数据库并打印集合文档数量
    try:
        db = get_db()
        print("[信息] 成功连接到数据库")
        print(f"[信息] 当前 books 集合文档数: {db['books'].count_documents({})}")
        print(f"[信息] 当前 readers 集合文档数: {db['readers'].count_documents({})}")
        print(f"[信息] 当前 borrow_logs 集合文档数: {db['borrow_logs'].count_documents({})}")
    except Exception as e:
        print("[错误] 数据库连接失败，请检查 MongoDB 服务。")
        return

    # 无限循环，直到用户选择 0 退出
    while True:
        show_menu()
        choice = input("请选择功能编号: ")
        
        # 根据用户输入的编号调用对应的函数
        if choice == "1": top_books()
        elif choice == "2": search_book()
        elif choice == "3": add_book()
        elif choice == "4": update_stock()
        elif choice == "5": delete_book()
        elif choice == "6": list_readers()
        elif choice == "7": count_by_college()
        elif choice == "8": level_distribution()
        elif choice == "9": borrow_book()
        elif choice == "10": return_book()
        elif choice == "11": query_overdue()
        elif choice == "12": category_stats()
        elif choice == "13": borrow_trend()
        elif choice == "14": best_sellers()
        elif choice == "0":
            print("已退出系统。")
            break
        else:
            print("[提示] 输入无效，请重新选择。")

if __name__ == "__main__":
    main()