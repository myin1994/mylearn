# 路由Routers

对于视图集ViewSet，我们除了可以自己手动指明请求方式与动作action之间的对应关系外，还可以使用Routers来帮助我们快速实现路由信息。

REST framework提供了两个router

- **SimpleRouter**
- **DefaultRouter**

## 使用方法

+ 创建router对象，并注册视图集，例如

  ```python
  from rest_framework.routers import DefaultRouter,SimpleRouter
  # router = DefaultRouter() 调试页
  router = SimpleRouter() #原始django黄页
  router.register("goods",views.GoodsModelViewSet,basename="goods")
  ```

  register(prefix, viewset, basename)

  - prefix 该视图集的路由前缀
  
  - viewset 路由对应的视图集
  
  - basename 路由别名的前缀(默认为model类表名小写?),适用于所有生成的相关路由
  
  - 生成路由效果
  
    ```python
    opt/ ^goods/$ [name='goods-list']
    opt/ ^goods/(?P<pk>[^/.]+)/$ [name='goods-detail']
    ```
  
+ 添加路由

  + 第一种方式（常用）

    ```python
    urlpatterns = [
        ...
    ]
    urlpatterns += router.urls
    ```

  + 第二种方式

    ```python
    urlpatterns = [
        ...
        url(r'^', include(router.urls))
    ]
    ```

+ 实例

  + urls

    ```python
    from opt import views
    from rest_framework.routers import DefaultRouter,SimpleRouter
    # router = DefaultRouter()
    router = SimpleRouter()
    router.register("goods",views.GoodsModelViewSet,basename="goods")
    
    urlpatterns = []
    urlpatterns += router.urls
    ```

  + views

    ```python
    from .serializer import GoodsModelSerializer
    from goods.models import Goods
    
    # Create your views here.
    from rest_framework.viewsets import ModelViewSet
    class GoodsModelViewSet(ModelViewSet):
        queryset = Goods.objects
        serializer_class = GoodsModelSerializer
    ```

    

## 自定义方法生成路由-actions

在视图集中，如果想要让Router自动帮助我们为自定义的动作生成路由信息，需要使用`rest_framework.decorators.action`装饰器。

以action装饰器装饰的方法名会作为action动作名，与list、retrieve等同。

action装饰器相关参数：

- **methods**: 声明该action对应的请求方式，列表传递

- **detail**: 声明该action的路径是否与单一资源对应，即是否添加pk值

  ```
  xxx/<pk>/action方法名/
  ```

  - True 表示路径格式是`xxx/<pk>/action方法名/`
  - False 表示路径格式是`xxx/action方法名/`
  
- **url_path** 字符串,表示生成路由时,指向当前视图方法的路由地址

- **url_name** 字符串,表示生成路由时,指向当前视图方法的路由别名

- 实例

  - url

    ```python
    from opt import views
    from rest_framework.routers import DefaultRouter,SimpleRouter
    # router = DefaultRouter()
    router = SimpleRouter()
    router.register("goods",views.GoodsModelViewSet,basename="goods")
    
    urlpatterns = []
    urlpatterns += router.urls
    ```

  - views

    ```python
    from rest_framework.viewsets import ModelViewSet
    from rest_framework.decorators import action
    class GoodsModelViewSet(ModelViewSet):
        queryset = Goods.objects
        serializer_class = GoodsModelSerializer
    
        @action(methods=["get","post"],
         detail=True,url_path="get_two",url_name="get_two")
        def get_two(self,request):
            return Response("get_two方法")
    ```

  - 对应生成的url

    ```python
    opt/ ^goods/$ [name='goods-list']
    opt/ ^goods/(?P<pk>[^/.]+)/$ [name='goods-detail']
    opt/ ^goods/(?P<pk>[^/.]+)/get_two/$ [name='goods-get_two']
    ```

    

## 路由router形成URL的方式

+ SimpleRouter

![SimpleRouter]($%7Basserts%7D/SimpleRouter.png)

