# -*- coding: utf-8 -*-
import redis

# 创建连接和操作对象
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, encoding='utf-8')
r = redis.Redis(connection_pool=pool)

# 获取字符串，起始结束为字节位置
r.set('name', 'qiye安全博客')
print(r.getrange('name', 4, 9))

# 从指定字符串开始向后修改字符串的内容
r.setrange('name', 1, 'pyt')
print(r.get('name'))
bytes1 = r.get('name')

# 上面输出结果是16进制的汉字编码（属于python的byte类型）
# 下面可以采用两种方式转换可以正常显示的中文字符
# 下面转码过程，必须原编码是汉字转换过来的才行

# bytes1 = b'qpyt\xe5\xae\x89\xe5\x85\xa8\xe5\x8d\x9a\xe5\xae\xa2'

# 方法1：
str1 = str(bytes1, encoding='utf-8')
print(str1)

# 方法2：
str2 = bytes.decode(bytes1)
print(str2)
