# day03学习笔记

## 今日内容

字符串详解

1. 整型
2. 进制转换
3. 索引
4. 切片
5. 步长
6. 字符串的方法

## 整型

+ int()转换

+ 比较和计算

+ 进制转换

  + 10进制-->2进制

    + 除二取余法：整除2取余数，从下至上整合

    + bin()转换

      ```python
      print(bin(3))
      print(bin(9))
      print(bin(15))
      ```

  + 2进制-->10进制

    + 按权展开求和

      ```
      1010  从右向左，计算机从0数
      0 * 2 ** 0 + 1 * 2 ** 1 + 0 * 2 ** 2 + 1 * 2 ** 3 = 10
      ```

    + int("字符串"，n=2)

      将某个进制的（这里是2进制）数转换为10进制，传入的字符串要符合原始进制规则

      ```
      print(int("1010",2))
      print(int("27",8))
      ```

    + print(0b1010) 

      直接打印二进制数也为10进制数

+ 整型是不可变数据类型

  + 可在原地修改的叫做可变数据类型，不能在原地修改的叫做不可修改数据类型

  + 验证方法：id() -->查看空间内存地址

    ```
    a = 10
    print(id(a))
    a = a +1
    print(id(a)) #内存地址改变
    ```

## 索引（下标）

| 字符串 |  a   |  b   |  c   |  d   |  e   |
| :----: | :--: | :--: | :--: | :--: | :--: |
|  顺序  |  0   |  1   |  2   |  3   |  4   |
|  反序  |  -5  |  -4  |  -3  |  -2  |  -1  |

+ 通过索引准确定位内容

  ```
  print(name[2])
  print(name[-2])
  ```

+ 切片

  [起始位置:终止位置]      规则：顾首不顾尾

  ```
  name = "meet_alex_wusir"
  print(name[5:9])   #-->alex
  print(name[-5:])   #-->wusir
  print(name[:])     #-->全部字符串 meet_alex_wusir
  ```

+ 步长

  [起始位置:终止位置:步长（默认为1）] 

  可以用来控制查找步数和方向

  ```
  name = "meet_alex_wusir"
  print(name[2:7:2])  #找好收尾，看好方向和步长即可-->e_l
  print(name[4:-4:3]) 
  print(name[-1:4:-1]) 
  print(name[-1::-1]) 
  print(name[::-1])   #反向输出字符串
  ```

  注：索引时超出最大索引值会报错；

  ​		切片时超出最大索引值不会报错，理解为边界无限延伸

+ 索引切片只能给有序数据类型数据使用

+ 字符串是不可变数据类型

  + 有序：索引

  + 不可变数据类型：内存地址

    ```
    name = "meet"
    name1 = "meet"
    print(id(name))
    print(id(name1)) #小数据池--驻留机制，name,name1两变量内存地址一样(指向数据一致)
    name = name + 'xxx'
    print(id(name)) #name指向了新的字符串，则内存地址改变
    ```

## 字符串的方法详解（常用）

+ .upper()  全部转换为大写

+ .lower()  全部转换为小写

  + 栗子

  ```
  name = "xYzd"
  name1 = name.upper() #全部大写
  name2 = name.lower() #全部小写
  print(name)
  print(name1)
  print(name2)
  ```

  + 应用场景（验证码统一不区分大小写）

  ```
  yzm = "10jQkA"
  
  my_yzm = input(f'请输入验证码{yzm}：')
  if yzm.upper() == my_yzm.upper():
      print("正确")
  else:
      print("错误")
  ```

+ .startswith() 判断是否以某字符开头，返回bool；支持切片

+ .endswith() 判断是否以某字符结尾，返回bool；支持切片

  + 栗子

  ```
  name = "xyzd"
  print(name.startswith("x",1,3)) #-->False,即判断"yz"是否以"x"开头
  print(name.endswith("d",0,))    #-->True，切片时终止位置可缺省，开始位置不可
  ```

+ .count()  计数（统计）某字符串中某段字符串的个数，返回int

  ```
  name = "aaaeeeccbb"
  print(name.count("e")) 
  print(name.count("ee")) 
  ```

+ .strip() 去除头尾两端及换行符，制表符（空格，换行符：\n，制表符：\t）

  + 栗子

  ```
  name = "  你\n好   "  #\n 换行
  name1 = "  你\t好   \t"  #\n 制表符（tab）
  print(name1.strip())
  ```
  +  可指定内容去除头尾两端指定字符串（全部，直到没有）

  ```
  name = "aa  33a"
  print(name.strip("a"))  #去除头尾两端指定字符串（全部，直到没有）
  ```

  + 应用场景（去除账号密码前后的空格）

  ```
  account = input("账号：").strip()
  psw = input("密码：").strip()
  if account == "zhanghao" and psw == "12345":
      print("OK")
  else:
      print("NO")
  ```

+ .split() 默认按照空格及换行符，制表符进行分割(同时)；返回值为列表;同时分割符消失

  + 栗子

  ```
  a = "alex alex1234"
  print(a.split()) 
  ```

  + 可按指定内容进行分割

  ```
  a = "alex:alex1234"
  print(a.split(":")) 
  ```

  注：无分割符时整个被转换为列表的一个元素

+ is系列-判断用

  ```
  name = "alex"
  print(name.isalnum()) #判断是否由中文，字母，数字组成，返回bool
  print(name.isalpha()) #判断是否由中文，字母组成，返回bool
  print(name.isdigit()) #判断是否是阿拉伯数字（① ②也算->bug），返回bool
  print(name.isdecimal()) #判断是否是十进制，返回bool
  ```

## for 循环

+ 循环结构

  ```
  for i in xxx：
  
  for 关键字
  i 变量
  in 关键字
  xxx 可迭代对象
  ```

  + 可迭代对象：

    ```
    str --字符串
    list --列表
    tuple --元祖
    set --集合
    dict --字典
    range --范围
    ```

  + 不可迭代对象：

    ```
    int --整型
    bool --布尔型
    ```

+ for 循环实现打印

  ```
  for i in name: #内部for对i进行赋值,按顺序进行迭代，最后返回值为最后的值
      print(i)
  ```

  + 面试题

    ```
    name = "alex"
    for i in name:
        pass #占位（当行）
    print(i)
    
    输出：x
    ```

    