

# 今日内容



## 基于双下划线的跨表查询(left-join？)

+ filter()
+ values()
+ 若存在外键属性则通过外键`__`寻找，否则通过小写类名`__`

```python
   # 一对一
    # 正向连表  靠属性
    # 查询旭东的家庭住址
    # ret = models.Author.objects.filter(name='旭东').values('ad__addr')
    # print(ret)
    # select app01_authordetail.addr from app01_author inner join app01_authordetail on app01_author.ad_id = app01_authordetail.id where app01_author.name='旭东';
	# 反向连表靠 类名小写
    # ret = models.AuthorDetail.objects.filter(author__name='旭东').values('addr')
    # print(ret)

    # 一对多
    # 查询东京出版社出版了哪些书
    # select app01_book.title from app01_publish inner join app01_book on app01_publish.id = app01_book.publishs_id where app01_publish.name='东京出版社';

    # ret = models.Publish.objects.filter(name='东京出版社').values('book__title')
    # print(ret)
    # ret = models.Book.objects.filter(publishs__name='东京出版社').values('title')
    # print(ret)


    # 多对多
    # 查询一下金龙2写了哪些书

    ret = models.Book.objects.filter(authors__name='金龙2').values('title')
    print(ret)

    ret = models.Author.objects.filter(name='金龙2').values('book__title')
    print(ret)
```

##  聚合查询

+ 聚合函数--aggregate( *args, **kwargs )
  + Avg
  + Max
  + Min
  + Count
  + Sum

```python
    
    aggregate聚合查询,结果是普通字典,queryset的结束符
    from django.db.models import Avg,Max,Min,Count,Sum
    
    obj = models.Book.objects.all().aggregate(a=Max('price')) #{'price__avg': 200.0}
    print(obj)
	Book.objects.aggregate(Avg('price'), Max('price'), Min('price')) 

```

## 分组查询(每个出版社出版的书的最高价格)

+ 方式1：按照values中字段联合分组

  ```python
  ret = models.Book.objects.values('publishs_id').annotate(m=Max('price'))
  ```

  总结:values写在annotate前面,意思是以values括号内的字段作为分组的依据,annotate里面是你要做的统计结果,这样,返回结果为queryset类型数据,里面是字典{'publishs_id':1,'m':100}

+ 方式2：默认按照对象主键分组

  ```python
  ret = models.Publish.objects.annotate(m=Max('book__price')).values('m','name')
  ```

  总结: annotate直接写在了objects后面,意思是按照前面表的所有的数据(默认是id值)作为分组依据,结果返回的是前面这个表的所有models对象(model对象中包含了每个对象自己的统计结果),在通过values来取值,取值时可以直接写字段和统计结果的别名,也是queryset类型,里面是字典{'m':100,'name':'东京出版社'}

+ 其它实例

  ```python
      查询每个作者的姓名以及出版的书的最高价格
  
  
      ret = models.Book.objects.values('authors__name','authors__id').annotate(m=Max('price'))  # group by authors__name,authors__id
      print(ret)
  
      ret = models.Author.objects.annotate(m=Max('book__price')).values('name','m')
      print(ret)
  ```

## F查询

+  F() 的实例可以在查询中引用字段，来比较同一个 model 实例中两个不同字段的值 

  ```python
  # 查询一下点赞数大于评论数的所有书籍
  
  ret = models.Book.objects.filter(dianzan__gt=F('comment')).values('title')
  ```

+  Django 支持 F() 对象之间以及 F() 对象和常数之间的加减乘除和取模的操作。 

  ```python
  # 查询评论数大于收藏数2倍的书籍
  Book.objects.filter(commentNum__lt=F('keepNum')*2)
  
  #本表字段进行四则运算
  models.Book.objects.all().update(
      price=F('price')+20  #支持四则运算
  )
  ```

## Q查询

+  `filter()` 等方法中的关键字参数查询都是一起进行“AND” 的。 如果你需要执行更复杂的查询（例如`OR` 语句），你可以使用`Q 对象`。 

  ```python
  from django.db.models import Q
  Q(title__startswith='Py')
  ```

  +  `Q` 对象可以使用`&(与)` 、`|（或）、~（非）` 操作符组合起来。当一个操作符在两个`Q` 对象上使用时，它产生一个新的`Q` 对象。 

    ```python
    bookList=Book.objects.filter(Q(authors__name="yuan")|Q(authors__name="egon"))
    ```

  +  可以组合`&` 和`|` 操作符以及使用括号进行分组来编写任意复杂的`Q` 对象。同时，`Q` 对象可以使用`~` 操作符取反，这允许组合正常的查询和取反(`NOT`) 查询 

    ```python
    bookList=Book.objects.filter(Q(authors__name="yuan") & ~Q(publishDate__year=2017)).values_list("title")
    bookList=Book.objects.filter(Q(Q(authors__name="yuan") & ~Q(publishDate__year=2017))&Q(id__gt=6)).values_list("title") #可以进行Q嵌套，多层Q嵌套等，其实工作中比较常用
    ```

  +  查询函数可以混合使用`Q 对象`和关键字参数。所有提供给查询函数的参数（关键字参数或`Q` 对象）都将"AND”在一起。但是，如果出现`Q` 对象，它必须位于所有关键字参数的前面。 

    ```python
    bookList=Book.objects.filter(Q(publishDate__year=2016) | Q(publishDate__year=2017),
                                  title__icontains="python"  #也是and的关系，但是Q必须写在前面
                                 )
    ```

