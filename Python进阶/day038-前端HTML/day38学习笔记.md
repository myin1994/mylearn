# HTML

## 文档结构

```html
<!DOCTYPE html>  文档声明
<html lang="en">  语言
<head>  网站配置信息
    <meta charset="UTF-8">  解码方式
    <title>皇家赌场</title>  网站标题
</head>
<body>   网站显示内容
    <h1>
        26期 皇家赌场
    </h1>

</body>
</html>
```



## head标签

### 1. meta 文档字符编码

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>我的网页</title>
    </head>
    <body>
        <h1>叫爸爸</h1>
    </body>
</html>
```

#### 标签写法分类

```html
全封闭标签  <h1 xx='ss'>xxx</h1>  
标签属性 :<h1 xx='ss'>xxx</h1>    xx:属性名  ss:属性值
自封闭标签  <meta charset="UTF-8">

```

### 1.2 meta 页面刷新

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>世上最牛逼的页面标题</title>
        <meta http-equiv="Refresh" content="5;url=xxx" /> 超时自动跳转新页面
    </head>
    <body>
        <h1>这是个栗子，快尼玛给我运行起来。</h1>
    </body>
</html>
```

### 1.3  meta 关键字

meta标签可以设置关键字，用于搜索引擎收录和关键字搜索。

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>世上最牛逼的页面标题</title>
        <meta name="keywords" content="欧美，日韩，国产，网红,直播" />
    </head>
    <body>
        <h1>这个栗子就别运行老子了，随便去看一个网站的源代码吧。</h1>
    </body>
</html>
```



### 1.4 meta 网站描述

meta标签可以设置网站描述信息，用于在搜索引擎搜索时，显示网站基本描述信息。

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>野鸭子</title>
        <meta name="keywords" content="欧美，日韩，国产，网红" />
        <meta name="description" content="野鸭子是一个面向全球的皮条平台。" />
    </head>
    <body>
        <h1>这个栗子就别运行老子了，随便去看一个网站的源代码吧。</h1>
    </body>
</html>
```

### 1.5 meta 触屏缩放



meta标签可以设置页面是否支持触屏缩放功能，其中各元素的含义如下：

- `width=device-width` ，表示宽度按照设备屏幕的宽度。
- `initial-scale=1.0`，初始显示缩放比例。
- `minimum-scale=0.5`，最小缩放比例。
- `maximum-scale=1.0`，最大缩放比例。
- `user-scalable=yes`，是否支持可缩放比例（触屏缩放）

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标题标题标题标题</title>
    
    <!--支持触屏缩放-->
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes">

    <!--不支触屏持缩放-->
    <!--<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">-->

</head>
<body>

    <h1 style="width: 1500px;background-color: green;">一起为爱鼓掌吧</h1>
</body>
</html>
```

### 1.6 link 图标

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>野鸭子</title>
		<link rel="icon" href="图标文件路径">
    </head>
    <body>
        <h1>隔壁王老汉的幸福生活</h1>
    </body>
</html>
```



### 简单head内部标签总结

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>野鸡平台</title>
    <meta name="keywords" content="欧美，日韩，国产，网红"/>
    <meta name="description" content="野鸡是一个面向全球的皮条平台。"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes">
    <link rel="icon" href="/image/chicken.icon">

</head>
<body>
    <h1 style="width: 1500px;background-color: green;">我们一起为爱鼓掌呀！！！</h1>
</body>
</html>
```





## body标签

### h1 - h6标签 ,标题标签

```html
<body>

    <h1>李晨浩</h1>
    <h2>冯俊</h2>
    <h3>刘炳良,大圣</h3>
    <h4>王勇杰</h4>
    <h5>苑子萌</h5>
    <h6>李海煜</h6>
</body>
```



### br标签  换行 

```html
    <h1>李晨浩</h1>
    <h2>冯<br>俊</h2>
```

注意点:**所有的回车空格等空白内容都被认为是一个空格**



### hr 标签  一行横线

```html
<h2>冯<hr>俊</h2>
```

body标签里面的没有其他标签包裹的内容,**就是普通文本显示**

```html
<body>
    你好!!!


</body>
```



### a 标签  超链接标签

1. 不加href属性,就是普通文本显示

```html
<a>python短片</a>
```

2. 加上href属性,不加值

```html
<a href="">python短片</a>
文字有颜色效果,还有下划线,并且点击后会刷新当前的html页面
```

3. 加上href属性,并且加上值

```html
<a href="http://www.pythonav.com" target="_self">python短片</a>

跳转对应网址的页面 
未访问之前是蓝色的字体颜色
访问之后是紫色的字体颜色
target属性:
	_self:在当前标签页打开 href属性值的那个网址
    _blank:在新的标签页打开 href属性值的那个网址

