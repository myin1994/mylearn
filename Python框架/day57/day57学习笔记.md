

## jquery之cookie操作

+ 引入（搜索下载）

  ```html
  <script type="text/javascript" src="js/jquery.min.js"></script>
  <script type="text/javascript" src="js/jquery.cookie.js"></script>
  ```

+ 设置cookie

  ```javascript
  $.cookie('the_cookie', 'the_value');
  ```

+ 设置有效期（天）/有效路径

  ```javascript
  $.cookie('the_cookie', 'the_value', { expires: 7 });
  $.cookie('the_cookie', 'the_value', { expires: 7, path: '/' });
  ```

+ 读取cookie

  ```javascript
  $.cookie('the_cookie');
  ```

+ 删除cookie

  ```javascript
  $.cookie('the_cookie', null);   //通过传递null作为cookie的值即可
  ```

+ 可选参数

  ```javascript
  $.cookie('the_cookie','the_value',{
      expires:7, 
      path:'/',
      domain:'jquery.com',
      secure:true
  })　
  ```

  + expires：（Number|Date）有效期；设置一个整数时，单位是天；也可以设置一个日期对象作为Cookie的过期日期；
  + path：（String）创建该Cookie的页面路径；
  + domain：（String）创建该Cookie的页面域名；
  + secure：（Booblean）如果设为true，那么此Cookie的传输会要求一个安全协议，例如：HTTPS；

+ 通过ajax通过csrf的第三种方式

  ```javascript
     $('#btn').click(function () {
  
          var uname = $('[type="text"]').val();
          var pwd = $('[type="password"]').val();
  
          $.ajax({
              url:'/login/',
              type:'post',
              headers:{'X-CSRFToken':$.cookie('csrftoken')}, // 设置请求头:
              data:{uname:uname,pwd:pwd,},
              success:function (res) {
                  console.log(res);
              }
          })
  ```

+ 全局配置（ 为所有的ajax请求做一个集体配置 ）

  ```javascript
  var csrftoken = $.cookie('csrftoken');
  
  function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  
  $.ajaxSetup({
      beforeSend: function (xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
  
  $(function () {
      $('#btn').click(function () {
          $.ajax({
              url: '/login/',
              type: "POST",
              data: {'username': 'root', 'pwd': '123123'},
              success: function (arg) {
  
              }
          })
      })
  });
  ```

+ 装饰器配置

  ​	 在讲完基本的csrf验证操作之后，我们还有一个可说的地方。在平时的产品需求当中，并不一定所有的接口验证都需要进行csrf验证，而我们之前采用的是在settings.py中间件配置进行全局配置，那么如果遇到了不需要开启csrf的时候该怎么办呢？ 

  ```python
  
  from django.views.decorators.csrf import csrf_exempt,csrf_protect
   
  @csrf_protect#开启csrf验证
  def index(request):
      .....
   
  @csrf_exempt#关闭csrf验证
  def login(request):
      .....
  ```

+ 详述CSRF

  ​		CSRF（Cross-site request forgery），中文名称：跨站请求伪造，也被称为：one click attack/session riding，缩写为：CSRF/XSRF。攻击者通过HTTP请求江数据传送到服务器，从而盗取回话的cookie。盗取回话cookie之后，攻击者不仅可以获取用户的信息，还可以修改该cookie关联的账户信息。

  　　所以解决csrf攻击的最直接的办法就是生成一个随机的csrftoken值，保存在用户的页面上，每次请求都带着这个值过来完成校验。

## form组件

```
1. 生成页面可用的HTML标签
2. 对用户提交的数据进行校验
3. 保留上次输入内容
```

使用步骤

1 创建form类

```

from django import forms

class LoginForm(forms.Form):
    # username = request.POST.get('username')
    # if '--' in username:
    #     raise
    # {'username':'xxxx','password':''}
    username = forms.CharField(
        label='用户名:',
        required=True,  #不 能为空
        max_length=7, # 长度不能超过7个字符
        min_length=2, # 最短不能低于2个字符
        # initial='张三', #初始值
        widget=forms.TextInput(attrs={'class':'c1','placeholder':'请输入用户名'}),
        error_messages={
            'required':'不能为空',
            'max_length':'太长了,难受!',
            'min_length':'太短了,更难受!',

        },
    )

    password = forms.CharField(
        required=True,
        label='密码:',
        widget=forms.PasswordInput(attrs={'class':'c1','placeholder':'请输入密码'},render_value=True), # render_value=True让密码输入的数据保留

    )

    sex = forms.ChoiceField(
        choices=[(1,'男'),(2,'女')],
        widget=forms.RadioSelect(attrs={'xx':'none'}),

    )
```



2 在views中实例化这个类对象,并交给前端html页面

```
def login(request):
    if request.method == 'GET':
        form_obj = LoginForm()

        return render(request,'login.html', {'form_obj':form_obj})
    else:

        form_obj = LoginForm(request.POST)
        # print(request.POST)
        status = form_obj.is_valid() # 开始校验
        # form_obj
        # username:alexxxxxx -- form_obj.username.errors.append('太长了!!')
        # username:alexxxxxx -- form_obj.username.errors.append('包含了--!feifa zifu')
        # password  form_obj.password.errors.append('太长了!!')
        print(status)


        return render(request,'login.html', {'form_obj':form_obj})
```

第三步 进行数据格式校验

```
        form_obj = LoginForm(request.POST)
        # print(request.POST)
        status = form_obj.is_valid() # 开始校验
        # form_obj
        # username:alexxxxxx -- form_obj.username.errors.append('太长了!!')
        # username:alexxxxxx -- form_obj.username.errors.append('包含了--!feifa zifu')
        # password  form_obj.password.errors.append('太长了!!')
        print(status)


        return render(request,'login.html', {'form_obj':form_obj})
```
