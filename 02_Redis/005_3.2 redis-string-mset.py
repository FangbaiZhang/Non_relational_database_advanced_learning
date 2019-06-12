# -*- coding: utf-8 -*-
# 一次存入多个键值,以字典的方式存入

import redis

# 创建连接和操作对象
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# 创建一个字典
keydict = {'age': 20, 'country': 'china'}
# 设置多个键值
r.mset(keydict)

# 取出多个键对应的值，使用list列表或者直接写出多个键
list = ['age', 'country']

# 取出的结果是一个列表
print(r.mget(list))
print(r.mget('age', 'country'))