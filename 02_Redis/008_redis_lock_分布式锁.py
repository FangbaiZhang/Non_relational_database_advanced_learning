# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/4 20:58
Desc:
'''
import redis
import uuid
import time

class RedisLock():

    def __init__(self, lock_name, time_out, acquire_time):
        # 连接redis数据库
        self.redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        self.lock_name = lock_name   # 锁的名称(锁的唯一ID)
        self.time_out = time_out  # 锁的超时时间(超过时间，自动释放锁)
        self.acquire_time = acquire_time  # 获取锁的时间(超过时间，放弃获取锁)

    def acquire_lock(self):
        '''获取一个分布式锁'''
        # 生成一个唯一的uuid值作为锁(键)的值(补充：UUID，Universally Unique Identifier，翻译为中文是通用唯一识别码，UUID 的目的是让分布式系统中的所有元素都能有唯一的识别信息)
        identifier = str(uuid.uuid4())
        end = time.time() + self.acquire_time
        lock = 'string:lock:' + self.lock_name
        while time.time() < end:
            # 设置一个锁，设置锁的名称和唯一的UUID值
            if self.redis_client.setnx(lock, identifier):
                # 给锁设置超时时间，防止进程崩溃导致其它进程无法获取锁
                self.redis_client.expire(lock, self.time_out)
                return identifier
            elif not self.redis_client.ttl(lock): # ttl获取锁的生存时间
                self.redis_client.expire(lock, self.time_out)
            time.sleep(0.001)
        return False

    def release_lock(self, identifier):
        """通用的锁释放函数"""
        lock = "string:lock:" + self.lock_name
        pip = self.redis_client.pipeline(True)
        while True:
            try:
                pip.watch(lock)
                # 获取锁的值，即设置锁时的UUID值
                lock_value = self.redis_client.get(lock)
                if not lock_value:
                    return True

                if lock_value.decode() == identifier:
                    pip.multi()
                    pip.delete(lock)
                    pip.execute()
                    return True
                pip.unwatch()
                break
            except redis.exceptions.WatchError:
                pass
        return False


if __name__ == '__main__':
    redis_lock = RedisLock(lock_name='lock001', time_out=10, acquire_time=10)