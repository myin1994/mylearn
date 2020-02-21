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

#### APIView

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

