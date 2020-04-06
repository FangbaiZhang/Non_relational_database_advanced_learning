# Non_relational_database_advanced_learning
# 非关系型数据进阶系统学习

# MongoDB

MongoDB教程：
- https://www.runoob.com/mongodb/mongodb-tutorial.html
- https://www.mongodb.org.cn/tutorial/


- 第一部分：MongoDB安装
- 第二部分：MongoDB常用操作
- 第三部分：MongoDB高级操作
- 第四部分：MongoDB与Python交互



# 第一部分：MongoDB安装及基本概念

# 1. MongoDB安装
- MongoDB安装的安装查看博文：[MongoDB v4.0.7的安装、启动和停止](https://blog.csdn.net/u011318077/article/details/88849634)
- 注意：
    - 软件安装完成后，先要添加安装目录的bin文件夹到系统变量的环境变量path路径中
    - (bin目录下有mongo.exe、mongod.exe等应用程序)
    - MongoDB安装之后，需要手动创建数据库文件夹(用于存储数据)，一个文件夹是一个独立的数据库
    - MongoDB服务启动方式常用两种：
    方式1：
        建议打开两个CMD窗口，一个窗口启动服务，一个窗口操作数据
        打开第一个窗口：
        命令行启动：mongod --dbpath H:\mongodb\data\db 
        (H:\mongodb\data\db为创建的数据库路径，启动时候可以指定端口号，数据库位置等参数，参考副本集创建)
        默认启动的接口是：127.0.0.1:27017
    方式2：
        参考博文中内容：
        注册为系统服务后启动，管理员运行CMD窗口后，执行：net start mongodb
        打开第二个窗口执行：mongo(连接到数据库，默认连接27017端口)
         
    - 上面注册只是将H盘下的mongodb数据库（一个存储数据的文件夹）创建为系统服务
    - 如果有又创建了另外一个mongodb1数据库，需要重新注册到系统服务 启动执行net start mongodb1

- MongoDB启动命令和注册为系统服务：
    Python爬虫开发与项目实战8.3.1节内容
    
# 2. MongoDB副本集
- 查看Python爬虫开发与项目实战笔记及截图
- 参考博文：MongoDB集群(副本集)新手入门图文教程（版本号：V4.0.7）
- https://blog.csdn.net/u011318077/article/details/88936999

# 3. MongoDB基本概念
- 文档document
文档是MongoDB中的基本单元即BSON，类似关系数据库中的行，文档有唯一的标识_id，文档都是以键值方式
文档的键值类似字典形式，键使用双引号(可省略)，值字符串使用双引号(不能省略)，整数不用双引号
- 文档的特性：
    1. 文档的键值对是有序的
    2. 文档的值可以是字符串，整数，列表，字典，数组，以及文档等类型
    3. 文档的值区分大小写及值的类型
    4. 文档中的值不仅可以是在双引号里面的字符串，还可以是其他几种数据类型（甚至可以是整个嵌入的文档)。
    5. 文档不能有重复的键。
    6. 文档的键是字符串。除了少数例外情况，键可以使用任意UTF-8字符。

- 集合collection
    集合是一组文档，没有固定的结构

- 数据库database
    一个MongoDB实例中中可以建立多个数据库，数据库都放在data文件夹下面，默认数据库是db，该数据库存储在data目录下。
    MongoDB单个实例可以容纳多个独立的数据库，不同的数据库又放置在不同的文件中，show dbs查看当前MongoDB实例下所有的数据库。

- 数据库结构：MongoDB实例---数据库database---集合collection---文档document

- 文档集合数据库参考003/004图片

4. MongoDB优势及应用
MongoDB 是由C++语言编写的，是一个基于分布式文件存储的开源数据库系统。
在高负载的情况下，添加更多的节点，可以保证服务器性能。
MongoDB 旨在为WEB应用提供可扩展的高性能数据存储解决方案。

MongoDB 将数据存储为一个文档，数据结构由键值(key=>value)对组成。
MongoDB 文档类似于 JSON 对象。字段值可以包含其他文档，数组及文档数组。

