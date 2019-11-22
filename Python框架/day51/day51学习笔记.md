



# 今日内容



```
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'statics'), #文件夹名称尽量不要和别名的名称冲突
]

```

静态文件的另外一种引入方式

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="{% static 'bootstrap-3.3.7-dist/css/bootstrap.min.css' %}">
</head>
<body>

</body>
<script src="{% static 'jquery.js' %}"></script>
<script src="{% static 'bootstrap-3.3.7-dist/js/bootstrap.min.js' %}"></script>
</html>
```



编辑按钮携带数据

```
<a href="{% url 'book_edit' %}?book_id={{ book.id }}" class="btn btn-warning btn-sm">编辑</a>#}

{#   <a href="/book/edit/{{ book.id }}/" class="btn btn-warning btn-sm">编辑</a>#}

<a href="{% url 'book_edit' book.id %}" class="btn btn-warning btn-sm">编辑</a>
```

url别名反向解析时 如果需要参数怎么搞:

```
html
	{% url '别名' 3 %}         url(r'^index/(\d+)/',views.index,name='index');
	-- /index/3/
	
views视图
	reverse('index',args=(3,))    -- /index/3/
```



## 13个查询接口

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

+ order_by(*field)

  + queryset类型的数据来调用，对查询结果排序,默认是按照id来升序排列的，返回值还是queryset类型
  + 升序`models.Book.objects.order_by('price','id')`
  + 降序`models.Book.objects.all().order_by('price','-id')`
  + 多条件`order_by('price','id')` ,按照price进行升序，price相同的数据，按照id进行升序

+ reverse()

  + queryset类型的数据来调用，对查询结果反向排序(先进行order_by排序)，返回值还是queryset类型

+ count()

  + queryset类型的数据来调用，返回数据库中匹配查询(QuerySet)的对象数量

    ```python
    ret = models.UserInfo.objects.all().count()
    ```

+ first()

  + queryset类型的数据来调用，返回第一条记录-model对象

    ```python
    Book.objects.all()[0] = Book.objects.all().first()
    #得到的都是model对象，不是queryset
    ```

+ last()

  + queryset类型的数据来调用，返回最后一条记录

+ exists()

  + queryset类型的数据来调用，如果QuerySet包含数据，就返回True，否则返回False

    ```python
    all_books = models.Book.objects.all().exists() 
    #翻译成的sql是SELECT (1) AS `a` FROM `app01_book` LIMIT 1，就是通过limit 1，取一条来看看是不是有数据
    ```

+ values(*field)

  + queryset类型的数据来调用，返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象，而是一个可迭代的字典序列,只要是返回的queryset类型，就可以继续链式调用queryset类型的其他的查找方法，其他方法也是一样的。

  + 筛选键

    ```python
    ret = models.UserInfo.objects.all().values('age','username')
    
    ret = models.UserInfo.objects.values('age','username')   #objects调用--对所有数据进行取值
    ```

+ values_list(*field)

  + 与values()相似，它返回的是一个元组序列，values返回的是一个字典序列

+ distinct()

  + values和values_list得到的queryset类型的数据来调用，从返回结果中剔除重复纪录

    ```python
    ret = models.UserInfo.objects.all().values('age','username').distinct()   
    
    ret = models.UserInfo.objects.values('age','username').distinct()   
    ```



## 创建时,日期字段数据的添加方式

```
        models.Book.objects.create(
            # publish_date = "2019-08-01",  字符串
            # publish_date = datetime.datetime.now(), 时间日期数据
        )

```



## update进行更新和delete删除时:注意

```python
update更新
	models.Book.objects.filter(id=2).update(username='xxx')  #update的调用者是queryset类型数据
delete删除(调用者可以是一个model对象，也可以是一个queryset集合)
    models.Book.objects.filter(id=2).delete()
    models.Book.objects.get(id=2).delete()
```



### 基于双下划线的模糊查询

+ `in`

  ```python
  Book.objects.filter(price__in=[100,200,300]) 
  #price值等于这三个里面的任意一个的对象
  ```

+ `>`

  ```python
  Book.objects.filter(price__gt=100)  
  #大于，大于等于是price__gte=100，别写price>100，这种参数不支持
  Book.objects.filter(price__gte=100) #大于等于
  ```

+ `<`

  ```python
  Book.objects.filter(price__lt=100)
  Book.objects.filter(price__lte=100)#小于等于
  ```

+ `between and`

  ```python
  Book.objects.filter(price__range=[100,200])  #大于等于100，小于等于200
  ```

+ `like`

  + 包含

    ```python
    Book.objects.filter(title__contains="python")  #title值中包含python的
    
    Book.objects.filter(title__icontains="python") #不区分大小写
    ```

  + 开头

    ```python
    Book.objects.filter(title__startswith="py") #以什么开头
    
    Book.objects.filter(title__istartswith="py") #不区分大小写
    ```

  + 结尾

    ```python
    Book.objects.filter(title__endswith="py") #以什么结尾
    
    Book.objects.filter(title__endswith="py") #不区分大小写
    ```

+ 时间匹配

  ```python
  Book.objects.filter(pub_date__year=2012)
  Book.objects.filter(pub_date__month=2)
  Book.objects.filter(pub_date__day="02")
  ```

练习

```python
1 查询某某出版社出版过的价格大于200的书籍
 ret = models.Book.objects.filter(price__gt=200)
2 查询2017年8月出版的所有以py开头的书籍名称
 ret = models.Book.objects.filter(title__startswith="py",publish_date__year=2017,publish_date__month=8).values("title")
3 查询价格为50,100或者150的所有书籍名称及其出版社名称
 ret = models.Book.objects.filter(price__in=[50,100,150]).values("title","publish")
4 查询价格在100到200之间的所有书籍名称及其价格
 ret = models.Book.objects.filter(price__range=[100,200]).values("title","price")
5 查询所有人民出版社出版的书籍的价格（从高到低排序，去重）
ret = models.Book.objects.filter(publish="人民出版社").values("price").order_by("-price").distinct()
```