+ DefaultRouter

![DefaultRouter]($%7Basserts%7D/DefaultRouter.png)

DefaultRouter与SimpleRouter的区别是，DefaultRouter会多附带一个默认的API根视图，返回一个包含所有列表视图的超链接响应数据。

# 认证Authentication

+ 试验准备

  + 创建管理员账户

    ```
    python manage.py createsuperuser
    ```

  + 先修改站点的语言配置

    ```python
    #settings
    LANGUAGE_CODE = 'zh-hans'
    TIME_ZONE = 'Asia/Shanghai'
    ```

## 全局配置

+ 配置文件源路径

  ```
  python3.6/site-packages/rest_framework/settings.py
  ```

+ 全局配置(默认)

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': (
          'rest_framework.authentication.SessionAuthentication',  # session认证
          'rest_framework.authentication.BasicAuthentication',   # 基本认证
      )
  }
  ```

## 局部配置

在每个视图中通过设置authentication_classess属性来设置

```python
class GoodsModelViewSet(ModelViewSet):
    queryset = Goods.objects
    serializer_class = GoodsModelSerializer
    #类属性
    authentication_classess = [SessionAuthentication, BasicAuthentication]

    @action(methods=["get"], detail=False, url_path="get_two", url_name="get_two")
    def get_two(self, request):
        return Response("get_two方法")
```

认证失败会有两种可能的返回值，这个需要我们配合权限组件来使用：

- 401 Unauthorized 未认证
- 403 Permission Denied 权限被禁止

# 权限Pemissions

权限控制可以限制用户对于视图的访问和对于具体数据对象的访问。

- 在执行视图的as_view()方法的dispatch()方法前，会先进行视图访问权限的判断
- 在通过get_object()获取具体对象时，会进行模型对象访问权限的判断

## 提供的权限

- AllowAny 允许所有用户
- IsAuthenticated 仅通过登录认证的用户
- IsAdminUser 仅管理员用户
- IsAuthenticatedOrReadOnly 已经登陆认证的用户可以对数据进行增删改操作，没有登陆认证的只能查看数据。

## 全局配置

+ 全局配置

  ```python
  REST_FRAMEWORK = {
      ....
      
      'DEFAULT_PERMISSION_CLASSES': (
          'rest_framework.permissions.IsAuthenticated',
      )
  }
  ```

+ 默认全局配置

  ```python
  'DEFAULT_PERMISSION_CLASSES': (
     'rest_framework.permissions.AllowAny',
  )
  ```

## 局部配置

在具体的视图中通过permission_classes属性来设置

```python
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class GoodsModelViewSet(ModelViewSet):
    queryset = Goods.objects
    serializer_class = GoodsModelSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(methods=["get"], detail=False, url_path="get_two", url_name="get_two")
    def get_two(self, request):
        return Response("get_two方法")
```

## 自定义权限

+ 如需自定义权限，需继承rest_framework.permissions.BasePermission父类，并实现以下两个任何一个方法或全部
  + `.has_permission(self, request, view)`

    是否可以访问视图， view表示当前视图对象

  + `.has_object_permission(self, request, view, obj)`

    是否可以访问数据对象， view表示当前视图， obj为模型数据对象

+ 实例

  + 在当前子应用下，创建一个权限文件permissions.py中声明自定义权限类

    ```python
    from rest_framework.permissions import BasePermission
    
    class IsXiaoMingPermission(BasePermission):
        def has_permission(self, request, view):
            if( request.user.username == "xiaoming" ):
                return True
            else:
                return False
    ```

  + views使用

    ```python
    #添加类属性
    permission_classes = [IsXiaoMingPermission]
    ```

# 限流Throttling

可以对接口访问的频次进行限制，以减轻服务器压力，或者实现特定的业务。

一般用于付费购买次数,投票等场景使用。

## 全局配置

+ 全局配置（前提）

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_THROTTLE_CLASSES': (
          'rest_framework.throttling.AnonRateThrottle',# 针对匿名用户,很少用
          'rest_framework.throttling.UserRateThrottle' # 针对登录用户,很少用
      ),
      'DEFAULT_THROTTLE_RATES': {
          'anon': '100/day',# 匿名用户，对应AnonRateThrottle限流器
          'user': '1000/day'# 普通用户，对应UserRateThrottle限流器
      }
  }
  ```

  `DEFAULT_THROTTLE_RATES` 可以使用 `second`, `minute`, `hour` 或`day`来指明周期。

