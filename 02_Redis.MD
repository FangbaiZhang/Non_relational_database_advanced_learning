# Non_relational_database_advanced_learning
# 非关系型数据进阶系统学习

# Redis

Redis教程：
- 中文教程：https://www.redis.net.cn/tutorial/3501.html
- 菜鸟网：https://www.runoob.com/redis/redis-tutorial.html
- Redis中文网：http://redis.cn/

Redis命令：
- Redis官网全部命令：
    https://redis.io/commands
- Redis命令参考中文网：
    http://doc.redisfans.com/

- Redis使用参考：
    Python爬虫开发与项目实战PDF文件中的第16章 分布式爬虫与Scrapy
    Python爬虫开发与项目实战项目文件的ch16中的Python交互实例
    ch12中的sht爬虫项目采用的就是:ShtSpider(RedisSpider)(使用的redis爬取去重)
    ch17中的yunqshuyuan项目去重方式也是采用的redis去重


- 第一部分：Redis简介及安装
- 第二部分：Redis数据操作
- 第三部分：Redis与Python交互
- 第四部分：Redis主从与集群


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

- redis启动
    第一步：启动服务器
        先CMD启动redis-server
        默认使用的默认的配置文件conf，也可以自定义修改
    第二步：启动客户端
        再打开一个CMD窗口，输入redis-cli,启动Redis客户端
        注意：redis-cli默认启动本地客户端，
        远程连接redis-server：输入IP和port接口，下面的是本地接口，远程连接对应修改即可
        C:\Users\HP>redis-cli -h 127.0.0.1 -p 6379
        127.0.0.1:6379>
        修改IP和port接口可以连接远程服务器
        连接客户端后，使用ping命令测试，连接成功返回PONG：
        127.0.0.1:6379> ping
        PONG
    
# 3. Redis配置

Redis 的配置文件位于 Redis 安装目录下，文件名为 redis.conf(Windows 名为 redis.windows.conf)。
你可以通过 CONFIG 命令查看或设置配置项。

# 配置说明及设置参考网址：
https://www.runoob.com/redis/redis-conf.html
https://blog.csdn.net/ljphilp/article/details/52934933

- redis 127.0.0.1:6379> CONFIG GET loglevel
使用 * 号获取所有配置项：
- redis 127.0.0.1:6379> CONFIG GET *
- 数据库命令：
    - 默认连接的就是db0数据库
    - select 1    切换到db1数据库
    - key *       查看所有的redis键
    - type 键名   查看键的数据类型，每种类型的值操作方法不同，先查看类型然后进行对于操作
    - flushdb     清空当前的db数据库
    - flushall    清空所有的db数据库 （慎用，跑路才用）


# 4. Redis数据类型
- Redis支持五种数据类型：
    string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。

# 5. Redis默认数据库
Redis是一个字典结构的存储服务器，而实际上一个Redis实例提供了多个用来存储数据的字典，
客户端可以指定将数据存储在哪个字典中。这与我们熟知的在一个关系数据库实例中可以创建多个数据库类似，
所以可以将其中的每个字典都理解成一个独立的数据库。

每个数据库对外都是一个从0开始的递增数字命名，Redis默认支持16个数据库（可以通过配置文件支持更多，无上限），
可以通过配置databases来修改这一数字。客户端与Redis建立连接后会自动选择0号数据库，
不过可以随时使用SELECT命令更换数据库，如要选择1号数据库：select 1

查看数据库所有的key: keys *


# 第二部分：Redis数据操作

- Redis官网全部命令：
    https://redis.io/commands
- Redis命令参考中文网：
    http://doc.redisfans.com/
- 下面主要介绍一些常用数据操作命令


# 6. 键命令
- 查看所有键
    keys *

- 查看名字中包含a的键
    127.0.0.1:6379> keys a*
    1) "a2"
    2) "a1"
    3) "a3"
    