MongoDB 应用案例
下面列举一些公司MongoDB的实际应用：
    Craiglist上使用MongoDB的存档数十亿条记录。
    FourSquare，基于位置的社交网站，在Amazon EC2的服务器上使用MongoDB分享数据。
    Shutterfly，以互联网为基础的社会和个人出版服务，使用MongoDB的各种持久性数据存储的要求。
    bit.ly, 一个基于Web的网址缩短服务，使用MongoDB的存储自己的数据。
    spike.com，一个MTV网络的联营公司， spike.com使用MongoDB的。
    Intuit公司，一个为小企业和个人的软件和服务提供商，为小型企业使用MongoDB的跟踪用户的数据。
    sourceforge.net，资源网站查找，创建和发布开源软件免费，使用MongoDB的后端存储。
    etsy.com ，一个购买和出售手工制作物品网站，使用MongoDB。
    纽约时报，领先的在线新闻门户网站之一，使用MongoDB。
    CERN，著名的粒子物理研究所，欧洲核子研究中心大型强子对撞机的数据使用MongoDB。



# 第二部分：MongoDB常用操作

# 1. MongoDB客户端
- 启动MongoDB服务后(net start mongodb 启动已经注册的数据库文件夹)
    - mongo 启动本地客户端，连接已经启动的数据库文件夹
    - mongo –help  查看帮助
    - exit或者ctrl+c   退出mongo客户端

# 2. database基本命令
- 查看当前使用的数据库：db
- 查看所有的数据库：show dbs / show databases
- 切换数据库：use db_name (如果没有该数据库，就自动创建该数据库)
- 删除当前的数据库：db.dropDatabase()

# 3. 集合文档

- show collections 显示当前数据库下的集合（或者使用show tables,新版本增加了该命令）
- db.collection_name.drop()   删除该集合，成功删除选定集合，则 drop() 方法返回 true，否则返回 false。
- 注意：show tables 本来是mysql关系型数据可显示的是在当前数据库（mongodb中的databases）
        下有哪些数据表tables（数据表就相当于mongodb中的集合collections）

- db.collection_name.find()  显示该集合下所有的文档
        
- 文档documents就是MongoDB的最基本单元，每次插入的一个json字典就是一个文档
    - 集合里面可以存着多个文档，文档的键值对个数可以不一样
    - 但是为了方便管理，查找，同一个集合中的文档最好格式保持一致
    - 比如stu(学生)集合中，可以传入文档没有age和gender(不建议一个集合中文档格式不同)
        db.stu.insert({name:"段王爷", hometown:"大理", age:45, gender:true})
        db.stu.insert({name:"洪七公", hometown:"华山", age:18, gender:true})
        db.stu.insert({name:"洪", hometown:"泰山"})


- 插入insert：(插入时候会自动创建集合)
    db.集合名称.insert(document)
    
    - use test 创建test数据库
    - 向当前数据库test创建test1000集合并插入文档
    - 插入的文档都是键值对格式(类似字典)，实际是json格式(键可以不用双引号)
    - db.test1000.insert({name:"xiaowang",age:10})
    
    db.test1000.insert({_id:"20170101",name:'gj',age:1})
    插⼊⽂档时， 如果不指定_id参数， MongoDB会为⽂档分配⼀个唯⼀的ObjectId
    db.test1000.find() 查看该集合下的所有文档，可以显示出_id
    注意：如果插入文档时，指定_id参数，数据中本来有该id，则会出现错误，可以使用save或者update

- 保存save（指定id）
    db.集合名称.save(document)
    如果⽂档的_id已经存在则修改， 如果⽂档的_id不存在则添加
    
    先插入数据，使用id
    db.test1000.insert({_id:"10086",name:"xiaozhang",age:25})
    保存数据，使用id,新的文档会修改替换原来的文档
    db.test1000.save({_id:"10086",name:"Felix",age:"20"})

