

# 今日内容

## jquery选择器补充

```css
:checked  找到被选中的input标签
:selected  找被选中的select标签中的option标签
:disabled  不可操作的标签 
:enabled   可操作的标签
示例:
	html代码:
		用户名:<input type="text" id="username" disabled>
		密码: <input type="text" id="password">
	jquery代码:
		$(':enabled');  
		$(':disabled');

```



模态对话框

## 创建标签

```js
添加标签:  $('.c1').html('<a href="http://www.baidu.com">百度</a>'); 但是这个属于替换内容,将标签内原来的内容全部替换掉.

js
	var a = document.createElement('a');
	
jquery:
	$('<a>',{
			text:'这还是个链接',
			href:'http://www.baidu.com',
			class:'link',
			id:'baidu',
			name:'baidu'
	})
```



## 文档操作

```
1 标签内部的后面插入内容 append
	html代码:
        <div class="c1">
            <h1>xx</h1>

        </div>
	方式1:
		1. var a = document.createElement('a'); 创建标签
		2. a.href = 'http://www.jd.com';  添加属性
		3. a.innerText = '京东'; 添加文本
		$('.c1').append(a);
	方式2: 常用
		$('.c1').append('<a href="http://www.baidu.com">百度</a>');
2 标签内部的上面插入内容 prepend
	$('.c1').prepend('<a href="http://www.baidu.com">百度</a>');
	$('.c1').prepend('<h1>亚洲</h1>');

3 标签外部的下面插入内容 after
	$('.c1').after('<h1>兄弟</h1>');
4 标签外部的上面插入内容 before
	$('.c1').before('<h1>兄弟</h1>');

简单示例:
	var s = $('<div>',{'class':'c2','text':'彭于晏'});
	$('.c1').after(s);
```



## empty清空标签

```
方式1:$('.c1').empty();
方式2:$('.c1').html(''); .text('')
```

## remove删除标签

```
$('.c1').remove();
```

## 字符占位符${变量名}

```
var tr_str = `<tr><td><input type="checkbox"></td><td>${inp_name}</td><td>${inp_hobby}</td><td><button class="delete">删除</button></td></tr>`;
```

增加和删除的示例

### 事件冒泡

点击儿子标签会触发父级标签\祖父标签..等等的所有点击事件,这叫事件冒泡

```js
html代码
    <div class="c1">
        <div class="c2"></div>
    </div>
css代码
	   .c1{
            border: 1px solid red;
            height: 100px;
        }
        .c2{
            border: 1px solid green;
            height: 50px;
            width: 50px;
        }

jquery代码
	$('.c1').click(function () {
        alert('父级标签c1');
    });
    $('.c2').click(function () {
        alert('儿子标签c2');
        return false; // 阻止后续事件发生
    });


```



### 事件委托

```
    // 事件委托
    $('tbody').on('click','.delete',function () {
        // $(this) 还是你点击的那个按钮标签
        $(this).parent().parent().remove(); // tr
        
    });
```



### prop属性操作

```
selected checked disabled enabled
设置属性
	$('#d1').prop('checked',true);    选中
	$('#d1').prop('checked',false);   取消选中
查看属性
	$('#d1').prop('checked'); true表示选中了,false表示未选中
```



### 逻辑运算符

```
and  &&
or   ||
not  !
```

### 全选反选取消的代码示例

```
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <title>Title</title>
</head>
<body>
<button id="all">全选</button>
<button id="reverse">反选</button>
<button id="cancel">取消</button>
<table border="1">
 <thead>
 <tr>
 <th>#</th>
 <th>姓名</th>
 <th>爱好</th>
 </tr>
 </thead>
 <tbody>
    <tr>
 <td><input type="checkbox"></td>
 <td>金老板</td>
 <td>开车</td>
 </tr>
 <tr>
 <td><input type="checkbox"></td>
 <td>景女神</td>
 <td>茶道</td>
 </tr>
 <tr>
 <td><input type="checkbox"></td>
 <td>苑昊（苑局）</td>
 <td>不洗头、不翻车、不要脸</td>
 </tr>
 </tbody>
</table>
<script src="jquery.js"></script>
<script>

    $('#all').click(function () {
        $('[type="checkbox"]').prop('checked',true);

    });
    $('#cancel').click(function () {
        $('[type="checkbox"]').prop('checked',false);

    });

    // 反选
    $('#reverse').click(function () {

        var all_inp = $('[type="checkbox"]');
        for (var i=0;i<all_inp.length;i++){
            var status = all_inp.eq(i).prop('checked');
            // if (status){
            //     all_inp.eq(i).prop('checked',false);
            // }else{
            //     all_inp.eq(i).prop('checked',true);
            // }

            // 简写方式
            all_inp.eq(i).prop('checked',!status);

        }


    })



 </script>
</body>
</html>
```

新增和删除

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <style>
        .shadow{
            position: fixed;  /* 固定定位 */
            top:0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0,0,0,0.8);
            z-index: 90; /* 控制定位的元素的层级,数字越大越在上层显示 */
        }

        .login{
            position: fixed;
            top:50%;
            left: 50%;
            background-color: white;
            width: 300px;
            height: 360px;
            z-index: 100;
            margin-left: -150px;
            margin-top: -180px;
        }

        .hide{
            display: none;
        }

    </style>

</head>
<body>

