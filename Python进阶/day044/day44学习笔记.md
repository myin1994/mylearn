# 今日内容

input

```
    // 根据用户输入的内容,实时触发的事件
    $('#username').on('input',function () {
        // console.log($(this).val());
        // xxoo
       
    });
```



### 页面载入

```
window.onload =function(){}  等页面内容全部加载完毕之后触发的事件,但是存在覆盖现象.它属于原生js的方法

jquery写法
	$(function () {
            $('.c1').click(function () {
                $(this).toggleClass('c2');
            })
        });
  等待所有标签加载完成之后触发的事件,不存在覆盖现象      
        
```







# 记录问题

```
$(this).toggleClass('c4'); 不能使用同一个类值
```



## bootstrap

是一个开源框架,是对html\css\js\jquery等的封装,用法,复制黏贴一把梭.

网址: https://www.bootcss.com/



```
border-radius: 50%;  /* 边框圆角 */
```

font-awesome http://www.fontawesome.com.cn/





作业







































