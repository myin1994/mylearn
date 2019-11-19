## 模板渲染

### 标签

#### for循环标签

+ 循环列表

  ```django
  <ul>
      {% for i in l1 %}
          <li>{{ i }}</li>
      {% endfor %}
  </ul>
  ```

+ 翻转循环列表

  ```django
  <ul>
      {% for i in l1 reversed %}
          <li>{{ i }}</li>
      {% endfor %}
  </ul>
  ```

+ 循环字典

  ```django
  <ol>
      {% for key in d1.keys %}  #循环字典的键
          <li>{{ key }}</li>
      {% endfor %}
      
      {% for key in d1.values %} #循环字典的值
          <li>{{ key }}</li>
      {% endfor %}
      
      {% for key,value in d1.items %} #循环字典的键值对
  		{{ forloop.counter }}
          <li>{{ forloop.last }}>>>>{{ key }}---{{ value }}</li>
          
          {% for foo in d1.hobby %}
              {{ forloop.parentloop.counter }}---{{ forloop.counter }}<a href="">{{ foo }}</a>
          {% endfor %}
  
      {% endfor %}
  
  </ol>
  ```

+ forloop计数

  ```django
  forloop.counter            当前循环的索引值(从1开始)，forloop是循环器，通过点来使用功能
  forloop.counter0           当前循环的索引值（从0开始）
  forloop.revcounter         当前循环的倒序索引值（从1开始）
  forloop.revcounter0        当前循环的倒序索引值（从0开始）
  forloop.first              当前循环是不是第一次循环（布尔值）
  forloop.last               当前循环是不是最后一次循环（布尔值）
  forloop.parentloop         本层循环的外层循环的对象，再通过上面的几个属性来显示外层循环的计数等
  ```

+ for …  empty

   给出的组是空的或者没有被找到时，可以有所操作 

  ```django
  {% for i in l1 %} #当没有数据时,会生成empty的内容
  <li>{{ i }}</li>
  {% empty %}
  <p>啥数据也没有!</p>
  {% endfor %}
  ```

#### if标签

​	if语句支持 and 、or、==、>、<、!=、<=、>=、in、not in、is、is not判断，注意条件两边都有空格。

```django

{% if num == 11 %}
    <a href="">详细些</a>
{% else %}
    <p>hahahhahah</p>
{% endif %}

多条件判断
    {% if num > 100 or num < 0 %}
        <p>无效</p>  <!--不满足条件，不会生成这个标签-->
    {% elif num > 80 and num < 100 %}
        <p>优秀</p>
    {% else %}  <!--也是在if标签结构里面的-->
        <p>凑活吧</p>
    {% endif %}
    
结合过滤来使用
    {% if user_list|length > 5 %}  <!--结合过滤器来使用-->
      七座豪华SUV
    {% else %}
        黄包车
    {% endif %}
```

#### with标签

用于给一个复杂的变量起别名 

+ `as`

  ```django
  <h1>
      {% with l2.1.name as sb  %}  #只能在with标签内部使用
          {{ sb }}  
          <a href="">{{ sb }}</a>
      {% endwith %}
  {#    {{ l2.1.name }}#}
  </h1>
  ```

+ `=`

  ```django
  {% with total=business.employees.count %}
      {{ total }} <!--只能在with语句体内用-->
  {% endwith %}
  ```

#### csrf_token通过csrf认证机制

+ 作用

  用于跨站请求伪造保护

+ 使用

  ```
  在页面的form表单里面（注意是在form表单里面）任何位置写上{% csrf_token %}，这个东西模板渲染的时候替换成了
  <input type="hidden" name="csrfmiddlewaretoken" value="8J4z1wiUEXt0gJSN59dLMnktrXFW0hv7m4d40Mtl37D7vJZfrxLir9L3jSTDjtG8">的隐藏标签，这个标签的值是个随机字符串，提交的时候，这个东西也被提交了，首先这个东西是我们后端渲染的时候给页面加上的，那么当你通过我给你的form表单提交数据的时候，你带着这个内容我就认识你，不带着，我就禁止你，因为后台我们django也存着这个东西，和你这个值相同的一个值，可以做对应验证是不是我给你的token。　　
  ```

