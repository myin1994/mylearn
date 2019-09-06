## while

+ 关键字

+ 循环：不断的重复做某件事情

+ 先判断关键字后的条件，满足时执行，执行完最后一个语句返回继续判断，直到条件不成立

+ 理解逻辑

  + 死循环

    ```
    print("循环开始之前")
    while True: #死循环
        print("郭德纲")
        print("于谦")
        print("小岳岳")
        print("孙悦")
        print("五环之歌")
        print("鸡你太美")
        print("大面")
    print("造作")
    ```

  + 有限次数循环

    + break：终止当前循环

      ```
      count = 0
      while True:  #死循环
          print(111)
          count += 1  #先执行 = 右边的内容
          if count == 5:
              print(count)
              break #有限循环
      ```

    + continue：跳出本次循环继续下次循环（continue 就是伪装成循环体中最后一行代码）

      ```
      count = 0
      while True:  #死循环
          count += 1  #先执行 = 右边的内容
          if count == 5:
              print(111)
              continue
          print(count)
      ```

    + 注：continue 和 break 下方的代码都不会被执行

  + 通过条件控制循环次数

    + 计数器

      ```
      count = 0
      while count <2:
          print(count)
          count += 1
      ```

    + 练习题

      打印4-67

      ```
      count = 4
      while count <68:
          print(count)
          count += 1
      ```

      打印100-6

      ```
      count = 100
      while count >= 6:
          print(count)
          count -= 1
      ```

      打印1,3,5,7,9

      ```
      count = 1
      while count < 10:
          print(count)
          count += 2
      ```

  + while else:与if else相似，是一体的

    理解为while某次判断不满足条件时执行else中的语句

    + ```
      print(111)
      count = 0
      while count < 3:
          print(count) #若一直死循环，则可能是计算器没有进行计算
          count += 1
      print(222)
      ```
    
      ```
      print(111)
      count = 0
      while count < 3:
          print(count) #若一直死循环，则可能是计算器没有进行计算
          count += 1
      else: #理解为while某次次判断不满足条件时执行
          print(222)
      ```
    
      如上，两种方式输出的结果是一致的，但是下方的else属于循环之中的内容
    
    + ```
      print(111)
      count = 0
      while count < 3:
          print(count)
          count += 1
          break #结束当前循环，执行循环外的内容
      else:
          print(222)
      ```
    
      ```
      print(111)
      count = 0
      while count < 3:
          print(count)
          count += 1
          continue #相当于结束一次循环
      else:
          print(222)
      ```

## 格式化输出

按照固定的格式输出一些可变内容(如下：姓名，年龄，男，女)

```
msg = """
------infor------
name：姓名
age：18
sex：男
hobby：女
--------end------
"""
```

+ %方式-占位

  `msg = "%s,%d,%%"%(name,age)`

  + %s：传入字符串类型（也可填充数字）

  + %d|%i：传入整型（必须填充数字）

    ```
    name = input("name：")
    age = input("age：")
    sex = input("sex：")
    hobby = input("hobby：")
    
    msg = """
    ------infor------
    name：%s
    age：%d #%d决定传入的数据类型为整型，则下方需要对应
    sex：%s
    hobby：%s
    --------end------
    """
    print(msg%(name,int(age),sex,hobby)) #按位置顺序补位，占位数据类型要和变量类型保持一致
    ```

  + %%转义：使后面的%普通输出

    ```
    msg = "目前的学习进度为%s%%"
    print(msg%(2))
    ```

+ f-strings python3.6版本及以上才能使用

  `f"{name},{age},{{}}%"`

  ```
  msg = f"my name is {input('name:')} I'm {input('age:')} years old"
  print(msg)
  ```

## 常用运算符

1. 比较运算符

   ```
   > <
   >= <=
   ==
   !=
   ```

2. 算术运算符

   ```
   + - * / 
   // 整除，向下取整(地板除)
   ** 幂
   % 取余，取模
   ```

3. 赋值运算符

   | 运算符 | 描述             | 实例                                  |
   | :----- | :--------------- | :------------------------------------ |
   | =      | 简单的赋值运算符 | c = a + b 将 a + b 的运算结果赋值为 c |
   | +=     | 加法赋值运算符   | c += a 等效于 c = c + a               |
   | -=     | 减法赋值运算符   | c -= a 等效于 c = c - a               |
   | *=     | 乘法赋值运算符   | c *= a 等效于 c = c * a               |
   | /=     | 除法赋值运算符   | c /= a 等效于 c = c / a               |
   | %=     | 取模赋值运算符   | c %= a 等效于 c = c % a               |
   | **=    | 幂赋值运算符     | c ******= a 等效于 c = c ** a         |
   | //=    | 取整除赋值运算符 | c //= a 等效于 c = c // a             |

4. 逻辑运算符

   ```
   与（and）：同真为真，有假为假
   或（or）：有真为真，同假为假
   非（not）：取反
   优先级：() > not > and > or
   查找顺序：从左向右,返回值为最后一个变量
   ```

   

   逻辑操作符and 和or 也称作**短路操作符**（short-circuitlogic）或者惰性求值（lazy evaluation）：它们的参数从左向右解析，一旦结果可以确定就停止。

   例如，如果A 和C 为真而B 为假， A and B and C 不会解析C 。作用于一个普通的非逻辑值时，短路操作符的返回值通常是最后一个变量。
   而或逻辑（or），即只要有一个是true，即停止解析运算数，返回最近为true的变量，即 3 or 4，值为3；改变顺序4 or 3 即为4

   总结：从左向右，and遇假即返回假值，都为真则返回最后的真值

   ​								or遇真即返回真值，都为假返回最后的假值

5. 成员运算符

   + in 在
   + not in 不在

       ```
   name = 'name'
   msg = input('输入内容')
   if name in msg:  #in 判断的是整体的字符
       print("在")
   else:
       print("不在")
       ```

## 编码初始

编码集（密码本）

+ ASCII 
  + 不支持中文
  + 一个字符占8位（共256种可能）
+ gbk（包含ASCII） 国标
  + 英文：一个字符占8位（1个字节）
  + 中文：一个字符占16位（2个字节）
+ unicode
  + 英文：4个字节 32位
  + 中文：4个字节 32位
+ utf-8（最流行的编码集）
  + 英文： 1个字节 8位
  + 欧洲：2个字节 16位
  + 亚洲：3个字节 24位

单位转换

```
    1Bytes = 8bit   ****
    1024Bytes = 1KB ****
    1024KB = 1MB
    124MB = 1GB
    1024GB = 1TB #够用
    1024TB = 1PB
```



