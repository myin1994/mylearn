

# 今日内容



## js补充

### class类值操作

```
var div1 = document.getElementById('d1');
div1.classList;  // 获取标签类值
div1.classList.add('c2'); // 添加类值
div1.classList.remove('c3'); // 删除类值
div1.classList.toggle('c3');  // 有就删除,没有就添加
var t = setInterval("div1.classList.toggle('c3')",1000);  //定时器添加
```

### HTML的label标签补充

```
    <label >用户名: 
        <input type="text" name="username" id="username">
    </label>
    <label for="password">密码: </label>
    <input type="password" name="password" id="password">
```

### button补充

```
普通按钮,没有提交效果
<input type="button">
<button type="button">注册</button>

下面两个能够提交form表单数据
<input type="submit" value='登录'>
<button type="submit">注册</button>

```



## jQuery

###  jquery引入

```
外部网址引入
	<!--<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>-->

本地文件引入
	<script src="jquery.js"></script>  //jquery.js本地文件路径

```



### jQuery初识

```
var d1 = $('#d1'); -- jquery对象  -- jQuery.fn.init [div#d1]
var d = document.getElementById('d1');  -- 原生dom对象 -- <div id='d1'></div>
jquery对象和dom对象之前不能调用互相的方法

jquery对象和dom对象可以互相转换
d1[0] -- dom对象
$(d) -- jquery对象
```



### 选择器

#### id选择器

```
$('#d1')  -- 同css
```

#### 类选择器

```
$('.c1') 
```

#### 元素选择器

```
$('标签名称') -- $('span')  
```

#### 组合选择器

```css
$('#d1,.c2')
示例:
	html代码
		<div id="d1"></div>
        <div class="c2">
            这是c2
        </div>
    css代码:
        #d1,.c2{
            background-color: red;
            height: 100px;
            width: 100px;
            border-bottom: 1px solid black;
        }
  
  jquery代码:
  	$('#d1,.c2').css('background-color','green');
  	$('#d1,.c2')[1];  -- 索引为1的dom对象
  	$('#d1,.c2').eq(1); -- 索引为1 的jquery对象

```



#### 层级选择器

```
$("form input")
```



#### 属性选择器

```
html代码:
    <div class="c1" xx="oo">
        这是啥!
    </div>
css代码:
    [xx]{
    	color:red;
    }

input标签:  type='xx'   [type='xx']--对应的input标签
$('[xx]').css('color','green');
$('[xx="oo"]').css('color','pink');

```

表单对象属性选择器

```
:checked  找到被选中的input标签
:selected  找被选中的select标签中的option标签
```



#### 表单选择器

```
$(":text") // 找到所有input标签
// $(":input") 找到所有input标签
// $(":password") 找到所有input且type=password的标签
// $(":radio") 找到所有input且type=radio的标签
// $(":checkbox") 找到所有input且type=checkbox的标签

html代码:
	<form action="">
        <input type="text" id="username">
        <input type="text" id="username2">
        <input type="password" id="pwd">

        <input type="submit">
    </form>
jquery代码:找到所有的type=text的input标签
	$(':text');

```



#### 筛选器方法

```
html代码
    <ul>

        <li>谢一峰</li>
        <li class="c1">王子宇</li>
        <li>孙波</li>
        <li class="c2">石淦</li>
        <li>
            <span>白雪冰</span>
        </li>
        <li>方伯仁</li>

    </ul>

```

##### parent()

```
var c = $('.c1');
c.parent();
c.parents();  直系的祖先辈
c.parentsUntil('body');  往上找,直到找到body标签为止,不包含body标签
```

##### children()

```
var u = $('ul');
u.children();  找到所有儿子标签
u.children('.c1'); 找到符合.c1选择器的儿子标签
```

##### next() 

```
var c = $('.c1');
c.next();
nextAll();  下面所有兄弟
c.nextUntil('.c2');  下面到某个兄弟为止,不包含那个兄弟
```

##### prev()

```
var c = $('.c1');
c.prev();
c.prevAll(); 上面所有兄弟,注意顺序都是反的
c.prevUntil('.c1'); 上面到某个兄弟为止,不包含那个兄弟,注意顺序都是反的
```

##### siblings()

```
c.siblings();  找到不包含自己的所有兄弟
c.siblings('.c1');  筛选兄弟中有class类值为c1的标签
```

##### find() 找后代

```
$('li').find('span'); 等同于css的 li span选择器
```

##### first()和last() 和eq(索引值)

```
$('li').first();  找所有li标签中的第一个
$('li').last(); 找所有li标签中的最后一个
$('li').eq(0);  按照索引取对应的那个标签,索引从0开始
$('li').eq(-1);  最后一个
 
```



### text()  和 html() 

 同js的innerText和innerHTML

```
取文本:
	c.text();  不带标签
	c.html();  带标签
设置文本:
	c.text('文本');
	c.html('文本'); -- 文本--"<a href=''>皇家赌场</a>"
```



### class类值操作

```

html代码
	<div class="c1">
    
	</div>
css代码:
	   .c1{
            background-color: red;
            height: 100px;
            width: 100px;
        }
        .c2{
            background-color: green;
        }
jquery
$('div').addClass('c2');
$('div').removeClass('c2');
$('div').toggleClass('c2');
示例:
	var t = setInterval("$('div').toggleClass('c2');",500);
```

### val值操作

```
示例:
html代码:

    <input type="text" id="username">
    <input type="radio" class="a1" name="sex" value="1">男
    <input type="radio" class="a1" name="sex" value="2">女
    <input type="checkbox" class="a2" name="hobby" value="1">抽烟
    <input type="checkbox" class="a2" name="hobby" value="2">喝酒
    <input type="checkbox" class="a2" name="hobby" value="3">烫头
    <select name="city" id="s1">
     <option value="1">北京</option>
     <option value="2">上海</option>
     <option value="3">深圳</option>
    </select>
    <select name="lover" id="s2" multiple>
     <option value="1">波多</option>
     <option value="2">苍井</option>
     <option value="3">小泽</option>
    </select>

jquery代码:
	
```

```
获取值：
 文本输人框：$('#username').val();
 单选radio框：$('.a1:checked').val();
 多选checkout框：$('.a2:checked').val()是不行的;需要循环取值，如下：
 var d = $(':checkbox:checked');
 for (var i=0;i<d.length;i++){
 console.log(d.eq(i).val());
 }
 单选select框：$('#city').val()；
 多选select框：$('#lover').val();
```

```
设置值：
 文本输入框：$('#username').val('you are my love');
 单选radio框：$('.a1').val([2]); #注意内容必须是列表，写的是value属性对应的值
 多选checkout框：$('.a2').val(['2','3'])
 单选select框：$('#city').val('1')；
 多选select框：$('#lover').val(['2','3'])
```

点击事件绑定

```
    $('.c1').click(function () {
        //$(this)表示的就是它自己
        $(this).css('background-color','green');
        // $('.c1').css('background-color','green');
    })
```









































































2 jquery选择器



3 文本操作



4 样式操作

















