- 更新update
    db.集合名称.update(<query> ,<update>,{multi: <boolean>})
    参数query:查询条件
    参数update:更新操作符
    参数multi:可选，默认是false，表示只更新找到的第⼀条记录， 值为true表示把满⾜条件的⽂档全部更新
    
    db.test1000.update({name:"hr"},{name:"mnc"})   替换一条数据
    db.test1000.update({name:"hr"},{$set:{name:"hys"}})    更新一条数据,hr更新为hys,multi默认是false
    db.test1000.update({},{$set:{gender:0}},{multi:true})   条件为空，更新全部数据
    注意：就代表是更新操作符，更新多条要multi:true参数
    
- 删除remove
    db.集合名称.remove(<query>,{justOne: <boolean>})
    参数query:可选，删除的⽂档的条件
    参数justOne:可选， 如果设为true或1， 则只删除⼀条， 默认false， 表示删除多条
    
    将name叫xiaohong的删除
    db.test1000.remove({name:"小红"},{justOne:false})

- 删除集合，条件为空，删除集合全部数据
    db.stu.remove({},{justOne:false})
    
# 4. 数据查询

数据来源查看：
    > show dbs
    admin         0.000GB
    config        0.000GB
    local         0.000GB
    papers        0.000GB
    pythonSpider  0.000GB
    test          0.000GB
    yunqi         0.000GB
    > use test
    switched to db test
    > show collections 或者show tables
    dv3
    stu
    test1000
    >

- 方法find()： 查询
	db.集合名称.find({条件⽂档})
- 方法findOne()：查询，只返回第⼀个
	db.集合名称.findOne({条件⽂档})
- 方法pretty()： 将结果格式化，输出结果更加美观，符合编码规范
	db.集合名称.find({条件⽂档}).pretty()

## 4.1 条件运算符(比较运算符)
-   等于： 默认是等于判断， 没有运算符
    ⼩于：$lt （less than）
    ⼩于等于：$lte （less than equal）
    ⼤于：$gt （greater than）
    ⼤于等于：$gte
    不等于：$ne
    db.stu.find({age:{$gte:18}})

## 4.2 比较运算符
-   等于： 默认是等于判断， 没有运算符
    ⼩于：$lt （less than）
    ⼩于等于：$lte （less than equal）
    ⼤于：$gt （greater than）
    ⼤于等于：$gte
    不等于：$ne
    db.stu.find({age:{$gte:18}})
    
## 4.3 逻辑运算符
- and：在json中写多个条件即可
    查询年龄⼤于或等于18， 并且性别为true的学⽣
    db.stu.find({age:{$gte:18},gender:true})

- or:使⽤$or， 值为数组(列表里面字典)， 数组中每个元素为json
    查询年龄⼤于18， 或性别为false的学⽣
    db.stu.find({$or:[{age:{$gt:18}},{gender:false}]})
    查询年龄⼤于18或性别为男⽣， 并且姓名是郭靖
    db.stu.find({$or:[{age:{$gte:18}},{gender:true}],name:'郭靖'})

- 使⽤"$in"， "$nin" 判断是否在某个范围内
查询年龄为18、 28的学⽣
db.stu.find({age:{$in:[18,28]}})

## 4.4 正则表达式
-   使⽤//或$regex编写正则表达式，推荐使用$regex
    查询姓⻩的学⽣
    db.stu.find({name:/^⻩/})
    db.stu.find({name:{$regex:"^黄"}})  注意要使用双引号，单引号查询没有结果

## 4.5 limit和skip
- ⽅法limit()： ⽤于读取指定数量的⽂档
    db.集合名称.find().limit(NUMBER)
    查询2条学⽣信息
    db.stu.find().limit(2)
    
- ⽅法skip()： ⽤于跳过指定数量的⽂档
    db.集合名称.find().skip(NUMBER)
    db.stu.find().skip(2)
    
- 同时使用
    db.stu.find().limit(4).skip(5)
    或 
    db.stu.find().skip(5).limit(4)
    
- 主要用在翻页
    