- 判断键是否存在，如果存在返回1，不存在返回0,如果键的值不存在则返回nil，类似MySQL的null
    exists key1
    判断键a1是否存在
    127.0.0.1:6379> exists a1
    (integer) 1
    127.0.0.1:6379> exists a1 a2
    (integer) 2
    127.0.0.1:6379>
    
- 查看键对应的value的类型
    type key
    查看键a1的值类型，为redis⽀持的五种类型中的⼀种
    127.0.0.1:6379> type a1
    string

- 删除键及对应的值
    del key1 key2 ...
    删除键a2、a3
    127.0.0.1:6379> del a2 a3
    (integer) 2
    127.0.0.1:6379> mget a1 a2 a3
    1) "pythonhaha"
    2) (nil)
    3) (nil)
    
- 设置过期时间，以秒为单位,如果没有指定过期时间则⼀直存在，直到使⽤DEL移除
    expire key seconds
    设置键'a1'的过期时间为20秒
    查看有效时间，以秒为单位           
    ttl key
    
    127.0.0.1:6379> set a1 python
    OK
    127.0.0.1:6379> get a1
    "python"
    127.0.0.1:6379> expire a1 20
    (integer) 1
    127.0.0.1:6379> get a1
    "python"
    127.0.0.1:6379> ttl a1
    (integer) 13
    127.0.0.1:6379> ttl a1
    (integer) 10
    127.0.0.1:6379> ttl a1
    (integer) 0
    127.0.0.1:6379> ttl a1
    (integer) -2
    127.0.0.1:6379> get a1
    (nil)

- 更多键命令参考：https://www.runoob.com/redis/redis-keys.html


# 7. string字符串

- 字符串类型是Redis中最为基础的数据存储类型，它在Redis中是二进制安全的，这便意味着该类型可以接受任何格式的数据，
- 如JPEG图像数据或Json对象描述信息等。在Redis中字符串类型的Value最多可以容纳的数据长度是512M。

- 如果设置的键不存在则为添加，如果设置的键已经存在则修改

- 设置单个键值
    set key value
    例1：
    127.0.0.1:6379> set name itcast
    OK
    127.0.0.1:6379> get name
    "itcast"
    
- 设置键的名称、过期时间、键的值，以秒为单位
    setex key seconds value
    例2：设置键为aa值为aa过期时间为3秒的数据
    127.0.0.1:6379> set aa 3 aa
    OK
    127.0.0.1:6379> get aa
    (nil)
    
- 设置多个键值
    mset key1 value1 key2 value2 ...
    例3：设置键为'a1'值为'python'、键为'a2'值为'java'、键为'a3'值为'c'
    127.0.0.1:6379> mset a1 python a2 java a3 c
    OK
    127.0.0.1:6379> get a1
    "python"
    127.0.0.1:6379> get a2
    "java"
    127.0.0.1:6379> get a3
    "c"
    
- 追加值,直接拼接在原字符串后面
    append key value
    例4：向键为a1中追加值' haha'
    127.0.0.1:6379> append a1 haha
    (integer) 10
    127.0.0.1:6379> get a1
    "pythonhaha"
    
- 获取：根据键获取值，如果不存在此键则返回nil
    get key
    根据多个键获取多个值
    mget key1 key2 ...
    
    127.0.0.1:6379> mget a1 a2 a3
    1) "pythonhaha"
    2) "java"
    3) "c"

- 更多字符串命令参考：https://www.runoob.com/redis/redis-strings.html


# 8. hash
- Redis hash 是一个string类型的field和value的映射表，hash特别适合用于存储对象。
- hash就类似于字典，一个人,对应很多属性，每个属性都有值
    Redis 中每个 hash 可以存储 232 - 1 键值对（40多亿）。
    hash⽤于存储对象(key)，对象的结构为属性(field)、值(value)
    值的类型为string 
    
    注意：scrapy的数据类型也是类似的，scrapy.Field()就是类似字典字典的数据，都是一个键对应一个值
    class JobBoleArticleItem(scrapy.Item):
        title = scrapy.Field()
        create_date = scrapy.Field()