<div>
    <button id="btn">新增</button>
</div>

<table border="1">
    <thead>
    <tr>
        <th>#</th>
        <th>姓名</th>
        <th>爱好</th>
        <th>操作</th>
    </tr>
    </thead>
    <tbody>
        <tr>
            <td><input type="checkbox"></td>
            <td>潘景祥</td>
            <td>日京,日韩</td>
            <td>
                <button class="delete">删除</button>
            </td>
        </tr>
        <tr>
            <td><input type="checkbox"></td>
            <td>薛晓博</td>
            <td>日景祥,开车</td>
            <td>
                <button class="delete">删除</button>
            </td>
        </tr>

        <tr>
            <td><input type="checkbox"></td>
            <td>王赛</td>
            <td>日景祥</td>
            <td>
                <button class="delete">删除</button>
            </td>
        </tr>


    </tbody>
</table>




<div class="login hide" >
    <!--<form action="">-->

        <div>
            姓名:<input type="text" id="name">
        </div>
        <div>
             毕生追求:<input type="text" id="want">
        </div>
        <div>
            <button id="login-btn">保存</button>
            <button id="login-cancel">取消</button>
        </div>

    <!--</form>-->
</div>

<div class="shadow hide"></div>

</body>
<script src="jquery.js"></script>

<script>

    // $('#btn').click(function () {
    //     $('.shadow').removeClass('hide');
    //     $('.login').removeClass('hide');
    // });
    //
    // $('#login-cancel').click(function () {
    //     $('.shadow').addClass('hide');
    //     $('.login').addClass('hide');
    // });


    //一 新增 绑定用户的点击操作,弹出模态对话框
    $('#btn').click(function () {
        $('.shadow').removeClass('hide');
        $('.login').removeClass('hide');
    });

    //2 点击取消 关闭模态对话框
    $('#login-cancel').click(function () {
        // 2.1
        $('.shadow').addClass('hide');
        $('.login').addClass('hide');
        // 2.2 清空
        $('#name').val('');
        $('#want').val('');

    });
    // 3 保存
    // 3.1 用户输入数据,然后点击保存时获取用户输入的数据
    $('#login-btn').click(function(){
        var inp_name = $('#name').val();
        var inp_hobby = $('#want').val();

        // 3.2 创建标签,将数据加入到标签里面
        // var tr_str = '<tr><td><input type="checkbox"></td><td>'+ inp_name +'</td><td>'+ inp_hobby +'</td><td><button class="delete">删除</button></td></tr>';
        var tr_str = `<tr><td><input type="checkbox"></td><td>${inp_name}</td><td>${inp_hobby}</td><td><button class="delete">删除</button></td></tr>`;

        // 3.3 给tbody标签添加上我们做好的tr标签
        $('tbody').append(tr_str);
        // 3.4 关闭模态对话框,并且清空用户之前输入的数据
        $('.shadow').addClass('hide');
        $('.login').addClass('hide');
        $('#name').val('');
        $('#want').val('');


    });

    //二 删除
    // $('.delete').click(function () {
    //     // $(this)标签点击的那个按钮
    //     $(this).parent().parent().remove();
    //
    //
    // });

    // $('.delete').on('click',function () {
    //         $(this).parent().parent().remove();
    // })

    // 事件委托
    $('tbody').on('click','.delete',function () {
        // $(this) 还是你点击的那个按钮标签
        $(this).parent().parent().remove(); // tr

    });


</script>
</html>
```



### 常用事件

focus和blur

```
html代码:

	<input type="text" id="username">
	<div class="c1"></div>

css代码:
	    .c1{
            background-color: red;
            height: 200px;
            width: 200px;
        }
        .c2{
            background-color: green;
        }

    // focus获取光标时触发的事件
    $('#username').focus(function () {
        $(this).css({'background-color':'yellow'});
        $('.c1').addClass('c2');

    });
    // blur失去光标时触发的事件
    $('#username').blur(function () {
        $(this).css({'background-color':'white'});
        $('.c1').removeClass('c2');

    });
```



change

域内容发生变化时触发的事件

```
$('select').change(function () {
        // $('.c1').toggleClass('c2');
        // console.log($(this));
        // console.log($(this).options);
        // console.log($(this).selectedIndex)
        // console.log(this);  //dom对象  $(this)jquery对象
        // console.log(this.options);
        // console.log(this.selectedIndex);
        var option_text = this.options[this.selectedIndex].innerText;
        console.log(option_text);
        // if (option_text === '喝酒'){}
	// 获取被选中的option标签的文本内容
	// $(':selected').text();
    });
```



hover 

鼠标悬浮事件

```
示例
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1{
            background-color: red;
            height: 200px;
            width: 200px;
        }
    </style>
</head>
<body>

<div class="c1"></div>


</body>
<script src="jquery.js"></script>
<script>
    $('.c1').hover(
        // 鼠标进入时触发的事件
        function(){
            $('.c1').css({'background-color':'yellow'});
        },
        // 鼠标移出时触发的事件
        function(){
            $('.c1').css({'background-color':'blue'});
        }
    )


</script>
</html>
```



绑定事件的两个方式

```
$('.c1').click(function(){})
$('.c1').on('click',function(){})

事件委托
$('.c1').on('click','子辈的标签选择器',function(){})
```



input



页面载入













