## 4.6 投影
-   在查询到的返回结果中， 只选择必要的字段
    db.集合名称.find({},{字段名称:1,...})
    参数为字段与值， 值为1表示显示， 不显示该字段不写
    特殊： 对于_id列默认是显示的， 如果不显示需要明确设置为0
    例如：
    db.stu.find({},{_id:0,name:1,gender:1})
    年龄大于5的，只显示name字段
    db.test1000.find({age:{$gt:5}},{_id:0,name:1})

## 4.7 排序
-   ⽅法sort()， ⽤于对	集进⾏排序
    db.集合名称.find().sort({字段:1,...})
    参数1为升序排列
    参数-1为降序排列
    根据性别降序， 再根据年龄升序
    db.stu.find().sort({gender:-1,age:1})

4.8 统计个数
- ⽅法count()⽤于统计结果集中⽂档条数
    查询集合中的文档个数
    db.test1000.find().count()
    
- 条件统计可以使用以下两种方式：
    db.集合名称.find({条件}).count()
    db.集合名称.count({条件})
    例如：
    db.stu.find({gender:true}).count()
    db.stu.count({age:{$gt:20},gender:true})

## 4.9 消除重复
- ⽅法distinct()对数据进⾏去重
    db.集合名称.distinct('去重字段',{条件})
    例如：
    年龄大于18，筛选出不重复的家乡
    db.stu.distinct('hometown',{age:{$gt:18}})  
    筛选出不重复的名字
    db.test1000.distinct("name",{})


# 第三部分：MongoDB高级操作

# 5 聚合分组统计(管道)   
## 5.1 聚合aggregate
- 聚合(aggregate)是基于数据处理的聚合管道，每个文档通过一个由多个阶段（stage）组成的管道，
- 可以对每个阶段的管道进行分组、过滤等功能，然后经过一系列的处理，输出相应的结果。 
- db.集合名称.aggregate({管道:{表达式}})

- 先传入数据到stu(学生)集合中
db.stu.insert({name:"郭靖", hometown:"蒙古", age:20, gender:true})
db.stu.insert({name:"黄蓉", hometown:"桃花岛", age:18, gender:false})
db.stu.insert({name:"华筝", hometown:"蒙古", age:18, gender:false})
db.stu.insert({name:"黄药师", hometown:"桃花岛", age:40, gender:true})
db.stu.insert({name:"段誉", hometown:"大理", age:16, gender:true})
db.stu.insert({name:"段王爷", hometown:"大理", age:45, gender:true})
db.stu.insert({name:"洪七公", hometown:"华山", age:18, gender:true})
db.stu.insert({name:"洪", hometown:"泰山"})

注意：
MongoDB语句可以现在pycharm中编写，然后复制到CMD窗口中
现在pycharm中使用ctrl+c复制命令，然后CMD窗口点击鼠标右键，就自动粘贴了
可以一次复制多行，有时候会出现粘贴不上去的情况


- db.集合名称.aggregate({管道:{表达式}})
- 管道和表达式都可以有多个
- 管道：
    在mongodb中，⽂档处理完毕后， 通过管道进⾏下⼀次处理
    常用管道如下：
    $group： 将集合中的⽂档分组， 可⽤于统计结果
    $match： 过滤数据， 只输出符合条件的⽂档
    $project： 修改输⼊⽂档的结构， 如重命名、 增加、 删除字段、 创建计算结果
    $sort： 将输⼊⽂档排序后输出
    $limit： 限制聚合管道返回的⽂档数
    $skip： 跳过指定数量的⽂档， 并返回余下的⽂档
    $unwind： 将数组类型的字段进⾏拆分
    
- 表达式：
    处理输⼊⽂档并输出
    语法：表达式:'$列名'
    常⽤表达式:
    $sum： 计算总和， 
    $sum:1 表示以⼀倍计数
    $avg： 计算平均值
    $min： 获取最⼩值
    $max： 获取最⼤值
    $push： 在结果⽂档中插⼊值到⼀个数组中
    $first： 根据资源⽂档的排序获取第⼀个⽂档数据
    $last： 根据资源⽂档的排序获取最后⼀个⽂档数据        

## 5.2 $group分组统计

