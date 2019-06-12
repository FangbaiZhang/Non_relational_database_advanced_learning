# -*- coding: utf-8 -*-
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# 设置键，属性和值
r.hset('student', 'name', 'qiye')
print(r.hget('student', 'name'))

# 设置键，多个属性和对应的值
r.hmset('student', {'name': 'qiye', 'age': 20})
print(r.hmget('student', 'name', 'age'))
