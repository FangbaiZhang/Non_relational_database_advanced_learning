# Non_relational_database_advanced_learning
# 非关系型数据进阶系统学习

# MongoDB

MongoDB教程：
- https://www.runoob.com/mongodb/mongodb-tutorial.html
- https://www.mongodb.org.cn/tutorial/


- 第一部分：MongoDB安装
- 第二部分：MongoDB常用操作
- 第三部分：



# 第一部分：MongoDB安装及基本概念

# 1. MongoDB安装
- MongoDB安装的安装查看博文：[MongoDB v4.0.7的安装、启动和停止](https://blog.csdn.net/u011318077/article/details/88849634)
- 注意：
    - 软件安装完成后，先要添加安装目录的bin文件夹到系统变量的环境变量path路径中(bin目录下有mongo.exe、mongod.exe等应用程序)
    - MongoDB安装之后，需要手动创建数据库文件夹(用于存储数据)，一个文件夹是一个独立的数据库
    - MongoDB服务启动方式常用两种：
        建议打开两个CMD窗口，一个窗口启动服务，一个窗口操作数据
        打开第一个窗口：
        命令行启动：mongod --dbpath H:\mongodb\data\db (H:\mongodb\data\db为创建的数据库路径)
        注册为系统服务后启动：net start mongodb
        打开第二个窗口执行：mongo(连接到数据库)
        
    - 上面注册只是将H盘下的mongodb数据库（一个存储数据的文件夹）创建为系统服务
    - 如果有又创建了另外一个mongodb1数据库，需要重新注册到系统服务 启动执行net start mongodb1

- MongoDB启动命令和注册为系统服务及：
    Python爬虫开发与项目实战8.3.1节内容
    
# 2. MongoDB副本集


# 3. MongoDB基本概念
- 文档document
文档是MongoDB中的基本单元即BSON，类似关系数据库中的行，文档有唯一的标识_id，文档都是以键值方式
文档的键值类似字典形式，键使用双引号(可省略)，值字符串使用双引号，整数不用双引号
- 文档的特性：
    1. 文档的键值对是有序的
    2. 文档的值可以是字符串，整数，数组，以及文档等类型
    3. 文档区分大小写及值类型

- 集合collection
    集合是一组文档，没有固定的结构

- 数据库database
    一个MongoDB中可以建立多个数据库，默认数据库是db，该数据库存储在data目录下。
    MongoDB单个实例可以容纳多个独立的数据库，不同的数据库又放置在不同的文件中

- 文档集合数据库参考003/004图片

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
注意：
MongoDB语句可以现在pycharm中编写，然后复制到CMD窗口中
我的CMD粘贴后，有时候复制不进去


- show collections 显示当前数据库下的集合

- 插入insert：
    db.集合名称.insert(document)
    
    - use test 创建test数据库
    - 向当前数据库创建test1000集合并插入文档
    - 插入的文档都是键值格式，实际是json格式(键可以不用双引号)
    - db.test1000.insert({name:"xiaowang",age:10})
    
    db.test1000.insert({_id:"20170101",name:'gj',age:1})
    插⼊⽂档时， 如果不指定_id参数， MongoDB会为⽂档分配⼀个唯⼀的ObjectId
    db.test1000.find() 查看该集合下的所有文档，可以显示出_id
    注意：如果插入文档时，指定_id参数，数据中本来有该id，则会出现错误，可以使用save或者update



- 保存save
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
    db.test1000.update({name:"hr"},{$set:{name:"hys"}})    更新一条数据
    db.test1000.update({},{$set:{gender:0}},{multi:true})   更新全部数据
    注意：更新多条要使用$操作符
    
- 删除remove
    db.集合名称.remove(<query>,{justOne: <boolean>})
    参数query:可选，删除的⽂档的条件
    参数justOne:可选， 如果设为true或1， 则只删除⼀条， 默认false， 表示删除多条
    
    将name叫xiaohong的删除
    db.test1000.remove({name:"小红"},{justOne:false})
    
4. 数据查询
- 方法find()： 查询
	db.集合名称.find({条件⽂档})
- 方法findOne()：查询，只返回第⼀个
	db.集合名称.findOne({条件⽂档})
- 方法pretty()： 将结果格式化，输出结果更加美观，符合编码规范
	db.集合名称.find({条件⽂档}).pretty()

## 4.1 条件运算符
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

- or:使⽤$or， 值为数组， 数组中每个元素为json
    查询年龄⼤于18， 或性别为false的学⽣
    db.stu.find({$or:[{age:{$gt:18}},{gender:false}]})
    查询年龄⼤于18或性别为男⽣， 并且姓名是郭靖
    db.stu.find({$or:[{age:{$gte:18}},{gender:true}],name:'gj'})

- 使⽤"$in"， "$nin" 判断是否在某个范围内
查询年龄为18、 28的学⽣
db.stu.find({age:{$in:[18,28]}})

## 4.4 正则表达式
-   使⽤//或$regex编写正则表达式
    查询姓⻩的学⽣
    db.stu.find({name:/^⻩/})
    db.stu.find({name:{$regex:'^⻩'}})

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
    
## 4.10 聚合aggregate
- 聚合(aggregate)是基于数据处理的聚合管道，每个文档通过一个由多个阶段（stage）组成的管道，
- 可以对每个阶段的管道进行分组、过滤等功能，然后经过一系列的处理，输出相应的结果。 
- db.集合名称.aggregate({管道:{表达式}})

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
    $sum： 计算总和， $sum:1 表示以⼀倍计数
    $avg： 计算平均值
    $min： 获取最⼩值
    $max： 获取最⼤值
    $push： 在结果⽂档中插⼊值到⼀个数组中
    $first： 根据资源⽂档的排序获取第⼀个⽂档数据
    $last： 根据资源⽂档的排序获取最后⼀个⽂档数据        
