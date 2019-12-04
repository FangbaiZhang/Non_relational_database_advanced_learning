# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/4 16:54
Desc:
'''

import time
import redis

class RedisLock:
    def __init__(self):
        self.conn = redis.Redis(host='127.0.0.1', port=6379, db=0)
        self._lock = 0
        self.lock_key = ""
    @staticmethod
    def my_float(timestamp):
        """
        Args:
            timestamp:
        Returns:
            float或者0
            如果取出的是None，说明原本锁并没人用，getset已经写入，返回0，可以继续操作。
        """
        if timestamp:
            return float(timestamp)
        else:
            #防止取出的值为None，转换float报错
            return 0

    @staticmethod
    def get_lock(cls, key, timeout=10):
        cls.lock_key = f"{key}_dynamic_lock"
        while cls._lock != 1:
            timestamp = time.time() + timeout + 1
            cls._lock = cls.conn.setnx(cls.lock_key, timestamp)
            # if 条件中，可能在运行到or之后被释放，也可能在and之后被释放
            # 将导致 get到一个None，float失败。
            if cls._lock == 1 or (
                            time.time() > cls.my_float(cls.conn.get(cls.lock_key)) and
                            time.time() > cls.my_float(cls.conn.getset(cls.lock_key, timestamp))):
                break
            else:
                time.sleep(0.3)

    @staticmethod
    def release(cls):
        if cls.conn.get(cls.lock_key) and time.time() < cls.conn.get(cls.lock_key):
            cls.conn.delete(cls.lock_key)


def redis_lock_deco(cls):
    def _deco(func):
        def __deco(*args, **kwargs):
            cls.get_lock(cls, args[1])
            try:
                return func(*args, **kwargs)
            finally:
                cls.release(cls)
        return __deco
    return _deco


@redis_lock_deco(RedisLock())
def my_func():
    print("myfunc() called.")
    time.sleep(20)

if __name__ == "__main__":
    my_func()