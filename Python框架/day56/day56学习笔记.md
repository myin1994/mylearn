## Cookie和session

### Cookie

+ 由来与概念

  + 由来

    HTTP协议是无状态的， 状态可以理解为客户端和服务器在某次会话中产生的数据，那无状态的就以为这些数据不会被保留。会话中产生的数据又是我们需要保存的，也就是说要“保持状态”。因此Cookie就是在这样一个场景下诞生。 

  + 概念

     cookie是浏览器的技术，Cookie具体指的是一段小信息，它是服务器发送出来存储在浏 览器上的一组组键值对，可以理解为服务端给客户端的一个小甜点，下次访问服务器时浏览器会自动携带这些键值对，以便服务器提取有用信息。  

+ Cookie的原理（ 通过HTTP请求和响应头在客户端和服务器端传递 ）

  +  Cookie：请求头，客户端发送给服务器端 
  + 格式：Cookie: a=A; b=B; c=C。即多个Cookie用分号离开；  Set-Cookie：响应头，服务器端发送给客户端；
  + 一个Cookie对象一个Set-Cookie： Set-Cookie: a=A Set-Cookie: b=B Set-Cookie: c=C 
  +  服务器端发送重复的Cookie会覆盖原有的Cookie 

  浏览器访问服务端，带着一个空的cookie，然后由服务器产生内容，浏览器收到相应后保存在本地；当浏览器再次访问时，浏览器会自动带上Cookie，这样服务器就能通过Cookie的内容来判断这个是“谁”了。

  <img src='https://images2018.cnblogs.com/blog/877318/201805/877318-20180516192005344-137605378.png'>

+ Cookie规范

  + Cookie大小上限为4KB
  +  一个服务器最多在客户端浏览器上保存20个Cookie 
  +  一个浏览器最多保存300个Cookie，因为一个浏览器可以访问多个服务器。 

+ Django 操作Cookie

  + 设置cookie(通过response对象)

    + 设置cookie(可设置多个-不允许中文)：set_cookie()
    + 设置签名cookie：set_signed_cookie()

    ```python
    ret = redirect(reverse("app01:books"))
    ret.set_cookie("login_status","success")
    
    #ret.set_signed_cookie("login_status","success","xxxooo")
    return ret
    ```

    + 相关参数
      +  key---键 
      +  value---值 
      +  max_age=None---超长时间 ,有效事件，max_age=20意思是这个cookie20秒后就消失了，默认时长是2周,这个是以秒为单位的
      +  expires=None---超长时间，值是一个datetime类型的时间日期对象，到这个日期就失效的意思
      +  path='/'--- Cookie生效的路径，/ 表示根路径，特殊的：根路径的cookie可以被任何url的页面访问 
      +  domain=None---Cookie生效的域名 
      +  secure=False----https传输 
      +  httponly=False ----只能http协议传输，无法被JavaScript获取（不是绝对，底层抓包可以获取到也可以被覆盖） 

  + 获取cookie(通过获取键)

    ```python
    login_status = request.COOKIES.get("login_status")
    login_status = request.get_signed_cookie("login_status",salt="xxxooo")
    ```

  + 删除cookie

    ```python
    ret.delete_cookie('login_status')
    #删除用户浏览器上之前设置的login_status值
    ```

+  cookie设置中文时的编码问题解决方案

  + 方式1:利用编码规则

    ```python
    def login(request):
    
        ret = HttpResponse('ok')
        
        ret.set_cookie('k1','你好'.encode('utf-8').decode('iso-8859-1'))
        
        #取值：request.COOKIES['k1'].encode('utf-8').decode('iso-8859-1').encode('iso-8859-1').decode('utf-8')
    
        return ret
    ```

  + 方式2:通过json

    ```python
    def login(request):
    
        ret = HttpResponse('ok')
        
        import json
    
        ret.set_cookie('k1',json.dumps('你好'))
        #取值 json.loads(request.COOKIES['k1'])
        return ret
    ```

    

