# -*- coding: utf-8 -*-
# 注意，先要启动本地的MongoDB服务器

from pymongo import MongoClient

class TestMongo():

    # 初始化时自动创建连接
    def __init__(self):

        # 创建MongoDB客户端
        client = MongoClient(host='127.0.0.1', port=27017)
        # 使用方括号选择test数据库里面的t251集合
        self.collection = client["test"]["t251"]
        # 也可以使用.的方式
        # self.collection = client.test.t251

# 实例化
test_mongo = TestMongo()
