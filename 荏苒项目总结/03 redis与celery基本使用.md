# Redis安装与使用

window系统的redis是微软团队根据官方的linux版本高仿的

官方原版: https://redis.io/

中文官网:http://www.redis.cn

菜鸟教程:https://www.runoob.com/redis/

## redis下载和安装

下载地址： https://github.com/MicrosoftArchive/redis/releases

 ![img](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday104/day018/assets/867021-20190120213315530-199992307.png)

![img](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday104/day018/assets/867021-20190120213337245-1919434508.png)

![img](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday104/day018/assets/867021-20190120213351947-466120029.png)

![img](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday104/day018/assets/867021-20190120213613576-1092651557.png)

![img](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday104/day018/assets/867021-20190120213732137-1070050780.png)

![img](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday104/day018/assets/867021-20190120213836094-663215847.png)

![img](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday104/day018/assets/867021-20190120213850621-1280736381.png)

![img](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday104/day018/assets/867021-20190120214101037-1456534345.png)

 

![img](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday104/day018/assets/867021-20190120214000974-189830387.png)

使用以下命令启动redis服务端

```
redis-server C:/tool/redis/redis.windows.conf
```

![1553244955947](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday104/day018/assets/1553244955947.png)

关闭上面这个cmd窗口就关闭redis服务器服务了。

+ redis作为windows服务启动方式

  ```
  redis-server --service-install redis.windows.conf
  ```

+ 启动服务：redis-server --service-start

+ 停止服务：redis-server --service-stop

+ 启动内置客户端连接redis服务：redis-cli

## redis的配置

redis 安装成功以后,window下的配置文件保存在软件安装目录下,如果是mac或者linux,则默认安装`/etc/redis/redis.conf`

### redis的核心配置选项

- 绑定ip：如果需要远程访问，可将此⾏注释，或绑定⼀个真实ip

  > bind 127.0.0.1  ::1

- 端⼝，默认为6379

  > port 6379

- 是否以守护进程运⾏[这里的配置主要是linux和mac下面需要配置的]

  - 如果以守护进程运⾏，则不会在命令⾏阻塞，类似于服务
  - 如果以⾮守护进程运⾏，则当前终端被阻塞
  - 设置为yes表示守护进程，设置为no表示⾮守护进程
  - 推荐设置为yes

  > daemonize yes

- 数据⽂件

  > dbfilename dump.rdb

- 数据⽂件存储路径

  > dir /var/lib/redis

- ⽇志⽂件

  > logfile /var/log/redis/redis-server.log

- 数据库，默认有16个

  > database 16

- 主从复制，类似于双机备份。

  > slaveof

- 访问密码，连接redis时需要输入指定密码，默认是注释状态的。

  > requirepass foobared



### Redis的使用

Redis 是一个高性能的key-value数据格式的内存缓存，NoSQL数据库。

NOSQL：Not Only SQL，泛指非关系型数据库。

关系型数据库: (mysql, oracle, sql server, db2, sqlite, PostgreSQL)

```
1. 数据存放在表中，表之间有关系。
2. 通用的SQL操作语言。
3. 大部分支持事务。
```

非关系型数据库[ redis，hadoop，mangoDB]:

```
1. 没有数据表的概念，不同的nosql数据库存放数据位置不同。
2. nosql数据库没有通用的操作语言。
3. 基本不支持事务。   redis支持简单事务
```

redis：
内存型(数据存放在内存中)的非关系型(nosql)key-value(键值存储)数据库，支持数据的持久化(注: 数据持久化时将数据存放到文件中，每次启动redis之后会先将文件中数据加载到内存)，经常用来做缓存(用来缓存一些经常用到的数据，提高读写速度)。

redis是一款基于CS架构的数据库，所以redis有客户端，也有服务端。

其中，客户端可以使用python等编程语言，也可以终端命令行工具

![1553246999266](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday104/day018/assets/1553246999266.png)

redis客户端连接服务器:

```
redis-cli -h `redis服务器ip` -p `redis服务器port`
```

## 通用命令

- 如果在配置文件中设置了访问密码，则需要在连接redis时填写密码。

```bash
redis-cli -h <Ip地址，默认127.0.01> -p<端口,默认3306> # 进入redis，如果是本地，则不需要声明-h。
auth <密码>                       # 填写密码
```