## 局部配置使用

在具体视图中通过throttle_classess属性来配置

```python
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
class GoodsModelViewSet(ModelViewSet):
    queryset = Goods.objects
    serializer_class = GoodsModelSerializer
	
    #配置限流器，决定使用全局的哪一种限流器
    throttle_classes = [AnonRateThrottle]

    @action(methods=["get"], detail=False, url_path="get_two", url_name="get_two")
    def get_two(self, request):
        return Response("get_two方法")
```

## 可选限流类

+ AnonRateThrottle
  + 限制所有匿名未认证用户，使用IP区分用户。
  + 使用`DEFAULT_THROTTLE_RATES['anon']` 来设置频次
+ UserRateThrottle
  + 限制认证用户，使用User id 来区分。
  + 使用`DEFAULT_THROTTLE_RATES['user']` 来设置频次

+ ScopedRateThrottle

  + 限制用户对于每个视图的访问频次，使用ip或user id。

  + 全局配置

    ```python
    REST_FRAMEWORK = {
        'DEFAULT_THROTTLE_CLASSES': (
            'rest_framework.throttling.ScopedRateThrottle',
        ),
        'DEFAULT_THROTTLE_RATES': {
            'contacts': '1000/day',#指定不同的限流频次
            'uploads': '20/day'
        }
    }
    ```

  + 局部使用---指定**throttle_scope**参数对应全局的限流频次

    ```python
    from rest_framework.throttling import ScopedRateThrottle
    class GoodsModelViewSet(ModelViewSet):
        queryset = Goods.objects
        serializer_class = GoodsModelSerializer
    
        throttle_classes = [ScopedRateThrottle]
        throttle_scope = "uploads"
    ```

# 过滤Filtering

+ 添加扩展

  对于列表数据可能需要根据字段进行过滤，我们可以通过添加django-fitlter扩展来增强支持。

  ```
  pip install django-filter
  ```

+ settings配置

  + 注册应用

    ```python
    INSTALLED_APPS = [
        ...
        'django_filters',  # 需要注册应用，
    ]
    ```

  + 全局配置(很少用)

    ```python
    REST_FRAMEWORK = {
        ...
        'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
    }
    ```

  + 局部配置----在视图类中添加类属性filter_backends进行指定（会覆盖全局）

    ```python
    filter_backends = [DjangoFilterBackend]
    ```

+ 使用---在视图类中添加类属性filter_fields，指定可以过滤的字段

  ```python
  from django_filters.rest_framework import DjangoFilterBackend
  class GoodsModelViewSet(ModelViewSet):
      queryset = Goods.objects
      serializer_class = GoodsModelSerializer
  
      filter_backends = [DjangoFilterBackend]
      filter_fields = ("id",'title', 'price')
  
  #http://127.0.0.1:8000/opt/goods/?title=python入门112
  ```

  **注意：只能进行等值过滤**

# 排序

对于列表数据，REST framework提供了**OrderingFilter**过滤器来帮助我们快速指明数据按照指定字段进行排序。

+ 使用方法

  + 在类视图中设置filter_backends，使用`rest_framework.filters.OrderingFilter`过滤器

    REST framework会在请求的查询字符串参数中检查是否包含了ordering参数，如果包含了ordering参数，则按照ordering参数指明的排序字段对数据集进行排序。

  + 前端可以传递的ordering参数的可选字段值需要在ordering_fields中指明

