# 视图相关应用使用

drf除了在数据序列化部分简写代码以外，还在视图中提供了简写操作。所以在django原有的django.views.View类基础上，drf封装了多个视图子类出来提供给我们使用。

Django REST framwork 提供的视图的主要作用：

- 控制序列化器的执行（检验、保存、转换数据）
- 控制数据库查询的执行
- 调用请求类和响应类【这两个类也是由drf帮我们再次扩展了一些功能类。】

## 请求与响应

### Request

REST framework 传入视图的request对象不再是Django默认的HttpRequest对象，而是REST framework提供的扩展了HttpRequest类的**Request**类的对象。

REST framework 提供了**Parser**解析器，在接收到请求后会自动根据Content-Type指明的请求数据类型（如JSON、表单等）将请求数据进行parse解析，解析为类字典[QueryDict]对象保存到**Request**对象中。

**Request对象的数据是自动根据前端发送数据的格式进行解析之后的结果。**

无论前端发送的哪种格式的数据，我们都可以以统一的方式读取数据。

#### 常用属性

+ .data

  `request.data` 返回解析之后的请求体数据。类似于Django中标准的`request.POST`和 `request.FILES`属性，但提供如下特性：

  + 包含了解析之后的文件和非文件数据
  + 包含了对POST、PUT、PATCH请求方式解析后的数据
  + 利用了REST framework的parsers解析器，不仅支持表单类型数据，也支持JSON数据.query_params

+ .query_params

  `request.query_params`与Django标准的`request.GET`相同，只是更换了更正确的名称而已。

+ .body ……

  可继续使用原有的request的方法属性,如（body,path,GET,POST……）

### Response

```
rest_framework.response.Response
```

REST framework提供了一个响应类`Response`，使用该类构造响应对象时，响应的具体数据内容会被转换（render渲染器）成符合前端需求的类型。

REST framework提供了`Renderer` 渲染器，用来根据请求头中的`Accept`（接收数据类型声明）来自动转换响应数据到对应格式。如果前端请求中未进行Accept声明，则会采用默认方式处理响应数据，我们可以通过配置来修改默认响应格式。