- 切换数据库

  默认情况下，我们在终端下面连接redis，进入的数据库，是0号数据库。如果要切换数据库，则可以使用select命令

```bash
select <db>
```



## redis数据类型

### string 字符串类型

+ 类型解释

  + 字符串类型是 Redis 中最为基础的数据存储类型，它在 Redis 中是二进制安全的，也就是byte类型
  + 单个数据的最大容量是512M
  + 格式：`key: string`

+ 使用场景

  >用于保存一些项目中的普通数据或者有时效的数据，只要键值对的都可以保存，例如，保存 session,定时记录状态,保存一个倒计时时间值。

+ 常用命令

  + 设置/修改键值（如果设置的键不存在则为添加，如果设置的键已经存在则修改）

    >set key value
    >
    >set name xiaoming  设置键为`name`值为`xiaoming`的数据

  + 设置键值及过期时间，以秒为单位		

    > setex key seconds value
    >
    > setex name 20 xiaoming  设置过期时间为20s

  + 给已有的数据重新设置有效期

    >expire key time

  + 设置多个键值

    >mset key1 value1 key2 value2 ...
    >
    >例：mset python 100 java 80  c 78

  + 追加值

    >append key value

  + 获取：根据键获取值，如果不存在此键则返回`nil

    >get key

  + 根据多个键获取多个值

    >mget key1 key2 ...



### hash 哈希类型

+ 类型解释

  + hash用于存储对象，对象的结构为属性、值，值的类型为string。

  + 格式

    ```
    键key:{
       	域field:值value[这里的值只能是字符串],
       	域field:值value,
    }
    ```

+ 使用场景

  >用于保存项目中的一些字典数据，但是不能保存多维的字典，例如，商城的购物车或者登陆用户的信息。

+ 常用命令

  + 设置单个属性

    > hset key field value

    > hset user name xiaohong   设置键 `user`的属性`name`为`xiaohong`

  + 设置多个属性

    > hmset key field1 value1 field2 value2 ...

    > 例：hmset u2 name xiaohong age 11

  + 获取指定键所有的域值

    > hkeys key

  + 获取⼀个域对应的值

    > hget key field

    > 例：hget u2 name  获取键`u2`属性`name`的值

  + 获取多个属性的值

    > hmget key field1 field2 ...

    例5：获取键`u2`属性`name`、`age`的值

    > hmget u2 name age

  + 获取所有域对应的值

    > hvals key

  + 删除域，域对应的值会被⼀起删除（可删除多个）

    > hdel key field1 field2 ...

  + 获取成员个数（即域或值的个数）

    > hmset brother liubei 28 guanyu 20 zhangfei 14
    >
    > hlen brother
    >
    > 输出结果：3

### list列表类型

+ 类型解释

  + 列表的元素类型为string
  + 按照插⼊顺序排序
  + 格式 `key:[ 值1，值2,值3..... ]`

+ 使用场景

  >用于保存项目中的列表数据，但是也不能保存多维的列表，例如，队列，秒杀系统，挂号系统，排单系统，访问历史记录。

+ 常用命令

  + 在左侧插⼊数据

    > lpush key value1 value2 ...

    > 例：lpush a1 a b c  从键为`a1`的列表左侧加⼊数据`a、b、c`

  + 在右侧插⼊数据

    > rpush key value1 value2 ...

    > 例：rpush a1 0 1  从键为`a1`的列表右侧加⼊数据`0、1`

  + 在指定元素的前或后插⼊新元素

    > linsert key before或after 现有元素 新元素

    > 例：linsert a1 before b 3  在键为`a1`的列表中元素`b`前加⼊`3`

  + 设置指定索引位置的元素值

    + 索引从左侧开始，第⼀个元素为0

    + 索引可以是负数，表示尾部开始计数，如`-1`表示最后⼀个元素

      > lset key index value

      > 例：lset a1 1 z  修改键为`a1`的列表中下标为`1`的元素值为`z`

  + 删除指定元素

    - 将列表中前`count`次出现的值为`value`的元素移除

      > lrem key count value

    - count > 0: 从头往尾移除，如果count=2，则从头开始，删除2个成员value

    - count < 0: 从尾往头移除，如果count=-2，则从尾开始，删除2个成员value

      > 例：从`a2`列表右侧开始删除2个`b`
      >
      > lpush a2 a b a b a b
      >
      > lrem a2 -2 b

    - count = 0: 移除所有

    - 删除指定索引位置的元素

      >lset key index del
      >
      >lrem key 0 del

  + 从列表中获取指定返回的元素

    >lrange key start stop
    >
    >例：lrange a2 0 -1  查看列表`a2`的所有元素

  + 获取指定列表的长度

    > lpush arr1 a b c
    >
    > llen arr1
    >
    > 输出结果： 3

### set无序集合类型

+ 类型解释

  + 元素为string类型
  + 元素唯一不重复，没有修改操作。
  + 格式 `key:{值1,值4,值3,值5}`

+ 使用场景

  >用于保存项目中的一些不能重复的数据，可以用于过滤，例如，投票海选的时候，过滤候选人，收藏(去重)。

+ 常用命令

  + 添加元素

    > sadd key member1 member2 ...

    例1：向键`a3`的集合中添加元素`zhangsan`、`lisi`、`wangwu`

    > sadd a3 zhangsan sili wangwu

  - 返回所有的元素

    > smembers key

    例2：获取键`a3`的集合中所有元素

    > smembers a3

  - 删除指定元素

    > srem key value

    例3：删除键`a3`的集合中元素`wangwu`

    > srem a3 wangwu

  - 随机抽取一个成员

    spop 随机抽取并从集合中删除这个成员

    srandmember 随机抽取一个集合的成员，不会删除这个成员。

    > sadd name_list liubei caocao sunquan
    >
    > spop name_list
    >
    > 输出结果：任意一个成员。

  - 获取集合的成员个数

    > sadd name_list liubei caocao sunquan
    >
    > scard name_list
    >
    > 输出结果：3



### zset有序集合类型

+ 类型解释

  + 官方名称：sortedset，元素为string类型

  + 元素唯一不重复，没有修改操作，按照权重值进行排序。

  + 格式

    ```
    key: {
        值1 权重值4,
        值2 权重值3,
        值3 权重值2,
        值4 权重值1,
    }
    ```

+ 使用场景

  >用于保存项目中一些不能重复，但是需要进行排序的数据，分数排行榜。

## 键操作

- 查找当前数据库中的键，参数⽀持正则表达式

  > keys pattern

  例1：查看所有键

  > keys *

  例2：查看名称中包含`a`的键

  > keys a*

- 判断键是否存在，如果存在返回`1`，不存在返回`0`

  > exists key1

  例3：判断键`a1`是否存在

  > exists a1

- 查看键对应的`value`的类型

  > type key

  例4：查看键`a1`的值类型，为redis⽀持的五种类型中的⼀种

  > type a1

- 删除键及对应的值

  > del key1 key2 ...

  例5：删除键`a2、a3`

  > del a2 a3

- 查看有效时间，以秒为单位

  > ttl key

  例6：查看键`bb`的有效时间

  > ttl bb

- 清空当前数据库中所有的键

  > flushall

## Python操作redis

python有很多的模块都可以实现操作redis，常用有redis和pyredis，这两个模块的使用操作是类似的。

所以，我们这里使用redis来进行演示。

+ 安装命令

  ```
  pip install redis
  ```

+ 代码演示

  + 连接redis数据库

    ```python
    from redis import Redis
    #若无密码则password不填
    redis = Redis(host="127.0.0.1",port=6379,db=1,password="123456")
    ```

  + 字符串操作

    + 添加一个字符串数据

      ```python
      #set name xiaoming
      redis.set("name","xiaoming")
      ```

    + 添加一个临时数据

      ```python
      #setex title 30 hello
      redis.setex("title",30,"hello")
      ```

    + 查看一个数据的有效期(-2表示过期,-1表示永久)

      ```python
      time = redis.ttl("title")
      print(time)
      ```

    + 获取一个字符串

      ```python
      name = redis.get("name")
      print(name)  # 得到的结果是bytes类型的   b'xiaoming'
      print(name.decode()) # 必须要解码,xiaoming
      ```

    + 删除key,因为del是一个关键词,所以在redis模块,凡是命令如果是一个关键词,全部改成单词的全拼

      ```python
      redis.delete("name")
      ```

  + 哈希的操作

    + 添加

      ```python
      dict1 = {
          "liubei": 28,
          "guanyu": 20,
          "zhangfei": 14,
      }
      redis.hmset("brother",dict1)
      ```

    + 获取哈希里面的所有成员

      ```python
      dict_data = redis.hgetall("brother")
      print(dict_data) # {b'liubei': b'28', b'guanyu': b'20', b'zhangfei': b'14'}
      for key,name in dict_data.items():
          print(key.decode(),name.decode())
          """
          liubei 28
          guanyu 20
          zhangfei 14
          """
      age = dict_data.get("liubei".encode()).decode()
      print(age) # b'28'
      ```

  + redis开启事务

    ```python
    #redis_conn = get_redis_connection("sms_code")
    redisredis_conn = Redis(host="127.0.0.1",port=6379,db=1,password="123456")
    # redis的事务是通过管道对象来设置命令
    pipe = redis_conn.pipeline()
    pipe.multi()   # 开启事务
    #pipe.命令()
    #pipe.命令()
    pipe.execute() # 提交事务
    ```

    

# Celery安装与使用

Celery是一个功能完备即插即用的异步任务队列系统。它适用于异步处理问题，当发送邮件、或者文件上传, 图像处理等等一些比较耗时的操作，我们可将其异步执行，这样用户不需要等待很久，提高用户体验。

文档：http://docs.jinkan.org/docs/celery/getting-started/index.html

Celery的特点是：

- 简单，易于使用和维护，有丰富的文档。
- 高效，单个celery进程每分钟可以处理数百万个任务。
- 灵活，celery中几乎每个部分都可以自定义扩展。

```python
任务队列是一种跨线程、跨机器工作的一种机制.
任务队列中包含称作任务的工作单元。有专门的工作进程持续不断的监视任务队列，并从中获得新的任务并处理.
celery通过消息进行通信，通常使用一个叫Broker(中间人)来协助client(任务的发出者)和worker(任务的处理者). clients发出消息到队列中，broker将队列中的信息派发给worker来处理。
```

**Celery**的运作流程

Celery的架构由三部分组成，消息队列（message broker），任务执行单元（worker）和任务执行结果存储（task result store）组成。

![img](${asserts}/720333-20170126182955581-1727025143.png)

![img](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday105/day019/celery/assets/3.png)

```python
一个celery系统可以包含很多的worker和broker

