## 视图函数

### request对象



### response对象

```
render  回复html页面

redirect  重定向
使用请求转发时，浏览器上显示的网址是首页的网址；而使用重定向时，浏览器上显示的网址是后台的网址。登录之后显示首页地址是不符合逻辑的，所以使用从定向。

HttpResponse  回复字符串
```

### CBV和FBV

```
FBV:function based view :基于函数的视图逻辑
CBV:class based view :基于类的视图逻辑
```

CBV中url写法

```
 # url(r'^login/', views.login),
    url(r'^login/', views.LoginView.as_view()),
    url(r'^login/(\d*)/', views.LoginViews.as_view(name="alex"))接收参数与对类属性赋值
```

视图写法

```python
from django.views import View

class LoginView(View):

    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        if uname == 'alex' and pwd == 'dsb':
            return redirect('/home/')
        else:
            return redirect('/login/')
```

源码重点

```python
    def dispatch(self, request, *args, **kwargs):  #根据请求方法去分发对应的类发放来执行
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:  
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)  #反射!!!!
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

```

重写dispatch方法

```python
class LoginView(View):
    def dispatch(self, request, *args, **kwargs):
        print(11111)
        # print(request.META)  #http所有相关请求头信息
        ret = super().dispatch(request, *args, **kwargs) #render(request, 'login.html')
        print(2222)
        return ret
    def get(self,request):
        print('this is get method!!!')
        return render(request, 'login.html')
    def post(self,request):
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if uname == 'alex' and pwd == 'dsb':
            return redirect('/home/')
        else:
            return redirect('/login/')
```



### CBV和FBV的装饰器

```python
def func(f):
    def foo(request):
        print(1111)
        ret = f(request)
        print(2222)
        return ret
    return foo


#FBV 模式下,和普通函数加装饰器是一样的写法
    @func   
    def home(request):
        print('home')
        return HttpResponse('你好,老了老弟,进来玩会!')
    
    
CBV加装饰的三个姿势:
    # @method_decorator(func,name='get') 位置3
    class LoginView(View):
        # @method_decorator(func) #位置2
        def dispatch(self, request, *args, **kwargs):
            print('aaaa')
            ret = super().dispatch(request, *args, **kwargs) #render(request, 'login.html')
            print('bbbb')
            return ret
        @method_decorator(func)  #位置1
        def get(self,request):
            print('this is get method!!!')
            return render(request, 'login.html')

        def post(self,request):
            uname = request.POST.get('username')
            pwd = request.POST.get('password')
            if uname == 'alex' and pwd == 'dsb':
                return redirect('/home/')
            else:
                return redirect('/login/')
```

### 上传文件到服务器的写法

```python
html:
<form action="" method="post" enctype="multipart/form-data">
    <input type="text" name="name" placeholder="书名"><br>
    <input type="file" name="icon"><br>
    <input type="submit" value="提交">
</form>

settings:
MEDIA_ROOT = os.path.join(BASE_DIR, "static/uploads")#配置上传文件存储路径

views:

import os
import uuid,hashlib
from day49 import settings
def get_unique_str():#生成不重复的文件名
    uuid_str = str(uuid.uuid4())
    md5 = hashlib.md5()
    md5.update(uuid_str.encode('utf-8'))
    return md5.hexdigest()


class Upload(View):
    def get(self,request):
        return render(request,"upload.html")

    def post(self,request):
        name = request.POST.get('name')
        myfile = request.FILES.get('icon')
        filename = get_unique_str() + '.' + myfile.name.split('.')[-1]

        # 文件路径
        filepath = os.path.join(settings.MEDIA_ROOT, filename)
        f = open(filepath, 'wb')
        for i in myfile.chunks():
            f.write(i)
        f.close()
        return HttpResponse('OK')
```



## 模板渲染

### settings配置

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]  #别忘了配置这个路径
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



### 模板语法

```
{{ 变量 }}  {% 逻辑 %}
```

### 万能的据点号  .

