# Web应用模式

在开发Web应用中，有两种应用模式：

1. 前后端不分离[客户端看到的内容和所有界面效果都是由服务端提供出来的。]

![前后端不分离]($%7Basserts%7D/depended_frontend_backend.png)

2. 前后端分离【把前端的界面效果(html，css，js分离到另一个服务端，python服务端只需要返回数据即可)】

前端形成一个独立的网站，服务端构成一个独立的网站

![前后端分离]($%7Basserts%7D/indepent_frontend_backend.png)

# api接口

+ 概念

  ​		api就是开发提供给第三方或者外界通过方法/url地址进行调用的一个数据功能，可以理解为django里面的一个视图的方法或者一个能够被访问的函数。

  ​		为了在团队内部形成共识、防止个人习惯差异引起的混乱，我们需要找到一种大家都觉得很好的接口实现规范，而且这种规范能够让后端写的接口，用途一目了然，减少双方之间的合作成本。

目前市面上大部分公司开发人员使用的接口服务架构主要有：restful、rpc、soap。



+ rpc: 翻译成中文:远程过程调用[远程服务调用].

  服务端提供一个统一的访问地址：http://api.renran.cn/，通过参数声明调用哪一个方法，以及调用方法的参数。

  rpc基本都会要求，使用http的post请求，

  action=get_all_student&params=301&sex=1

  接口多了,对应函数名和参数就多了,前端在请求api接口时,就会比较难找.容易出现重复的接口

+ restful: 翻译成中文: 资源状态转换.

  把后端所有的数据/文件都看成资源. 

  那么接口请求数据,本质上来说就是对资源的操作了.

  web项目中操作资源,无非就是增删查改.所以要求在地址栏中声明要操作的资源是什么,然后通过http请求动词来说明对资源进行哪一种操作.资源对应的往往就是数据表的表名。

  POST http://www.renran.cn/api/students/   添加学生数据

  GET    http://www.renran.cn/api/students/   获取所有学生

  DELETE http://www.renran.cn/api/students/<pk>/   删除id=pk的一个学生

  PUT   http://www.renran.cn/api/students/<pk>/       修改一个学生的全部信息 [id,name,sex,age,]

  PATCH  http://www.renran.cn/api/students/<pk>/    修改一个学生的部分信息[age]

# RESTful API规范

![restful]($%7Basserts%7D/restful.gif)

REST全称是Representational State Transfer，中文意思是表述（编者注：通常译为表征）性状态转移。 它首次出现在2000年Roy Fielding的博士论文中。

RESTful是一种定义Web API接口的设计风格，尤其适用于前后端分离的应用模式中。

这种风格的理念认为后端开发任务就是提供数据的，对外提供的是数据资源的访问接口，所以在定义接口时，客户端访问的URL路径就表示这种要操作的数据资源。

而对于数据资源分别使用POST、DELETE、GET、UPDATE等请求动作来表达对数据的增删查改。

| 请求方法 | 请求地址       | 后端操作           |
| -------- | -------------- | ------------------ |
| GET      | /students      | 获取所有学生       |
| POST     | /students      | 增加学生           |
| GET      | /students/<pk> | 获取编号为pk的学生 |
| PUT      | /students/<pk> | 修改编号为pk的学生 |
| DELETE   | /students/<pk> | 删除编号为pk的学生 |



事实上，我们可以使用任何一个框架都可以实现符合restful规范的API接口。

参考文档：http://www.runoob.com/w3cnote/restful-architecture.html

接口实施过程中，会存在幂等性。所谓幂等性是指代客户端发起多次请求是否对于服务端里面的资源产生不同结果。如果多次请求，服务端结果还是一样，则属于幂等接口，如果多次请求，服务端产生结果是不一样的，则属于非幂等接口。在http请求，get/put/patch/delete都属于幂等性接口，post属于非幂等接口。



# 序列化

api接口开发，最核心最常见的一个过程就是序列化，所谓序列化就是把**数据转换格式**，序列化可以分两个阶段：

+ **序列化**： 把我们识别的数据转换成指定的格式提供给别人。

  例如：我们在django中获取到的数据默认是模型对象，但是模型对象数据无法直接提供给前端或别的平台使用，所以我们需要把数据进行序列化，变成字符串或者json数据，提供给别人。

