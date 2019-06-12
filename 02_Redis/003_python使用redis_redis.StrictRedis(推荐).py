# -*- coding: utf-8 -*-

import redis

# 使用redis.StrictRedis类操作redis数据库
# 使用命令与redis客户端的命令一致

def python_redis():
    # 创建一个StrictRedis对象，连接操作redis数据库
    # 创建连接池管理redis连接，可以避免每次建立和释放连接的开销
    # 指定主机和端口建立redis连接,默认使用的0数据库，可以不写
    try:
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
        sr = redis.StrictRedis(connection_pool=pool)
        # 添加一个键值对，输出返回结果，添加成功True，添加失败False
        res = sr.set('name', 'python')
        print(res)
        # 取出键的值,如果不存在，返回None
        res = sr.get('name')
        print(res)
        # 修改键的值,键存在就直接修改其值
        res = sr.set('name', 'php')
        print(res)
        # 再次取出键的值
        res = sr.get('name')
        print(res)
        # 删除键值，成功则返回删除的个数，否则返回0
        res = sr.delete('name')
        print(res)
        # 获取所有的键,输出结果是一个所有键的列表，否则返回空lieb
        res = sr.keys()
        print(res)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    python_redis()