- 设置获取单个属性
    hset key field value
    127.0.0.1:6379> hset user name felix
    (integer) 1
    127.0.0.1:6379> hget user name
    "felix"

- 设置获取多个属性
    hmset key field1 value1 field2 value2 ...
    设置键u2的属性name为xiaohong、属性age为11
    127.0.0.1:6379> hmset u2 name xiaohong age 11
    OK
    127.0.0.1:6379> hmget u2 name age
    1) "xiaohong"
    2) "11"

- 获取所有属性的值
    hvals key
    获取键'u2'所有属性的值
    127.0.0.1:6379> hvals u2
    1) "xiaohong"
    2) "11"
    
- 删除整个hash键及值，使⽤del命令
    删除属性，属性对应的值会被⼀起删除
    hdel key field1 field2 ...
    删除键'u2'的属性'age'
    127.0.0.1:6379> hdel u2 age
    (integer) 1
    127.0.0.1:6379> hvals u2
    1) "xiaohong"
    
- 更多哈希命令参考：https://www.runoob.com/redis/redis-hashes.html

# 9. list
- Redis列表是简单的字符串列表，按照插入顺序排序。
    你可以添加一个元素到列表的头部（左边）或者尾部（右边）
    一个列表最多可以包含 232 - 1 个元素 (4294967295, 每个列表超过40亿个元素)。
    列表的元素类型为string
    按照插⼊顺序排序
    
- 常用命令：
    - lpush mylist world    从mylist列表左侧添加一个值
    - lrange mylist         返回mylist列表中所有的值
    - llen mylist           返回mylist的长度

- 在左侧插⼊取出数据
    lpush key value1 value2 ...
    从键为'a1'的列表左侧分别加⼊数据a 、 b 、c，后面的数据在最左侧
    127.0.0.1:6379> lpush a1 a b c
    (integer) 3
    127.0.0.1:6379> lrange a1 0 10  
    1) "c"
    2) "b"
    3) "a"

- 在右侧插⼊数据
    rpush key value1 value2 ...
    从键为'a1'的列表右侧加⼊数据0 1 2
    127.0.0.1:6379> rpush a1 0 1 2
    (integer) 6
    取出索引为0-5的数据
    127.0.0.1:6379> lrange a1 0 5
    1) "c"
    2) "b"
    3) "a"
    4) "0"
    5) "1"
    6) "2"
    

- 在指定元素的前或后插⼊新元素
    linsert key before或after 现有元素 新元素        
    在键为'a1'的列表中元素'b'前加⼊'3'
    127.0.0.1:6379> linsert a1 before b 3
    (integer) 7
    127.0.0.1:6379> lrange a1 0 6
    1) "c"
    2) "3"
    3) "b"
    4) "a"
    5) "0"
    6) "1"
    7) "2"
    
- 返回列表⾥指定范围内的元素
    start、stop为元素的下标索引
    索引从左侧开始，第⼀个元素为0
    索引可以是负数，表示从尾部开始计数，如-1表示最后⼀个元素
    lrange key start stop

    获取键为'a1'的列表所有元素，取出a1键对应列表的所有元素
    127.0.0.1:6379> lrange a1 0 -1
    1) "c"
    2) "3"
    3) "b"
    4) "a"
    5) "0"
    6) "1"
    7) "2"
    
- 设置指定索引位置的元素值
    索引从左侧开始，第⼀个元素为0
    索引可以是负数，表示尾部开始计数，如-1表示最后⼀个元素
    
    修改键为'a1'的列表中下标为1的元素值为'z',下标为1的值本来是“3”
    127.0.0.1:6379> lset a1 1 z
    OK
    127.0.0.1:6379> lrange a1 0 -1
    1) "c"
    2) "z"
    3) "b"
    4) "a"
    5) "0"
    6) "1"
    7) "2"
    