+ **反序列化**：把别人提供的数据转换/还原成我们需要的格式。

  例如：前端js提供过来的json数据，对于python而言就是字符串，我们需要进行反序列化换成模型类对象，这样我们才能把数据保存到数据库中。

# Django Rest_Framework

核心思想: 缩减编写api接口的代码

Django REST framework是一个建立在Django基础之上的Web 应用开发框架，可以快速的开发REST API接口应用。在REST framework中，提供了序列化器Serialzier的定义，可以帮助我们简化序列化与反序列化的过程，不仅如此，还提供丰富的类视图、扩展类、视图集来简化视图的编写工作。REST framework还提供了认证、权限、限流、过滤、分页、接口文档等功能支持。REST framework提供了一个API 的Web可视化界面来方便查看测试接口。

![drf_logo]($%7Basserts%7D/drf_logo.png)

中文文档：https://q1mi.github.io/Django-REST-framework-documentation/#django-rest-framework

github: https://github.com/encode/django-rest-framework/tree/master

## 特点

- 提供了定义序列化器Serializer的方法，可以快速根据 Django ORM 或者其它库自动序列化/反序列化；
- 提供了丰富的类视图、Mixin扩展类，简化视图的编写；
- 丰富的定制层级：函数视图、类视图、视图集合到自动生成 API，满足各种需要；
- 多种身份认证和权限认证方式的支持；[jwt]
- 内置了限流系统；
- 直观的 API web 界面；【方便我们调试开发api接口】
- 可扩展性，插件丰富

# drf环境安装与配置

DRF需要以下依赖：

- Python (2.7, 3.2以上)
- Django (1.10, 1.11, 2.0以上)

**DRF是以Django的子应用方式提供的，所以我们可以直接利用已有的Django环境而无需从新创建。（若没有Django环境，需要先创建环境安装Django）**



## 安装DRF

前提是已经安装了django，建议安装在虚拟环境

+ 创建虚拟环境

  ```bash
  mkvirtualenv drfdemo -p python3
  ```

+ 安装相关包

  ```bash
  pip install django==2.2.0  -i https://pypi.douban.com/simple
  
  pip install djangorestframework -i https://pypi.douban.com/simple
  
  pip install pymysql -i https://pypi.douban.com/simple
  ```

## 创建django项目

```
cd ~/Desktop
django-admin startproject drfdemo
```

![1557022536078]($%7Basserts%7D/1557022536078.png)

使用pycharm打开项目，设置虚拟环境的解析器，并修改manage.py中的后缀参数。



## 添加rest_framework应用

在**settings.py**的**INSTALLED_APPS**中添加'rest_framework'。

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

接下来就可以使用DRF提供的功能进行api接口开发了。在项目中如果使用rest_framework框架实现API接口，开发过程中编写视图为主，视图里面的代码无非有以下三个步骤：

- 将请求的数据（如JSON格式）转换为模型类对象【json->字典->模型对象】
- 通过模型类对象操作数据库【操作数据库】
- 将模型类对象转换为响应的数据（如JSON格式）【模型对象->字典->json】

## 体验drf完全简写代码提供api接口的过程

### 创建子应用

首先我们需要创建一个子应用来开发。所以在终端下面，我们直接创建students子应用。

```
python manage.py startapp students
```

把创建好的子应用注册到settings.py，代码：

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework', # 把drf框架注册到django项目中

    'students', # 注册子应用
]
```

在开发中，不管是开发一个api接口还是一个普通的业务功能，在django/drf中都会有一个套路：

```
1. 先考虑考虑好整个功能应用到的外部工具[配置信息，第三方模块，]
2. 创建相关数据模型[models.py]
3. 编写序列化器[django不需要这个步骤]
4. 编写视图代码
5. 编写路由，绑定视图
```

为了方便测试，所以我们可以先创建一个数据库。

```
create database students charset=utf8mb4;
```

初始化数据库连接

```
安装pymysql
pip install pymysql
```

主引用中`__init__.py`设置使用pymysql作为数据库驱动

```python
import pymysql

