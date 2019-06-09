# -*- coding: utf-8 -*-

from pymongo import MongoClient


# 第一步：创建连接
client = MongoClient()
# 使用方括号选择数据库及其集合
collection = client["test"]["t251"]
# 也可以使用.的方式
# collection = client.test.t251

# 第二步：插入数据（插入一次就注释掉，不然再次运行由于已经存在相同_id，会出现报错）
# data_list = [{"_id":i, "name":"py{}".format(i)} for i in range(1000)]
# collection.insert(data_list)

# 第三步:查询数据
ret = collection.find()
data_list = list(ret)
# 挑选出100整数倍的数据,每个i都是字典
data_list_100 = [ i for i in data_list if i["_id"]%100==0 and i["_id"]!=0]
for i_100 in data_list_100:
    print(i_100)