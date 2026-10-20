# 图书情报检索与统计平台实训项目

## 项目信息
* **课程名称**：《NoSQL数据库技术与应用》
* **班级**：[24数科1班]
* **学号**：[202414870113]
* **姓名**：[于炳阳]

## 项目结构
* `mongodb_connect.py`：数据库连接模块
* `book_manager.py`：图书信息管理模块
* `reader_manager.py`：读者信息管理模块
* `borrow_manager.py`：借阅流水管理模块
* `stat_manager.py`：统计分析模块
* `main.py`：菜单式主程序入口
* `data/`：数据文件目录（包含 books.txt, readers.txt, borrow_logs.txt 以及 Compass 导出的 JSON 文件）

## 运行环境与说明
* **数据库**：MongoDB 8.0.32（部署于 CentOS Stream 9，已开启权限认证）
* **开发环境**：Python 3.9+ / PyMongo
* **运行方式**：直接在终端运行 `python main.py`，根据菜单提示输入数字进行操作。
* **注意**：运行代码前，请确保 `mongodb_connect.py` 中的连接字符串（虚拟机 IP、账号、密码）配置正确。