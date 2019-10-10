# -*- coding: utf-8 -*-
import pymongo

# 第一步：建立数据库连接
# 先启动本地数据库服务
# 注意，脚本不能命名为pymongo.py，不然会报错找不到MongoClient属性
# 连接本地的MongoDB服务器默认端口127.0.0.1:27017
client = pymongo.MongoClient()
# 可以指定端口
# client = pymongo.MongoClient(host='localhost', port=27017)
# client = pymongo.MongoClient(host='127.0.0.1', port=27017)


# 第二步：获取数据库和集合
# 获取数据库,没有就直接创建
db = client.papers
# 获取一个集合
collection = db.books

# 获取集合可以使用句点法，也可以使用中括号
# collection = client.papers.books
# collection = client["papers"]["books"]

# 第三步：操作数据库
# 插入文档
# 注意，代码每运行一次，就像数据库中插入一次文档，所以，下面查询文档，结果会越来越多
book = {"author": "Mike",
        "text": "My first book!",
        "tags": ["爬虫", "python", "网络"]
        }
book_id = collection.insert(book)
# 查询文档
book_result = collection.find_one({"author": "Mike"})
print(book_result)

# 查看所有符合条件的文档数量
print(collection.find({"author": "Mike"}).count())


# 查询所有符合条件的文档
book_results = collection.find({"author": "Mike"})
for result in book_results:
        print(result)

# 前面插入了文档，该处删除文档，最后books还是为空
# 删除所有符合条件的文档
collection.delete_many({"author": "Mike"})


