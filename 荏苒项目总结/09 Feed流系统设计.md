# Feed流系统

## Feed流的定义

Feed流是Feed + 流，Feed的本意是饲料，Feed流的本意就是有人一直在往一个地方投递新鲜的饲料，如果需要饲料，只需要盯着投递点就可以了，这样就能源源不断获取到新鲜的饲料。 在信息工程里面，Feed其实是一个信息单元，比如一条朋友圈状态、一条微博、一条咨询或一条短视频等，所以Feed流就是不停更新的信息单元，只要关注某些发布者就能获取到源源不断的新鲜信息，我们的用户也就可以在移动设备上逐条去浏览这些信息单元。

当前最流行的Feed流产品有微博、微信朋友圈、头条的资讯推荐、快手抖音的视频推荐等，还有一些变种，比如私信、通知等，这些系统都是Feed流系统，接下来我们会介绍如何设计一个Feed流系统架构。

## Feed流系统特点

Feed流本质上是数据流，是服务端系统将 “多个发布者的信息内容” 通过 “关注收藏等关系” 推送给 “多个接收者”。

![1579146889360](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday115/day029/assets/1579146889360.png)

- 多账号内容流：Feed流系统中肯定会存在成千上万的账号，账号之间可以关注，取关，加好友和拉黑等操作。只要满足这一条，那么就可以当做Feed流系统来设计。
- 非稳定的账号关系：由于存在关注，取关等操作，所以系统中的用户之间的关系就会一直在变化，是一种非稳定的状态。
- 读写比例100:1：读写严重不平衡，读多写少。
- 消息必达性要求高：比如发送了一条朋友圈后，结果部分朋友看到了，部分朋友没看到，如果偏偏女朋友没看到，那么可能会产生很严重的感情矛盾，后果很严重。



## Feed流系统分类

Feed流的分类有很多种，但最常见的分类有两种：

- Timeline：按发布的时间顺序排序，先发布的先看到，后发布的排列在最顶端，类似于微信朋友圈，微博等。这也是一种最常见的形式。产品如果选择Timeline类型，那么就是认为`Feed流中的Feed不多，但是每个Feed都很重要，都需要用户看到`。
- Rank：按某个非时间的因子排序，一般是按照用户的喜好度排序，用户最喜欢的排在最前面，次喜欢的排在后面。这种一般假定用户可能看到的Feed非常多，而用户花费在这里的时间有限，那么就为用户选择出用户最想看的Top N结果，场景的应用场景有图片分享、新闻推荐类、商品推荐等。

上面两种是最典型，也是最常见的分类方式，另外的话，也有其他的分类标准，在其他的分类标准中的话，会多出两种类型：

- Aggregate：聚合类型，比如好几个朋友都看了同一场电影，这个就可以聚合为一条Feed：A，B，C看了电影《你的名字》，这种聚合功能比较适合在客户端做。一般的Aggregate类型是Timeline类型 + 客户端聚合。
- Notice：通知类型，这种其实已经是功能类型了，通知类型一般用于APP中的各种通知，私信等常见。这种也是Timeline类型，或者是Aggregate类型。



## 设计Feed流系统的2个核心

Feed流系统是一个数据流系统，如果要设计一个Feed流系统，最关键的两个核心，一个是数据存储(发布Feed)，一个是数据推送(读取Feed)。

这两个核心我们稍后再谈，我们先从数据层面看，数据分为三类，分别是：

- 发布者的数据：发布者发布数据，然后数据需要按照关注者进行组织，需要根据关注者查到所有数据，

  ​                          比如微博的个人页面、朋友圈的个人相册等。

- 关注关系：系统中个体间的关系，微博中是关注，是单向流，朋友圈是好友，是双向流。

  ​                   不管是单向还是双向，当发布者发布一条信息时，该条信息的流动永远是单向的。

- 粉丝的数据：从不同发布者那里获取到的数据，然后通过某种顺序（一般为时间timeline）组织到一起，

  ​                       比如微博首页、朋友圈首页等。

  ​                       这些数据具有时间热度属性，越新的数据越有价值，越新的数据就要排在最前面。

### Feed数据

针对这三类数据，我们可以定义为：

- 存储库：存储发布者的Feed数据，永久保存。我们已经存放到mysql中
- 关注表：用户关系表，永久保存。
- 同步库[未读池]:存储接收者的时间热度数据，只需要保留最近一段时间的数据即可。



### 数据存储

Feed消息的特点：

- Feed信息的最大特点就是数据量大，而且在Feed流系统里面很多时候都会选择写扩散（推模式）模式，这时候数据量会再膨胀几个数量级，所以这里的数据量很容易达到100TB，甚至PB级别。
- 数据格式简单
- 数据不能丢失，可靠性要求高
- 自增主键功能，保证个人发的Feed的消息ID在个人发件箱中都是严格递增的，这样读取时只需要一个范围读取即可。由于个人发布的Feed并发度很低，这里用时间戳也能满足基本需求，但是当应用层队列堵塞，网络延迟变大或时间回退时，用时间戳还是无法保证严格递增。这里最好是有自增功能。



根据上述这些Feed数据的特征，最佳的系统应该是`具有主键自增功能的分布式NoSQL数据库`，但是在开源系统里面没有，所以常用的做法有两种：

- 关系型数据库 + 分库分表
- 关系型数据库 + 分布式NoSQL数据库：其中 关系型数据库提供主键自增功能。

目前业界大部分著名的Feed流产品，早期都是上面的2种模式之一，但是这会存在一个非常大的问题就是关系型数据库，比如开源MySQL数据库的主键自增功能性能差。不管是用MyISAM，还是InnoDB引擎，要保证自增ID严格递增，必须使用表锁，这个粒度非常大，会严重限制并发度，影响性能。

基于上述原因，部分技术公司早已经开始考虑使用表格存储(TableStore)。

表格存储是一个具有自增主键功能的分布式NoSQL数据库，这样就只需要使用一种系统即可，除此之外表格存储还有以下的特点：

- 天然分布式数据库，`无需分库分表`，单表可达10PB，10万亿行，可支持千万级TPS/QPS
- 号称SLA可用性可达到`10个9`，Feed内容不容易丢失。
- 主键自增功能性能极佳，其他所有系统在做自增功能的时候都需要加锁，但是表格存储的主键自增功能在写入自增列行的时候，完全不需要锁，既不需要表锁，也不需要行锁。



### 数据推送

数据推送的实现，有3种方案，分别是：

- 拉方案：也称为`读扩散`。很多Feed流产品的第一版会采用这种方案，但很快就抛弃了。
- 推方案：也成为`写扩散`。Feed流系统中最常用、有效的模式，用户关系数比较均匀，或者有上限，比较出名的有微信朋友圈。
- 推拉组合：大部分用户的账号关系都是几百个，但是有个别用户是1000万以上，比如微博。

| 类型         | 推模式      | 拉模式                               | 推拉结合模式 |
| :----------- | :---------- | :----------------------------------- | :----------- |
| 写放大       | 高          | 无                                   | 中           |
| 读放大       | 无          | 高                                   | 中           |
| 用户读取延时 | 毫秒        | 秒                                   | 秒           |
| 读写比例     | 1:99        | 99:1                                 | 50:50        |
| 系统要求     | 写能力强    | 读能力强                             | 读写都适中   |
| 常见系统     | 分布式NoSQL | 内存缓存或搜索系统<br>(推荐排序场景) | 两者结合     |
| 架构复杂度   | 简单        | 复杂                                 | 更复杂       |

- 如果产品中是双向关系，那么就采用推模式。
- 如果产品中是单向关系，且用户数少于1000万，那么也采用推模式，足够了。
- 如果产品是单向关系，单用户数大于1000万，那么采用推拉结合模式，这时候可以从推模式演进过来，不需要额外重新推翻重做。
- 永远不要只用拉模式。
- 如果是一个初创企业，先用推模式，快速把系统设计出来，然后让产品去验证、迭代，等客户数大幅上涨到1000万后，再考虑升级为推拉集合模式。

所以，接下来我们选择的先是写扩散，然后推拉组合。



同步库表设计结构:

Table：user_message_table

| 主键列 | 第1列主键 | 第2列主键              | 第3列主键      | 第4列主键                                                    | 属性列                                     |
| :----- | :-------- | :--------------------- | :------------- | :----------------------------------------------------------- | :----------------------------------------- |
| 列名   | user_id   | sequence_id            | sender_id      | message_id                                                   | other                                      |
| 解释   | 接收者ID  | 消息顺序ID，要求自增。 | 发送者的用户ID | 消息ID。通过sender_id和message_id可以到存储库中查询到消息内容 | 其他字段内容，同步库中不需要包括消息内容。 |

关注或好友关系表设计结构：

Table：user_relation_table

| 主键顺序    | 第1列主键 | 第2列主键      | 属性列    | 属性列     |
| :---------- | :-------- | :------------- | :-------- | :--------- |
| Table字段名 | user_id   | follow_user_id | timestamp | other      |
| 备注        | 用户ID    | 粉丝用户ID     | 关注时间  | 其他属性列 |

未读池表设计结构：

Table: user_message_session_table

| 主键列顺序 | 第一列主键   | 属性列                                 |
| :--------- | :----------- | :------------------------------------- |
| 列名       | user_id      | last_sequence_id                       |
| 备注       | 接收者用户ID | 该接收者已经推送给客户端的最新的顺序ID |



# Feed流系统的实现前置准备

## tablestore