## orm执行原生sql语句(了解)

+  raw()管理器（ 用于原始的SQL查询，并返回模型的实例 ）

  +  *注意：raw()语法查询必须包含主键* 

  +  返回一个django.db.models.query.RawQuerySet 实例。 这个RawQuerySet 实例可以像一般的QuerySet那样，通过迭代来提供对象实例 

    ```python
    ret = models.Book.objects.raw('select * from app01_book;')
    for i in ret:
        print(i.title)
    print(ret)
    ```

  +  raw()查询可以查询其他表的数据 

  +  raw()方法自动将查询字段映射到模型字段。还可以通过translations参数指定一个把查询的字段名和ORM对象实例的字段名互相对应的字典 

    ```python
    d = {'tname': 'haha'}
        ret = models.Student.objects.raw('select * from app02_teacher', translations=d)
        for i in ret:
            print(i.id, i.sname, i.haha)
    ```

  +  原生SQL还可以使用参数，注意不要自己使用字符串格式化拼接SQL语句，防止SQL注入！ 

    ```python
    d = {'tname': 'haha'}
        ret = models.Student.objects.raw('select * from app02_teacher where id > %s', translations=d, params=[1,])
        for i in ret:
            print(i.id, i.sname, i.haha)
    ```

+ 直接执行自定义SQL

   直接从django提供的接口中获取数据库连接，然后像使用pymysql模块一样操作数据库 

  ```python
  from django.db import connection, connections
  cursor = connection.cursor()  # cursor = connections['default'].cursor()
  cursor.execute("""SELECT * from auth_user where id = %s""", [1])
  ret = cursor.fetchone()
  ```

+ 直接使用pymysql

  ```python
  conn = pymysql.connect(
       host='127.0.0.1',
       port=3306,
       user='root',
       password='123',
       database='orm02',
       charset='utf8'
  )
  cursor = conn.cursor(pymysql.cursors.DictCursor)
  cursor.execute('select * from app01_book;')
  print(cursor.fetchall())
  ```



## django外部脚本调用models数据库操作

```python
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm02.settings")
    import django
    django.setup()
    
	from app01 import models
    ret = models.Book.objects.all().values('title')
    print(ret)
```



## ORM事务和锁

+ 行级锁

  ```python
  select_for_update(nowait=False, skip_locked=False) #注意必须用在事务里面
  
  models.Book.objects.select_for_update().filter(id=1)
  ```

+ 事务

  + 全局开启（ 需要将配置项ATOMIC_REQUESTS设置为True ）

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mxshop',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'USER': 'root',
            'PASSWORD': '123',
            'OPTIONS': {
                "init_command": "SET default_storage_engine='INNODB'",
    　　　　　　　#'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", #配置开启严格sql模式
    
    
            }
            "ATOMIC_REQUESTS": True, #全局开启事务，绑定的是http请求响应整个过程
            "AUTOCOMMIT":False, #全局取消自动提交，慎用
        }，
    　　'other':{
    　　　　'ENGINE': 'django.db.backends.mysql', 
                ......
    　　} #还可以配置其他数据库
    }
    ```

  +  上面这种方式是统一个http请求对应的所有sql都放在一个事务中执行（要么所有都成功，要么所有都失败）。是全局性的配置， 如果要对某个http请求放水（然后自定义事务），可以用non_atomic_requests修饰器，那么他就不受事务的管控了 

    ```python
    from django.db import transaction
    
    @transaction.non_atomic_requests
    def my_view(request):
        do_stuff()
    
    @transaction.non_atomic_requests(using='other')
    def my_other_view(request):
        do_stuff_on_the_other_database()
    ```

  + 局部使用事务

    +  给函数做装饰器来使用

      ```python
      from django.db import transaction
      
      @transaction.atomic
      def viewfunc(request):
          # This code executes inside a transaction.
          do_stuff()
      ```

    +  作为上下文管理器来使用，其实就是设置事务的保存点 

      ```python
      from django.db import transaction
      
      def viewfunc(request):
          # This code executes in autocommit mode (Django's default).
          do_stuff()
      
          with transaction.atomic():   #保存点
              # This code executes inside a transaction.
              do_more_stuff()
      
          do_other_stuff()
      ```

      ```python
      #一旦把atomic代码块放到try/except中，完整性错误就会被自然的处理掉了，比如下面这个例子：
      
      from django.db import IntegrityError, transaction
      
      @transaction.atomic
      def viewfunc(request):
          create_parent()
      
          try:
              with transaction.atomic():
                  generate_relationships()
          except IntegrityError:
              handle_exception()
      
          add_children()
      ```