### session

+ session概念

  Session是服务器端技术，利用这个技术，服务器在运行时可以 为每一个用户的浏览器创建一个其独享的session对象，由于 session为用户浏览器独享，所以用户在访问服务器的web资源时 ，可以把各自的数据放在各自的session中，当用户再去访问该服务器中的其它web资源时，其它web资源再从用户各自的session中 取出数据为用户服务。

  <img src="https://images2018.cnblogs.com/blog/877318/201805/877318-20180516210726463-1449400075.png">

  <img src='https://images2018.cnblogs.com/blog/867021/201805/867021-20180514143525989-365124875.png'>

+ session特点

  + 借助于cookie进行传输
  + 非明文显示
  + 长度不限

+ session优点

  + 比cookie相对安全一些
  + session没有大小限制
  + 可以配置多个存储方案,可以配置到缓存中

+ Django中使用session(理解为使用一个字典)

  + 使用流程

    ```
    1 生成随机字符串
    2 放到cookie中进行传输
    3 将随机字符串和对应数据保存到自己服务端的数据库中,django-session表
    ```

  + 设置session

    + request.session[key] = value
    + request.session.setdefault(key,value) # 存在则不设置

    ```python
    #设置的内容都通过键值对保存起来（先序列化再加密）
    request.session['login_status'] = "success"
    request.session['login_status1'] = "success1"
    ```

  + 获取session

    ```python
    login_status = request.session.get("login_status")
    login_status2 = request.session.get("login_status1")
    
    print(request.session.keys())
    print(request.session.values())
    print(request.session.items())
    ```

  + 获取会话session的key（数据库表中）

    ```python
    session_key = request.session.session_key  #获取sessionid的值
    session_key = request.COOKIES.get("sessionid")
    ```

  + 检查会话session的key在数据库中是否存在

    ```python
    request.session.exists("session_key") 
    #session_key就是那个sessionid的值
    ```

  + 删除方法

    + 将过期的session删除

      ```pythonpy
      request.session.clear_expired()
      ```

    + 删除当前会话的所有Session数据

      ```python
      request.session.delete()
      ```

    + 删除当前的会话数据并删除会话的Cookie

      ```python
      request.session.flush()  
      #常用，清空所有cookie---删除session表里的这个会话的记录，
      #这用于确保前面的会话数据不可以再次被用户的浏览器访问
      #例如，django.contrib.auth.logout() 函数中就会调用它。
      ```

  + 设置会话Session和Cookie的超时时间

    ```python
    request.session.set_expiry(value)
    * 如果value是个整数，session会在些秒数后失效。
    * 如果value是个datatime或timedelta，session就会在这个时间后失效。
    * 如果value是0,用户关闭浏览器session就会失效。
    * 如果value是None,session会依赖全局session失效策略。
    ```

+ Django中的Session配置

   Django中默认支持Session，其内部提供了5种类型的Session供开发者使用。 

  ```python
  1. 数据库Session
  SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）
  
  2. 缓存Session
  SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
  SESSION_CACHE_ALIAS = 'default'                            # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
  
  3. 文件Session
  SESSION_ENGINE = 'django.contrib.sessions.backends.file'    # 引擎
  SESSION_FILE_PATH = None                                    # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir() 
  
  4. 缓存+数据库
  SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'        # 引擎
  
  5. 加密Cookie Session
  SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'   # 引擎
  
  其他公用设置项：
  SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
  SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
  SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
  SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
  SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
  SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
  SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
  SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
  ```

  

### 实例