- 删除指定元素
    将列表中前count次出现的值为value的元素移除
    count > 0: 从头往尾移除
    count < 0: 从尾往头移除
    count = 0: 移除所有

    lrem key count value

    向列表'a2'中加⼊元素'a'、'b'、'a'、'b'、'a'、'b'
    从'a2'列表右侧开始删除2个'b'，然后再次查看a2的所有元素
    127.0.0.1:6379> lpush a2 a b a b a b
    (integer) 6
    127.0.0.1:6379> lrange a2 0 -1
    1) "b"
    2) "a"
    3) "b"
    4) "a"
    5) "b"
    6) "a"
    127.0.0.1:6379> lrem a2 -2 b
    (integer) 2
    127.0.0.1:6379> lrange a2 0 -1
    1) "b"
    2) "a"
    3) "a"
    4) "a"
    
- 删除列表第一个元素
    lpos listname
    
    127.0.0.1:6379> lpop a2
    "b"
    127.0.0.1:6379> lrange a2 0 -1
    1) "a"
    2) "a"
    3) "a"

- 更多list命令参考：https://www.runoob.com/redis/redis-lists.html
    

# 10. set无序集合
- set特点
    ⽆序集合
    元素为string类型
    元素具有唯⼀性，不重复
    说明：对于集合没有修改操作
    
- set的特性是没有重复的元素，可以用于爬虫去重

- set常用命令：
    - sadd myset hello      往集合中添加数据
    - smembers myset        获取集合中所有的元素
    - scard myse            获取集合中元素的数量

- 添加获取元素
    sadd key member1 member2 ...
    向键'a3'的集合中添加元素'zhangsan'、'lisi'、'wangwu'
    返回所有的元素
    smembers key
    
    127.0.0.1:6379> sadd a3 zhangsan sili wangwu
    (integer) 3
    127.0.0.1:6379> smembers a3
    1) "wangwu"
    2) "zhangsan"
    3) "sili"
    
- 删除指定元素
    srem key member
    删除键'a3'的集合中元素'wangwu'
    
    127.0.0.1:6379> srem a3 wangwu
    (integer) 1
    127.0.0.1:6379> smembers a3
    1) "zhangsan"
    2) "sili"

- 更多set命令参考：https://www.runoob.com/redis/redis-sets.html
    
# 11. zset有序集合
- zset特点
    sorted set，有序集合
    元素为string类型
    元素具有唯⼀性，不重复
    每个元素都会关联⼀个double类型的score，表示权重，通过权重将元素从⼩到⼤排序
    说明：没有修改操作
    
- 常用命令：
    - zadd myzset 1 one   添加元素one,权重是1
    - zrange myzset 0 -1  返回有序集合所有的值，按顺序返回
    - zcard myzest        返回有序集合中元素的数量
    - zrange myzset 0 -1 withscores    返回有序集合所有的值即权重值，按顺序返回

- 添加元素
    zadd key score1 member1 score2 member2 ...
    向键'a4'的集合中添加元素'lisi'、'wangwu'、'zhaoliu'、'zhangsan'，权重分别为4、5、6、3
    127.0.0.1:6379> zadd a4 4 lisi 5 wangwu 6 zhaoliu 3 zhangsan
    (integer) 4
    
- 获取
    返回指定范围内的元素
    start、stop为元素的下标索引
    索引从左侧开始，第⼀个元素为0
    索引可以是负数，表示从尾部开始计数，如-1表示最后⼀个元素
    zrange key start stop
    
    返回score值在min和max之间的成员，指定返回一个权重范围的值
    zrangebyscore key min max
    
    返回成员xxx的score值,即成员的权重值
    zscore key xxx
    
    127.0.0.1:6379> zrange a4 0 -1
    1) "zhangsan"
    2) "lisi"
    3) "wangwu"
    4) "zhaoliu"
    127.0.0.1:6379> zrangebyscore a4 4 6
    1) "lisi"
    2) "wangwu"
    3) "zhaoliu"
    127.0.0.1:6379> zscore a4 zhaoliu
    "6"

