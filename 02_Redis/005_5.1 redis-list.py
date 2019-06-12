# -*- coding: utf-8 -*-
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# 向值列表中添加元素，每个新元素添加在最左边，一直向左边添加元素
# 向右边添加元素使用rpush
r.lpush('digit', 11, 22, 33)