- $group注意点
    - $group对应字典中有几个键，结果中对应就有几个值
    - 分组依据必须放在_id的值中
    - 取不同的字段的时候需要使用$,比如$country，$age
    - 取字典嵌套的字典中的值的时候$,$_id.country
    - 能够同时按照多个组进行分组
    - 管道依次按顺序处理，常用处理顺序过滤-分组-重整

### 实例
- 语法格式：
    先写分组,必须使用_id作为键，然后里面的_id代表以哪个字段进行分组
    后面的字段是分组里面进行统计，求和，求平均值，最大值等等
    分组里面的键都是自己指定的，值是集合里面有的字段，前面都需要$符号

- 统计整个文档
    - _id为null
    - 整个文档求和求平均值
    db.stu.aggregate(
        {$group:{_id:null, count:{$sum:1}, mean_age:{$avg:"$age"}}}
        )

- 指定条件进行分组，然后统计
    - 按性别分组（注意$符号不能遗漏，还要注意}不要遗漏）
    db.stu.aggregate(
    {$group:{_id:"$gender"}}
    )
    - 按性别分组，然后统计每个性别的和，同时求最小值
    db.stu.aggregate(
    {$group:{_id:"$gender", count:{$sum:1}, min_age:{$min:"$age"}}}
    )
    
    - 按家乡进行分组,统计个数，求平均年龄
    db.stu.aggregate(
    {$group:{_id:"$hometown", count:{$sum:1}, mean_age:{$avg:"$age"}}}
    )
    
## 5.3 $project重构
- 修改文档结构，修改输出的格式
    _id字段的键使用gender进行替换
    _id:0 不显示_id字段
    count:1 显示count字段
    avg_age:1 显示avg_age字段
    
    db.stu.aggregate(
        {$group:{_id:"$gender", count:{$sum:1}, avg_age:{$avg:"$age"}}},
        {$project:{_id:0, gender:"$_id", count:1, avg_age:1}}
        )

## 5.4 $match过滤
- 选择年龄大于20的学生，观察男性和女性的人数
      db.stu.aggregate(
        {$match:{age:{$gt:16}}},
        {$group:{_id:"$gender", count:{$sum:1}}},
        {$project:{_id:0, gender:"$_id", count:1}}
        )
      
- 选择年龄大于20或者家乡是蒙古或大理的学生，观察男性和女性的人数
      db.stu.aggregate(
        {$match:{$or:[{age:{$gt:16}},{hometown:{$in:["蒙古", "大理"]}}]}},
        {$group:{_id:"$gender", count:{$sum:1}}},
        {$project:{_id:0, gender:"$_id", count:1}}
        )   

- 综合练习：       
- 统计出每个country/province下的userid的数量（同一个userid只统计一次）        
db.dv3.insert({"country" : "china", "province" : "sh", "userid" : "a" } ) 
db.dv3.insert({  "country" : "china", "province" : "sh", "userid" : "b" } )
db.dv3.insert({  "country" : "china", "province" : "sh", "userid" : "a" }  )
db.dv3.insert({  "country" : "china", "province" : "sh", "userid" : "c" } )
db.dv3.insert({  "country" : "uk", "province" : "bj", "userid" : "da" } )
db.dv3.insert({  "country" : "china", "province" : "bj", "userid" : "fa" }  )

- 所有字段进行分组，可以达到去重的效果，上面第一行于第三行数据相同
db.dv3.aggregate(
    {$group:{_id:{country:"$country", province:"$province", userid:"$userid"}}}
)

- 上面去重后的结果继续按照国家和省份进行分组,然后统计每个分组的和
- 第一次分组后第二次分组，第二次分组使用第一次的分组的_id
- 分组后的结果重整结构
db.dv3.aggregate(
    {$group:{_id:{country:"$country", province:"$province", userid:"$userid"}}},
    {$group:{_id:{country:"$_id.country", province:"$_id.province"}, count:{$sum:1}}},
    {$project:{country:"$_id.country", province:"$_id.province", count:1, _id:0}}
)
 

## 5.5 sort排序，skip，limit
- 学生按年龄升序排列
    db.stu.aggregate(
        {$sort:{age:1}}
    )