```
<h1>{{ num }}</h1>
<h1>{{ s }}</h1>
<h1>{{ l1.1 }}</h1>
<h1>{{ d1.number }}</h1>
<h1>{{ a.yue }}</h1>  #注意,调用方法时,不能加括号,所有如果方法带参数,就没法用了
<h1>{{ a.xx }}</h1>

views.py的写法
def home(request):

    num = 100
    s = 'hello my girl I love you'
    l1 = [11,22,33]
    d1 = {'name':'冠希哥','number':1000}
    class A:
        balance = 2000
        def __init__(self):
            self.xx = 'oo'
        def yue(self):
            return 'how much!'
    a = A()
    # render({'xx':'oo'})
    return render(request,'home.html',{'num':num,'s':s,'l1':l1,'d1':d1,'a':a})
```

### 过滤器

过滤器用法 {{ 变量|过滤器名称:'参数' }}  ,不是所有过滤器都有参数,如果没参数的话写法:{{ 变量|过滤器名称 }}

#### 内置过滤器

```
<h1>{{ s|truncatechars:n }}</h1> 过滤器里面的参数都可以写后端返回的变量

default -- <h1>{{ xx|default:'抱歉,没有数据!!' }}</h1> #默认值
length  -- <h1>{{ l1|length }}</h1>  获取变量数据长度
filesizeformat -- <h2>{{ file_size|filesizeformat }}</h2> #大小按照人类可读的显示
slice -- <h2>{{ s|slice:'0:7' }}</h2> #切片 顾头不顾腚
date: -- <h3>{{ now|date:'Y-m-d H:i:s' }}</h3>  #日期格式化显示
safe -- <h1>{{ a_tag|safe }}</h1> 数据:    a_tag = "<a href='http://www.baidu.com'>百度</a>"
	safe介绍
　　　　Django的模板中在进行模板渲染的时候会对HTML标签和JS等语法标签进行自动转义，原因显而易见，这样是为了安全，django担心这是用户添加的数据，比如如果有人给你评论的时候写了一段js代码，这个评论一提交，js代码就执行啦，这样你是不是可以搞一些坏事儿了，写个弹窗的死循环，那浏览器还能用吗，是不是会一直弹窗啊，这叫做xss攻击，所以浏览器不让你这么搞，给你转义了。但是有的时候我们可能不希望这些HTML元素被转义，比如我们做一个内容管理系统，后台添加的文章中是经过修饰的，这些修饰可能是通过一个类似于FCKeditor编辑加注了HTML修饰符的文本，如果自动转义的话显示的就是保护HTML标签的源文件。为了在Django中关闭HTML的自动转义有两种方式，如果是一个单独的变量我们可以通过过滤器“|safe”的方式告诉Django这段代码是安全的不必转义。
truncatechars -- <h1>{{ s|truncatechars:'6' }}</h1>
　　　　
join -- <h1>{{ l1|join:'+' }}</h1>

```



## 补充内容

url斜杠

```
url(r'^home/', views.home),  #前置导航斜杠不需要写,后面的斜杠是根据django的配置来的,如果在settings配置文件中我们设置了
# APPEND_SLASH = False,那么浏览器发送来的请求如果没有带着后面的斜杠,也是可以正常请求的,但是如果没有这个配置的话,django要求浏览器必须带着路径后面的斜杠来进行访问,如果你输入路径的时候没有加/,那么django让你的浏览器发一个重定向请求带上/.
```

## 静态文件配置

```
在项目中,其实js\css\jgp图片等等都称为静态文件.
在django中的使用
1 配置,在settings配置文件中写上以下配置

STATIC_URL = '/static/' #127.0.0.1:8000/static/bootstrap/css.

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'jingtaiwenjianjia'),
]

2 html文件中使用
    <link rel="stylesheet" href="/static/bootstrap-3.3.7-dist/css/bootstrap.min.css">  相对路径引入静态文件时,前置斜杠必须加上,不管是什么,a标签也是一样,相对路径访问,必须前面的斜杠
```
