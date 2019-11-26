

# 今日内容



## 基于双下划线的跨表查询(join)

+ 

```
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

```
    
    aggregate聚合查询,结果是普通字典,queryset的结束符
    from django.db.models import Avg,Max,Min,Count,Sum
    
    obj = models.Book.objects.all().aggregate(a=Max('price')) #{'price__avg': 200.0}
    print(obj)
	Book.objects.aggregate(Avg('price'), Max('price'), Min('price')) 



```

## 分组查询

```
分组查询 -- group by app01_book.publishs_id
    每个出版社出版的书的最高价格
    方式1:
    	ret = models.Book.objects.values('publishs_id').annotate(m=Max('price'))
	总结:values写在annotate前面,意思是以values括号内的字段作为分组的依据,annotate里面是你要做的统计结果,这样,返回结果为queryset类型数据,里面是字典{'publishs_id':1,'m':100}
	
	方式2
    	ret = models.Publish.objects.annotate(m=Max('book__price')).values('m','name')
	总结: annotate直接写在了objects后面,意思是按照前面表的所有的数据(默认是id值)作为分组依据,结果返回的是前面这个表的所有models对象(model对象中包含了每个对象自己的统计结果),在通过values来取值,取值时可以直接写字段和统计结果的别名,也是queryset类型,里面是字典{'m':100,'name':'东京出版社'}
    print(ret)

    查询每个作者的姓名以及出版的书的最高价格


    ret = models.Book.objects.values('authors__name','authors__id').annotate(m=Max('price'))  # group by authors__name,authors__id
    print(ret)

    ret = models.Author.objects.annotate(m=Max('book__price')).values('name','m')
    print(ret)
```



## F查询

```
查询结果是本表中两个字段的比较之后的符合条件的结果集
   # 查询一下点赞数大于评论数的所有书籍
    # list1 = []
    # books = models.Book.objects.all()
    # for i in books:
    #     if i.dianzan > i.comment:
    #         list1.append(i)

    # ret = models.Book.objects.filter(dianzan__gt=F('comment')).values('title')\

    # ret = models.Book.objects.filter(dianzan__lt=F('comment')).values('title')
    # print(ret)

    
本表字段进行四则运算
    # models.Book.objects.all().update(
    #     price=F('price')+20  #支持四则运算
    # )

```

## Q查询

```
    # 查询一下点赞大于300或者价钱小于300的书,Q的连接符:& -- and,  |--or,~ -- not 取反
    # ret = models.Book.objects.filter(Q(dianzan__gt=300)|~Q(price__lt=500),xx='oo').values('title')
    ret = models.Book.objects.filter(Q(dianzan__gt=300)).values('title')
    # 
    # ret = models.Book.objects.filter(Q(Q(dianzan__gt=300)|~Q(price__lt=500))&Q(xx='oo')).values('title')
    # print(ret)
    

Q查询能够进行各种复杂条件的拼接
```

## orm执行原生sql语句(了解)

```

    # 方式1
    # ret = models.Book.objects.raw('select * from app01_book;')
    # for i in ret:
    #     print(i.title)
    # print(ret)
    
    #方式2 django自带的连接通道(配置的pymysql)
    from django.db import connection
    import pymysql
    # conn = pymysq.connect()
    # cursor = connection.cursor()
    # cursor.execute('select * from app01_book;')
    # print(cursor.fetchall())
    #
    
    # 方式3 pymysql
    # conn = pymysql.connect(
    #     host='127.0.0.1',
    #     port=3306,
    #     user='root',
    #     password='123',
    #     database='orm02',
    #     charset='utf8'
    # 
    # )
    # cursor = conn.cursor(pymysql.cursors.DictCursor)
    # cursor.execute('select * from app01_book;')
    # print(cursor.fetchall())
```



## django外部脚本调用models数据库操作

```


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

```
锁:
	models.Book.objects.select_for_update().filter(id=1)

事务:
方式1 全局配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mxshop',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123',
        "ATOMIC_REQUESTS": True, #全局开启事务，绑定的是http请求响应整个过程当中的sql
    }
}


方式2: 视图函数加装饰器
	from django.db import transaction
    @transaction.atomic
    def viewfunc(request):
        # This code executes inside a transaction.
        do_stuff()
方式3: 上下文加装饰器
	from django.db import transaction
    def viewfunc(request):
        # This code executes in autocommit mode (Django's default).
        do_stuff()

        with transaction.atomic():   #保存点
            # This code executes inside a transaction.
            do_more_stuff()

        do_other_stuff()
```





