```

4. 锚点

   页面内容进行跳转

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<div id="top">这是顶部</div>

<a href="#i1">第一章 初入贵境</a>
<a href="#i2">第二章 开局一人一条狗</a>
<a href="#i3">第三章 就是干</a>
<a href="#i4">第四章 大结局</a>


<div id="i1" style="background-color: red;">第一章 初入贵境</div>
<p>
    没干啥好事儿!!
</p>
<p>
    没干啥好事儿!!
</p>
<p>
    没干啥好事儿!!
</p>
<p>
    没干啥好事儿!!
</p>
<div id="i2" style="background-color: red;">第二章 开局一人一条狗</div>
<p>
    给狗洗澡!!
</p>
<p>
    给狗洗澡!!
</p>
<p>
    给狗洗澡!!
</p>
<p>
    给狗洗澡!!
</p>
<div id="i3" style="background-color: red;">第三章 就是干</div>
<p>
    干狗!!!
</p>
<p>
    干狗!!!
</p>
<p>
    干狗!!!
</p>
<p>
    干狗!!!
</p>
<p>
    干狗!!!
</p>
<div id="i4" style="background-color: red;">第四章 大结局</div>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>
<p>
    中毒身亡!!!
</p>

<a href="#top">返回顶部</a>

</body>
</html>
```

描述:标签设置id属性=值(xx),a标签href属性的值写法:href='#xx',点击这个a标签就能跳转到id属性为xx的那个标签所在位置.

### img标签 图片标签

```html
<!--<img src="图片网络地址或者本地图片地址" alt="">-->
<!--<img width="200" height="200" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1572847825593&di=77d528287e8f7d62938cfd13888a2e7a&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20180505%2Fd2613066757341c28cc6f19a0a4bfdba.jpeg" alt="">-->
<img width="200" height="200" src="timg.jpg" alt="这是一个美女图片,稍等片刻" title="子萌">

src属性:图片路径  必须写
alt属性:图片加载失败或者正在加载时提示的内容
title属性:鼠标悬浮时显示的内容

# 不常用,通过css来控制
width:设置宽度
height:设置高度

```



### div标签和span标签

```
没有任何的文本修饰效果
```

### 标签分类

```
块级标签(行外标签):独占一行,h1-h6\p\br\hr\div\ul\li
	块级标签能够包含内联标签,和某些块级标签
内联标签(行内标签):不独占一行,img\a\span  只能包含内联标签,不能包含块级标签
```



### 列表标签 ul和ol标签

```html
示例:
	兴趣爱好:
    <ul>
        <li>抽烟</li>
        <li>喝酒</li>
        <li>烫头</li>

    </ul>
    
    喜欢的姑娘:
    <ol type="I" start="2">
        <li>韩红</li>
        <li>贾玲</li>
        <li>李宇春</li>
    </ol>
    
 #dl标签了解
    <dl>
        <dt>河北省</dt>
        <dd>邯郸</dd>
        <dd>石家庄</dd>
        <dt>山西省</dt>
        <dd>太原</dd>
        <dd>平遥</dd>
    </dl>
```



### table表格标签

```html
<table border="1">
        <thead>
        <tr>
            <th>id</th>
            <th>name</th>
            <th>hobby</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>1</td>
            <td>李晨浩</td>
            <td>看电影</td>
        </tr>
        <tr>
            <td>2</td>
            <td>冯俊</td>
            <td>迟到</td>
        </tr>
        <tr>
            <td>3</td>
            <td>大圣</td>
            <td>玩棍儿</td>
        </tr>

        </tbody>

    </table>
```



表格合并(rowspan="2"纵行合并    colspan='2' :横列合并)

```html
<table border="1">
        <thead>
        <tr>
            <th>id</th>
            <th>name</th>
            <th>hobby</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>1</td>
            <td>李晨浩</td>
            <!--<td rowspan="2">看电影</td>-->  
            <td>看电影</td>
        </tr>
        <tr>
            <td>2</td>
            <td>冯俊</td>
            <td>迟到</td>
        </tr>
        <tr>
            <td>3</td>
            <td colspan="2">大圣</td>
            <!--<td>玩棍儿</td>-->
        </tr>
        </tbody>

    </table>
```



### form标签  表单标签

```html
<form action="http://127.0.0.1:8001">
</form>
action属性: 指定提交路径,提交到哪里去

#form表单标签会将嵌套在form标签里面的输入框的数据全部提交到指定路径
```



### input标签  输入框