+ 实例

  + 单独使用排序

    ```python
    class StudentListView(ListAPIView):
        queryset = Student.objects.all()
        serializer_class = StudentModelSerializer
        filter_backends = [OrderingFilter]
        ordering_fields = ('id', 'age')
    
    # 127.0.0.1:8000/books/?ordering=-age
    # -id 表示针对id字段进行倒序排序
    # id  表示针对id字段进行升序排序
    ```

  + 排序结合过滤使用

    全局配置下的过滤组件不能和排序组件一起使用，只支持局部配置的过滤组件和排序组件一起使用。

    ```python
    from django_filters.rest_framework import DjangoFilterBackend
    from rest_framework.filters import OrderingFilter
    class GoodsModelViewSet(ModelViewSet):
        queryset = Goods.objects
        serializer_class = GoodsModelSerializer
    
        filter_backends = [DjangoFilterBackend,OrderingFilter]
        filter_fields = ("id",'title', 'price')
        ordering_fields = ("id",'title', 'price')
    
    #http://127.0.0.1:8000/opt/goods/?price=102&ordering=-id
    ```

# 分页Pagination

## 全局配置(很少用)

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':  'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100  # 每页数目
}
```

**注意：**如果在配置settings.py文件中， 设置了全局分页，那么在drf中凡是调用了ListModelMixin的list()，都会自动分页。如果项目中出现大量需要分页的数据，只有少数部分的分页，则可以在少部分的视图类中关闭分页功能。

```python
class 视图类(ListAPIView):
	pagination_class = None
```

## 局部配置---自定义Pagination类(可选分页器)

### PageNumberPagination

+ 前端访问网址形式

  ```http
  GET  http://127.0.0.1:8000/students/?page=4
  ```

+ 可以在子类中定义的属性

  + page_size 每页数目
  + page_query_param 前端发送的页数关键字名，默认为"page"
  + page_size_query_param 前端发送的每页数目关键字名，默认为None
  + max_page_size 前端最多能设置的每页数量

+ 使用--在类视图中设置**pagination_class**属性

+ 实例

  ```python
  from rest_framework.pagination import PageNumberPagination
  class StandardPageNumberPagination(PageNumberPagination):
      page_size = 2 # 默认de 每一页的数据量
      max_page_size = 3 # 允许客户端设置的每一页数据量的上限
      page_query_param = "pn" # 地址栏上面的页码参数
      page_size_query_param = "size" # 页码大小的参数[客户端可以通过size参数来指定每一页返回的数量]
  
  
  class GoodsModelViewSet(ModelViewSet):
      queryset = Goods.objects.all()
      serializer_class = GoodsModelSerializer
  
      pagination_class = StandardPageNumberPagination
  ```

### LimitOffsetPagination

+ 前端访问网址形式

  ```http
  GET http://127.0.0.1/four/students/?limit=100&offset=100
  ```

+ 可以在子类中定义的属性

  + default_limit 默认限制，默认值与`PAGE_SIZE`设置一致
  + limit_query_param limit参数名，默认'limit'
  + offset_query_param offset偏移量参数名，默认'offset'
  + max_limit 最大limit限制，默认None

+ 实例

  ```python
  from rest_framework.pagination import LimitOffsetPagination
  class StandardLimitOffsetPagination(LimitOffsetPagination):
      # 默认每一页查询的数据量,类似上面的page_size
      default_limit = 2
      limit_query_param = "size"
      offset_query_param = "start"
  
  class StudentAPIView(ListAPIView):
      queryset = Student.objects.all()
      serializer_class = StudentModelSerializer
      # 调用页码分页类
      # pagination_class = StandardPageNumberPagination
      # 调用查询偏移分页类
      pagination_class = StandardLimitOffsetPagination
  ```

# 异常处理 Exceptions

REST framework提供了异常处理，我们可以自定义异常处理函数。例如我们想在要创建一个自定义异常函数，这个函数，我们保存到当前子应用opt中[注意，开发时，我们会找个独立的公共目录来保存这种公共的函数/工具/类库]。

```python
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # 先调用REST framework默认的异常处理方法获得标准错误响应对象
    response = exception_handler(exc, context)

    # 在此处补充自定义的异常处理
    if response is None:
        response.data['status_code'] = response.status_code

    return response