Celery本身不提供消息队列功能，但是可以很方便地和第三方提供的任务队列进行集成，包括RabbitMQ ,Redis, MongoDB 等
```

## 安装

```python
pip install -U celery==4.3.0

# 提醒：因为celery默认使用了多进程，所以在celery4.0.0版本以后，不支持windows系统的。
# 在windows下面即便安装了celery4.0.0以前的版本，其实也有兼容问题的。
```

也可从官方直接下载安装包:<https://pypi.python.org/pypi/celery/>

```python
tar xvfz celery-0.0.0.tar.gz
cd celery-0.0.0
python setup.py build
python setup.py install
```

安装完成了celery以后，接下来要确保服务器下有任务队列，可以是redis，也可以是RabbitMQ。在这里，我们已经安装了redis，可以直接使用redis作为任务队列，也可以使用RabbitMQ【注意，我们提供的ubuntu下是没有RBMQ的，安装文档：https://blog.csdn.net/qq_22638399/article/details/81704372】

## 使用

使用celery第一件要做的最为重要的事情是需要先创建一个Celery实例，我们一般叫做celery应用，或者更简单直接叫做一个app。app应用是我们使用celery所有功能的入口，比如创建任务，管理任务等，在使用celery的时候，app必须能够被其他的模块导入。

一般celery任务目录直接放在项目的根目录下即可，路径:

```python
renranapi/
├── mycelery/
    ├── config.py     # 配置文件
    ├── __init__.py   
    ├── main.py       # 主程序,导入celery并进行任务注册和加载配置
    └── sms/          # 一个目录可以放置多个任务,该目录下存放当前任务执行时需要的模块或依赖
        └── tasks.py  # 任务的文件，名称必须是这个!!!