- 学生按性别分组，统计个数，然后按个数降序排列
    db.stu.aggregate(
        {$group:{_id:"$gender", count:{$sum:1}}},
        {$sort:{count:-1}}
    )
    
- skip和limit
    - 先跳过两个，然后选定两个
    db.stu.aggregate({$skip:2},{$limit:2})

## 5.6 unwind拆分
- 将⽂档中的某⼀个数组类型字段拆分成多条， 每条包含数组中的⼀个值
- 语法：db.集合名称.aggregate({$unwind:'$字段名称'})

    db.t2.insert({_id:1,item:'t-shirt',size:['S','M','L']})
    db.t2.aggregate({$unwind:'$size'})
    结果如下：
    { "_id" : 1, "item" : "t-shirt", "size" : "S" }
    { "_id" : 1, "item" : "t-shirt", "size" : "M" }
    { "_id" : 1, "item" : "t-shirt", "size" : "L" }

- 字段unwind拆分后，统计长度
    - 插入数据
    db.t3.insert({username:"Alex", tags:["C+", "Java", "Python"]})
    - 拆分tags，统计拆分后的文档个数
    db.t3.aggregate({$match:{username:"Alex"}}, {$unwind:"$tags"}, {$group:{_id:null, sum:{$sum:1}}})
    - 先匹配到用户，然后对tags进行拆分，然后按null(不指定字段，所有文档分组)分组，然后统计分组的个数
    
# 6 创建索引
- 先插入数据,使用js语法
    for(i=0;i<10000;i++){db.t12.insert({name:"test"+i,age:i})}
    数据较多，插入较慢，一分钟左右
    查看数据条数
    db.t12.find().count()
    