```

在配置文件中声明自定义的异常处理

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'my_project.my_app.utils.custom_exception_handler'
}
```

如果未声明，会采用默认的方式，如下

```python
#rest_frame/settings.py
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'
}
```

例如：

补充上处理关于数据库的异常

```python
from rest_framework.views import exception_handler
from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # 先调用REST framework默认的异常处理方法获得标准错误响应对象
    response = exception_handler(exc, context)

    # 在此处补充自定义的异常处理
    if response is None:
        """response的值为None,有2种情况,
            1. 程序正常执行,没有发生异常
            2. 程序抛出异常,但是drf没有识别
        """
        response.data['status_code'] = response.status_code
        if isinstance(exc, DatabaseError):
            """判断是否为数据库异常"""
            # 把异常记录起来
            # context["view"] # 异常发生时的视图类
            view = context['view']
            print('[%s]: %s' % (view, exc))
            return Response({"detail":"程序内部错误!"}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response

```

## REST framework定义的异常

- APIException 所有异常的父类
- ParseError 解析错误
- AuthenticationFailed 认证失败
- NotAuthenticated 尚未认证
- PermissionDenied 权限决绝
- NotFound 未找到
- MethodNotAllowed 请求方式不支持
- NotAcceptable 要获取的数据格式不支持
- Throttled 超过限流次数
- ValidationError 校验失败

也就是说，很多的没有在上面列出来的异常，就需要我们在自定义异常中自己处理了。

#  自动生成接口文档

REST framework可以自动帮助我们生成接口文档。接口文档以网页的方式呈现。自动接口文档能生成的是继承自`APIView`及其子类的视图。

## 安装依赖

REST framewrok生成接口文档需要`coreapi`库的支持。

```python
pip install coreapi
```

## 设置接口文档访问路径

在总路由中添加接口文档路径。

文档路由对应的视图配置为`rest_framework.documentation.include_docs_urls`，

参数`title`为接口文档网站的标题。

```python
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    ...
    path('docs/', include_docs_urls(title='站点页面标题'))
]
```

在settings.py中配置接口文档。

```python
REST_FRAMEWORK = {
    # 。。。 其他选项
    # 接口文档
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
}
```

## 文档描述说明的定义位置

+ 单一方法的视图，可直接使用类视图的文档字符串，如

```python
class BookListView(generics.ListAPIView):
    """
    返回所有图书信息.
    """
```

+ 包含多个方法的视图，在类视图的文档字符串中，分开方法定义，如

```python
class BookListCreateView(generics.ListCreateAPIView):
    """
    get:
    返回所有图书信息.

    post:
    新建图书.
    """
```

+ 对于视图集ViewSet，仍在类视图的文档字符串中封开定义，但是应使用action名称区分，如

```python
class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    list:
    返回图书列表数据

    retrieve:
    返回图书详情数据

    latest:
    返回最新的图书数据

    read:
    修改图书的阅读量
    """
```

## 访问接口文档网页

浏览器访问 127.0.0.1:8000/docs/，即可看到自动生成的接口文档。

![æ¥å£ææ¡£ç½é¡µ]($%7Basserts%7D/%E6%8E%A5%E5%8F%A3%E6%96%87%E6%A1%A3%E9%A1%B5%E9%9D%A2.png)

#### 两点说明

+ 视图集ViewSet中的retrieve名称，在接口文档网站中叫做read
+ 参数的Description需要在模型类或序列化器类的字段中以help_text选项定义，如：

```python
class Student(models.Model):
    ...
    age = models.IntegerField(default=0, verbose_name='年龄', help_text='年龄')
    ...
```

或

```python
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        extra_kwargs = {
            'age': {
                'required': True,
                'help_text': '年龄'
            }
        }
```