+ 登录验证(通过加装饰器)

   CSRF Token相关装饰器在CBV只能加到dispatch方法上，或者加在视图类上然后name参数指定为dispatch方法。 

  +  csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置全局中间件。 
  +  csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了全局中间件。 

  ```python
  class Login(View):
      def get(self, request):
  
          return render(request, "login.html")
  
      def post(self, request):
          username = request.POST.get("login_name")
          password = request.POST.get("login_password")
          print(request.POST)
          obj = models.UserInfo.objects.filter(password=password, username=username)
          if obj:
              ret = redirect(reverse("app01:books"))
              # ret.set_cookie("login_status","success")
              request.session['login_status'] = "success"
              return ret
          else:
              return HttpResponse("error")
  
  def login_sign(f):
      def inner(request):
          login_status = request.session.get("login_status")
          # login_status = request.COOKIES.get("login_status")
          if login_status != "success":
              return redirect("app01:login")
          else:
              ret = f(request)
              return ret
      return inner
  
  
  @method_decorator(login_sign,name='get')
  class Books(View):
      # @method_decorator(login_sign)
      def dispatch(self, request, *args, **kwargs):
          ret = super().dispatch(request, *args, **kwargs)
          return ret
  
      def get(self, request):
          dic = dict()
          obj = models.Book.objects.all()
          for i in obj:
              dic[i]=" ".join([j.name for j in i.authors.all()])
  ```

+ 退出功能

  ```python
  @func
  def logout(request):
      request.session.flush()  # 删除session
      '''
          1 删除cookie中的sessionid那个键值对
          2 删除了数据库中的这条记录
      '''
  
      return redirect('login')
  ```



## 中间件

+ 概念

  中间件是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出。因为改变的是全局，所以需要谨慎实用，用不好会影响到性能。（中间件位于wsgi与url之间）

  <img src='https://img2018.cnblogs.com/blog/988061/201903/988061-20190307152249812-1922952163.png'>

   当用户发起请求的时候会依次经过所有的的中间件，这个时候的请求时process_request,最后到达views的函数中，views函数处理后，在依次穿过中间件，这个时候是process_response,最后返回给请求者。 

  <img src='https://images2017.cnblogs.com/blog/877318/201710/877318-20171012212952512-1143032176.png'>

