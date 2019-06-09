# -*- coding: utf-8 -*-

from pymongo import MongoClient

class TestMongo:
    def __init__(self):
        # 初始化时自动创建连接
        client = MongoClient()
        # 使用方括号选择数据库及其集合
        self.collection = client["test"]["t251"]
        # 也可以使用.的方式
        # self.collection = client.test.t251


test_mongo = TestMongo()
