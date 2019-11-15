# 今日内容



wsgi(web服务网关接口)

```
应用程序和服务器程序之间沟通数据的格式要求
```



返回动态页面

```

模板渲染:
    模板 -- html文件
    渲染 -- 字符串替换


```



## MVC和MTV模式

```
MVC模式，所谓MVC就是把Web应用分为模型(M)，控制器(C)和视图(V)

MTV:
M: model 数据库相关操作
T:template 模板(html)相关操作
V:views 视图(业务逻辑,函数--类)
+ urls(url控制器) 将一个个URL的页面请求分发给不同的View处理
```

## django

### 指令创建项目

```
下载安装
	pip install django==1.11.9
创建项目(找到一个文件夹,切换到这个文件夹下执行下面的指令)
	django-admin startproject 项目名称
创建应用
	python manage.py startapp 应用名称
在和项目同名的那个文件夹里面的settings配置文件中找到下面的配置:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'app01',  #加上咱们项目文件夹下面的这个应用名称,将项目和应用关联到一起
]
启动项目:
	python manage.py runserver 127.0.0.1:8001
	#如果端口不写,默认是8000
	#如果ip地址和端口号都不写,默认是127.0.0.1:8000


```

### pycharm IDE创建django项目的流程

![1573785562870](day47.assets/1573785562870.png)

![1573785544300](day47.assets/1573785544300.png)



### 项目目录文件介绍

```
项目文件夹:
    manage.py ----- Django项目里面的工具，通过它可以调用django shell和数据库，启动关闭项目与项目交互等，不管你将框架分了几个文件，必然有一个启动文件，其实他们本身就是一个文件。
    settings.py ---- 包含了项目的默认设置，包括数据库信息，调试标志以及其他一些工作的变量。
    urls.py ----- 负责把URL模式映射到应用程序。
    wsgi.py ---- runserver命令就使用wsgiref模块做简单的web server，后面会看到renserver命令，所有与socket相关的内容都在这个文件里面了，目前不需要关注它。
```



## urls路由

```
urlpatterns = [
    # 循环进行匹配,一旦匹配成功,就会执行后面的函数,并且不再往下面进行匹配了
    url(r'^admin/', admin.site.urls), #第一个参数:正则   第二个参数:视图函数
    url(r'^home/', views.home),  
]

```

### 响应方法

```
# render回复html页面
# HttpResponse 回复字符串
```

### url写法

```
无名分组
    url(r'^books/(\d+)/(\d+)/', views.books), #url无名分组,也可以叫做无名参数
	视图函数写法:
		def books(request,y,n):pass  y:拿到的是第一个参数,n拿到的是第二个参数
		传参方式是 位置传参
		
有名分组
    url(r'^books/(?P<year>\d+)/(?P<month>\d+)/', views.books), 
    视图函数写法:
		def books(request,year,month):pass  year和month拿到的正则有名分组匹配到的那个名字相同的参数,
		传参方式是 关键字传参,不考虑参数顺序,但是名称一定要和正则的相同
		
def books(request,y,n=None):pass	 n=None就是默认值,当url正则匹配不到数据时,使用默认值,匹配到了的话,使用匹配结果	

注意:捕获的参数永远都是字符串

```



## 视图函数

request对象

```
#     print(request.path)  #request.path当前请求路径
#     print(request.method) #当前请求方法(get,post...)
#     print(request.GET)
#     print(request.POST)
#     print(request.body)
#     # request.GET 获取所有get请求携带过来的数据
#     # request.POST 获取所有post请求携带过来的数据
#     # request.body 获取所有post请求携带过来的数据的原始格式
```



```
验证post请求时,记得改一下配置,在settings配置文件中
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


```





























