1. [开通阿里云表格存储服务](https://www.aliyun.com/product/ots?spm=a2c4g.11186623.2.7.6f0b23a5RBru3P)

   ![1579170876748](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday115/day029/assets/1579170876748.png)

2. 获取python操作TableStore的[SDK](https://github.com/aliyun/aliyun-tablestore-python-sdk)

   <https://help.aliyun.com/document_detail/31723.html?spm=a2c4g.11186623.6.891.563c3d76sdVMpI>

```bash
pip install tablestore
```

settings/dev.py，添加TableStore的API接口配置（使用自己的）

```python
# tablestore
OTS_ID = "LTAI4FxkXpCaQwsNTMzxGmMk"
OTS_SECRET = "AxS8Y0m3US8prS8XJuqkHDpd2XGRii"
OTS_INSTANCE = "renranzixun"
OTS_ENDPOINT = "https://renranzixun.cn-hangzhou.ots.aliyuncs.com"
```

Tablestore目前只支持四种数据类型：INTEGER、STRING、DOUBLE和BOOLEAN。其中DOUBLE类型不能做主键类型，BOOLEAN不可以做主键的第一列(分区键)。

为了方便演示,所以我们另外创建一个单独的子应用store来编写tablestore的代码.

```
cd renranapi/apps
python ../../manage.py startapp store
```

在settings/dev.py注册,

```
INSALL_APPS = [
    'store', # 用于演示tableStore，后续删除掉即可
]
```



### 表操作

> tablestore里面创建表的时候必须设置表名，主键列，还有表元信息和表的描述项[有效期，版本，吞吐量]
>
> 创建表的时候，除了主键列以外，还可以设置预设字段列，这个不常用，因为当前使用tablestore是NoSQL数据，所以我们表结构的字段列可以在添加数据的时候再指定。

视图代码:

```python
# Create your views here.
from tablestore import TableMeta,TableOptions,ReservedThroughput,CapacityUnit,OTSClient
from tablestore import PK_AUTO_INCR
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

class TableAPIView(APIView):
    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)
    def post(self,request):
        """创建表"""
        # 设置主键和字段
        table_name = "user_message_table"

        # schema_of_primary_key = [
        # ('字段名', '字段类型', PK_AUTO_INCR),
        # ('uid', 'STRING')
        # ]
        # 主键列
        schema_of_primary_key = [
            ('user_id', 'INTEGER'),
            ('sequence_id', 'INTEGER',PK_AUTO_INCR),
            ("sender_id",'INTEGER'),
            ("message_id",'INTEGER')
        ]
        # 设置表的元信息
        table_meta = TableMeta(table_name, schema_of_primary_key)
        # 设置数据的有效期
        table_option = TableOptions(7*86400, 5)
        # 设置数据的预留读写吞吐量
        reserved_throughput = ReservedThroughput(CapacityUnit(0, 0))
        try:
            # 创建数据表
            self.client.create_table(table_meta, table_option, reserved_throughput)
            return Response({"message":"create table succeeded"})
        except Exception:
            return Response({"error":"create table failed."})


    def delete(self,request):
        """删除表"""
        table = "user_message_table"
        try:
            self.client.delete_table(table)
            return Response({"message":"delete table succeeded"})
        except Exception:
            return Response({"error":"delete table failed"})

    def get(self,request):
        """列出所有的表名"""
        table_list = self.client.list_table()
        return Response({"message": table_list})
```

```
注意：
1. 创建表后需要 1 分钟进行加载，在此期间对该表的读/写数据操作均会失败。
   应用程序应该等待表加载完毕后再进行数据操作。
2. 创建表格存储的表时必须指定表的主键。
   主键包含 1~4 个主键列，每一个主键列都有名字和类型。
3.更多操作参考官方文档即可
```

路由:

```python
from django.urls import path,re_path
from . import views
urlpatterns = [
    path("table/", views.TableAPIView.as_view()),
]

# 总路由
    path('ots/', include("store.urls")),
```



### 一条数据的操作

```python
from datetime import datetime
from tablestore import Row, Condition, RowExistenceExpectation, OTSServiceError, OTSClientError


class DataAPIView(APIView):
    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def post(self, request):
        """添加数据到表格中"""
        table_name = "user_message_table"
        # 主键列－对应插入值
        primary_key = [
            # ('主键名', 值),
            ('user_id', 3),  # 接收Feed的用户ID
            ('sequence_id', PK_AUTO_INCR),  # 如果是自增主键，则值就是 PK_AUTO_INCR
            ("sender_id", 1),  # 发布Feed的用户ID
            ("message_id", 4),  # 文章ID
        ]
        # 通过主键构造行的其他数据
        attribute_columns = [
            ('recevice_time', datetime.now().timestamp()),
            ('read_status', False)
        ]
        row = Row(primary_key, attribute_columns)

        # 行条件检查为：期望行不存在。如果行存在就会报错：Condition Update Failed。（可以不设置）
        # condition = Condition(RowExistenceExpectation.EXPECT_NOT_EXIST)
        try:
            # 调用put_row方法，如果没有指定ReturnType，则return_row为None。
            consumed, return_row = self.client.put_row(table_name, row)
            return Response({"message": 'put row succeed, consume %s write cu.' % consumed.write})
        # 客户端异常，一般为参数错误或者网络异常。
        except OTSClientError as e:
            return Response({"error": "put row failed, http_status:%d, error_message:%s" % (
            e.get_http_status(), e.get_error_message())})
        # 服务端异常，一般为参数错误或者流控错误。
        except OTSServiceError as e:
            return Response(
                {"error": "put row failed, http_status:%d, error_code:%s, error_message:%s, request_id:%s" % (
                    e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id())})

    def get(self, request):
        """获取指定数据"""
        table_name = "user_message_table"

        primary_key = [('user_id', 3), ('sequence_id', 1584625817222000), ("sender_id", 1), ("message_id", 4)]

        # 需要返回的属性列：。如果columns_to_get为[]，则返回所有属性列。
        columns_to_get = []
        # columns_to_get = ['recevice_time', 'read_status', 'age', 'sex']

        try:
            consumed, return_row, next_token = self.client.get_row(table_name, primary_key, columns_to_get)

            print('Read succeed, consume %s read cu.' % consumed.read)
            print('Value of primary key: %s' % return_row.primary_key)
            print('Value of attribute: %s' % return_row.attribute_columns)
            for att in return_row.attribute_columns:
                # 打印出每一列的key，value和version值。
                print('name:%s\tvalue:%s\ttimestamp:%d' % (att[0], att[1], att[2]))
            # [('read_status', False, 1584625817222), ('recevice_time', 1584625816.642665, 1584625817222)]
            return Response({"message": "ok"})
        except:
            return Response({"error": "error"})
```

路由,代码:

```python
    path("data/", views.DataAPIView.as_view()),
```



### 多条数据的操作

```python
from tablestore import INF_MAX,INF_MIN,CompositeColumnCondition,LogicalOperator,SingleColumnCondition,ComparatorType,Direction,Condition,RowExistenceExpectation,PutRowItem
from tablestore import BatchWriteRowRequest,TableInBatchWriteRowItem
class RowAPIView(APIView):
    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    """多行数据操作"""
    def get(self,request):
        """按范围获取多行数据"""

        table_name = "user_message_table"

        # 范围查询的起始主键
        inclusive_start_primary_key = [
            ('user_id', 3),
            ('sequence_id', INF_MIN),
            ('sender_id', INF_MIN),
            ('message_id', INF_MIN)
        ]

        # 范围查询的结束主键
        exclusive_end_primary_key = [
            ('user_id', 3),
            ('sequence_id', INF_MAX),
            ('sender_id', INF_MAX),
            ('message_id', INF_MAX)
        ]

        # 查询所有列
        columns_to_get = [] # 表示返回所有列
        limit = 5

        # 设置多条件
        # cond = CompositeColumnCondition(LogicalOperator.AND) # 逻辑条件
        # cond = CompositeColumnCondition(LogicalOperator.OR)
        # cond = CompositeColumnCondition(LogicalOperator.NOT)

        # 多条件下的子条件
        # cond.add_sub_condition(SingleColumnCondition("read_status", False, ComparatorType.EQUAL)) #  比较运算符:　等于
        # cond.add_sub_condition(SingleColumnCondition("属性列", '属性值', ComparatorType.NOT_EQUAL)) #  比较运算符:　不等于
        # cond.add_sub_condition(SingleColumnCondition("属性列", '属性值', ComparatorType.GREATER_THAN)) #  比较运算符:　大于
        # cond.add_sub_condition(SingleColumnCondition("recevice_time", 1579246049, ComparatorType.GREATER_EQUAL)) #  比较运算符:　大于等于
        # cond.add_sub_condition(SingleColumnCondition("属性列", '属性值', ComparatorType.LESS_THAN)) #  比较运算符:　小于
        # cond.add_sub_condition(SingleColumnCondition("recevice_time", 1579246049, ComparatorType.LESS_EQUAL)) #  比较运算符:　小于等于

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name, # 操作表名
            Direction.FORWARD, # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key, # 取值范围
            columns_to_get, # 返回字段列
            limit, #　结果数量
            # column_filter=cond, # 条件
            max_version=1         # 返回版本数量
        )

        print("一共返回了：%s" % len(row_list))

        for row in row_list:
            print ( row.primary_key, row.attribute_columns )

        return Response({"message":"ok"})

    def post(self,request):
        """添加多条数据"""

        table_name = "user_message_table"

        put_row_items = []

        for i in range(0, 10):
            # 主键列
            primary_key = [  # ('主键名', 值),
                ('user_id', i), # 接收Feed的用户ID
                ('sequence_id', PK_AUTO_INCR), # 如果是自增主键，则值就是 PK_AUTO_INCR
                ("sender_id",1), # 发布Feed的用户ID
                ("message_id",5), # 文章ID
            ]

            attribute_columns = [('recevice_time', datetime.now().timestamp()), ('read_status', False)]
            row = Row(primary_key, attribute_columns)
            condition = Condition(RowExistenceExpectation.IGNORE)
            item = PutRowItem(row, condition)
            put_row_items.append(item)

        request = BatchWriteRowRequest()
        request.add(TableInBatchWriteRowItem(table_name, put_row_items))
        result = self.client.batch_write_row(request)
        print(result)
        print(result.is_all_succeed())

        return Response({"message":"ok"})

```

多行路由,代码:

```python
    path("row/", views.RowAPIView.as_view()),
```

## Django自定义终端命令

1. 在app子应用 home目录下创建`management`包，并在`management`包下面创建命令包目录`commands`，`commands`下面就可以创建命令模块文件了。【注意，app子应用必须注册到INSTALL_APPS应用列表中】

2. 在commands包下面创建命令文件，并在文件中声明命令类，例如：tablestore.py，代码：

   ```python
   from django.core.management import BaseCommand
   
   class Command(BaseCommand):
       help = """测试命令的帮助文档"""
   
       def add_arguments(self,parser):
           """参数设置"""
           parser.add_argument("argument",nargs="*", help="必填参数的说明") # 位置参数
           parser.add_argument("--option",'-p', default=None, help="可选参数的说明") # 选项参数
   
       def handle(self, *args, **options):
           """命令主方法
           options: 参数列表
           """
           argument = options.get("argument") # 获取位置参数
           option = options.get("option") # 获取位置参数
   
           self.stdout.write("argument: %s" % argument)
           self.stdout.write("option: %s" % option)
   
           if option is None:
               self.stdout.write("没有设置option选项参数")
   
   ```

   注意：

   ```
   1. 命令类必须继承于django.core.management.BaseCommand，并且类名必须叫Command。
   2. 命令名称就是文件名，例如，命令文件叫table，则终端下调用命令为： python manage.py table
   3. 命令参数左边加上--，则表示可选参数，可选参数建议设置默认值，方便在handle方法中判断进行默认处理。
   4. 命令参数如果没有--，则表示位置参数，则调用命令时，必须为当前命令传递参数，否则报错！
   5.示例 ：python manage.py tablestore abc c -p="hello"
   ```

   

   接下来我们直接在项目中提供TableStore的操作用于创建Feed系统的表结构。

   ```python
   from django.conf import settings
   from tablestore import OTSClient,TableMeta, CapacityUnit, TableOptions, ReservedThroughput,PK_AUTO_INCR
   class Command(BaseCommand):
       help = """表格存储命令必须接收而且只接收1个命令参数，如下：
           create  表示创建项目使用的表格
           delete  表示删除项目使用的表格
           """
   
       def add_arguments(self, parser):
           """参数设置"""
           parser.add_argument("argument", nargs="*", help="操作类型")  # 位置参数
   
       def handle(self, *args, **options):
           """表格存储的初始化"""
           argument = options.get("argument")
           if len(argument) == 1:
               if argument[0] == "create":
                   """创建表格"""
                   self.create_table()
   
               elif argument[0] == "delete":
                   """删除表格"""
                   self.delete_table()
               else:
                   self.stdout.write(self.help)
           else:
               self.stdout.write(self.help)
   
       @property
       def client(self):
           return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)
   
       def set_table(self, table_name, schema_of_primary_key, time_to_live=-1):
           # 设置表的元信息
           table_meta = TableMeta(table_name, schema_of_primary_key)
           # 设置数据的有效型
           table_option = TableOptions(time_to_live=time_to_live, max_version=5)
           # 设置数据的预留读写吞吐量
           reserved_throughput = ReservedThroughput(CapacityUnit(0, 0))
           # 创建数据
           self.client.create_table(table_meta, table_option, reserved_throughput)
   
       def create_table(self):
           # 创建存储库
           table_name = "user_message_table"
           schema_of_primary_key = [  # 主键列
               ('user_id', 'INTEGER'),
               ('sequence_id', 'INTEGER', PK_AUTO_INCR),
               ("sender_id", 'INTEGER'),
               ("message_id", 'INTEGER')
           ]
   
           self.set_table(table_name, schema_of_primary_key, time_to_live=7 * 86400)
           self.stdout.write("创建表格%s完成" % table_name)
   
           # 　关系库
           table_name = "user_relation_table"
           # 主键列
           schema_of_primary_key = [
               ('user_id', 'INTEGER'),
               ("follow_user_id", 'INTEGER'),
           ]
           self.set_table(table_name, schema_of_primary_key)
           self.stdout.write("创建表格%s完成" % table_name)
   
           # 未读池
           table_name = "user_message_session_table"
           # 主键列
           schema_of_primary_key = [
               ('user_id', 'INTEGER'),
               ("last_sequence_id", 'INTEGER'),
           ]
           self.set_table(table_name, schema_of_primary_key)
           self.stdout.write("创建表格%s完成" % table_name)
   
       def delete_table(self):
           """删除表"""
           table_list = self.client.list_table()
           for table in table_list:
               self.client.delete_table(table)
               self.stdout.write("删除%s完成" % table)
   ```

以后,我们创建项目相关的表格,就可以使用`python manage.py create`,如果删除表格则`python manage.py delete`.



## 判断访问者是否关注了作者

在文章详情页中判断当前用户是否关注了文章作者

编写tablestore的utils工具

```python
from tablestore import *
from django.conf import settings
class TableStore(object):
    """tablestore工具类"""
    def __init__(self):
        self.client = OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def get_one(self,table_name, primary_key,columns_to_get = []):
        """根据主键获取一条数据"""
        try:
            consumed, return_row, next_token = self.client.get_row(table_name, primary_key, columns_to_get)
        except:
            return {}
        if return_row is None:
            return {}
        else:
            result = return_row.primary_key + return_row.attribute_columns
            data = {}
            for item in result:
                data[item[0]] = item[1]
            return data

    def add_one(self, table_name, primary_key, attribute_columns):
        """添加一条数据"""
        row = Row(primary_key, attribute_columns)
        condition = Condition(RowExistenceExpectation.IGNORE)
        try:
            # 调用put_row方法，如果没有指定ReturnType，则return_row为None。
            consumed, return_row = self.client.put_row(table_name, row, condition)
        # 客户端异常，一般为参数错误或者网络异常。
        except OTSClientError as e:
            print(e.get_error_message())
            return False
        # 服务端异常，一般为参数错误或者流控错误。
        except OTSServiceError as e:
            print("put row failed, http_status:%d, error_code:%s, error_message:%s, request_id:%s" % (
            e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id()))
            return False
        return True

    def del_one(self, table_name, primary_key, ):
        """删除一条数据"""
        row = Row(primary_key)
        try:
            consumed, return_row = self.client.delete_row(table_name, row, None)
            # 客户端异常，一般为参数错误或者网络异常。
        except OTSClientError as e:
            print("删除数据失败!, 状态吗:%d, 错误信息:%s" % (e.get_http_status(), e.get_error_message()))
            return False
        # 服务端异常，一般为参数错误或者流控错误。
        except OTSServiceError as e:
            print("update row failed, http_status:%d, error_code:%s, error_message:%s, request_id:%s" % (
            e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id()))
            return False
        return True
```



serializers 序列化器

```python
from users.models import User
class AuthorModelSerializer(serializers.ModelSerializer):
    """文章作者"""
    class Meta:
        model = User
        fields = ["id","nickname","avatar","money"] # 自己编写需要显示的字段即可

from .models import ArticleCollection
class CollectionInfoModelSerializer(serializers.ModelSerializer):
    """文集信息"""
    class Meta:
        model = ArticleCollection
        fields = ["id","name"] # 自己编写需要显示的字段即可

from renranapi.utils.tablestore import TableStore
class ArticleInfoModelSerializer(serializers.ModelSerializer):
    user = AuthorModelSerializer()
    collection = CollectionInfoModelSerializer()
    focus = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = [
            "name", "render","content", "user",
            "collection", "updated_time",
            "read_count", "like_count",
            "collect_count", "comment_count",
            "reward_count","focus"
        ]

    def get_focus(self, obj):
        """
        获取当前用户是否关注了文章作者
        (-1,"访问者和文章作者是同一个人")
        (0,"未关注")
        (1,"关注了")
        :param obj:当前文章对象
        :return:
        """
        # 访问者没有登陆
        focus = 0  # 当前访问者没有登陆,默认没有关注
        user = self.context["request"].user
        if isinstance(user, User):
            # 判断访问者是否曾经关注过作者
            author = obj.user
            # 如果访问者和文章作者是同一个人,则不存在关注
            if author.id == user.id:
                focus = -1
            else:
                # 从关系库中获取当前访问者与作者之间的关注关系
                ts = TableStore()
                data = ts.get_one(
                    "user_relation_table",
                    [('user_id', author.id), ('follow_user_id', user.id)])

                if data:
                    # 已经登陆并且关注了
                    focus = 1
                else:
                    # 已经登陆了,没有关注
                    focus = 0
        return focus

```



article/views.py,代码;

```python
from rest_framework.generics import RetrieveAPIView
from .serializers import ArticleInfoModelSerializer
class ArticleInfoAPIView(RetrieveAPIView):
    """文章详情信息"""
    serializer_class = ArticleInfoModelSerializer
    queryset = Article.objects.filter(is_public=True)
```

urls路由

```python
# 获取文章详细内容
re_path("^detail/(?P<pk>\d+)/$", views.ArticleInfoAPIView.as_view()),
```

在客户端中根据返回的关注状态`focus`来判断显示关注按钮

```vue
<button data-locale="zh-CN" type="button" class="_3kba3h _1OyPqC _3Mi9q9 _34692-" v-if="article.focus===1" @mouseover="user_focus_text='取消关注'" @mouseout="user_focus_text='已关注'" @click="change_focus(article.focus)"><span>{{user_focus_text}}</span></button>
                  <button data-locale="zh-CN" type="button" class="_3kba3h _1OyPqC _3Mi9q9 _34692-" v-if="article.focus===0" @click="change_focus(article.focus)"><span>关注</span></button>
```



## 用户关注或取消关注文章的作者

服务端实现用户关注作者的api接口

users/views.py,代码:

```python
from users.models import User
from renranapi.utils.tablestore import TableStore
class UserFocusAPIView(APIView):
    """关注和取消关注"""
    permission_classes = [IsAuthenticated]
    def post(self,request):
        # 关注者[粉丝]
        user = request.user
        # 作者
        author_id = request.data.get("author_id")
        try:
            User.objects.get(pk=author_id)
        except User.DoesNotExist:
            return Response("对不起, 您关注的用户不存在!",status=status.HTTP_404_NOT_FOUND)

        # 获取关注状态[0表示关注,1表示取消关注]
        focus = request.data.get("focus")
        ts = TableStore()
        if not focus:
            """关注"""
            ret = ts.add_one(
                "user_relation_table",
                [('user_id', author_id), ('follow_user_id', user.id)],
                [('focus_time', datetime.now().timestamp())]),
        else:
            """取消关注"""
            ret = ts.del_one("user_relation_table",
                [('user_id', author_id), ('follow_user_id', user.id)])

        if ret:
            return Response("操作成功!")
        else:
            return Response("操作失败!",status=status.HTTP_400_BAD_REQUEST)
```

路由代码:

```python
path("focus/", views.UserFocusAPIView.as_view()),
```

客户端发送请求,申请 关注/取消关注

```vue
<template>
  <div class="_21bLU4 _3kbg6I" @click.stop="is_show_reward_window=false">
    <Header></Header>
    <div class="_3VRLsv" role="main">
      <div class="_gp-ck">
        <section class="ouvJEz">
          <h1 class="_1RuRku">{{article.name}}</h1>
          <div class="rEsl9f">
            <div class="_2mYfmT">
              <router-link to="" class="_1OhGeD"><img class="_13D2Eh" :src="article.user.avatar" alt=""/></router-link>
              <div style="margin-left: 8px;">
                <div class="_3U4Smb">
                  <span class="FxYr8x"><a class="_1OhGeD" href="">{{article.user.nickname}}</a></span>
                  <button data-locale="zh-CN" type="button" class="_3kba3h _1OyPqC _3Mi9q9 _34692-" v-if="article.focus===1" @mouseover="user_focus_text='取消关注'" @mouseout="user_focus_text='已关注'" @click="change_focus(article.focus)"><span>{{user_focus_text}}</span></button>
                  <button data-locale="zh-CN" type="button" class="_3kba3h _1OyPqC _3Mi9q9 _34692-" v-if="article.focus===0" @click="change_focus(article.focus)"><span>关注</span></button>
                </div>
                <div class="s-dsoj">
                  <time :datetime="article.updated_time">{{article.updated_time|timeformat}}</time>
                  <span>字数 {{article.content && article.content.length}}</span>
                  <span>阅读 {{article.read_count}}</span>
                </div>
              </div>
            </div>
          </div>

          <div>
            <mavon-editor
              class="md v-show-content v-note-panel"
              :value="article.render"
              :subfield="prop.subfield"
              :defaultOpen="prop.defaultOpen"
              :toolbarsFlag="prop.toolbarsFlag"
              :editable="prop.editable"
              :scrollStyle="prop.scrollStyle"
              :previewBackground="prop.previewBackground"
              :boxShadow="false"
            ></mavon-editor>
          </div>
          <div class="_1kCBjS">
            <div class="_18vaTa">
              <div class="_3BUZPB">
                <div class="_2Bo4Th" role="button" tabindex="-1" aria-label="给文章点赞">
                  <i aria-label="ic-like" class="anticon">
                    <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
                      <use xlink:href="#ic-like"></use>
                    </svg>
                  </i>
                </div>
                <span class="_1LOh_5" role="button" tabindex="-1" aria-label="查看点赞列表">{{article.like_count}}人点赞<i
                  aria-label="icon: right" class="anticon anticon-right">
           <svg viewbox="64 64 896 896" focusable="false" class="" data-icon="right" width="1em" height="1em"
                fill="currentColor" aria-hidden="true">
            <path
              d="M765.7 486.8L314.9 134.7A7.97 7.97 0 0 0 302 141v77.3c0 4.9 2.3 9.6 6.1 12.6l360 281.1-360 281.1c-3.9 3-6.1 7.7-6.1 12.6V883c0 6.7 7.7 10.4 12.9 6.3l450.8-352.1a31.96 31.96 0 0 0 0-50.4z"></path>
           </svg></i></span>
              </div>
              <div class="_3BUZPB">
                <div class="_2Bo4Th" role="button" tabindex="-1">
                  <i aria-label="ic-dislike" class="anticon">
                    <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
                      <use xlink:href="#ic-dislike"></use>
                    </svg>
                  </i>
                </div>
              </div>
            </div>
            <div class="_18vaTa">
              <a class="_3BUZPB _1x1ok9 _1OhGeD" href="/nb/38290018" target="_blank" rel="noopener noreferrer"><i
                aria-label="ic-notebook" class="anticon">
                <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
                  <use xlink:href="#ic-notebook"></use>
                </svg>
              </i><span>{{article.collection.name}}</span></a>
              <div class="_3BUZPB ant-dropdown-trigger">
                <div class="_2Bo4Th">
                  <i aria-label="ic-others" class="anticon">
                    <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
                      <use xlink:href="#ic-others"></use>
                    </svg>
                  </i>
                </div>
              </div>
            </div>
          </div>
          <div class="_19DgIp" style="margin-top:24px;margin-bottom:24px"></div>
          <div class="_13lIbp">
            <div class="_191KSt">
              &quot;小礼物走一走，来简书关注我&quot;
            </div>
            <button type="button" class="_1OyPqC _3Mi9q9 _2WY0RL _1YbC5u" @click.stop="is_show_reward_window=true">
              <span>赞赏支持</span></button>
            <span class="_3zdmIj" v-if="article.reward_count>0">已经有{{article.reward_count}}人赞赏，支持一下</span>
            <span class="_3zdmIj" v-else>还没有人赞赏，支持一下</span>
          </div>
          <div class="d0hShY">
            <a class="_1OhGeD" href="/u/a70487cda447" target="_blank" rel="noopener noreferrer"><img class="_27NmgV"
                                                                                                     :src="article.user.avatar"
                                                                                                     alt="  "/></a>
            <div class="Uz-vZq">
              <div class="Cqpr1X">
                <a class="HC3FFO _1OhGeD" href="/u/a70487cda447" :title="article.user.nickname" target="_blank"
                   rel="noopener noreferrer">{{article.user.nickname}}</a>
                <span class="_2WEj6j" title="你读书的样子真好看。">你读书的样子真好看。</span>
              </div>
              <div class="lJvI3S">
                <span>总资产0</span>
                <span>共写了78.7W字</span>
                <span>获得6,072个赞</span>
                <span>共1,308个粉丝</span>
              </div>
            </div>
            <button data-locale="zh-CN" type="button" class="_1OyPqC _3Mi9q9"><span>关注</span></button>
          </div>
        </section>
        <div id="note-page-comment">
          <div class="lazyload-placeholder"></div>
        </div>
      </div>
      <aside class="_2OwGUo">
        <section class="_3Z3nHf">
          <div class="_3Oo-T1">
            <a class="_1OhGeD" href="/u/a70487cda447" target="_blank" rel="noopener noreferrer"><img class="_3T9iJQ"
                                                                                                     :src="article.user.avatar"
                                                                                                     alt=""/></a>
            <div class="_32ZTTG">
              <div class="_2O0T_w">
                <div class="_2v-h3G">
                  <span class="_2vh4fr" :title="article.user.nickname"><a class="_1OhGeD" href="/u/a70487cda447"
                                                                          target="_blank" rel="noopener noreferrer">{{article.user.nickname}}</a></span>
                </div>
                <button data-locale="zh-CN" type="button" class="tzrf9N _1OyPqC _3Mi9q9 _34692-"><span>关注</span>
                </button>
              </div>
              <div class="_1pXc22">
                总资产:{{article.user.money}}元
              </div>
            </div>
          </div>
          <div class="_19DgIp"></div>
        </section>
        <div>
          <div class="">
            <section class="_3Z3nHf">
              <h3 class="QHRnq8 QxT4hD"><span>推荐阅读</span></h3>
              <div class="cuOxAY" role="listitem">
                <div class="_3L5YSq" title="这些话没人告诉你，但必须知道的社会规则">
                  <a class="_1-HJSV _1OhGeD" href="/p/a3e56a0559ff" target="_blank" rel="noopener noreferrer">这些话没人告诉你，但必须知道的社会规则</a>
                </div>
                <div class="_19haGh">
                  阅读 5,837
                </div>
              </div>
              <div class="cuOxAY" role="listitem">
                <div class="_3L5YSq" title="浙大学霸最美笔记曝光：真正的牛人，都“变态”到了极致">
                  <a class="_1-HJSV _1OhGeD" href="/p/d2a3724e2839" target="_blank" rel="noopener noreferrer">浙大学霸最美笔记曝光：真正的牛人，都“变态”到了极致</a>
                </div>
                <div class="_19haGh">
                  阅读 12,447
                </div>
              </div>
              <div class="cuOxAY" role="listitem">
                <div class="_3L5YSq" title="征服一个女人最好的方式：不是讨好她，而是懂得去折腾她">
                  <a class="_1-HJSV _1OhGeD" href="/p/f6acf67f039b" target="_blank" rel="noopener noreferrer">征服一个女人最好的方式：不是讨好她，而是懂得去折腾她</a>
                </div>
                <div class="_19haGh">
                  阅读 5,311
                </div>
              </div>
              <div class="cuOxAY" role="listitem">
                <div class="_3L5YSq" title="告别平庸的15个小方法">
                  <a class="_1-HJSV _1OhGeD" href="/p/cff7eb6b232b" target="_blank" rel="noopener noreferrer">告别平庸的15个小方法</a>
                </div>
                <div class="_19haGh">
                  阅读 7,040
                </div>
              </div>
              <div class="cuOxAY" role="listitem">
                <div class="_3L5YSq" title="轻微抑郁的人，会说这3句“口头禅”，若你一个不占，偷着乐吧">
                  <a class="_1-HJSV _1OhGeD" href="/p/2a0ca1729b4b" target="_blank" rel="noopener noreferrer">轻微抑郁的人，会说这3句“口头禅”，若你一个不占，偷着乐吧</a>
                </div>
                <div class="_19haGh">
                  阅读 16,411
                </div>
              </div>
            </section>
          </div>
        </div>
      </aside>
    </div>

    <div class="_23ISFX-body" v-if="is_show_reward_window" @click.stop="is_show_reward_window=true">
      <div class="_3uZ5OL">
        <div class="_2PLkjk">
          <img class="_2R1-48" src="" alt=""/>
          <div class="_2h5tnQ">
            给作者送糖
          </div>
        </div>
        <div class="_1-bCJJ">
          <div class="LMa6S_" :class="reward_info.money==num?'_1vONvL':''" @click="reward_info.money=num"
               v-for="num in reward_list"><span>{{num}}</span></div>
        </div>
        <textarea class="_1yN79W" placeholder="给Ta留言..." v-model="reward_info.content"></textarea>
        <div class="_1_B577">
          选择支付方式
        </div>
        <div class="_1-bCJJ">
          <div class="LMa6S_ _3PA8BN" :class="reward_info.pay_type==key?'_1vONvL':''"
               @click="reward_info.pay_type=key" v-for="type,key in pay_type_list"><span>{{type}}</span></div>
        </div>
        <button type="button" class="_3A-4KL _1OyPqC _3Mi9q9 _1YbC5u" @click="payhandler">
          <span>确认支付</span><span> ￥</span>{{reward_info.money}}
        </button>
      </div>
    </div>

    <Footer></Footer>
  </div>
</template>

<script>
    import Header from "./common/Header";
    import Footer from "./common/Footer";
    import {mavonEditor} from 'mavon-editor'
    import 'mavon-editor/dist/css/index.css'

    export default {
        name: "Article",
        components: {
            Header,
            Footer,
        },
        data() {
            return {
                token: "",
                article_id: 0,
                is_show_reward_window: false,
                user_focus_text:"已关注",
                article: {
                    user: {},
                    collection: {},
                },
                reward_list: [2, 5, 10, 20, 50, 100],
                pay_type_list: ["支付宝", "余额支付"],
                reward_info: {
                    money: 2,
                    content: "",
                    pay_type: 0,
                }
            }
        },
        computed: {
            prop() {
                let markdown_data = {
                    subfield: false,// 单双栏模式
                    defaultOpen: 'preview',//edit： 默认展示编辑区域 ， preview： 默认展示预览区域
                    editable: false,
                    toolbarsFlag: false,
                    scrollStyle: true,
                    previewBackground: '#FFFFFF'
                };
                return markdown_data
            }
        },
        created() {
            this.token = localStorage.user_token || sessionStorage.user_token;
            this.article_id = this.$route.params.id;
            this.get_article();
        },
        filters: {
            timeformat(time) {
                if (time) {
                    return time.split(".")[0].replace("T", " ");
                }
            }
        },
        methods: {
            get_article() {
                // 获取文章信息
                if (this.token) {
                    this.$axios.get(`${this.$settings.Host}/article/detail/${this.article_id}/`, {
                        headers: {
                            Authorization: "jwt " + this.token,
                        }
                    }).then(response => {
                        this.article = response.data;
                    }).catch(error => {
                        this.$message.error("当前文章已删除!");
                        this.$router.go(-1);
                    });
                } else {
                    this.$axios.get(`${this.$settings.Host}/article/detail/${this.article_id}/`).then(response => {
                        this.article = response.data;
                    }).catch(error => {
                        this.$message.error("当前文章已删除!");
                        this.$router.go(-1);
                    });
                }
            },
            payhandler() {
                // 支付处理
                this.reward_info.article_id = this.article_id;
                this.$axios.post(`${this.$settings.Host}/payments/alipay/`, this.reward_info, {
                    headers: {
                        Authorization: "jwt " + this.token,
                    }
                }).then(response => {
                    location.href = response.data;
                }).catch(error => {
                    this.$message.error("发起打赏请求失败!");
                })

            },
            change_focus(focus_status) {
                // 关注
                this.token = this.$settings.check_user_login();
                if (this.token) {
                    // 已经登陆的情况下
                    // 发送ajax
                    this.$axios.post(`${this.$settings.Host}/article/focus/`, {
                        author_id: this.article.user.id,
                        focus: focus_status, // 这里提供给服务端
                    }, {
                        headers: {
                            Authorization: "jwt " + this.token,
                        }
                    }).then(response => {
                        if (focus_status) {
                            this.article.focus = 0;
                        } else {
                            this.article.focus = 1; // 这里提供给客户端判断用的
                            this.user_focus_text = "已关注";
                        }

                    }).catch(error => {
                        this.$message.error("关注失败!");
                    })

                }
            },
        }

    }
</script>
```



## 作者发布文章以后, 推送Feed流

+ views视图

  ```python
  from rest_framework.views import APIView
  from rest_framework import status
  import logging
  from renranapi.utils.tablestore import TableStore
  from tablestore import *
  
  class ArticlePublicStatusAPIView(APIView):
      """切换文章的发布状态"""
      permission_classes = [IsAuthenticated]
  
      def put(self, request, pk):
          user = request.user
          try:
              article = Article.objects.get(pk=pk, user=user)
          except Article.DoesNotExist:
              return Response("对不起,当前文章不存在!", status=status.HTTP_400_BAD_REQUEST)
          article.is_public = not article.is_public
          article.pub_date = None
          article.save()
  
          # 获取当前作者的粉丝列表
          fans_list = self.get_fans_list(article.user.id)
          if article.is_public:
              """在作者发布内容以后, 把feed推送粉丝"""
              ret = self.push_feed(article.user.id, article.id, fans_list)
              if not ret:
                  logging.error("推送Feed失败!")
          return Response("操作成功!")
  
      def push_feed(self, author_id, message_id, fans_list):
          """推送Feed流"""
          put_row_items = []
          ts = TableStore()
          for fans in fans_list:
              primary_key = [  # ('主键名', 值),
                  ('user_id', fans),  # 接收Feed的用户ID
                  ('sequence_id', PK_AUTO_INCR),  # 如果是自增主键，则值就是 PK_AUTO_INCR
                  ("sender_id", author_id),  # 发布Feed的用户ID
                  ("message_id", message_id),  # 文章ID
              ]
              attribute_columns = [('recevice_time', datetime.now().timestamp()), ('read_status', False)]
              put_row_items.append( ts.add_all(primary_key, attribute_columns) )
  
          return ts.do_all("user_message_table", put_row_items)
  
  
      def get_fans_list(self, author_id):
          """获取作者的粉丝"""
          print("author",author_id)
          ts = TableStore()
          inclusive_start_primary_key = [
              ('user_id', author_id),
              ('follow_user_id', INF_MIN),
          ]
  
          # 范围查询的结束主键
          exclusive_end_primary_key = [
              ('user_id', author_id),
              ('follow_user_id', INF_MAX),
          ]
          ret = ts.get_all("user_relation_table",inclusive_start_primary_key, exclusive_end_primary_key)
          fans_list = []
          if len(ret) > 0:
              for item in ret:
                  fans_list.append(item["follow_user_id"])
          return fans_list
  
  ```

+ tablestore的utils工具

  ```python
  from tablestore import *
  from django.conf import settings
  class TableStore(object):
      """tablestore工具类"""
      def __init__(self):
          self.client = OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)
  
      def get_one(self,table_name, primary_key,columns_to_get = []):
          """根据主键获取一条数据"""
          try:
              consumed, return_row, next_token = self.client.get_row(table_name, primary_key, columns_to_get)
          except:
              return {}
          if return_row is None:
              return {}
          else:
              result = return_row.primary_key + return_row.attribute_columns
              data = {}
              for item in result:
                  data[item[0]] = item[1]
              return data
  
      def add_one(self, table_name, primary_key, attribute_columns):
          """添加一条数据"""
          row = Row(primary_key, attribute_columns)
          condition = Condition(RowExistenceExpectation.IGNORE)
          try:
              # 调用put_row方法，如果没有指定ReturnType，则return_row为None。
              consumed, return_row = self.client.put_row(table_name, row, condition)
          # 客户端异常，一般为参数错误或者网络异常。
          except OTSClientError as e:
              print(e.get_error_message())
              return False
          # 服务端异常，一般为参数错误或者流控错误。
          except OTSServiceError as e:
              print("put row failed, http_status:%d, error_code:%s, error_message:%s, request_id:%s" % (
              e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id()))
              return False
          return True
  
      def del_one(self, table_name, primary_key, ):
          """删除一条数据"""
          row = Row(primary_key)
          try:
              consumed, return_row = self.client.delete_row(table_name, row, None)
              # 客户端异常，一般为参数错误或者网络异常。
          except OTSClientError as e:
              print("删除数据失败!, 状态吗:%d, 错误信息:%s" % (e.get_http_status(), e.get_error_message()))
              return False
          # 服务端异常，一般为参数错误或者流控错误。
          except OTSServiceError as e:
              print("update row failed, http_status:%d, error_code:%s, error_message:%s, request_id:%s" % (
              e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id()))
              return False
          return True
  
  
      def get_all(self, table_name, inclusive_start_primary_key, exclusive_end_primary_key, limit=None,columns_to_get = None, cond=None):
          """获取多条数据"""
          consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
              table_name,  # 操作表明
              Direction.FORWARD,  # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
              inclusive_start_primary_key, exclusive_end_primary_key,  # 取值范围
              columns_to_get,  # 返回字段列
              limit,  # 结果数量
              column_filter=cond, # 条件
              max_version=1  # 返回版本数量
          )
  
          if len(row_list) > 0:
              data = []
              for row in row_list:
                  result = row.primary_key + row.attribute_columns
                  item_data = {}
                  data.append(item_data)
                  for item in result:
                      item_data[item[0]] = item[1]
              return data
          else:
              return []
  
      def do_all(self,table_name,put_row_items=[]):
          """操作多条数据"""
          request = BatchWriteRowRequest()
          request.add(TableInBatchWriteRowItem(table_name, put_row_items))
          result = self.client.batch_write_row(request)
          return result.is_all_succeed()
  
      def add_all(self,primary_key,attribute_columns):
          """添加多条数据"""
          row = Row(primary_key, attribute_columns)
          condition = Condition(RowExistenceExpectation.IGNORE)
          item = PutRowItem(row, condition)
          return item
  
      def del_all(self,primary_key):
          """删除多条数据"""
          row = Row(primary_key)
          condition = Condition(RowExistenceExpectation.IGNORE)
          item = DeleteRowItem(row, condition)
          return item
  ```

+ urls 路由

  ```python
  # 切换文章发布状态
      re_path("^public/(?P<pk>\d+)/$", views.ArticlePublicStatusAPIView.as_view()),
  ```

  

## 首页数据内容展示

首页数据在Feed流系统中, 需要考虑2大问题:

针对没有登录的游客显示内容的问题:

1. 纯粹的游客
2. 已经注册但是没有关注过任何作者

```
解决:
   1. 从数据库查找到热门内容推送给用户[评论量高的, 赞赏量高的, 点赞量高的]
      如果是登录用户, 在查看了内容后, 针对用户ID保存查看记录, 哪一篇用户看过了就记录到tablestore里面
      如果是游客, 1. 在本地存储中,记录用户的浏览历史
                 2. 在tablestore里面记录当前IP的浏览历史

```



针对登录的用户显示内容的问题:

1. 用户关注了很多作者 
2. 用户关注了作者很少, 这些作者可能没有新的内容产生



```python
解决推送内容不足的情况, 接下来我们可以根据用户行为进行分析的实现基于物品的协同过滤算法来计算出用户的兴趣, 进行智能推荐.

```

综合上面所述,我们必须要显示首页的内容先然后对显示的内容进行一下步骤的过滤

```
1. 判断用户是否登录
   1.1. 用户登录了
        1.1.1 用户已经关注了其他作者
          1.1.1.1 用户关注作者中,有足够的内容展示给用户
          1.1.1.2 用户关注作者中,没有足够内容展示给用户
        1.1.2 用户没有关注任何的作者
          1.1.1.1 根据浏览历史查找内容进行热度推荐
   1.2. 用户未登录
        1.1.3 根据浏览历史查找内容进行热度推荐

```



### 客户端根据用户的登录状态发起请求获取数据

```vue
<template>
  <div id="home">
    <Header></Header>
    <div class="container">
      <div class="row">
        <div class="main">
          <!-- Banner -->
          <div class="banner">
            <el-carousel height="272px" indicator-position="none" interval="2000">
              <el-carousel-item v-for="item in 4" :key="item">
                <h3 class="small">{{ item }}</h3>
              </el-carousel-item>
            </el-carousel>
          </div>
          <div id="list-container">
            <!-- 文章列表模块 -->
            <ul class="note-list">
              <li class="">
                <div class="content">
                  <a class="title" target="_blank" href="">常做此运动，让你性福加倍</a>
                  <p class="abstract">运动，是人类在发展过程中有意识地对自己身体素质的培养的各种活动 运动的方式多种多样 不仅仅是我们常知的跑步，球类，游泳等 今天就为大家介绍一种男...</p>
                  <div class="meta">
                    <span class="jsd-meta">
                      <img src="/static/image/paid1.svg" alt=""> 4.8
                    </span>
                    <a class="nickname" target="_blank" href="">上班族也健身</a>
                    <a target="_blank" href="">
                      <img src="/static/image/comment.svg" alt=""> 4
                    </a>
                    <span><img src="/static/image/like.svg" alt=""> 31</span>
                  </div>
                </div>
              </li>
              <li class="have-img">
                <a class="wrap-img" href="" target="_blank">
                  <img class="img-blur-done" src="/static/image/10907624-107943365323e5b9.jpeg" />
                </a>
                <div class="content">
                  <a class="title" target="_blank" href="">“不耻下问”，正在毁掉你的人生</a>
                  <p class="abstract">
                    在过去，遇到不懂的问题，你不耻下问，找个人问问就行；在现在，如果你还这么干，多半会被认为是“搜商低”。 昨天，35岁的表姐把我拉黑了。 表姐是医...
                  </p>
                  <div class="meta">
                    <span class="jsd-meta">
                      <img src="/static/image/paid1.svg" alt=""> 6.7
                    </span>
                    <a class="nickname" target="_blank" href="">_飞鱼</a>
                    <a target="_blank" href="">
                      <img src="/static/image/comment.svg" alt=""> 33
                    </a>
                    <span><img src="/static/image/like.svg" alt=""> 113</span>
                    <span><img src="/static/image/shang.svg" alt=""> 2</span>
                  </div>
                </div>
              </li>
            </ul>
            <!-- 文章列表模块 -->
          </div>
        <a href="" class="load-more">阅读更多</a></div>
        <div class="aside">
          <!-- 推荐作者 -->
          <div class="recommended-author-wrap">
            <!---->
            <div class="recommended-authors">
              <div class="title">
                <span>推荐作者</span>
                <a class="page-change"><img class="icon-change" src="/static/image/exchange-rate.svg" alt="">换一批</a>
              </div>
              <ul class="list">
                <li>
                  <a href="" target="_blank" class="avatar">
                    <img src="/static/image/avatar.webp" />
                  </a>
                  <a class="follow" state="0"><img src="/static/image/follow.svg" alt="" />关注</a>
                  <a href="" target="_blank" class="name">董克平日记</a>
                  <p>写了807.1k字 · 2.5k喜欢</p>
                </li>
                <li>
                  <a href="" target="_blank" class="avatar">
                    <img src="/static/image/avatar.webp" />
                  </a>
                  <a class="follow" state="0"><img src="/static/image/follow.svg" alt="" />关注</a>
                  <a href="" target="_blank" class="name">董克平日记</a>
                  <p>写了807.1k字 · 2.5k喜欢</p>
                </li>

              </ul>
              <a href="" target="_blank" class="find-more">查看全部 ></a>
              <!---->
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>
<script>
  import Header from "./common/Header";
  import Footer from "./common/Footer";
  export default {
      name:"Home",
      data(){
          return {
            token:{},
            article_list:[]
          }
      },
      created(){
        this.token = this.get_login_user();
        this.get_article_list()
      },
      methods:{
          get_login_user(){
            // 获取登录用户
            return localStorage.user_token || sessionStorage.user_token;
          },
          get_article_list(){
            // 获取推送文章
            let headers = {};
            if(this.token){
              headers = {
                Authorization:"jwt " +this.token,
              }
            }
            this.$axios.get(`${this.$settings.Host}/home/article/`,{
              headers
            }).then(response=>{
              this.article_list = response.data;
            }).catch(eror=>{
              this.$message.error("获取推送文章失败！");
            });
          }
      },
      components:{
        Header,
        Footer,
      }
  }
</script>


```



### 服务端提供推送文章的内容

home/views.py,代码:

```python
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from article.models import Article
from .serializers import ArticleListModelSerializer
from .paginations import HomeArticlePageNumberPagination
from django.db.models import QuerySet
class ArticleListAPIView(ListAPIView):
    serializer_class = ArticleListModelSerializer
    pagination_class = HomeArticlePageNumberPagination

    def get_queryset(self):
        queryset = Article.objects.exclude(pub_date=None,).order_by("-reward_count","-comment_count","-like_count","-id")
        return queryset   

```

home/paginations.py,代码:

```python
from rest_framework.pagination import PageNumberPagination
class HomeArticlePageNumberPagination(PageNumberPagination):
    """首页推送文章的分页器"""
    page_query_param = "page" # 地址上面代表页码的参数名
    max_page_size = 20 # 每一页显示的最大数据量
    page_size = 10     # 默认每一页显示的数据量
    page_size_query_param = "size" # 地址上面代表数据量的参数名

```

home/serializers.py,代码:

```python
from rest_framework import serializers
from article.models import Article
from users.models import User
class ArticleAuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id","nickname"]
        model = User
class ArticleListModelSerializer(serializers.ModelSerializer):
    user = ArticleAuthorModelSerializer()
    class Meta:
        model = Article
        fields = ["id","title","content","user","like_count","reward_count","comment_count"]

```

home/urls.py 子应用路由和总路由

```python
from django.urls import path
from . import views
urlpatterns = [
    path("article/", views.ArticleListAPIView.as_view() ),
]

# 总路由
    path('home/', include("home.urls")),

```



客户端展示内容 

```vue
<template>
  <div id="home">
    <Header></Header>
    <div class="container">
      <div class="row">
        <div class="main">
          <!-- Banner -->
          <div class="banner">
            <el-carousel height="272px" indicator-position="none" :interval="2000">
              <el-carousel-item v-for="item in 4" :key="item">
                <h3 class="small">{{ item }}</h3>
              </el-carousel-item>
            </el-carousel>
          </div>
          <div id="list-container">
            <!-- 文章列表模块 -->
            <ul class="note-list">
<!--              <li class="">-->
<!--                <div class="content">-->
<!--                  <a class="title" target="_blank" href="">常做此运动，让你性福加倍</a>-->
<!--                  <p class="abstract">运动，是人类在发展过程中有意识地对自己身体素质的培养的各种活动 运动的方式多种多样 不仅仅是我们常知的跑步，球类，游泳等 今天就为大家介绍一种男...</p>-->
<!--                  <div class="meta">-->
<!--                    <span class="jsd-meta">-->
<!--                      <img src="/static/image/paid1.svg" alt=""> 4.8-->
<!--                    </span>-->
<!--                    <a class="nickname" target="_blank" href="">上班族也健身</a>-->
<!--                    <a target="_blank" href="">-->
<!--                      <img src="/static/image/comment.svg" alt=""> 4-->
<!--                    </a>-->
<!--                    <span><img src="/static/image/like.svg" alt=""> 31</span>-->
<!--                  </div>-->
<!--                </div>-->
<!--              </li>-->
              <li :class="check_img(article.content)?'have-img':''" v-for="article in article_list">
                <a class="wrap-img" href="" target="_blank" v-if="check_img(article.content)">
                  <img class="img-blur-done" :src="check_img(article.content)" />
                </a>
                <div class="content">
                  <router-link class="title" target="_blank" :to="`/article/${article.id}`">{{article.title}}</router-link>
                  <p class="abstract"　v-html="subtext(article.content,120)">
                  </p>
                  <div class="meta">
                    <a class="nickname" target="_blank" href="">{{article.user.nickname}}</a>
                    <a target="_blank" href="">
                      <img src="/static/image/comment.svg" alt=""> {{article.comment_count}}
                    </a>
                    <span><img src="/static/image/like.svg" alt=""> {{article.like_count}}</span>
                    <span v-if="article.reward_count>0"><img src="/static/image/shang.svg" alt=""> {{article.reward_count}}</span>
                  </div>
                </div>
              </li>
            </ul>
            <!-- 文章列表模块 -->
          </div>
        <a href="" class="load-more">阅读更多</a></div>
        <div class="aside">
          <!-- 推荐作者 -->
          <div class="recommended-author-wrap">
            <!---->
            <div class="recommended-authors">
              <div class="title">
                <span>推荐作者</span>
                <a class="page-change"><img class="icon-change" src="/static/image/exchange-rate.svg" alt="">换一批</a>
              </div>
              <ul class="list">
                <li>
                  <a href="" target="_blank" class="avatar">
                    <img src="/static/image/avatar.webp" />
                  </a>
                  <a class="follow" state="0"><img src="/static/image/follow.svg" alt="" />关注</a>
                  <a href="" target="_blank" class="name">董克平日记</a>
                  <p>写了807.1k字 · 2.5k喜欢</p>
                </li>
                <li>
                  <a href="" target="_blank" class="avatar">
                    <img src="/static/image/avatar.webp" />
                  </a>
                  <a class="follow" state="0"><img src="/static/image/follow.svg" alt="" />关注</a>
                  <a href="" target="_blank" class="name">董克平日记</a>
                  <p>写了807.1k字 · 2.5k喜欢</p>
                </li>

              </ul>
              <a href="" target="_blank" class="find-more">查看全部 ></a>
              <!---->
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>
<script>
  import Header from "./common/Header";
  import Footer from "./common/Footer";
  export default {
      name:"Home",
      data(){
          return {
            token:{},
            article_list:[
              {
                "user":{

                }
              }
            ]
          }
      },
      created(){
        this.token = this.get_login_user();
        this.get_article_list()
      },
      methods:{
          subtext(content,len=100){
            // 如果文章开头有图片，则过滤图片
            if(content){
              while (content.search("<img") != -1){
                content = content.replace(/<img.*?src="(.*?)".*?>/,"")
              }
              return content.split("").slice(0,len).join("")+'...';
            }
            return "";
          },
          check_img(content){
            if(content){
              let ret = content.match(/<img.*?src="(.*?)".*?>/)
              if(ret){
                return ret[1];
              }
            }

            return false;

          },
          get_login_user(){
            // 获取登录用户
            return localStorage.user_token || sessionStorage.user_token;
          },
          get_article_list(){
            // 获取推送文章
            let headers = {};
            if(this.token){
              headers = {
                Authorization:"jwt " +this.token,
              }
            }
            this.$axios.get(`${this.$settings.Host}/home/article/`,{
              headers
            }).then(response=>{
              this.article_list = response.data.results;
              this.article_count = response.data.count;
              this.new_article_list = response.data.next;
            }).catch(eror=>{
              this.$message.error("获取推送文章失败！");
            });
          }
      },
      components:{
        Header,
        Footer,
      }
  }
</script>

```

使用函数节流, 在用户频繁点击ajax按钮时, 阻止点击

```vue
<template>
  <div id="home">
    <Header></Header>
    <div class="container">
      <div class="row">
        <div class="main">
          <!-- Banner -->
          <div class="banner">
            <el-carousel height="272px" indicator-position="none" :interval="2000">
              <el-carousel-item v-for="item in 4" :key="item">
                <h3 class="small">{{ item }}</h3>
              </el-carousel-item>
            </el-carousel>
          </div>
          <div id="list-container">
            <!-- 文章列表模块 -->
            <ul class="note-list">
<!--              <li class="">-->
<!--                <div class="content">-->
<!--                  <a class="title" target="_blank" href="">常做此运动，让你性福加倍</a>-->
<!--                  <p class="abstract">运动，是人类在发展过程中有意识地对自己身体素质的培养的各种活动 运动的方式多种多样 不仅仅是我们常知的跑步，球类，游泳等 今天就为大家介绍一种男...</p>-->
<!--                  <div class="meta">-->
<!--                    <span class="jsd-meta">-->
<!--                      <img src="/static/image/paid1.svg" alt=""> 4.8-->
<!--                    </span>-->
<!--                    <a class="nickname" target="_blank" href="">上班族也健身</a>-->
<!--                    <a target="_blank" href="">-->
<!--                      <img src="/static/image/comment.svg" alt=""> 4-->
<!--                    </a>-->
<!--                    <span><img src="/static/image/like.svg" alt=""> 31</span>-->
<!--                  </div>-->
<!--                </div>-->
<!--              </li>-->
              <li :class="check_img(article.content)?'have-img':''" v-for="article in article_list">
                <a class="wrap-img" href="" target="_blank" v-if="check_img(article.content)">
                  <img class="img-blur-done" :src="check_img(article.content)" />
                </a>
                <div class="content">
                  <router-link class="title" target="_blank" :to="`/article/${article.id}`">{{article.title}}</router-link>
                  <p class="abstract"　v-html="subtext(article.content,120)">
                  </p>
                  <div class="meta">
                    <a class="nickname" target="_blank" href="">{{article.user.nickname}}</a>
                    <a target="_blank" href="">
                      <img src="/static/image/comment.svg" alt=""> {{article.comment_count}}
                    </a>
                    <span><img src="/static/image/like.svg" alt=""> {{article.like_count}}</span>
                    <span v-if="article.reward_count>0"><img src="/static/image/shang.svg" alt=""> {{article.reward_count}}</span>
                  </div>
                </div>
              </li>
            </ul>
            <!-- 文章列表模块 -->
          </div>
        <a @click="get_next_article" class="load-more" v-if="new_article_list">阅读更多</a></div>
        <div class="aside">
          <!-- 推荐作者 -->
          <div class="recommended-author-wrap">
            <!---->
            <div class="recommended-authors">
              <div class="title">
                <span>推荐作者</span>
                <a class="page-change"><img class="icon-change" src="/static/image/exchange-rate.svg" alt="">换一批</a>
              </div>
              <ul class="list">
                <li>
                  <a href="" target="_blank" class="avatar">
                    <img src="/static/image/avatar.webp" />
                  </a>
                  <a class="follow" state="0"><img src="/static/image/follow.svg" alt="" />关注</a>
                  <a href="" target="_blank" class="name">董克平日记</a>
                  <p>写了807.1k字 · 2.5k喜欢</p>
                </li>
                <li>
                  <a href="" target="_blank" class="avatar">
                    <img src="/static/image/avatar.webp" />
                  </a>
                  <a class="follow" state="0"><img src="/static/image/follow.svg" alt="" />关注</a>
                  <a href="" target="_blank" class="name">董克平日记</a>
                  <p>写了807.1k字 · 2.5k喜欢</p>
                </li>

              </ul>
              <a href="" target="_blank" class="find-more">查看全部 ></a>
              <!---->
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>
<script>
  import Header from "./common/Header";
  import Footer from "./common/Footer";
  export default {
      name:"Home",
      data(){
          return {
            get_article_url:"",
            new_article_list:"",
            is_send_get_article_request:false, // 函数节流，判断当前ajax是否执行过程中
            token:{},
            article_list:[
              {
                "user":{

                }
              }
            ]
          }
      },
      created(){
        this.token = this.get_login_user();
        this.get_article_url = `${this.$settings.Host}/home/article/`;
        this.get_article_list()
      },
      methods:{
          subtext(content,len=100){
            // 如果文章开头有图片，则过滤图片
            if(content){
              while (content.search("<img") != -1){
                content = content.replace(/<img.*?src="(.*?)".*?>/,"")
              }
              return content.split("").slice(0,len).join("")+'...';
            }
            return "";
          },
          check_img(content){
            if(content){
              let ret = content.match(/<img.*?src="(.*?)".*?>/)
              if(ret){
                return ret[1];
              }
            }

            return false;

          },
          get_login_user(){
            // 获取登录用户
            return localStorage.user_token || sessionStorage.user_token;
          },
          get_article_list(){

            // 判断当前ajax是否正在执行
            if(this.is_send_get_article_request){
              this.$message.error("点击过于频繁！");
              return false;
            }

            this.is_send_get_article_request = true;

            // 获取推送文章
            let headers = {};
            if(this.token){
              headers = {
                Authorization:"jwt " +this.token,
              }
            }
            this.$axios.get(this.get_article_url,{
              headers
            }).then(response=>{
              if(!this.new_article_list){
                this.article_list = response.data.results;
              }else{
                this.article_list = this.article_list.concat(response.data.results);
              }
              this.article_count = response.data.count;
              this.new_article_list = response.data.next;

              // 开启再次执行ajax的状态
              this.is_send_get_article_request = false;
            }).catch(eror=>{
              this.$message.error("获取推送文章失败！");
            });
          },
          get_next_article(){
            this.get_article_url = this.new_article_list;
            this.get_article_list();
          }
      },
      components:{
        Header,
        Footer,
      }
  }
</script>


```

```
1. 判断用户是否登录
   1.1. 用户登录了
        1.1.1 用户已经关注了其他作者
          1.1.1.1 用户关注作者中,有足够的内容展示给用户
          1.1.1.2 用户关注作者中,没有足够内容展示给用户
        1.1.2 用户没有关注任何的作者
          1.1.1.1 根据浏览历史查找内容进行热度推荐
   1.2. 用户未登录
        1.1.3 根据浏览历史查找内容进行热度推荐

```

因为用户查看首页时, 显示的文章是不能重复的,所以接下来我们需要在每次推送文章给用户的时候,必须要进行记录:

## 实现用户和Feed内容的日志记录

用户和文章的推送日志

表格: user_message_log_table

| 第一主键 | (第二主键) | 属性列                                          |
| -------- | ---------- | ----------------------------------------------- |
| user_id  | message_id | is_push, is_read, is_like,is_reward, is_comment |

在home/management/commands/tablestore.py,自定义命令中,新增创建日志的命令:

```python
from django.core.management import BaseCommand
from tablestore import *
from django.conf import settings
class Command(BaseCommand):
    help = """表格存储命令必须接收而且只接收1个命令参数，如下：
    create  表示创建项目使用的表格
    delete  表示删除项目使用的表格
    """

    def add_arguments(self,parser):
        """参数设置"""
        parser.add_argument("argument",nargs="*", help="操作类型") # 位置参数

    def handle(self, *args, **options):
        """表格存储的初始化"""
        argument = options.get("argument")
        if len(argument)==1:
            if argument[0] == "create":
                """创建表格"""
                self.create_table()

            elif argument[0] == "delete":
                """删除表格"""
                self.delete_table()
            else:
                self.stdout.write(self.help)
        else:
            self.stdout.write(self.help)

    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def set_table(self,table_name,schema_of_primary_key,time_to_live=-1):
        # 设置表的元信息
        table_meta = TableMeta(table_name, schema_of_primary_key)
        # 设置数据的有效型
        table_option = TableOptions(time_to_live=time_to_live, max_version=5)
        # 设置数据的预留读写吞吐量
        reserved_throughput = ReservedThroughput(CapacityUnit(0, 0))
        # 创建数据
        self.client.create_table(table_meta, table_option, reserved_throughput)

    def create_table(self):
        """创建表格"""
        # 创建存储库
        table_name = "user_message_table"
        schema_of_primary_key = [ # 主键列
            ('user_id', 'INTEGER'),
            ('sequence_id', 'INTEGER',PK_AUTO_INCR),
            ("sender_id",'INTEGER'),
            ("message_id",'INTEGER'),
        ]

        self.set_table(table_name,schema_of_primary_key,time_to_live=7*86400)
        self.stdout.write("创建表格%s完成" % table_name)

        #　关系库
        table_name = "user_relation_table"
        # 主键列
        schema_of_primary_key = [
            ('user_id', 'INTEGER'),
            ("follow_user_id", 'INTEGER'),
        ]
        self.set_table(table_name, schema_of_primary_key)
        self.stdout.write("创建表格%s完成" % table_name)

        # 未读池
        table_name = "user_message_session_table"
        # 主键列
        schema_of_primary_key = [
            ('user_id', 'INTEGER'),
            ("last_sequence_id", 'INTEGER'),
        ]
        self.set_table(table_name, schema_of_primary_key)
        self.stdout.write("创建表格%s完成" % table_name)


        # 用户对文章的访问操作日志
        table_name = "user_message_log_table"
        schema_of_primary_key = [ # 主键列
            ('user_id', 'INTEGER'),
            ("message_id",'INTEGER'),
        ]
        self.set_table(table_name, schema_of_primary_key)
        self.stdout.write("创建表格%s完成" % table_name)

    def delete_table(self):
        """删除表"""
        table_list = self.client.list_table()
        for table in table_list:
            self.client.delete_table(table)
            self.stdout.write("删除%s完成" % table)

```



在首页获取推送内容时, 直接查询推送内容:

```python
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from article.models import Article
from .serializers import ArticleListModelSerializer
from .paginations import HomeArticlePageNumberPagination
from tablestore import *
from django.conf import settings
from users.models import User
from datetime import datetime
class ArticleListAPIView(ListAPIView):
    serializer_class = ArticleListModelSerializer
    pagination_class = HomeArticlePageNumberPagination

    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def get_queryset(self):
        week_timestamp = datetime.now().timestamp() - 7 * 86400
        week_date = datetime.fromtimestamp(week_timestamp) # 获取一周前的时间对象
        queryset = Article.objects.filter(pub_date__gte=week_date).exclude(pub_date=None,).order_by("-reward_count","-comment_count","-like_count","-id")

        # 记录本次给用户推送文章的记录
        user = self.request.user

        if isinstance(user, User):
            # 判断tablestore中是否曾经推送过当前当前文章给用户
            queryset = self.check_user_message_log(user, queryset)

            if len(queryset)>0:
                article_id_list = []
                for item in queryset:
                    article_id_list.append(item.id)
                self.push_log(user.id, article_id_list)

        return queryset

    def check_user_message_log(self, user, queryset):
        """判断系统是否曾经推送过文章给用户"""
        columns_to_get = []
        rows_to_get = []
        for article in queryset:
            primary_key = [('user_id', user.id), ('message_id', article.id)]
            rows_to_get.append(primary_key)
        request = BatchGetRowRequest()
        table_name = "user_message_log_table"

        cond = CompositeColumnCondition(LogicalOperator.OR)
        cond.add_sub_condition(SingleColumnCondition("is_read", True, ComparatorType.EQUAL))
        cond.add_sub_condition(SingleColumnCondition("is_like", True, ComparatorType.EQUAL))

        request.add(TableInBatchGetRowItem(table_name, rows_to_get, columns_to_get,column_filter=cond, max_version=1))
        result = self.client.batch_get_row(request)
        table_result = result.get_result_by_table(table_name)
        push_id_list = []
        for item in table_result:
            if item.row is not None:
                push_id_list.append(item.row.primary_key[1][1])

        return queryset.exclude(id__in=push_id_list)

    def push_log(self, user_id, article_id_list):
        """推送文章给用户的记录"""
        table_name = "user_message_log_table"

        put_row_items = []

        for i in article_id_list:
            # 主键列
            primary_key = [
                ('user_id', user_id),  # 用户ID
                ("message_id", i),  # 文章ID
            ]

            attribute_columns = [('is_push', True), ('is_read', False), ('is_like', False), ('is_reward',False), ('is_comment',False)]

            row = Row(primary_key, attribute_columns)
            condition = Condition(RowExistenceExpectation.IGNORE)
            item = PutRowItem(row, condition)
            put_row_items.append(item)

        request = BatchWriteRowRequest()
        request.add(TableInBatchWriteRowItem(table_name, put_row_items))
        result = self.client.batch_write_row(request)
        return result.is_all_succeed()

```



在用户点击阅读文章以后, 更新阅读记录

```python
    # Create your views here.

    from .models import ArticleImage
    from rest_framework.generics import CreateAPIView
    from .serializers import ArticleImageModelSerializer
    class ImageAPIView(CreateAPIView):
        queryset = ArticleImage.objects.all()
        serializer_class = ArticleImageModelSerializer


    from .models import ArticleCollection
    from .serializers import ArticleCollectionModelSerializer
    from rest_framework.generics import ListAPIView
    from rest_framework.permissions import IsAuthenticated
    from rest_framework.response import Response

    class CollecionAPIView(CreateAPIView, ListAPIView):
        """文集的视图接口"""
        queryset = ArticleCollection.objects.all()
        serializer_class = ArticleCollectionModelSerializer
        permission_classes = [IsAuthenticated]

        def list(self, request, *args, **kwargs):
            user = request.user
            queryset = self.filter_queryset(self.get_queryset().filter(user=user))

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

    from rest_framework.generics import UpdateAPIView
    from .serializers import ArticleCollectionDetailModelSerializer
    class CollecionDetailAPIView(UpdateAPIView):
        """文集的视图接口"""
        queryset = ArticleCollection.objects.all()
        serializer_class = ArticleCollectionDetailModelSerializer
        permission_classes = [IsAuthenticated]


    from rest_framework.viewsets import ModelViewSet
    from .models import Article
    from .serializers import ArticleModelSerializer
    from rest_framework.decorators import action
    from rest_framework import status
    from django_redis import get_redis_connection
    from datetime import datetime
    from django.db import transaction

    class ArticleAPIView(ModelViewSet):
        """文章的视图集接口"""
        queryset = Article.objects.all()
        serializer_class = ArticleModelSerializer
        permission_classes = [IsAuthenticated]

        @property
        def client(self):
            return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

        @action(methods=["PUT"], detail=True)
        def save_article(self,request,pk):
            # 接收文章内容，标题，编辑次数，文章ID
            content = request.data.get("content")
            title = request.data.get("title")
            save_id = int( request.data.get("save_id") )
            collection_id = request.data.get("collection_id")
            user = request.user
            if save_id is None:
                save_id = 1
            else:
                save_id += 1

            # 验证文章是否存在
            try:
                article = Article.objects.get(pk=pk)
            except Article.DoesNotExist:
                return Response({"message":"当前文章不存在！"}, status=status.HTTP_400_BAD_REQUEST)

            # 写入到redis中[先配置redis库]
            redis_conn = get_redis_connection("article")
            """
            article_<user_id>_<article>_<save_id>:{
                "title":   title,
                "content": content,
                "update_time": 1929293,
                "collection_id":collection_id,
            }
            """
            new_timestamp = datetime.now().timestamp()
            data = {
                "title": title,
                "content": content,
                "updated_time": new_timestamp,
                "collection_id": collection_id,
            }
            redis_conn.hmset("article_%s_%s_%s" % (user.id, pk, save_id), data)
            # 把用户针对当前文章的最新编辑记录ID保存起来
            redis_conn.hset("article_history_%s" % (user.id), pk, save_id )
            # 实现查看当前文章的编辑历史的思路：
            # article_edit_history = redis_conn.keys("article_%s_%s*" % (user.id, pk) )
            # data_list = []
            # for item in article_edit_history:
            #     ret = redis_conn.hgetall(item)
            #     data_list.append({
            #         "title": ret.get("title".encode()).decode(),
            #         "content": ret.get("content".encode()).decode(),
            #         "updated_time": ret.get("updated_time".encode()).decode(),
            #     })
            # print(data_list)
            # 返回结果
            return Response({"message":"保存成功！","save_id": save_id})

        def list(self, request, *args, **kwargs):
            user = request.user
            collection_id = request.query_params.get("collection")
            try:
                ArticleCollection.objects.get(pk=collection_id)
            except ArticleCollection.DoesNotExist:
                return Response({"message":"对不起，当前文集不存在！"})

            # 先到redis中查询
            redis_conn = get_redis_connection("article")
            history_dist = redis_conn.hgetall("article_history_%s" % (user.id) )
            data = []
            exclude_id = []
            if history_dist is not None:
                for article_id, save_id in history_dist.items():
                    article_id = article_id.decode()
                    save_id = save_id.decode()
                    article_data_byte = redis_conn.hgetall("article_%s_%s_%s" % (user.id, article_id, save_id) )
                    if article_data_byte["collection_id".encode()].decode() == collection_id:
                        data.append({
                            "id": article_id,
                            "title": article_data_byte["title".encode()].decode(),
                            "content": article_data_byte["content".encode()].decode(),
                            "save_id": save_id,
                            "collection": collection_id,
                        })
                        exclude_id.append(article_id)

            # 然后把redis中已经编辑过的内容结果排除出来，然后到MySQL中查询

            queryset = self.filter_queryset(self.get_queryset().filter(user=user, collection_id=collection_id).exclude(id__in=exclude_id) )

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)

            data +=serializer.data

            return Response(data)

        @action(methods=["patch"],detail=True)
        def pub_article(self,request,pk):
            """发布文章"""
            user    = request.user
            status  = request.data.get("is_pub")

            with transaction.atomic():
                save_id = transaction.savepoint()
                try:
                    article = Article.objects.get(user=user, pk=pk)
                except:
                    transaction.savepoint_rollback(save_id)
                    return Response({"message":"当前文章不存在或者您没有修改的权限！"})

                if status:
                    """发布文章"""
                    article.pub_date = datetime.now()

                    # 先查询到当前作者的粉丝 user_relation_table中查询　
                    fens_list = self.get_fens(user.id)

                    # 循环结果，把Feed进行推送
                    if len(fens_list) > 0:
                        ret = self.push_feed(fens_list, user.id, article.id)
                        if not ret:
                            transaction.savepoint_rollback(save_id)
                            message = {"message": "发布文章失败！"}
                        else:
                            message = {"message": "发布文章成功！"}
                    else:
                        message = {"message":"发布文章成功"}
                else:
                    """私密文章，取消发布"""
                    article.pub_date = None
                    message = {"message":"取消发布成功"}

                # 从redis的编辑记录中提取当前文章的最新记录
                redis_conn = get_redis_connection("article")
                user_history_dist = redis_conn.hgetall("article_history_%s" % user.id)
                save_id = user_history_dist.get(pk.encode()).decode()
                article_dict = redis_conn.hgetall("article_%s_%s_%s" % (user.id, pk, save_id) )
                if article_dict is not None:
                    article.title = article_dict["title".encode()].decode()
                    article.content = article_dict["content".encode()].decode()
                    timestamp = datetime.fromtimestamp(int(float(article_dict["updated_time".encode()].decode())))
                    article.updated_time = timestamp
                    article.save_id = save_id
                article.save()

                return Response(message)

        def push_feed(self, fens_list,author_id, article_id):
            """推送Feed给粉丝"""
            table_name = "user_message_table"

            put_row_items = []

            for i in fens_list:
                # 主键列
                primary_key = [  # ('主键名', 值),
                    ('user_id', i),  # 接收Feed的用户ID
                    ('sequence_id', PK_AUTO_INCR),  # 如果是自增主键，则值就是 PK_AUTO_INCR
                    ("sender_id", author_id),  # 发布Feed的用户ID
                    ("message_id", article_id),  # 文章ID
                ]

                attribute_columns = [('recevice_time', datetime.now().timestamp()), ('read_status', False)]
                row = Row(primary_key, attribute_columns)
                condition = Condition(RowExistenceExpectation.IGNORE)
                item = PutRowItem(row, condition)
                put_row_items.append(item)

            request = BatchWriteRowRequest()
            request.add(TableInBatchWriteRowItem(table_name, put_row_items))
            result = self.client.batch_write_row(request)

            return result.is_all_succeed()

        def get_fens(self, user_id):
            """获取当前用户的所有粉丝，后面自己整理下这个方法到工具库中"""
            table_name = "user_relation_table"

            # 范围查询的起始主键
            inclusive_start_primary_key = [
                ('user_id', user_id),
                ('follow_user_id', INF_MIN)
            ]

            # 范围查询的结束主键
            exclusive_end_primary_key = [
                ('user_id', user_id),
                ('follow_user_id', INF_MAX)
            ]

            # 查询所有列
            columns_to_get = [] # 表示返回所有列

            # 范围查询接口
            consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
                table_name,  # 操作表明
                Direction.FORWARD,  # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
                inclusive_start_primary_key, exclusive_end_primary_key,  # 取值范围
                columns_to_get,  # 返回字段列
                max_version=1  # 返回版本数量
            )

            fens_list = []
            for row in row_list:
                fens_list.append( row.primary_key[1][1] )

            return fens_list

        @action(methods=["patch"], detail=True)
        def change_collection(self, request, pk):
            """切换当前文章的文集ID"""
            user = request.user
            collection_id = request.data.get("collection_id")
            try:
                article = Article.objects.get(user=user, pk=pk)
            except:
                return Response({"message": "当前文章不存在或者您没有修改的权限！"})

            try:
                ArticleCollection.objects.get(user=user, pk=collection_id)
            except:
                return Response({"message": "当前文集不存在或者您没有修改的权限！"})

            # 当前文章如果之前有曾经被编辑，则需要修改redis中的缓存
            redis_conn = get_redis_connection("article")
            save_id_bytes = redis_conn.hget("article_history_%s" % (user.id),pk)
            if save_id_bytes is not None:
                save_id = save_id_bytes.decode()
                redis_conn.hset("article_%s_%s_%s" % (user.id, pk, save_id ), "collection_id", collection_id )
            article.collection_id = collection_id
            article.save()

            return Response({"message":"切换文章的文集成功！"})

    from .models import Special,SpecialArticle
    from .serializers import SpecialModelSerializer
    class SpecialListAPIView(ListAPIView):
        queryset = Special.objects.all()
        serializer_class = SpecialModelSerializer
        permission_classes = [IsAuthenticated]

        def list(self, request, *args, **kwargs):
            user = request.user
            ret = self.get_queryset().filter(mymanager__user=user)
            article_id = request.query_params.get("article_id")
            # 验证文章

            queryset = self.filter_queryset(ret)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            # 返回专题对于当前文章的收录状态
            data = []
            for special in serializer.data:
                try:
                    SpecialArticle.objects.get(article_id=article_id, special_id=special.get("id"))
                    special["post_status"] = True # 表示当前文章已经被专题收录了
                except SpecialArticle.DoesNotExist:
                    special["post_status"] = False  # 表示当前文章已经被专题收录了
                data.append(special)
            return Response(data)

    class ArticlePostSpecialAPIView(CreateAPIView):
        permission_classes = [IsAuthenticated]
        def post(self,request):
            """收录到我管理的专题"""
            article_id = request.data.get("article_id")
            special_id = request.data.get("special_id")
            user = request.user
            try:
                Article.objects.get(user=user, pk=article_id)
            except Article.DoesNotExist:
                return Response({"message": "当前文章不存在或者您没有操作的权限！"})

            try:
                Special.objects.get(mymanager__user=user, pk=special_id)
            except Article.DoesNotExist:
                return Response({"message": "当前专题不存在或者您没有操作的权限！"})

            SpecialArticle.objects.create(article_id=article_id,special_id=special_id)

            return Response({"message":"收录成功！"})

    from rest_framework.generics import RetrieveAPIView
    from .serializers import ArticleInfoModelSerializer
    from users.models import User
    from tablestore import *
    from django.conf import settings

    class ArticleInfoAPIView(RetrieveAPIView):
        """文章详情"""
        serializer_class = ArticleInfoModelSerializer
        queryset = Article.objects.exclude(pub_date=None)
        @property
        def client(self):
            return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

        def retrieve(self, request, *args, **kwargs):
            response = super().retrieve(request, *args, **kwargs)
            if isinstance(request.user, User):
                """用户登录了"""
                user = request.user                                    # 访问者
                author_id = response.data.get("user").get("id")        # 文章作者

                # 用户对文章的阅读记录
                article_id = kwargs.get("pk")
                self.read_log(user.id, article_id)

                if author_id != user.id:
                    # 到tablestore里面查询当前访问者是否关注了文章作者
                    table_name = "user_relation_table"

                    primary_key = [('user_id', author_id), ('follow_user_id', user.id)]

                    columns_to_get = []

                    consumed, return_row, next_token = self.client.get_row(table_name, primary_key, columns_to_get)

                    if return_row is None:
                        """没有关注"""
                        is_follow = 1
                    else:
                        """已经关注了"""
                        is_follow = 2

                else:
                    is_follow = 3 # 当前用户就是作者

            else:
                """用户未登录"""
                is_follow = 0  # 当前访问者未登录

            response.data["is_follow"] = is_follow
            return response

        def read_log(self,user_id, article_id):
            """更新用户对文章的阅读记录"""
            table_name = "user_message_log_table"
            primary_key = [('user_id', int(user_id)), ('message_id', int(article_id))]
            update_of_attribute_columns = {
                'PUT': [('is_read', True)],
            }
            row = Row(primary_key, update_of_attribute_columns)
            condition = Condition(RowExistenceExpectation.IGNORE,
                                  SingleColumnCondition("is_read", False, ComparatorType.EQUAL))  # update row on\
            consumed, return_row = self.client.update_row(table_name, row, condition)


```

在首页中展示 用户关注推送Feed内容

```python
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from article.models import Article
from .serializers import ArticleListModelSerializer
from .paginations import HomeArticlePageNumberPagination
from tablestore import *
from django.conf import settings
from users.models import User
from datetime import datetime
class ArticleListAPIView(ListAPIView):
    serializer_class = ArticleListModelSerializer
    pagination_class = HomeArticlePageNumberPagination

    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def get_queryset(self):
        week_timestamp = datetime.now().timestamp() - 7 * 86400
        week_date = datetime.fromtimestamp(week_timestamp) # 获取一周前的时间对象
        queryset = Article.objects.filter(pub_date__gte=week_date).exclude(pub_date=None,).order_by("-reward_count","-comment_count","-like_count","-id")

        # 记录本次给用户推送文章的记录
        user = self.request.user

        if isinstance(user, User):

            # 查询当前用户关注的作者是否有新的推送[查询同步库]
            # 先到未读池中提取当前访问用户上一次读取Feed的最大主键
            start_sequence_id = self.get_start_sequence_id(user.id)
            # 然后根据主键到同步库中查看数据
            message_id_list = self.get_feed_message(user.id, start_sequence_id)
            if len(message_id_list)>=10:
                """如果未读池存在10条以上的推送内容"""
                queryset = queryset.filter(id__in=message_id_list)

            else:
                # 基于物品进行协同过滤推荐文章
                message_id_list = self.get_message_by_itemCF(user.id)

                # 判断tablestore中是否曾经推送过当前当前文章给用户
                queryset = self.check_user_message_log(user, queryset)

            # 更新推送日志
            if len(queryset)>0:
                article_id_list = []
                for item in queryset:
                    article_id_list.append(item.id)
                self.push_log(user.id, article_id_list)

        return queryset

    def get_message_by_itemCF(self,user_id):
        """基于物品的协同过滤获取Feed内容"""
        pass

    def get_feed_message(self,user_id, start_sequence_id):
        """获取同步库中的数据"""
        table_name = "user_message_table"

        # 范围查询的起始主键
        inclusive_start_primary_key = [
            ('user_id', user_id),
            ('sequence_id', start_sequence_id),
            ('sender_id', INF_MIN),
            ('message_id', INF_MIN)
        ]

        # 范围查询的结束主键
        exclusive_end_primary_key = [
            ('user_id', user_id),
            ('sequence_id', INF_MAX),
            ('sender_id', INF_MAX),
            ('message_id', INF_MAX),
        ]

        columns_to_get = [] # 表示返回所有列
        limit = 10

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name, # 操作表明
            Direction.FORWARD, # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key, # 取值范围
            columns_to_get, # 返回字段列
            limit, #　结果数量
            max_version=1         # 返回版本数量
        )

        message_id_list = []
        for item in row_list:
            message_id_list.append( item.primary_key[3][1] )

        # 下一次读取同步库的开始主键
        try:
            self.set_start_sequence_id(user_id, start_sequence_id, next_start_primary_key[1][1])
        except:
            pass

        return message_id_list

    def set_start_sequence_id(self, user_id,old_start_sequence_id, next_start_primary_key):
        table_name = "user_message_session_table"
        try:
            primary_key = [('user_id', user_id), ('last_sequence_id', old_start_sequence_id)]
            row = Row(primary_key)
            consumed, return_row = self.client.delete_row(table_name, row, None)
        except:
            pass

        primary_key = [('user_id', user_id), ('last_sequence_id', next_start_primary_key)]
        attribute_columns = []
        row = Row(primary_key, attribute_columns)
        consumed, return_row = self.client.put_row(table_name, row)
        print(return_row)
        return return_row

    def get_start_sequence_id(self,user_id):
        """获取最后读取的Feed流id"""
        table_name = "user_message_session_table"

        # 范围查询的起始主键
        inclusive_start_primary_key = [
            ('user_id', user_id),
            ('last_sequence_id', INF_MIN)
        ]

        # 范围查询的结束主键
        exclusive_end_primary_key = [
            ('user_id', user_id),
            ('last_sequence_id', INF_MAX)
        ]

        columns_to_get = [] # 表示返回所有列
        limit = 1

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name, # 操作表明
            Direction.FORWARD, # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key, # 取值范围
            columns_to_get, # 返回字段列
            limit, #　结果数量
            # column_filter=cond, # 条件
            max_version=1         # 返回版本数量
        )

        if len(row_list) < 1:
            # 之前没有读取过推送内容
            return INF_MIN
        else:
            return row_list[0].primary_key[1][1]


    def check_user_message_log(self, user, queryset):
        """判断系统是否曾经推送过文章给用户"""
        columns_to_get = []
        rows_to_get = []
        for article in queryset:
            primary_key = [('user_id', user.id), ('message_id', article.id)]
            rows_to_get.append(primary_key)
        request = BatchGetRowRequest()
        table_name = "user_message_log_table"

        cond = CompositeColumnCondition(LogicalOperator.OR)
        cond.add_sub_condition(SingleColumnCondition("is_read", True, ComparatorType.EQUAL))
        cond.add_sub_condition(SingleColumnCondition("is_like", True, ComparatorType.EQUAL))

        request.add(TableInBatchGetRowItem(table_name, rows_to_get, columns_to_get,column_filter=cond, max_version=1))
        result = self.client.batch_get_row(request)
        table_result = result.get_result_by_table(table_name)
        push_id_list = []
        for item in table_result:
            if item.row is not None:
                push_id_list.append(item.row.primary_key[1][1])

        return queryset.exclude(id__in=push_id_list)

    def push_log(self, user_id, article_id_list):
        """推送文章给用户的记录"""
        table_name = "user_message_log_table"

        put_row_items = []

        for i in article_id_list:
            # 主键列
            primary_key = [
                ('user_id', user_id),  # 用户ID
                ("message_id", i),  # 文章ID
            ]

            attribute_columns = [('is_push', True), ('is_read', False), ('is_like', False), ('is_reward',False), ('is_comment',False)]

            row = Row(primary_key, attribute_columns)
            condition = Condition(RowExistenceExpectation.IGNORE)
            item = PutRowItem(row, condition)
            put_row_items.append(item)

        request = BatchWriteRowRequest()
        request.add(TableInBatchWriteRowItem(table_name, put_row_items))
        result = self.client.batch_write_row(request)
        return result.is_all_succeed()

```



在`user_message_log_table`表中, 用户和文章之间的关联形成一张巨型的矩阵.

|       | 文章1 | 文章2 | 文章3 | 文章4 |      |
| ----- | ----- | ----- | ----- | ----- | ---- |
| 用户1 | 1     | 0     | 1     | 0     |      |
| 用户2 | 1     | 1     | 0     | 0     |      |
| 用户3 | 0     | 1     | 1     | 1     |      |
| 用户4 | 1     | 1     | 0     | 0     |      |
| 用户5 | 1     | 0     | 0     | 0     |      |

现在推荐用户5去看文章: 文章2, 文章3

上面就是 根据用户行为进行分析的基于物品的协同过滤 ItemCF

```python
pip install numpy

```

```python
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from article.models import Article
from .serializers import ArticleListModelSerializer
from .paginations import HomeArticlePageNumberPagination
from tablestore import *
from django.conf import settings
from users.models import User
from datetime import datetime
from renranapi.utils.ItemCF import ItemCF
class ArticleListAPIView(ListAPIView):
    serializer_class = ArticleListModelSerializer
    pagination_class = HomeArticlePageNumberPagination

    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def get_queryset(self):
        week_timestamp = datetime.now().timestamp() - 7 * 86400
        week_date = datetime.fromtimestamp(week_timestamp) # 获取一周前的时间对象
        queryset = Article.objects.filter(pub_date__gte=week_date).exclude(pub_date=None,).order_by("-reward_count","-comment_count","-like_count","-id")

        # 记录本次给用户推送文章的记录
        user = self.request.user

        if isinstance(user, User):
            queryset1 = []
            # 查询当前用户关注的作者是否有新的推送[查询同步库]
            # 先到未读池中提取当前访问用户上一次读取Feed的最大主键
            start_sequence_id = self.get_start_sequence_id(user.id)
            # 然后根据主键到同步库中查看数据
            message_id_list = self.get_feed_message(user.id, start_sequence_id)
            if len(message_id_list) >= 10: # 同步库中有数据
                queryset = queryset.filter(id__in=message_id_list)
                limit_num = 0
            else:
                # 基于物品进行协同过滤推荐文章
                message_id_list = self.get_message_by_itemCF(user.id)
                if len(message_id_list) > 0:
                    queryset1 = queryset.filter(id__in=message_id_list)
                    queryset1 = list(queryset1)

            # 判断tablestore中是否曾经推送过当前当前文章给用户
            queryset2 = self.check_user_message_log(user, queryset)
            queryset2 = list(queryset2)
            queryset = queryset1 + queryset2
            queryset = list(set(queryset))[:10]
            # 更新推送日志
            if len(queryset)>0:
                article_id_list = []
                for item in queryset:
                    article_id_list.append(item.id)
                self.push_log(user.id, article_id_list)

        return queryset

    def get_user_read_history(self,user_id):
        """查找用户最近１个月的浏览历史记录"""
        table_name = "user_message_log_table"
        # 范围查询的起始主键
        inclusive_start_primary_key = [
            ('user_id', user_id),
            ('message_id', INF_MIN)
        ]

        # 范围查询的结束主键
        exclusive_end_primary_key = [
            ('user_id', user_id),
            ('message_id', INF_MAX)
        ]

        # 查询所有列
        columns_to_get = [] # 表示返回所有列

        # 设置多条件
        cond = CompositeColumnCondition(LogicalOperator.AND) # 逻辑条件

        # 多条件下的子条件
        cond.add_sub_condition(SingleColumnCondition("is_push", True, ComparatorType.EQUAL)) #  比较运算符:　等于
        cond.add_sub_condition(SingleColumnCondition("is_read", True, ComparatorType.EQUAL)) #  比较运算符:　等于

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name, # 操作表明
            Direction.FORWARD, # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key, # 取值范围
            columns_to_get,     # 返回字段列
            column_filter=cond, # 条件
            max_version=1       # 返回版本数量
        )

        data = []
        if len(row_list) == 0:
            return data

        for row in row_list:
            data.append(row.primary_key[1][1])
        return data

    def get_user_by_message_id(self,message_id):
        """根据文章ID获取用户列表"""
        table_name = "user_message_log_table"
        # 范围查询的起始主键
        inclusive_start_primary_key = [
            ('user_id', INF_MIN),
            ('message_id', message_id)
        ]

        # 范围查询的结束主键
        exclusive_end_primary_key = [
            ('user_id', INF_MAX),
            ('message_id', message_id)
        ]

        # 查询所有列
        columns_to_get = []  # 表示返回所有列

        # 设置多条件
        cond = CompositeColumnCondition(LogicalOperator.AND)  # 逻辑条件

        # 多条件下的子条件
        cond.add_sub_condition(SingleColumnCondition("is_push", True, ComparatorType.EQUAL))  # 比较运算符:　等于
        cond.add_sub_condition(SingleColumnCondition("is_read", True, ComparatorType.EQUAL))  # 比较运算符:　等于

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name, # 操作表明
            Direction.FORWARD, # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key, # 取值范围
            columns_to_get,     # 返回字段列
            column_filter=cond, # 条件
            max_version=1       # 返回版本数量
        )

        data = set()
        if len(row_list) == 0:
            return list(data)

        for row in row_list:
            data.add(row.primary_key[0][1])
        return list(data)

    def find_user_by_history(self, message_list):
        """根据阅读文章列表的记录查询出阅读这些文章的用户"""
        users =[]
        for message_id in message_list:
            users += self.get_user_by_message_id(message_id)
        users = list(set(users))
        return users

    def find_message_by_user(self, users):
        allUserItemsStarList=[]  # 用户和文章之间的矩阵关系
        messages = []  # 文章列表
        users_message = [] # 所有用户读取过的文章列表
        for user_id in users:
            ret = self.get_user_read_history(user_id)
            messages += ret
            users_message.append(ret)
        messages = list(set(messages))
        for item_user_message in users_message:
            message_list = []
            for msg in messages:
                message_list.append( 1 if(msg in item_user_message) else 0)
            allUserItemsStarList.append(message_list)

        return allUserItemsStarList, messages

    def get_message_by_itemCF(self, user_id):
        """基于物品的协同过滤获取Feed内容"""
        # 查询出当前用户的曾经浏览记录
        current_user_history_list = self.get_user_read_history(user_id)

        if len(current_user_history_list) == 0:
            return []

        # 根据浏览历史记录查到曾经浏览过文章的所有用户
        users = self.find_user_by_history(current_user_history_list)
        if len(users) == 0:
            return []

        # 用户和物品的关系[点赞,赞赏,阅读,收藏], 文章id列表
        allUserItemsStarList, messages = self.find_message_by_user(users)
        if len(allUserItemsStarList) < 1 or len(messages) < 1:
            return []

        cf = ItemCF(users, messages, allUserItemsStarList)

        return cf.calrecommendMoive(user_id)

    def get_feed_message(self,user_id, start_sequence_id):
        """获取同步库中的数据"""
        table_name = "user_message_table"

        # 范围查询的起始主键
        inclusive_start_primary_key = [
            ('user_id', user_id),
            ('sequence_id', start_sequence_id),
            ('sender_id', INF_MIN),
            ('message_id', INF_MIN)
        ]

        # 范围查询的结束主键
        exclusive_end_primary_key = [
            ('user_id', user_id),
            ('sequence_id', INF_MAX),
            ('sender_id', INF_MAX),
            ('message_id', INF_MAX),
        ]

        columns_to_get = [] # 表示返回所有列
        limit = 10

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name, # 操作表明
            Direction.FORWARD, # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key, # 取值范围
            columns_to_get, # 返回字段列
            limit, #　结果数量
            max_version=1         # 返回版本数量
        )

        message_id_list = []
        for item in row_list:
            message_id_list.append( item.primary_key[3][1] )

        # 下一次读取同步库的开始主键
        try:
            self.set_start_sequence_id(user_id, start_sequence_id, next_start_primary_key[1][1])
        except:
            pass

        return message_id_list

    def set_start_sequence_id(self, user_id,old_start_sequence_id, next_start_primary_key):
        table_name = "user_message_session_table"
        try:
            primary_key = [('user_id', user_id), ('last_sequence_id', old_start_sequence_id)]
            row = Row(primary_key)
            consumed, return_row = self.client.delete_row(table_name, row, None)
        except:
            pass

        primary_key = [('user_id', user_id), ('last_sequence_id', next_start_primary_key)]
        attribute_columns = []
        row = Row(primary_key, attribute_columns)
        consumed, return_row = self.client.put_row(table_name, row)
        print(return_row)
        return return_row

    def get_start_sequence_id(self,user_id):
        """获取最后读取的Feed流id"""
        table_name = "user_message_session_table"

        # 范围查询的起始主键
        inclusive_start_primary_key = [
            ('user_id', user_id),
            ('last_sequence_id', INF_MIN)
        ]

        # 范围查询的结束主键
        exclusive_end_primary_key = [
            ('user_id', user_id),
            ('last_sequence_id', INF_MAX)
        ]

        columns_to_get = [] # 表示返回所有列
        limit = 1

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name, # 操作表明
            Direction.FORWARD, # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key, # 取值范围
            columns_to_get, # 返回字段列
            limit, #　结果数量
            # column_filter=cond, # 条件
            max_version=1         # 返回版本数量
        )

        if len(row_list) < 1:
            # 之前没有读取过推送内容
            return INF_MIN
        else:
            return row_list[0].primary_key[1][1]


    def check_user_message_log(self, user, queryset):
        """判断系统是否曾经推送过文章给用户"""
        columns_to_get = []
        rows_to_get = []
        for article in queryset:
            primary_key = [('user_id', user.id), ('message_id', article.id)]
            rows_to_get.append(primary_key)
        request = BatchGetRowRequest()
        table_name = "user_message_log_table"

        cond = CompositeColumnCondition(LogicalOperator.OR)
        cond.add_sub_condition(SingleColumnCondition("is_read", True, ComparatorType.EQUAL))
        cond.add_sub_condition(SingleColumnCondition("is_like", True, ComparatorType.EQUAL))

        request.add(TableInBatchGetRowItem(table_name, rows_to_get, columns_to_get,column_filter=cond, max_version=1))
        result = self.client.batch_get_row(request)
        table_result = result.get_result_by_table(table_name)
        push_id_list = []
        for item in table_result:
            if item.row is not None:
                push_id_list.append(item.row.primary_key[1][1])

        return queryset.exclude(id__in=push_id_list)

    def push_log(self, user_id, article_id_list):
        """推送文章给用户的记录"""
        table_name = "user_message_log_table"

        put_row_items = []

        for i in article_id_list:
            # 主键列
            primary_key = [
                ('user_id', user_id),  # 用户ID
                ("message_id", i),  # 文章ID
            ]

            attribute_columns = [('is_push', True), ('is_read', False), ('is_like', False), ('is_reward',False), ('is_comment',False)]

            row = Row(primary_key, attribute_columns)
            condition = Condition(RowExistenceExpectation.IGNORE)
            item = PutRowItem(row, condition)
            put_row_items.append(item)

        request = BatchWriteRowRequest()
        request.add(TableInBatchWriteRowItem(table_name, put_row_items))
        result = self.client.batch_write_row(request)
        return result.is_all_succeed()

```