+ post爬虫

  ```python
  import requests
  
  ret = requests.post('http://127.0.0.1:8000/login/',data={
      'uname':'chao',
      'pwd':'123',
  })
  
  print(ret.content.decode('utf-8'))
  ```

#### 注意事项

+  Django的模板语言不支持连续判断，即不支持以下写法 

  ```django
  {% if a > b > c %}#错误
  ...
  {% endif %}
  ```

+  Django的模板语言中属性的优先级大于方法 

  ```python
  views:
  def xx(request):
      d = {"a": 1, "b": 2, "c": 3, "items": "100"}
      return render(request, "xx.html", {"data": d})
  
  如上，我们在使用render方法渲染一个页面的时候，传的字典d有一个key是items并且还有默认的 d.items() 方法，此时在模板语言中:
  {{ data.items }}#默认会取d的items key的值,即"100"
  ```

  

### 模板继承

​	Django模版引擎中最强大也是最复杂的部分就是模版继承了。模版继承可以让您创建一个基本的“骨架”模版，它包含您站点中的全部元素，并且可以定义能够被子模版覆盖的 blocks 。

+ 定义模板

  在模板任意位置`{% block block_name %} {% endblock block_name %}`

  ```django
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <link rel="stylesheet" href="style.css" />
      <title>{% block title %}My amazing site{%/span> endblock %}</title>
  </head>
  
  <body>
      <div id="sidebar">
          {% block sidebar %}
          <ul>
              <li><a href="/">Home</a></li>
              <li><a href="/blog/">Blog</a></li>
          </ul>
          {% endblock %}
      </div>
  
      <div id="content">
          {% block content %}{% endblock %}
      </div>
  </body>
  </html>
  ```

  注： 不能在一个模版中定义多个相同名字的 `block` 标签 

+ 使用模板

  ```django
  {% extends "base.html" %}#引入模板
  
  {% block content %}
  	{{ block.super }}#使用模板对应块中内容
  	{{重写内容}}
  {% endblock %}
  ```

### 组件

```
1 写好一个组件.html文件
2 在使用这个组件的html文件中写上下面的内容
	{% include 'zujian.html' %}
```

### 自定义 标签和过滤器

+ 自定义过滤器

  + 在app应用文件夹中创建templatetags文件夹模块名只能是templatetags

  + 创建任意 .py 文件，如：my_tags.py

  + 文件中写上以下内容,自定义过滤器(参数最多两个)

    ```python
    from django import template
    register = template.Library()  #register变量名称必须是它
    @register.filter
    def func(v1,v2):#第一个参数是过滤器|前的变量
        print(v1,v2)
        return v1 + v2 #返回值为过滤器结果
    ```

  + html文件中

    ```django
    {% load my_tags %}
    
    <h1>{{ name|func:'xx' }}</h1>
    ```

+ 自定义标签

  + 其余同上，标签函数写法（可接收任意数量参数）

    ```python
    from django import template
    @register.simple_tag
    def tag1(*args): #第一个参数是过滤器|前的变量
        print(args)
        return " ".join(args) + 'ootag'
    ```

  + html文件中

    ```django
    {% load my_tags %}
    
    <h1>{% tag1 name "11" "222" %}</h1>
    ```

+ 动态标签组件

  + 组件html写法

    ```django
    文件名"leftmenu.html"
    <div class="menus">
        {% for i in data %}#要使用的数据data从tags中请求
        <div class="item"><a href="{{ i.0 }}">{{i.1}}</a></div>
        {% endfor %}
    </div>
    ```

  + 标签函数写法

    ```python
    from django import template
    @register.inclusion_tag("leftmenu.html")
    def left_menu(v1):
        return {"data":v1}#将对应字典键的值返回给动态组件（可返回多个键值对）
    ```

  + 视图函数views写法

    ```python
    def left_lead(request):
        # l1 = ["客户管理", "销售管理", 'xxoo']
        l1 = [[1,"客户管理"], [2,"销售管理"], [3,'xxoo']]
        return render(request,"left-lead.html",{"l1":l1})
    ```

  + html使用（调用动态标签组件）

    ```django
    {% load my_tags %}
    {% left_menu l1 %}#使用方向视图函数views请求数据并传递给标签函数tags
    ```

  + 执行逻辑总结

    ```
    html中load并使用动态组件标签，动态组件标签接收参数并传递给相应组件渲染，最后在本html显示。
    ```

    