```



main.py，代码：

```python
# 主程序
from celery import Celery
# 创建celery实例对象
app = Celery("renran")

# 通过app对象加载配置
app.config_from_object("mycelery.config")

# 自动搜索并加载任务
# 参数必须必须是一个列表，里面的每一个任务都是任务的路径名称
# app.autodiscover_tasks(["任务1","任务2",....])
app.autodiscover_tasks(["mycelery.sms","mycelery.cache"])

# 启动Celery的命令
# 强烈建议切换目录到项目的根目录下启动celery!!
# celery -A mycelery.main worker --loglevel=info
```

celery的配置项文档：https://docs.celeryproject.org/en/stable/userguide/configuration.html

配置文件config.py，代码：

```python
# 任务队列的链接地址
broker_url = 'redis://127.0.0.1:6379/15'
# 结果队列的链接地址
result_backend = 'redis://127.0.0.1:6379/14'
```



创建一个任务文件sms/**tasks.py**，并创建任务，代码:

```python
# celery的任务必须写在tasks.py的文件中，别的文件名称不识别!!!
from mycelery.main import app

@app.task  # name表示设置任务的名称，如果不填写，则默认使用函数名做为任务名
def send_sms():
    print("发送短信!!!")

@app.task(name="send_sms2")  # name表示设置任务的名称，如果不填写，则默认使用函数名做为任务名
def send_sms2():
    print("发送短信任务2!!!")