- 删除指定元素
    zrem key member1 member2 ...
    
    删除权重在指定范围的元素
    zremrangebyscore key min max

    删除集合'a4'中元素'zhangsan'
    删除集合'a4'中权限在5、6之间的元素
    
    127.0.0.1:6379> zrem a4 zhangsan
    (integer) 1
    127.0.0.1:6379> zremrangebyscore a4 5 6
    (integer) 2
    127.0.0.1:6379> zrange a4 0 -1
    1) "lisi"

- 更多zset命令参考：https://www.runoob.com/redis/redis-sorted-sets.html


# 第三部分：Redis与Python交互
- 参考02_Redis文件中的003-005python实例


# 第四部分：Redis主从与集群

# 12. 主从及集群概念
- 主从概念
    ⼀个master可以拥有多个slave，⼀个slave⼜可以拥有多个slave，如此下去，
    形成了强⼤的多级服务器集群架构
    master用来写数据，slave用来读数据，经统计：网站的读写比率是10:1

    通过主从配置可以实现读写分离
    master和slave都是一个redis实例(redis服务)
    
    读写分离，负载均衡，数据备份
    
- 集群概念

- 为什么要有集群
    之前我们已经讲了主从的概念，一主可以多从，如果同时的访问量过大(1000w),
    主服务肯定就会挂掉，数据服务就挂掉了或者发生自然灾难
    大公司都会有很多的服务器(华东地区、华南地区、华中地区、华北地区等地区机房)

    集群是一组相互独立的、通过高速网络互联的计算机，它们构成了一个组，并以单一系统的模式加以管理。
    一个客户与集群相互作用时，集群像是一个独立的服务器。集群配置是用于提高可用性和可缩放性。
    当请求到来首先由负载均衡服务器处理，把请求转发到另外的一台服务器上。

- 集群分类
    软件层面
    硬件层面
    软件层面：只有一台电脑，在这一台电脑上启动了多个redis服务
    硬件层面：存在多台实体的电脑，每台电脑上都启动了一个redis或者多个redis服务
    
- 集群在哪个服务器上写数据：CRC16

    redis cluster在设计的时候，就考虑到了去中⼼化，去中间件，也就是说，
    集群中 的每个节点都是平等的关系，都是对等的，每个节点都保存各⾃的数据和整个集 群的状态。
    每个节点都和其他所有节点连接，⽽且这些连接保持活跃，
    这样就保 证了我们只需要连接集群中的任意⼀个节点，就可以获取到其他节点的数据
    
    Redis集群没有并使⽤传统的⼀致性哈希来分配数据，⽽是采⽤另外⼀种叫做哈希 槽 (hash slot)的⽅式来分配的。
    redis cluster 默认分配了 16384 个slot，当我们 set⼀个key 时，会⽤CRC16算法来取模得到所属的slot，
    然后将这个key 分到哈 希槽区间的节点上，具体算法就是：CRC16(key) % 16384。
    所以我们在测试的 时候看到set 和 get 的时候，直接跳转到了7000端⼝的节点
    
    Redis 集群会把数据存在⼀个 master 节点，然后在这个 master 和其对应的salve 之间进⾏数据同步。
    当读取数据时，也根据⼀致性哈希算法到对应的 master 节 点获取数据。
    只有当⼀个master 挂掉之后，才会启动⼀个对应的 salve 节点，充 当 master
    
    需要注意的是：必须要3个或以上的主节点，否则在创建集群时会失败，
    并且当存 活的主节点数⼩于总节点数的⼀半时，整个集群就⽆法提供服务了

    
- Redis主从服务搭建参考我的博文：
    Windows系统下搭建Redis主从服务图文教程（一主二从）
    https://blog.csdn.net/u011318077/article/details/91550295