可以在**rest_framework.settings**查找所有的drf默认配置项

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (  # 默认响应渲染类
        'rest_framework.renderers.JSONRenderer',  # json渲染器
        'rest_framework.renderers.BrowsableAPIRenderer',  # 浏览器API渲染器
    )
}
```

#### 构造方式

```python
Response(data, status=None, template_name=None, headers=None, content_type=None)
```

`data`数据不要是render处理之后的数据，只需传递python的内建类型数据即可，REST framework会使用`renderer`渲染器处理`data`。

`data`不能是复杂结构的数据，如Django的模型类对象，对于这样的数据我们可以使用`Serializer`序列化器序列化处理后（转为了Python字典类型）再传递给`data`参数。

参数说明：

- `data`: 为响应准备的序列化处理后的数据；
- `status`: 状态码，默认200；
- `template_name`: 模板名称，如果使用`HTMLRenderer` 时需指明；
- `headers`: 用于存放响应头信息的字典；
- `content_type`: 响应数据的Content-Type，通常此参数无需传递，REST framework会根据前端所需类型数据来设置该参数。

#### 常用属性

+ .data

  传给response对象的序列化后，但尚未render处理的数据

+ .status_code

  状态码的数字

+ .content

  经过render处理后的响应数据

#### 状态码

为了方便设置状态码，REST framewrok在`rest_framework.status`模块中提供了常用状态码常量。

##### 1）信息告知 - 1xx

此类状态代码表示临时响应。默认情况下，REST框架中没有使用1xx状态代码。

```python
HTTP_100_CONTINUE = 100      # 继续
HTTP_101_SWITCHING_PROTOCOLS = 101      # 交换协议
```

##### 2）成功 - 2xx

此类状态代码表示已成功接收，理解和接受客户端的请求。

```python
HTTP_200_OK = 200     # 请求成功OK
HTTP_201_CREATED = 201      # 请求已完成，并导致创建新资源
HTTP_202_ACCEPTED = 202      # 请求已被接受处理，但处理尚未完成
HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203      # 非权威信息
HTTP_204_NO_CONTENT = 204      # 无内容
HTTP_205_RESET_CONTENT = 205      # 重置内容
HTTP_206_PARTIAL_CONTENT = 206      # 服务器已完成对资源的部分GET请求。部分内容
HTTP_207_MULTI_STATUS = 207      # 多状态；由WebDAV(RFC 2518)扩展的状态码，代表之后的消息体将是一个XML消息，并且可能依照之前子请求数量的不同，包含一系列独立的响应代码。
```

##### 3）重定向 - 3xx

此类状态代码指示用户代理需要采取进一步操作才能完成请求。

```python
HTTP_300_MULTIPLE_CHOICES = 300      # 请求的资源具有多种选择
HTTP_301_MOVED_PERMANENTLY = 301      # 已为所请求的资源分配了一个新的永久URI；永久移动
HTTP_302_FOUND = 302      # 请求的网页被转移到一个新的地址，但客户访问仍继续通过原始URL地址，重定向，新的URL会在response中的Location中返回，浏览器将会使用新的URL发出新的Request。
HTTP_303_SEE_OTHER = 303      # 可以在不同的URI下找到对请求的响应，并且应该使用该资源上的GET方法检索。
HTTP_304_NOT_MODIFIED = 304      # 如果客户端已执行条件GET请求并允许访问，但文档尚未修改，则服务器应该响应此状态代码。
HTTP_305_USE_PROXY = 305      # 使用代理。必须通过Location字段给出的代理访问所请求的资源。
HTTP_306_RESERVED = 306      # 306状态代码在规范的先前版本中使用，不再使用，并且代码被保留。
HTTP_307_TEMPORARY_REDIRECT = 307      # 临时重定向。请求的资源暂时驻留在不同的URI下。
```

##### 4）客户端错误 - 4xx

4xx类状态代码适用于客户端似乎有错误的情况。除了在响应HEAD请求时，服务器应该包括一个实体，其中包含错误情况的解释，以及它是暂时的还是永久的。

```python
HTTP_400_BAD_REQUEST = 400      # 错误请求。由于语法格式错误，服务器无法理解请求。客户端不应该在没有修改的情况下重复请求。
HTTP_401_UNAUTHORIZED = 401      # 未经授权。该请求需要用户身份验证。
HTTP_402_PAYMENT_REQUIRED = 402      # 此代码保留供将来使用。
HTTP_403_FORBIDDEN = 403      # 服务器理解请求，但拒绝履行请求。
HTTP_404_NOT_FOUND = 404      # 服务器未找到与Request-URI匹配的任何内容。
HTTP_405_METHOD_NOT_ALLOWED = 405      # 客户端请求中的方法被禁止
HTTP_406_NOT_ACCEPTABLE = 406      # 服务器无法根据客户端请求的内容特性完成请求
HTTP_407_PROXY_AUTHENTICATION_REQUIRED = 407      # 此代码类似于401（未授权），但表示客户端必须首先使用代理进行身份验证。
HTTP_408_REQUEST_TIMEOUT = 408      # 请求超时。客户端在服务器准备等待的时间内没有产生请求。
HTTP_409_CONFLICT = 409      # 由于与资源的当前状态冲突，无法完成请求。
HTTP_410_GONE = 410      # 请求的资源在服务器上不再可用，并且不知道转发地址。预计这种情况将被视为永久性的。网站设计人员可通过301代码指定资源的新位置
HTTP_411_LENGTH_REQUIRED = 411     # 服务器无法处理客户端发送的不带Content-Length的请求信息
HTTP_412_PRECONDITION_FAILED = 412      # 在服务器上测试时，一个或多个请求标头字段中给出的前提条件被评估为false。
HTTP_413_REQUEST_ENTITY_TOO_LARGE = 413      # 服务器拒绝处理请求，因为请求实体大于服务器能够处理的请求实体。
HTTP_414_REQUEST_URI_TOO_LONG = 414      # 请求的资源URL长于服务器允许的长度
HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415      # 服务器无法处理请求附带的媒体格式
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = 416      # 客户端请求的范围无效
HTTP_417_EXPECTATION_FAILED = 417      # 服务器不满足请求Expect头字段指定的期望值，如果是代理服务器，可能是下一级服务器不能满足请求长。