- 查找数据，并查看耗费时间
    > db.t12.find().count()
    100000
    > db.t12.find({name:"test30000"})
    { "_id" : ObjectId("5cf8d888e1d09b780e764cd9"), "name" : "test30000", "age" : 30000 }
    > db.t12.find({age:30000}).explain('executionStats')
    {.......
            "executionStats" : {
                    "executionSuccess" : true,
                    "nReturned" : 1,
                    "executionTimeMillis" : 82,
                    "totalKeysExamined" : 0,
                    "totalDocsExamined" : 100000,
    ........
    }
    上面花费时间82ms
    
- 建立索引之后对比：
    语法：db.集合.ensureIndex({要建立索引的字段:1})，1表示升序， -1表示降序
    具体操作：
    db.t12.ensureIndex({name:1})
    {
            "createdCollectionAutomatically" : false,
            "numIndexesBefore" : 1,
            "numIndexesAfter" : 2,
            "ok" : 1
    }
    db.t12.find({name:"test30000"}).explain('executionStats')
    "inputStage" : {
                                "stage" : "IXSCAN",
                                "nReturned" : 1,
                                "executionTimeMillisEstimate" : 0,
                                "works" : 2,
    建立索引后查找时间0ms
    
- 查看索引
    db.t12.getIndexes()
    [
            {
                    "v" : 2,
                    "key" : {
                            "_id" : 1
                    },
                    "name" : "_id_",
                    "ns" : "test.t12"
            },
            {
                    "v" : 2,
                    "key" : {
                            "name" : 1
                    },
                    "name" : "name_1",
                    "ns" : "test.t12"
            }
    ]
    上面结果中有两个字典，key就是创建索引的字段
    数据库默认都会以_id字段创建默认索引，默认也是升序
    "name" : 1 就是我们刚刚给name字段额外创建的索引，创建索引后使用name字段查询，查询速度明显变快，

- 删除索引：
     db.t12.dropIndex('索引名称')
     db.t12.dropIndex({name:1})
     { "nIndexesWas" : 2, "ok" : 1 }
     删除之后就只有一个默认索引了
     
- 在默认情况下创建的索引均不是唯一索引。
    创建唯一索引（可以对数据进行去重，name字段相同的但是只会创建一个索引，自动排除重复的）:
         db.t12.ensureIndex({"name":1},{"unique":true})
    创建唯一索引并消除重复：
         db.t12.ensureIndex({"name":1},{"unique":true,"dropDups":true})  
    建立联合索引(什么时候需要联合索引)：
         db.t12.ensureIndex({name:1,age:1})
         
- 爬虫数据去重
    - 使用数据库建立的关键字段（一个或者多个）的唯一索引进行去重
    
    - URL地址对应数据不会变的情况，URL地址能够唯一判别一条数据的
        - 使用场景：
        URL地址持久化存储在redis集合中，具体步骤：
        拿到URL地址，判断url是否在redis的url集合中
        存在：说明url已经请求过，不再请求
        不存在：url没请求过，请求，同时存储url到该集合中
        - 布隆过滤器
            位操作，将url地址通过算法转换为对应的位置
    
    - 根据数据本身进行去重
        - 选择特定的字段，使用加密算法（md5,sha1）将字段进行加密，生成字符串
        - 后续新来一条数据，同样的方法进行加密，如果得到的字符串在redis集合中
        - 说明存在，对数据更新，如果不存在，则直接插入该数据

# 7 数据库备份与恢复                             
- 启动本地的mongodb数据库服务，不需要使用mongo连接数据库
- 直接启动后使用备份和恢复命令即可对mongodb数据库中所有的dbs进行备份操作
- 要想将其他数据恢复早mongodb中，也是在该级操作

- 数据备份：
    参考教程：http://www.baidu.com/link?url=I_GAWYpj6q4l_P4fmTfwd8CxCokr0sFvaZB7yhXT4vG-9BEx1pyXus1DocoxqogW7jUZ_7XbMunaCTlGDIk2S5gSQid5YE1Kd-WTR_YEvdq
    备份的语法：
    mongodump -h dbhost -d dbname -o dbdirectory
    -h： 服务器地址， 也可以指定端⼝号
    -d： 需要备份的数据库名称
    -o： 备份的数据存放位置， 此⽬录中存放着备份出来的数据
    -使用mongo连接数据库，可以看到该数据库的地址和端口号
    
    C:\WINDOWS\system32>net start mongodb
    请求的服务已经启动。
    
    请键入 NET HELPMSG 2182 以获得更多的帮助。    
    C:\WINDOWS\system32>mongo
    MongoDB shell version v4.0.7
    connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
    Implicit session: session { "id" : UUID("dd815f12-50ec-499d-a162-b5ee7f3003d5") }
    MongoDB server version: 4.0.7
    .....
    > exit
    bye
    
    备份test数据库到H盘的文件夹中：
    mongodump -h 127.0.0.1:27017 -d test -o H:\mongodb\mongobeifen
    
    C:\WINDOWS\system32>mongodump -h 127.0.0.1:27017 -d test -o H:\mongodb\mongobeifen
    2019-06-09T13:38:50.248+0800    writing test.t12 to
    2019-06-09T13:38:50.338+0800    writing test.stu to
    2019-06-09T13:38:50.339+0800    writing test.dv3 to
    2019-06-09T13:38:50.339+0800    writing test.test1000 to
    2019-06-09T13:38:50.343+0800    done dumping test.stu (7 documents)
    2019-06-09T13:38:50.344+0800    writing test.t3 to
    2019-06-09T13:38:50.347+0800    done dumping test.dv3 (6 documents)
    2019-06-09T13:38:50.348+0800    done dumping test.test1000 (4 documents)
    2019-06-09T13:38:50.349+0800    done dumping test.t3 (1 document)
    2019-06-09T13:38:50.916+0800    done dumping test.t12 (100000 documents)
    
- 数据恢复
    恢复语法：
         mongorestore -h dbhost -d dbname --dir dbdirectory
    -h： 服务器地址
    -d： 需要恢复的数据库实例
    --dir： 备份数据所在位置
    
    mongorestore -h 127.0.0.1:27017 -d douban --dir H:\mongodb\mongobeifen\douban


# 第四部分：MongoDB与Python交互

# 8 Python操作MongoDB
- 参考案例005/006/007
