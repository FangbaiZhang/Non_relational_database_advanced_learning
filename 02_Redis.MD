# Non_relational_database_advanced_learning
# 非关系型数据进阶系统学习

# Redis

Redis教程：
- 中文教程：https://www.redis.net.cn/tutorial/3501.html
- 菜鸟网：https://www.runoob.com/redis/redis-tutorial.html
- Redis中文网：http://redis.cn/


- 第一部分：Redis简介及安装
- 第二部分：MongoDB常用操作
- 第三部分：MongoDB高级操作
- 第四部分：MongoDB与Python交互



# 第一部分：Redis简介及安装

# 1. Redis简介
- NoSQL：一类新出现的数据库(not only sql)，它的特点：
    不支持SQL语法
    存储结构跟传统关系型数据库中的那种关系表完全不同，nosql中存储的数据都是KV形式
    NoSQL的世界中没有一种通用的语言，每种nosql数据库都有自己的api和语法，以及擅长的业务场景
    NoSQL中的产品种类相当多：
        Mongodb
        Redis
        Hbase hadoop
        Cassandra hadoop

- NoSQL和SQL数据库的比较：
    适用场景不同：sql数据库适合用于关系特别复杂的数据查询场景，nosql反之
    “事务”特性的支持：sql对事务的支持非常完善，而nosql基本不支持事务
    两者在不断地取长补短，呈现融合趋势

- Redis简介
    Redis是一个开源的使用ANSI C语言编写、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。
    Redis是 NoSQL技术阵营中的一员，它通过多种键值数据类型来适应不同场景下的存储需求，借助一些高层级的接口使用其可以胜任，
    如缓存、队列系统的不同角色

- Redis特性
    Redis 与其他 key - value 缓存产品有以下三个特点：
    Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
    Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
    Redis支持数据的备份，即master-slave模式的数据备份。

- Redis 优势
    性能极高 – Redis能读的速度是110000次/s,写的速度是81000次/s 。
    丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。
    原子 – Redis的所有操作都是原子性的，同时Redis还支持对几个操作全并后的原子性执行。
    丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。

- redis应用场景
    用来做缓存(ehcache/memcached)——redis的所有数据是放在内存中的（内存数据库）
    可以在某些特定应用场景下替代传统数据库——比如社交类的应用
    在一些大型系统中，巧妙地实现一些特定的功能：session共享、购物车
    只要你有丰富的想象力，redis可以用在可以给你无限的惊喜…….

# 2. Redis安装
- 参考：https://blog.csdn.net/u011318077/article/details/88796262
        https://www.runoob.com/redis/redis-install.html
- 安装步骤：
    - 下载软件，解压到安装目录即可
    - 软件安装文件夹添加到环境变量
    - CMD启动服务器和客户端
    
# 3. Redis配置

Redis 的配置文件位于 Redis 安装目录下，文件名为 redis.conf(Windows 名为 redis.windows.conf)。
你可以通过 CONFIG 命令查看或设置配置项。

# 配置说明及设置参考网址：
https://www.runoob.com/redis/redis-conf.html
https://blog.csdn.net/ljphilp/article/details/52934933


- redis 127.0.0.1:6379> CONFIG GET loglevel
使用 * 号获取所有配置项：
- redis 127.0.0.1:6379> CONFIG GET *

# 4. Redis数据类型
- Redis支持五种数据类型：
    string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。

