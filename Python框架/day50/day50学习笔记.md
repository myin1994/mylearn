## url别名和反向解析

+ url别名作用

  支持对url匹配规则的版本控制，避免硬编码

+ 别名写法

  + `url(r'^index/', views.index,name='index')`

+ 使用方法--反向解析

  + views视图函数

    ```python
    from django.urls import reverse
    
    reverse('index')---->解析结果：url规则路径，即/index/
    ```

  + html渲染

    ```html
    <form action="{% url 'index' %}" method="post">
            {% csrf_token %}
            用户名:<input type="text" name="uname">
            密码:<input type="text" name="pwd">
            <input type="submit">
    </form>
    ```

+ 反向解析携带参数

  ```python
  urls:
  from django.conf.urls import url
  
  from . import views
  
  urlpatterns = [
      # ...
      url(r'^articles/([0-9]{4})/$', views.year_archive, name='news-year-archive'),
      # ...
  ]
  
  html:
  <a href="{% url 'news-year-archive' 2012 %}">2012 Archive</a>
  
  <ul>
  {% for yearvar in year_list %}
  <li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }} Archive</a></li>
  {% endfor %}
  </ul>
  
  views:
  from django.urls import reverse
  from django.shortcuts import redirect
  
  def redirect_to_year(request):
      # ...
      year = 2006
      # ...
      return redirect(reverse('news-year-archive', args=(year,))) #或者直接return redirect('news-year-archive',year) redirect内部会自动调用reverse来进行反向解析
  ```

## include路由分发

+ 作用

  为每一应用单独设置url分发方法，项目url仅用于分发应用

+ 使用方法

  + 项目urls

    ```python
    from django.conf.urls import url,include
    from django.contrib import admin
    
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^app01/', include('app01.urls',namespace='app01')),
        url(r'^app02/', include('app02.urls',namespace='app02')),
    ]
    ```

  + app应用urls

    ```python
    from django.conf.urls import url
    from app01 import views
    urlpatterns = [
        url(r'^index/', views.index,name='index'),
    ]
    -------------------------------------------------------
    from django.conf.urls import url
    from app02 import views
    urlpatterns = [
        url(r'^index/', views.index,name='index'),
    ]
    ```

+ url命名空间

  将每个应用自己的url路径划分一个空间,将来通过别名反向解析时,通过空间名称可以找到对应应用下面的路径（进行唯一反向解析）。

  + views中`reverse('app01:index')`
  + html中`{% url 'app01:index' %}`

# 数据库操作

## ORM

 object relational mapping  对象关系映射

+ 使用步骤

  + 数据库配置

    + 本地数据库创建数据库（如orm01）

    + 配置settings.py以连接对应数据库

      ```python
      # DATABASES = {
      #     'default': {
      #         'ENGINE': 'django.db.backends.sqlite3',
      #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      #     }
      # }
      
      连接mysql的配置:	
          DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME':'bms', # 要连接的数据库，连接前需要创建好
              'USER':'root',# 连接数据库的用户名
              'PASSWORD':'', # 连接数据库的密码
              'HOST':'127.0.0.1',  # 连接主机，默认本级
              'PORT':3306 #  端口 默认3306
          }
      }
      ```

    + 在项目文件夹下的的init文件中指定连接数据库的模块

      ```python
      import pymysql
      pymysql.install_as_MySQLdb()
      ```

  + 在应用文件夹下面的models.py文件中建立表结构

    ```python
    class UserInfo(models.Model):
        id = models.AutoField(primary_key=True)  
        username = models.CharField(max_length=10)
        password = models.CharField(max_length=32)
    ```

  +  通过两条数据库迁移命令在指定的数据库中创建表（terminal下）

    ```python
    #生成记录，每次修改了models里面的内容或者添加了新的app，新的app里面写了models里面的内容，都要执行这两条
    
    python manage.py makemigrations  #在migrations文件夹下面生成记录文件
    python manage.py migrate #执行记录文件
    
    #执行上面这个语句的记录来创建表，生成的表名字前面会自带应用的名字，例如：你的book表在mysql里面叫做app01_book表
    
    #表名规则：应用名_类名小写
    ```

+  打印orm转换过程中的sql 

  + 需要在settings中进行如下配置 

    ```python
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console':{
                'level':'DEBUG',
                'class':'logging.StreamHandler',
            },
        },
        'loggers': {
            'django.db.backends': {
                'handlers': ['console'],
                'propagate': True,
                'level':'DEBUG',
            },
        }
    }
    ```

  + 第二种方法

    ```python
    from app01 import models
    
    def add_book(request):
        '''
        添加表记录
        :param request: http请求信息
        :return:
        '''
        book_obj = models.Book(title='python',price=123,pub_date='2012-12-12',publish='人民出版社')
        book_obj.save()
        from django.db import connection  #通过这种方式也能查看执行的sql语句
        print(connection.queries)
        return HttpResponse('ok')
    ```

## 数据库表操作

### 增加

+ 方式1

  ```python
  obj = models.UserInfo(username='alex',password='sb')
  obj.save()
  ```

+ 方式2

  ```python
  models.UserInfo.objects.create(username='一峰',password='666')
  ```

+ 方式3：批量创建

  ```python
  ----依次添加
  
  for i in range(10):
  	obj = models.UserInfo(username=str(i),password=str(i+1))
  	obj.save()
  
  ----批量添加，速度快
  lst = []
  for i in range(10):
  	obj = models.UserInfo(username=str(i),password=str(i+1))
  	lst.append(obj)
  models.UserInfo.objects.bulk_create(lst)
  ```

  

### 修改

+ 方式1:修改字段个数不限

  ```python
  models.UserInfo.objects.filter(id=1).update(
          username='alexxx',
          password='bigsb',
      )
  ```

+ 方式2:相当于设置对象的属性

  ```python
  obj = models.UserInfo.objects.filter(id=1)[0]
  obj.username = 'alex222'
  obj.password = '11111'
  obj.save()
  ```

+ 方式3：有就更新,没有就创建（只允许一个对象）

```python

    a,b = models.UserInfo.objects.update_or_create(
        username='alex',
        defaults={
            'id':20,
            'password':'ooooo',
            'age':84,
        }
    )

    print(a)  # 当前更新后的model对象,或者是你新增的记录的model对象
    print(b)  # 新增就是True,查询就False
```

### 删除

```python
 models.UserInfo.objects.filter(id=1).delete()
```

### 查询

+ all()

  + 查询所有结果，结果是queryset类型

+ filter(**kwargs)

  + 包含了与所给筛选条件相匹配的对象，结果也是queryset类型 

  + 多个条件用逗号分开，并且这几个条件必须都成立，是and的关系

    ```
    Book.objects.filter(title='linux',price=100)
    ```

+ get(**kwargs)

  + 返回与所给筛选条件相匹配的model对象，返回结果有且只有一个
  + 筛选条件的对象超过一个或者没有都会抛出错误
    + UserInfo matching query does not exist.
    + get() returned more than one UserInfo -- it returned 11!

+ exclude(**kwargs)

  + 排除的意思，它包含了与所给筛选条件不匹配的对象，没有不等于的操作昂，用这个exclude，返回值是queryset类型

    ```python
    Book.objects.exclude(id=6) #返回id不等于6的所有的对象
    
    Book.objects.all().exclude(id=6) #或者在queryset基础上调用
    ```