pymysql.install_as_MySQLdb()
```

settings.py配置文件中设置mysql的账号密码

```python
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "students",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD":"123",
    },
}
```



### 创建模型操作类

students/models.py，代码：

```python
class Student(models.Model):
    # 模型字段
    name = models.CharField(max_length=100,verbose_name="姓名")
    sex = models.BooleanField(default=1,verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    class_number = models.CharField(max_length=5,verbose_name="班级编号")
    description = models.TextField(max_length=1000,verbose_name="个性签名")

    class Meta:
        db_table="tb_student"
        verbose_name = "学生"
        verbose_name_plural = verbose_name
```

#### 执行数据迁移

终端下，执行。

```
python manage.py makemigrations
python manage.py migrate
```

错误列表

```python
# 执行数据迁移 python manage.py makemigrations 报错如下：
```

![1557024349366]($%7Basserts%7D/1557024349366.png)

解决方案：

```python
注释掉 backends/mysql/base.py中的35和36行代码。
```

![1557025991751]($%7Basserts%7D/1557025991751.png)



```python
# 执行数据迁移发生以下错误：
```

![1557026113769]($%7Basserts%7D/1557026113769.png)

解决方法：

backends/mysql/operations.py146行里面修改这句代码：

```python
        if query is not None:
        	# query = query.decode(errors='replace') # 原代码
            query = query.encode(errors='replace')
```

经过上面错误解决以后，执行数据迁移。效果如下：

![1581993950655]($%7Basserts%7D/1581993950655.png)



### 创建序列化器

在syudents应用目录中新建serializers.py用于保存该应用的序列化器。

创建一个StudentModelSerializer用于对接收客户端提供的数据时进行反序列化以及在提供数据给客户端时进行序列化。

```python
# 创建序列化器类，回头会在试图中被调用
from rest_framework import serializers
from .models import Student
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
```

- **model** 指明该序列化器处理的数据字段从模型类BookInfo参考生成
- **fields** 指明该序列化器包含模型类中的哪些字段，'__all__'指明包含所有字段

### 编写视图

在students应用的views.py中创建视图StudentViewSet，这是一个视图集合。

```python
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentModelSerializer
# Create your views here.
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
```

- **queryset** 指明该视图集在查询数据时使用的查询集
- **serializer_class** 指明该视图在进行序列化或反序列化时使用的序列化器

### 定义路由

在students应用的urls.py中定义路由信息。

```python
from . import views
from rest_framework.routers import DefaultRouter

# 路由列表
urlpatterns = []

router = DefaultRouter()  # 可以处理视图的路由器
router.register('students', views.StudentViewSet)  # 向路由器中注册视图集

urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
```

最后把students子应用中的路由文件加载到主应用的总路由文件中.

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("stu/",include("students.urls")),
]
```

### 运行测试

运行当前程序（与运行Django一样）

```shell
python manage.py runserver
```

在浏览器中输入网址127.0.0.1:8000，可以看到DRF提供的API Web浏览页面：

![1557027948031]($%7Basserts%7D/1557027948031.png)



1）点击链接127.0.0.1:8000/stu/students 可以访问**获取所有数据的接口**，呈现如下页面：

![1557027878963]($%7Basserts%7D/1557027878963.png)





2）在页面底下表单部分填写学生信息，可以访问**添加新学生的接口**，保存学生信息：

![1557027999506]($%7Basserts%7D/1557027999506.png)

点击POST后，返回如下页面信息：

![1557028072470]($%7Basserts%7D/1557028072470.png)



3）在浏览器中输入网址127.0.0.1:8000/stu/students/5/，可以访问**获取单一学生信息的接口**（id为5的学生），呈现如下页面：

![1557028115925]($%7Basserts%7D/1557028115925.png)

4）在页面底部表单中填写学生信息，可以访问**修改学生的接口**：

![1557028168350]($%7Basserts%7D/1557028168350.png)

点击PUT，返回如下页面信息：

![1557028208243]($%7Basserts%7D/1557028208243.png)

5）点击DELETE按钮，可以访问**删除学生的接口**：

![1557028242637]($%7Basserts%7D/1557028242637.png)

返回，如下页面：

![1557028266190]($%7Basserts%7D/1557028266190.png)