HTTP_422_UNPROCESSABLE_ENTITY = 422     # 不可处理的请求实体。请求格式正确，但是由于含有语义错误，无法响应。
HTTP_423_LOCKED = 423      # 锁定；当前资源被锁定。
HTTP_424_FAILED_DEPENDENCY = 424      # 错误接洽关系。由于之前的某个请求发生的错误，导致当前请求失败，例如 PROPPATCH。
HTTP_428_PRECONDITION_REQUIRED = 428      # 要求先决条件；先决条件是客户端发送 HTTP 请求时，如果想要请求能成功必须满足一些预设的条件。
HTTP_429_TOO_MANY_REQUESTS = 429      # 请求过多。
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431      # 请求头字段太大	
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = 451      # 因法律原因而被官方审查。
```

##### 5）服务器错误 - 5xx

以数字“5”开头的响应状态代码表示服务器知道它已经错误或无法执行请求的情况。除了在响应HEAD请求时，服务器应该包括一个实体，其中包含错误情况的解释，以及它是暂时的还是永久的。

```python
HTTP_500_INTERNAL_SERVER_ERROR = 500      # 服务器内部错误，无法完成请求
HTTP_501_NOT_IMPLEMENTED = 501      # 服务器不支持请求的功能，无法完成请求
HTTP_502_BAD_GATEWAY = 502      # 服务器在充当网关或代理时，在尝试完成请求时从其访问的上游服务器收到无效响应。
HTTP_503_SERVICE_UNAVAILABLE = 503      # 服务不可用；由于服务器的临时过载或维护，服务器当前无法处理请求。一般为暂时性的。
HTTP_504_GATEWAY_TIMEOUT = 504      # 作为网关或代理服务器，服务器没有收到来自URI指定的上游服务器的及时响应（例如HTTP，FTP，LDAP）或尝试完成时需要访问的其他辅助服务器（例如DNS）请求。
HTTP_505_HTTP_VERSION_NOT_SUPPORTED = 505      # 服务器不支持或拒绝支持请求消息中使用的HTTP协议版本。
HTTP_507_INSUFFICIENT_STORAGE = 507      # 存储空间不足
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = 511      # 网络认证请求；如果你频繁使用笔记本和智能手机，你可能会注意到大量的公用 WIFI 服务要求你必须接受一些协议或者必须登录后才能使用。
```

## 视图类

REST framework 提供了众多的通用视图基类与扩展类，以简化视图的编写。

### 2个视图基类

#### APIView--基本视图类

```
rest_framework.views.APIView
```

`APIView`是REST framework提供的所有视图的基类，继承自Django的`View`父类。

`APIView`与`View`的不同之处在于：

- 传入到视图方法中的是REST framework的`Request`对象，而不是Django的`HttpRequeset`对象；
- 视图方法可以返回REST framework的`Response`对象，视图会为响应数据设置（render）符合前端要求的格式；
- 任何`APIException`异常都会被捕获到，并且处理成合适的响应信息；
- 在进行dispatch()分发前，会对请求进行身份认证、权限检查、流量控制。

支持定义的类属性

- **authentication_classes** 列表或元组，身份认证类
- **permissoin_classes** 列表或元组，权限检查类
- **throttle_classes** 列表或元祖，流量控制类

在`APIView`中仍以常规的类视图定义方法来实现get() 、post() 或者其他请求方式的方法。

举例：

```python
#路由配置
urlpatterns = [
    re_path('^goodsapi/(?P<id>\d*)',views.GoodsApiView.as_view(),name="goodsapi"),
]
```

```python
#views视图
# Create your views here.
"""APIView是drf里面提供的所有视图类的父类
   APIView提供的功能/属性/方法是最少的,所以使用APIView基本类似我们使用django的View
"""
"""
GET   /goods/ 获取多个商品信息 
POST  /goods/ 添加一个商品信息

GET    /goods/<pk>/  获取一个商品信息 
PUT    /goods/<pk>/  修改一个商品信息
DELETE /goods/<pk>/  删除一个商品信息
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import GoodsModelSerializer
from rest_framework.status import *

class GoodsApiView(APIView):
    def get(self, request, id=0):
        if not id:
            goods_obj = Goods.objects.all()
        else:
            try:
                goods_obj = Goods.objects.get(id=id)
            except:
                return Response({"message":"not exist"})
        serializer = GoodsModelSerializer(instance=goods_obj, many=not bool(id))
        return Response(serializer.data)

    def post(self, request, id=0):
        serializer = GoodsModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=HTTP_202_ACCEPTED)

    def put(self, request, id=0):
        try:
            goods_obj = Goods.objects.get(id=id)
            serializer = GoodsModelSerializer(instance=goods_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=HTTP_202_ACCEPTED)
        except:
            return Response({"message": "not exist"},status=HTTP_204_NO_CONTENT)

    def delete(self, request, id=0):
        try:
            goods_obj = Goods.objects.get(id=id)
            goods_obj.delete()
            return Response({"message": "already deleted"},status=HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "not exist"},status=HTTP_204_NO_CONTENT)
```

#### GenericAPIView--通用视图类

通用视图类主要作用就是把视图中的独特的代码抽取出来，让视图方法中的代码更加通用，方便把通用代码进行简写。

```
rest_framework.generics.GenericAPIView
```

继承自`APIVIew`，**主要增加了操作序列化器和数据库查询的方法，作用是为下面Mixin扩展类的执行提供方法支持。通常在使用时，可搭配一个或多个Mixin扩展类。**

+ 相关属性及方法

  + 关于数据库查询的属性与方法

    + 属性

      + **queryset** 指明使用的数据查询集（即queryset对象/objects对象亦可）

        ```python
        #源码
        queryset = None
        ```

      + **lookup_field & lookup_url_kwarg** 模型对象的查询参数字段

        ```python
        #源码
        lookup_field = 'pk'
        lookup_url_kwarg = None
        ```
  
    + 相关方法

      +  **get_queryset(self)** 获取视图使用的查询集

        主要用来提供给Mixin扩展类使用，是列表视图与详情视图获取数据的基础，默认返回`queryset`属性，可以重写

        ```python
      #源码
        def get_queryset(self):
          assert self.queryset is not None, (
                "'%s' should either include a `queryset` attribute, "
              "or override the `get_queryset()` method."
                % self.__class__.__name__
          )
        
          queryset = self.queryset
            if isinstance(queryset, QuerySet):
                # Ensure queryset is re-evaluated on each request.
                queryset = queryset.all()
            return queryset
        ```
        
      +  **get_object(self)** --根据查询字段获取模型对象
  
         在试图中可以调用该方法获取详情信息的模型类对象。**若详情访问的模型类对象不存在，会返回404。**
  
         该方法会默认使用APIView提供的check_object_permissions方法检查当前对象是否有权限被访问。
  
         ```python
         #源码
         def get_object(self):
         
             queryset = self.filter_queryset(self.get_queryset())
         
             # Perform the lookup filtering.
             lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
         
             assert lookup_url_kwarg in self.kwargs, (
                 'Expected view %s to be called with a URL keyword argument '
                 'named "%s". Fix your URL conf, or set the `.lookup_field` '
                 'attribute on the view correctly.' %
                 (self.__class__.__name__, lookup_url_kwarg)
             )
         
             filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
             obj = get_object_or_404(queryset, **filter_kwargs)
         
             # May raise a permission denied
             self.check_object_permissions(self.request, obj)
         
             return obj
         ```
  
  + 关于序列化器使用的属性与方法
  
    + 属性--**serializer_class** 指明视图使用的序列化器
  
      ```python
    #源码
      serializer_class = None
      ```
    
    + 相关方法
  
      +  **get_serializer_class(self)** 获取当前序列化器
  
        ```python
        #源码
        def get_serializer_class(self):
            assert self.serializer_class is not None, (
                "'%s' should either include a `serializer_class` attribute, "
                "or override the `get_serializer_class()` method."
                % self.__class__.__name__
            )
            return self.serializer_class
        ```
  
        + 当出现一个视图类中调用多个序列化器时,那么可以通过条件判断在get_serializer_class方法中通过返回不同的序列化器类名就可以让视图方法执行不同的序列化器对象了。
  
          返回序列化器类，默认返回`serializer_class`，可以重写，例如：
  
          ```python
          def get_serializer_class(self):
              if self.request.user.is_staff:
                  return FullAccountSerializer
              return BasicAccountSerializer
          ```
  
      + **get_serializer(self, *args, \**kwargs)** 获取序列化器对象
  
        主要用来提供给Mixin扩展类使用，如果我们在视图中想要获取序列化器对象，也可以直接调用此方法。
  
        ```python
        #源码
        def get_serializer(self, *args, **kwargs):
            serializer_class = self.get_serializer_class()
            kwargs['context'] = self.get_serializer_context()
            return serializer_class(*args, **kwargs)
        ```
  
      + **get_serializer_context** --在获取序列化器对象时添加补充参数**context**
  
        ```python
        #源码
        def get_serializer_context(self):
        
            return {
                'request': self.request,
                'format': self.format_kwarg,
                'view': self
            }
        ```
  
        + **request** 当前视图的请求对象
        + **view** 当前请求的类视图对象
        + **format** 当前请求期望返回的数据格式
  
  + 其他可以设置的属性
  
    + **pagination_class** 指明分页控制类
    + **filter_backends** 指明过滤控制后端
  
  + 实例
  
    + urls
  
      ```python
      urlpatterns = [
          #GenericAPIView
          path('gen/goodsapi/',views.GoodsGenericAPIView.as_view()),
          re_path('^gen/goodsapi/(?P<pk>\d+)',views.Goods2GenericAPIView.as_view()),
      ]
      ```
  
    + views
  
      ```python
      #GenericAPIView
      from rest_framework.generics import GenericAPIView
      class GoodsGenericAPIView(GenericAPIView):
          queryset = Goods.objects
          serializer_class = GoodsSerializer
      
          def get(self,request):
              instance = self.get_queryset()
              serializer = self.get_serializer(instance=instance,many=True)
              return Response(serializer.data)
      
          def post(self,request):
              serializer = self.get_serializer(data=request.data)
              serializer.is_valid(raise_exception=True)
              serializer.save()
              return Response(serializer.data, status=HTTP_201_CREATED)
      
      class Goods2GenericAPIView(GenericAPIView):
          queryset = Goods.objects
          serializer_class = GoodsSerializer
      
          def get(self,request,pk):
              instance = self.get_object()
              serializer = self.get_serializer(instance=instance)
              return Response(serializer.data)
      
          def put(self,request,pk):
              instance = self.get_object()
              serializer = self.get_serializer(instance=instance,data=request.data)
              serializer.is_valid(raise_exception=True)
              serializer.save()
              return Response(serializer.data, status=HTTP_201_CREATED)
      
          def delete(self,request,pk):
              self.get_object().delete()
              return Response("ok", status=HTTP_204_NO_CONTENT)
      ```
  
      

### 5个视图扩展类Mixin

Mixins是drf框架为了配合GenricAPIView提供出来的视图扩展类,提供了几种后端视图（对数据资源进行曾删改查）处理流程的实现，如果需要编写的视图属于这五种，则视图可以通过继承相应的扩展类来复用代码，减少自己编写的代码量。

这五个扩展类需要搭配GenericAPIView父类，因为五个扩展类的实现需要调用GenericAPIView提供的序列化器与数据库查询的方法。

#### ListModelMixin

**列表视图扩展类**，提供`list(request, *args, **kwargs)`方法快速实现列表视图，返回200状态码。

该Mixin的list方法会对数据进行过滤和分页。

```python
#源码
class ListModelMixin:
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        #过滤
        queryset = self.filter_queryset(self.get_queryset())
		#分页
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
		#序列化
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
```

#### CreateModelMixin

**创建视图扩展类**，提供`create(request, *args, **kwargs)`方法快速实现创建资源的视图，成功返回201状态码。

如果序列化器对前端发送的数据验证失败，返回400错误。

```python
#源码
class CreateModelMixin(object):
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        # 获取序列化器
        serializer = self.get_serializer(data=request.data)
        # 验证
        serializer.is_valid(raise_exception=True)
        # 保存
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
```

#### RetrieveModelMixin

**详情视图扩展类**，提供`retrieve(request, *args, **kwargs)`方法，可以快速实现返回一个存在的数据对象。

如果存在，返回200， 否则返回404。

```python
#源码
class RetrieveModelMixin(object):
    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        # 获取对象，会检查对象的权限
        instance = self.get_object()
        # 序列化
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
```

#### UpdateModelMixin

更新视图扩展类，提供`update(request, *args, **kwargs)`方法，可以快速实现更新一个存在的数据对象。

同时也提供`partial_update(request, *args, **kwargs)`方法，可以实现局部更新。

成功返回200，序列化器校验数据失败时，返回400错误。

```python
#源码
class UpdateModelMixin(object):
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        #获取partial参数状态值用于设置是否局部更新
        partial = kwargs.pop('partial', False)
        #获取对象
        instance = self.get_object()
        #获取序列化器对象
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        #验证
        serializer.is_valid(raise_exception=True)
        #保存
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        #调用时增加参数partial=True
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
```

#### DestroyModelMixin

删除视图扩展类，提供`destroy(request, *args, **kwargs)`方法，可以快速实现删除一个存在的数据对象。

成功返回204，不存在返回404。

```python
#源码
class DestroyModelMixin(object):
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        #获取对象
        instance = self.get_object()
        #调用方法删除
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
```

#### 实例

+ urls

  ```python
  urlpatterns = [
      #Mixins
      path('mix/goodsapi/',views.GoodsMinxinAPIView.as_view()),
      re_path('^mix/goodsapi/(?P<pk>\d+)',views.Goods2MinxinAPIView.as_view()),
  ]
  ```

+ views

  ```python
  #Mixins是drf框架为了配合GenricAPIView提供出来的视图扩展类
  from rest_framework.mixins import CreateModelMixin,\
      UpdateModelMixin,\
      DestroyModelMixin,\
      ListModelMixin,\
      RetrieveModelMixin
  
  class GoodsMinxinAPIView(GenericAPIView, ListModelMixin,CreateModelMixin):
      queryset = Goods.objects
      serializer_class = GoodsSerializer
  
      def get(self,request):
          return self.list(request)
  
      def post(self,request):
          return self.create(request)
  
  class Goods2MinxinAPIView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
      queryset = Goods.objects
      serializer_class = GoodsSerializer
  
      def get(self,request,pk):
          return self.retrieve(request,pk=pk)
  
      def put(self,request,pk):
          return self.update(request,pk=pk)
  
      def delete(self, request, pk):
          return self.destroy(request,pk=pk)
  ```

### GenericAPIView的视图子类

+ CreateAPIView

  + 提供 post 方法
  + 继承自： GenericAPIView、CreateModelMixin

+ ListAPIView

  + 提供 get 方法
  + 继承自：GenericAPIView、ListModelMixin

+ RetrieveAPIView

  + 提供 get 方法
  + 继承自: GenericAPIView、RetrieveModelMixin

+ DestoryAPIView

  + 提供 delete 方法
  + 继承自：GenericAPIView、DestoryModelMixin

+ UpdateAPIView

  + 提供 put 和 patch 方法
  + 继承自：GenericAPIView、UpdateModelMixin

+ RetrieveUpdateAPIView

  + 提供 get、put、patch方法
  + 继承自： GenericAPIView、RetrieveModelMixin、UpdateModelMixin

+ RetrieveUpdateDestoryAPIView

  + 提供 get、put、patch、delete方法
  + 继承自：GenericAPIView、RetrieveModelMixin、UpdateModelMixin、DestoryModelMixin

+ 实例

  + urls

    ```python
    urlpatterns = [
        #GenericAPIView视图子类
        path('genmix/goodsapi/',views.GoodsSonAPIView.as_view()),
        re_path('^genmix/goodsapi/(?P<pk>\d+)',views.Goods2SonAPIView.as_view()),
    ]
    ```

  + views

    ```python
    #GenericAPIView视图子类
    from rest_framework.generics import \
        ListAPIView,\
        CreateAPIView,\
        RetrieveAPIView,\
        UpdateAPIView,\
        DestroyAPIView
    
    class GoodsSonAPIView(ListAPIView,CreateAPIView):
        queryset = Goods.objects
        serializer_class = GoodsSerializer
    
    class Goods2SonAPIView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
        queryset = Goods.objects
        serializer_class = GoodsSerializer
    ```

### ViewSet--视图集

使用视图集，可以将一系列逻辑相关的动作放到一个类中：

- list() 提供一组数据
- retrieve() 提供单个数据
- create() 创建数据
- update() 保存数据
- destory() 删除数据

ViewSet视图集类不再实现get()、post()等方法，而是实现动作 **action** 如 list() 、create() 等。

视图集只在使用as_view()方法的时候，才会将**action**动作与具体请求方式对应上。如：

```python
class BookInfoViewSet(viewsets.ViewSet):

    def list(self, request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            books = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInfoSerializer(books)
        return Response(serializer.data)

```

在设置路由时，我们可以如下操作

```python
urlpatterns = [
    url(r'^books/$', BookInfoViewSet.as_view({'get':'list'}),
    url(r'^books/(?P<pk>\d+)/$', BookInfoViewSet.as_view({'get': 'retrieve'})
]
```

#### ViewSetMixin中as_view()源码解读

源码很长，这里只关注重点

1. 首先，确定as_view的函数中action的值就是我们的urls中as_view方法中的字典

   ![image-20200223174044860]($%7Basserts%7D/image-20200223174044860.png)

   ![image-20200223174110905]($%7Basserts%7D/image-20200223174110905.png)

2. 然后看下as_view这个方法的返回值

   ![image-20200223174414346]($%7Basserts%7D/image-20200223174414346.png)

3.  然后我再看下as_view中的view方法

   1. 利用反射替换对应的请求方法

      ```python
      for method, action in actions.items():
          #这里的handler就是self.create、update等方法
      	handler = getattr(self, action)
          #给对象绑定属性结果为self.get = self.list ,self.retrieve
          setattr(self, method, handler)
      ```

   2. view方法的返回值,可以看到这个函数的返回值是self.dispatch

      ```python
      self.request = request
      self.args = args
      self.kwargs = kwargs
      
      # And continue as usual
      return self.dispatch(request, *args, **kwargs)
      ```

   3. 我们注意到self.dispatch这个方法，在as_view和view均找不到，这个self是什么呢？这个self就是视图函数的类，所以我们来我们的视图函数的类中找下,最终在**APIView**中找到了这个方法

4. 看下dispatch方法干了什么

   ![image-20200223180521984]($%7Basserts%7D/image-20200223180521984.png)

   可以发现，这里分发请求时对应的就是上面绑定的对应的方法了，所以执行self.get等方法就会调用我们前面已经对应的self.list。self.retrieve等方法。

#### 常用视图集父类

#####  ViewSet

继承自`APIView`与`ViewSetMixin`，作用也与APIView基本类似，提供了身份认证、权限校验、流量管理等。

**ViewSet主要通过继承ViewSetMixin来实现在调用as_view()时传入字典（如{'get':'list'}）的映射处理工作。**

在ViewSet中，没有提供任何动作action方法，需要我们自己实现action方法。

##### GenericViewSet

使用ViewSet通常并不方便，因为list、retrieve、create、update、destory等方法都需要自己编写，而这些方法与前面讲过的Mixin扩展类提供的方法同名，所以我们可以通过继承Mixin扩展类来复用这些方法而无需自己编写。但是Mixin扩展类依赖与`GenericAPIView`，所以还需要继承`GenericAPIView`。

**GenericViewSet**就帮助我们完成了这样的继承工作，继承自`GenericAPIView`与`ViewSetMixin`，在实现了调用as_view()时传入字典（如`{'get':'list'}`）的映射处理工作的同时，还提供了`GenericAPIView`提供的基础方法，可以直接搭配Mixin扩展类使用。

+ 实例

  + urls

    ```python
    urlpatterns = [
        path("students7/", views.Student4ViewSet.as_view({"get": "list", "post": "create"})),
        re_path("students7/(?P<pk>\d+)/", views.Student4ViewSet.as_view({"get": "retrieve","put":"update","delete":"destroy"})),
    
    ]
    ```

  + views

    ```python
    from rest_framework.viewsets import GenericViewSet
    from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
    class Student4ViewSet(GenericViewSet,ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
        queryset = Student.objects.all()
        serializer_class = StudentModelSerializer
    ```

##### ModelViewSet

继承自`GenericViewSet`，同时包括了ListModelMixin、RetrieveModelMixin、CreateModelMixin、UpdateModelMixin、DestoryModelMixin。

+ 实例

  + urls

    ```python
    urlpatterns = [
        #ModelViewSet
        path('model/goodsapi/',views.GoodsModelViewSet.as_view({"get": "list", "post": "create"})),
        re_path('^model/goodsapi/(?P<pk>\d+)',views.GoodsModelViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    ]
    ```

  + views

    ```python
    from rest_framework.viewsets import ModelViewSet
    class GoodsModelViewSet(ModelViewSet):
        queryset = Goods.objects
        serializer_class = GoodsSerializer
    ```

##### ReadOnlyModelViewSet

继承自`GenericViewSet`，同时包括了ListModelMixin、RetrieveModelMixin。



#### 视图集中定义附加action动作

在视图集中，我们可以通过action对象属性来获取当前请求视图集时的action动作是哪个。

```python
from rest_framework.viewsets import ModelViewSet
from students.models import Student
from .serializers import StudentModelSerializer
from rest_framework.response import Response
class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get_new_5(self,request):
        #通过路由访问到当前方法中.可以看到本次的action就是请求的方法名
        print(self.action) # 获取本次请求的视图方法名
```