```html
# input标签,如果要提交数据,别忘了写name属性  例如:name='username' -- username='zhangjianzhi'

<input type="text">   普通文本输入框
<input type="password"> 密文输入框
<input type="submit" value="登录">  提交按钮  触发form表单提交数据的动作
<input type="reset"> 重置按钮 清空输入的内容
<input type="button" value="注册"> 普通按钮  不会触发form表单提交数据的动作
<input type="date">  时间日期输入框
<input type="file">  文件选择框
<input type="number">  纯数字输入框

单选框
    性别
    <input type="radio" name="sex" value="1">男  
    <input type="radio" name="sex" value="2">女
复选框(多选框)
    喜欢的明星:
    <input type="checkbox" name="hobby" value="1"> 波多 
    <input type="checkbox" name="hobby" value="2"> 小泽
    <input type="checkbox" name="hobby" value="3"> 仓井
```



### select下拉框标签

```html
   <select name="city" id="city">
        <option value="1">北京</option>
        <option value="2">上海</option>
        <option value="3">深圳</option>
        <option value="4">惠州</option>

    </select>
    <select name="citys" id="citys" multiple>
        <option value="1">北京</option>
        <option value="2">上海</option>
        <option value="3">深圳</option>
        <option value="4">惠州</option>
    </select>
    
    multiple:多选的意思
```

### textarea 多行文本输入框

```html
<textarea name="comment" id="comment" cols="20" rows="10"></textarea>
```



# css

称为层叠样式表

## css样式引入方式

### 第一种

```html
head标签中引入
<style>
    /* 选择器{css属性名称:属性值;css属性名称:属性值;} */
    div{
        /* css注释 */
        width: 200px;
        height: 200px;
        background-color: red;
    }

</style>


```

### 第二种方式

```html
外部文件引入  工作中常用的
创建一个css文件,stylesheet文件,比如test.css文件
里面写上以下代码
div{
    /* css注释 */
    width: 200px;
    height: 200px;
    background-color: red;
}

在想使用这些css样式的html文件的head标签中写上下面的内容
<link rel="stylesheet" href="test.css"> href对应的是文件路径
```

### 第三种引入方式

```html
内联样式:
<div style="background-color: red;height: 100px;width: 100px;"></div>
```



## css选择器

### 基本选择器

#### 元素选择器

```html
div{width:100px;}
标签名称{css属性:值}
```

#### id选择器

```html
html示例代码:
	<div id="d1">

    </div>
css写法:
    #d1{
        background-color: green;
        width: 100px;
        height: 100px;
    }

```

#### 类选择器

```html
html代码:
<div id="d1" class="c1">
    李晨浩
</div>

<div id="d2" class="c2">
    李海煜
</div>

<div id="d3" class="c1">
    张建志
</div>

css写法
.c1{
    background-color: green;
    width: 100px;
    height: 100px;
}
```



### 属性选择器

```html
HTML代码
<div id="d1" class="c1" xx="ss">
    李晨浩
</div>

<div id="d2" class="c2" xx="kk">
    李海煜
</div>

css写法:
[xx]{  属性查找
    background-color: green;
    width: 100px;
    height: 200px;
}

[xx='ss']{ 属性带属性值查找
    background-color: green;
    width: 100px;
    height: 200px;
}

```

### 后代选择器

```html
html代码示例:
	<div id="d1" class="c1" xx="ss">
        <span>
            <a href="http://www.chenhao.com">李晨浩</a>
        </span>
    </div>

    <div id="d2" class="c2" xx="kk">
        <a href="http://www.chenhao.com">李海煜</a>

    </div>

    <div id="d3" class="c1">
        张建志
    </div>
    <a href="http://www.chenhao.com">xxxxxxx</a>
css代码:
    div a{	
        color:orange; /* 字体颜色 */
    }
```

### 组合选择器 (多个选择器逗号连接)

```html
html代码
    <div id="d1" class="c1" xx="ss">
        <span>
            <a href="http://www.chenhao.com">李晨浩</a>
        </span>
        <span>
            <span>xxx222</span>
        </span>
    </div>

    <div id="d2" class="c2" xx="kk">
        <a href="http://www.chenhao.com">李海煜</a>

    </div>

    <div id="d3" class="c1">
        <a href="">张建志</a>
    </div>
    <a href="http://www.chenhao.com">xxxxxxx</a>

    <span>官人,你好!</span>
    
css代码: 注意:a标签字体颜色设置,必须找到a标签才能设置
	#d1 a,#d3 a{
        background-color: pink;
        color:yellow;
    }

```

# 作业:

```
1.注册页面，需要包含：头像（文件上传）、用户名、密码、邮箱、性别、爱好、自我介绍
2.登录页面，需要包含：用户名、密码。
```