+ 自定义中间件

  + 基本步骤

    + 在应用下面创建文件夹，并建立py文件

    + 在文件中定义类并继承（MiddlewareMixin）

      ```python
      from django.utils.deprecation import MiddlewareMixin
      from django.shortcuts import render, redirect, HttpResponse
      from django.urls import reverse
      
      
      class Login_sign(MiddlewareMixin):
          white_list = [reverse("app01:login"),'/admin/login/']
          def process_request(self,request):
              login_status = request.session.get("login_status")
              print(request.path)
              if login_status == "success" or request.path in self.white_list:
                  return None
              else:
                  return redirect("app01:login")
      ```

    + settings配置文件中的MIDDLEWARE上添加这个类的路径

      ```python
      MIDDLEWARE = [
          'django.middleware.security.SecurityMiddleware',
          'django.contrib.sessions.middleware.SessionMiddleware',
          'django.middleware.common.CommonMiddleware',
          'django.middleware.csrf.CsrfViewMiddleware',
          'django.contrib.auth.middleware.AuthenticationMiddleware',
          'django.contrib.messages.middleware.MessageMiddleware',
          'django.middleware.clickjacking.XFrameOptionsMiddleware',
          'app01.mymiddleware.login_sign.Login_sign',
      ]
      ```

  + 可用的五个方法（重写父类方法）

    +  处理请求前 : 在每个请求上，request对象产生之后，url匹配之前调用，返回None或HttpResponse
      +  `process_request(self,request)`
    +  处理视图前 : 在每个请求上，url匹配之后，视图函数调用之前调用，返回None或HttpResponse对象。 
      + `process_view(self, request, view_func, view_args, view_kwargs)`
    +  处理响应后：视图函数调用之后，所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象。 
      + `process_response(self, request, response)`
    +  异常处理：当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象。 
      + `process_exception(self, request, exception)`
    + process_template_response(self,request,response): 是在视图函数执行完成后立即执行，但是它有一个前提条件，那就是视图函数返回的对象有一个render()方法（或者表明该对象是一个TemplateResponse对象或等价方法）。 

  + 中间件执行顺序

    + MD1

      ```python
      from django.utils.deprecation import MiddlewareMixin
      from django.shortcuts import render, redirect, HttpResponse
      
      
      class MD1(MiddlewareMixin):
      
          def process_request(self, request):
              print("MD1里面的 process_request")
      
          def process_response(self, request, response):
              print("MD1里面的 process_response")
              return response
      
          def process_view(self, request, view_func, view_args, view_kwargs):
              print("-" * 80)
              print("MD1 中的process_view")
              print(view_func, view_func.__name__)
      
          def process_exception(self, request, exception):
              print(exception)
              print("MD1 中的process_exception")
              return HttpResponse(str(exception))
      
          def process_template_response(self, request, response):
              print("MD1 中的process_template_response")
              return response
      
      ```

    + MD2

      ```python
      from django.utils.deprecation import MiddlewareMixin
      from django.shortcuts import render, redirect, HttpResponse
      
      
      class MD2(MiddlewareMixin):
          def process_request(self, request):
              print("MD2里面的 process_request")
              pass
      
          def process_response(self, request, response):
              print("MD2里面的 process_response")
              return response
      
          def process_view(self, request, view_func, view_args, view_kwargs):
              print("-" * 80)
              print("MD2 中的process_view")
              print(view_func, view_func.__name__)
      
          def process_exception(self, request, exception):
              print(exception)
              print("MD2 中的process_exception")
      
          def process_template_response(self, request, response):
              print("MD2 中的process_template_response")
              return response
      ```

    + 视图函数views

      ```python
      def index(request):
          print("app01 中的 index视图")
          # raise ValueError('出错啦') #异常1
          def render():
              print("in index/render")
              # raise ValueError('出错啦') #异常2-至于render函数中报错了，那么会先执行process_template_response方法，然后执行process_exception方法，如果是在render方法外面报错了，那么就不会执行这个process_template_response方法了。
              return HttpResponse("O98K") #返回的将是这个新的对象
          rep = HttpResponse("OK")
          rep.render = render
          return rep
      ```

    + 执行结果

      + 无异常时

        ```python
        页面：O98K
        
        
        MD1里面的 process_request
        MD2里面的 process_request
        --------------------------------------------------------------------------------
        MD1 中的process_view
        <function index at 0x000002EF310B7048> index
        MD2 中的process_view
        <function index at 0x000002EF310B7048> index
        app01 中的 index视图
        MD2 中的process_template_response
        MD1 中的process_template_response
        in index/render
        MD2里面的 process_response
        MD1里面的 process_response
        ```

      + 异常1

        ```python
        页面：出错啦1
        
        MD1里面的 process_request
        MD2里面的 process_request
        --------------------------------------------------------------------------------
        MD1 中的process_view
        <function index at 0x0000017D5AB7B048> index
        --------------------------------------------------------------------------------
        MD2 中的process_view
        <function index at 0x0000017D5AB7B048> index
        app01 中的 index视图
        出错啦
        MD2 中的process_exception
        出错啦
        MD1 中的process_exception
        MD2里面的 process_response
        MD1里面的 process_response
        ```

      + 异常2

        ```python
        页面：出错啦2
        
        MD1里面的 process_request
        MD2里面的 process_request
        MD1 中的process_view
        <function index at 0x000001F5B6B6B048> index
        --------------------------------------------------------------------------------
        MD2 中的process_view
        <function index at 0x000001F5B6B6B048> index
        app01 中的 index视图
        MD2 中的process_template_response
        MD1 中的process_template_response
        in index/render
        出错啦2
        MD2 中的process_exception
        出错啦2
        MD1 中的process_exception
        MD2里面的 process_response
        MD1里面的 process_response
        ```