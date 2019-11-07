

# 今日内容



## margin补充

```

margin-left:5%;  距离左边的距离为父级标签宽度的5%.

```



## js --  javascript

ECMAscript5 

ECMAscript6  -- vue.js  react ..

由三个部分组成

```
1 ECMAscript5的核心   js语言
2 BOM  浏览器对象模型  js操作浏览器,做出对应的一些效果
3 DOM  文档对象模型 -- HTML文件
```



## js代码引入方式

​	

```
三种方式
1 head标签的script标签里面(alert('xx'), confirm('xx'))
2 body标签的script标签里面
3 外部文件引入的方式来使用
	a 创建一个.js结尾的文件,写上咱们的js代码
		比如:alert('are you ok?');
	b 在想使用这个js代码的html文件中,head标签或者body标签下面或者上面写下面的内容	
		<script src="01test.js"></script>

```



## js语言基础

### 变量

```
var a = 10;  变量定义 var 变量名;
```



### 数据类型

#### 	number类型(整数,浮点数)

```
var n = 11;
var n2 = 11.11;
js代码注释  // js代码

查看数据类型 typeof 变量名;
	typeof n; -- number类型
	
变量声明,但没有赋值的时候,变量的值为undefined

```

#### 	string类型(字符串)

```
示例:
 var a = 'alexsb';
var a = new String('ss');  typeof a; -- "string"
字符串的操作方式
var s = '诱色可餐徐茂洁';
索引取值:  s[1] -- '色'
移除两端空格: s.trim();   s.trimLeft(); s.trimRight();

var value = name.charAt(index) 			// 根据索引获取字符
	示例: var s = 'hello'; -- s.charAt(4); -- 'o'
var value = name.substring(start,end) 	// 根据索引获取子序列,切片
	示例: s.substring(1,3); -- "el"

```

#### 	布尔类型(boolean类型)

```
var a = true;
var b = false;
```

#### 	undefined和null类型

```
undefined 变量声明了,但是没有赋值,此时这个变量是undefined类型
null : 变量不用了,就可以给变量赋值为null,--- object类型
```

#### 数组(array)

```
var name = [11,22,33];

数组常用方法:
names[0]						// 索引,索引也是从0开始的

names.push(ele)     			// 尾部追加元素
	示例:a.push('xx'); --  [11, 22, 33, "xx"]
var ele = names.obj.pop()     	// 尾部移除一个元素
	示例:a.pop(); -- [11, 22, 33]
names.unshift(ele)  			// 头部插入元素
	示例:a.unshift('ssss'); --  ["ssss", 11, 22, 33]
var ele = obj.shift()         	// 头部移除一个元素
	示例:a.shift(); --  [11, 22, 33]
names.splice(index,0,ele) 		// 在指定索引位置插入元素
names.splice(从哪删(索引),删几个(个数),删除位置替换的新元素(可不写,可写多个)) 
names.splice(index,1,ele) 		// 指定索引位置替换元素
names.splice(index,1)     		// 指定位置删除元素
	示例: a.splice(1,2) --  [11, 22, 33]
		a.splice(1,1,'xx','oo','asdf'); -- [11, "xx", "oo", "asdf", 33]


names.slice(start,end)        	// 切片
	示例:a.slice(1,3);--  [22, 33]
	
names.reverse()      			// 原数组反转
	示例:a.reverse(); -- [44, 33, 22, 11]
names.join(sep)       			// 将数组元素连接起来以构建一个字符串
	示例: var a = ['ni','hao','ma',18]
		a.join('+'); -- "ni+hao+ma+18"
names.concat(val,..)  			// 连接数组
	示例: var a = [11,22]; var b = ['aa','bb']
	var c = a.concat(b); c -- [11, 22, "aa", "bb"]
names.sort()         			// 对原数组进行排序
	很尬!
	需要自己定义规则:
		function compare(a,b){
           return a - b;  当大于0时,两个数据换位置
        };
        使用: a.sort(compare); 升序排列
```

#### 自定义对象(dict)

```
// 声明
info = {
    name:'武沛齐',
    "age":18
}

var a = {username:'xx',password:'123'}; //可以不加引号
typeof info;
"object"

// 常用方法
var val = info['name']		// 获取,通过键取值必须加引号,
info.name 也是可以的
info['age'] = 20			// 修改
info['gender'] = 'male'		// 新增
delete info['age']			// 删除
```



































































































































































