```



接下来，我们运行celery，效果如下：

![1562037230098](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday105/day019/celery/assets/1562037230098.png)

在程序中调用上面的异步任务，拿django进行举例：

```python
# 调用celery执行异步任务
from mycelery.sms.tasks import send_sms
send_sms.delay(mobile)
```

**注：若执行任务时celery未启动，下次celery启动时会自动执行上次提交的任务**

其他参考文档：

http://docs.celeryproject.org/en/latest/getting-started/introduction.html

https://github.com/celery/celery/tree/master/examples/django/

https://www.jianshu.com/p/1840035cb510

https://flower.readthedocs.io/en/latest/screenshots.html



接下来，我们需要把celery和django组合起来一起使用。

### 把django和celery进行组合

在main.py主程序中对django的配置文件进行加载

```python
# 主程序
import os
from celery import Celery
# 创建celery实例对象
app = Celery("renran")

# 把celery和django进行组合，识别和加载django的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'renranapi.settings.dev')

# 对django框架执行初始化
import django
django.setup()

# 通过app对象加载配置
app.config_from_object("mycelery.config")

# 加载任务
# 参数必须必须是一个列表，里面的每一个任务都是任务的路径名称
# app.autodiscover_tasks(["任务1","任务2"])
app.autodiscover_tasks(["mycelery.sms"])

# 启动Celery的命令
# 强烈建议切换目录到mycelery根目录下启动
# celery -A mycelery.main worker --loglevel=info
```

在需要使用django配置的任务中，直接加载配置，所以我们把注册的短信发送功能，整合成一个任务函数，代码：

```python
from mycelery.main import app
from .yuntongxun.sms import CCP
from . import constants
import logging

log = logging.getLogger("django")

# @app.task(name="send_sms")
# def send_sms(mobile):
#     print("发送短信给%s的异步任务执行了" % mobile)
#     return "任务结果！"


@app.task(name="send_sms")
def send_sms(mobile, sms_code):
    """异步发送短信"""
    ccp = CCP()
    try:
        result = ccp.send_template_sms(mobile, [sms_code, constants.SMS_EXPIRE_TIME//60 ], constants.SMS_TEMPLATE_ID)
        return result
    except:
        log.error("发送短信验证码失败！手机号：%s" % mobile)
```

在这个任务中，我们需要加载短信发送的sdk和相关的配置常量，所以我们可以直接把django中的短信发送模块和相关的常量配置文件直接剪切到当前sms任务目录中

```python
mycelery/
├── config.py
├── __init__.py
├── main.py
└── sms/
    ├── constant.py
    ├── __init__.py
    ├── tasks.py
    └── yuntongxun
        ├── CCPRestSDK.py
        ├── __init__.py
        ├── sms.py
        └── xmltojson.py
```

再次启动项目即可。



最终在django里面，我们调用Celery来异步执行任务。需要完成2个步骤：

```python
# 1. 声明一个和celery一模一样的任务函数，但是我们可以导包来解决
from mycelery.sms.tasks import send_sms

# 2. 调用任务函数，发布任务
send_sms.delay(mobile=mobile,sms_code=sms_code)
# send_sms.delay() 如果调用的任务函数没有参数，则不需要填写任何内容
```