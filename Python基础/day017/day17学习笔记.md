## 正则表达式（re模块）

**正则表达式模式**（对要匹配的内容用规则进行描述）

```
模式字符串使用特殊的语法来表示一个正则表达式：
字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。
多数字母和数字前加一个反斜杠时会拥有不同的含义。
标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。
反斜杠本身需要使用反斜杠转义。
由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 \\t )匹配相应的特殊字符。
下表列出了正则表达式模式语法中的特殊元素。如果你使用模式的同时提供了可选的标志参数，某些模式元素的含义会改变。
```

+ findall

  ```
  import re
  s = "alex,meeeet,meva_j"
  print(re.findall("e",s)) #参数1：要查找的内容，参数2：从哪查找
  >>>['e', 'e', 'e', 'e']
  print(re.findall("ee",s)) #参数1：要查找的内容，参数2：从哪查找
  >>>['ee']
  ```

+ 常用匹配模式

  + \w  匹配中文、数字、字母、下划线

  + \W  匹配特殊字符

    ```
    s = "alex,你 好met2,m_j@!"
    print(re.findall("\w",s))
    >>>['a', 'l', 'e', 'x', '你', '好', 'm', 'e', 't', '2', 'm', '_', 'j']
    print(re.findall("\W",s)) 
    >>>[',', ' ', ',', '@', '!']
    ```

  + \s 匹配空格

  + \S 匹配非空格（包括特殊符号）

    ```
    s = "alex,你 好met2,m_j@!"
    print(re.findall("\s",s))
    >>>[' ']
    print(re.findall("\S",s))
    >>>['a', 'l', 'e', 'x', ',', '你', '好', 'm', 'e', 't', '2', ',', 'm', '_', 'j', '@', '!']
    ```

  + \d 匹配数字

  + \D 匹配非数字

    ```
    s = "alex,你 好met2,m_j@!"
    print(re.findall("\d",s))
    >>>['2']
    print(re.findall("\D",s))
    >>>['a', 'l', 'e', 'x', ',', '你', ' ', '好', 'm', 'e', 't', ',', 'm', '_', 'j', '@', '!']
    ```

  + `\A`  `^` 匹配字符串的开头(匹配内容放在符号后)   `^`在某个模式前表示取反

    ```
    s = "alex,你 好met2,m_j@!"
    print(re.findall("\Aal",s))
    >>>['al']
    print(re.findall("^a",s))
    >>>['a']
    ```

  + `\Z`  `$` 匹配字符串的结尾(匹配内容放在符号前)

    ```
    s = "alex,你 好met2,m_j@!"
    print(re.findall("!\Z",s))
    >>>['!']
    print(re.findall("j@!$",s))
    >>>['j@!']
    ```

    一般开头结尾配合使用进行匹配，在Django中使用

    ```
    print(re.findall("^al.*!$",s))
    >>>['alex,你 好met2,m_j@!']
    ```

  + \t  \n  匹配\t 和\n

    ```
    s = "你好e\teet\n"
    print(re.findall("\t",s))  #['\t']
    print(re.findall("\n",s))  #['\n']
    ```

  + `.` 匹配任意字符（\n除外）

    可指定re.DOTALL标记以匹配所有字符

    ```
    s = "你好e\teet\n"
    print(re.findall(".",s))
    >>>['你', '好', 'e', '\t', 'e', 'e', 't']
    print(re.findall(".",s,re.DOTALL)) 
    >>>['你', '好', 'e', '\t', 'e', 'e', 't', '\n']
    ```

  + []  指定匹配范围

    [数字0-数字9]范围

    ```
    s = "1234!abcd-ABC@_"
    print(re.findall("[0-9]",s))
    >>>['1', '2', '3', '4']
    ```

    [数字0-数字9a-zA-Z]范围

    ```
    s = "1234!abcd-ABC@_"
    print(re.findall("[0-9a-zA-Z]",s))
    >>>['1', '2', '3', '4', 'a', 'b', 'c', 'd', 'A', 'B', 'C']
    ```

    ["单独的字符或字符串"] 可指定指定内容

    ```
    s = "1234!abcd-ABC@_"
    print(re.findall("[-!0-9@]",s))
    >>>['1', '2', '3', '4', '!', '-', '@']
    ```

    [^"内容"]  匹配内容取反的内容

    ```
    s = "1234!abcd-ABC@_"
    print(re.findall("[^a-z^1-9^A^!]",s))
    >>>['-', 'B', 'C', '@', '_']
    ```

    `.` 在[]中失效，代表`.`本身

    ```
    s = "1,3,5.6.7"
    print(re.findall("[.]",s))
    >>>['.', '.']
    print(re.findall("[^.]",s))
    >>>['1', ',', '3', ',', '5', '6', '7']
    ```

  + 贪婪匹配

    + `*`  贪婪匹配左边字符，0-无穷大（没有取空，有能连续取就连续取）

    + `+`  贪婪匹配左边字符，1-无穷大（只要能连续取就连续取）

      ```
      s = "1234e678eeee"
      print(re.findall("e*",s))
      >>>['', '', '', '', 'e', '', '', '', 'eeee', '']
      print(re.findall("e+",s))
      >>>['e', 'eeee']
      ```

  + 非贪婪匹配   `?`  0-1 （没有取空，有取一个）

    ```
    s = "1234e678eeee"
    print(re.findall("e?",s)) 
    >>>['', '', '', '', 'e', '', '', '', 'e', 'e', 'e', 'e', '']
    ```

  + {}  定义取值个数或范围数

    ```
    s = "123e4e67ee8eeeee"
    print(re.findall("e{2}",s))  #一次取2个(满足的取)
    >>>['ee', 'ee', 'ee']
    print(re.findall("e{0,3}",s)) #按最大范围值取
    >>>['', '', '', 'e', '', 'e', '', '', 'ee', '', 'eee', 'ee', '']
    ```

  + `|`   或模式

    ```
    s = "123aa4e678eeeev"
    print(re.findall("aa|e|v",s))  #找aa或e或v
    >>>['aa', 'e', 'e', 'e', 'e', 'e', 'v']
    ```

  + ( )  边界模式
  
     分组() 中加入?: 表示将整体匹配出来而不只是()里面的内容。
  
    ```
    s = "1lealea23lsssea"
    print(re.findall("(e)",s))  #找e
    >>>['e', 'e', 'e']
    print(re.findall("l(e)a",s))  #找la之间的e
    >>>['e', 'e']
    print(re.findall("l(e)a|s(e)a|l(s)s",s))  #找中间值
    >>>['e', 'e']
    ```
  
  + 小练习
  
    ```
    本身格式
    s = "1-2*(60+(-40.35/5)-(-4*3))"
    print(re.findall("\d+",s)) #获取纯连续数字
    >>>['1', '2', '60', '40', '35', '5', '4', '3']
    print(re.findall("-?\d+\.\d+|-?\d+",s)) #获取原有格式数字
    >>>['1', '-2', '60', '-40.35', '5', '-4', '3']
    ```
  
    ```
    位置格式
    s = 'alex_sb ale123_sb wu12sir_sb wusir_sb ritian_sb'
    print(re.findall(" ?(.+?)_sb",s))#取人名
    >>>['alex', 'ale123', 'wu12sir', 'wusir', 'ritian']
    ```
  
    ```
    s = "http://blog.csdn.net/make164492212@163.com/article/details/51656638" #匹配所有邮箱
    print(re.findall("/(ma.+com)/",s)) #位置
    print(re.findall("\w+@\d+\.com",s)) #格式
    >>>['make164492212@163.com']
    ```
  
    ```
    s = """
    时间就是1995-04-27,2005-04-27
    1999-04-27 老男孩教育创始人
    老男孩老师 alex 1980-04-27:1980-04-27
    2018-12-08
    """
    print(re.findall("\d{4}-\d{2}-\d{2}",s))
    print(re.findall("\d+-\d+-\d+",s))
    >>>['1995-04-27', '2005-04-27', '1999-04-27', '1980-04-27', '1980-04-27', '2018-12-08']
    ```
  
    ```
    s = "222222,33333,4444,5555555,9999,999999"
    print(re.findall("\d{5,11}",s))
    >>>['222222', '33333', '5555555', '999999']
    ```
  
+ search 从字符串任意位置进行匹配，查找到一个就停止（search中()两边的内容也会被提取）

  ```
  s1 = "alexmeet"
  print(re.findall("e",s1))
  >>>['e', 'e', 'e']
  print(re.search("e",s1).group())
  >>>e
  ```

+ match  从字符串开始位置进行匹配，找不到返回None

  ```
  s1 = "alexmeet"
  print(re.match("e",s1))
  >>>None
  print(re.match("a",s1).group())
  >>>a
  ```

+ split 分割，按定义的一批分隔符进行分割

  ```
  print(re.split('[ ：:,;；，]','alex wusir,日天，太白;女神;肖锋：吴超'))
  >>>['alex', 'wusir', '日天', '太白', '女神', '肖锋', '吴超']
  ```

+ sub 替换

  ```
  print(re.sub('barry', 'meet', 'barry是最好的讲师，barry就是一个普通老师，请不要将barry当男神对待。'))
  >>>meet是最好的讲师，meet就是一个普通老师，请不要将meet当男神对待。
  ```

+ compile 定义匹配规则

  ```
  boj = re.compile("\d{2}")
  print(boj.findall("dddd222ddfff"))
  >>>['22']
  ```

+ finditer 在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回

  ```
  a = re.finditer("e","meet,alex")
  print(next(a).group()) #e
  print(next(a).group()) #e
  print(next(a).group()) #e
  print(next(a).group()) #报错
  ```

+ 给匹配内容写标签

  ```
  ret = re.search("<\w+>\w+</\w+>","<h1>hello</h1>").group()
  print(ret)
  >>><h1>hello</h1>
  ret = re.search("<(?P<tag_name>\w+)>\w+</\w+>","<h1>hello</h1>")
  print(ret.group("tag_name"))
  >>>h1
  print(ret.group())
  >>><h1>hello</h1>
  ```

  

## 日志 logging模块

+ 日志的作用

  + 记录程序运行状态：时间，哪个文件，报错位置（行数），错误信息
  + 用户的喜好：分析用户的一些喜好，操作
  + 银行：记录账户流水

+ 日志的级别

  + debug 调试 ---10-- print
  + info 信息 -------20
  + worning 警告--30
  + error 错误 ------40
  + critical 危险 ----50

+ 基础版日志的使用（官方）

  + 注意点

    + 默认从等级30开始记录
    +  编码不能修改（GBK）
    + 屏幕和文件不能同时有（文件流和屏幕流）

  + 使用方法

    ```
    import logging
    logging.basicConfig(
        level=10,
        format="%(asctime)s %(name)s %(filename)s %(lineno)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="test.log", #使用时写入文件不出现屏幕流
        filemode="a"#
        )
    logging.debug("这是调试")
    logging.info("这是信息")
    logging.warning("这是警告")
    logging.error("这是错误")
    logging.critical("这是危险")
    
    >>>2019-09-28 19:24:37 root 05 logging.py 29 这是调试
    >>>2019-09-28 19:24:37 root 05 logging.py 30 这是信息
    >>>2019-09-28 19:24:37 root 05 logging.py 31 这是警告
    >>>2019-09-28 19:24:37 root 05 logging.py 32 这是错误
    >>>2019-09-28 19:24:37 root 05 logging.py 33 这是危险
    
    num = input("请输入数字：")
    try:
        num = int(num)
        print(num)
    except Exception:
        logging.warning("字符串不能转换为数字")
    ```

+ 进阶版日志（二次开发组装实现）

  + 同时支持屏幕流和文件流
  + 使用时可封装为函数

  ```
  import logging
  
  logger = logging.getLogger() #创建一个空架子，与logging独立
  fh = logging.FileHandler("test1.log","a",encoding="utf-8")  #创建一个文件句柄用来记录日志（文件流）
  ch = logging.StreamHandler()  #创建一个屏幕流（打印记录的内容）
  
  formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)s %(message)s") #定义一个记录文件的格式
  
  fh.setFormatter(formater)  #给文件句柄设置记录内容的格式
  ch.setFormatter(formater) #给中控台设置打印内容的格式
  
  logger.addHandler(fh)  #将文件句柄添加到logger对象中
  logger.addHandler(ch)  #将中控台添加到logger对象中
  
  logger.level = 10  #设置警告级别
  
  logger.debug("调试")
  logger.info("信息")
  logger.warning("警告")
  logger.error("错误")
  logger.critical("危险")
  >>>2019-09-28 19:32:41,307 root DEBUG 05 logging.py 60 调试
  >>>2019-09-28 19:32:41,307 root INFO 05 logging.py 61 信息
  >>>2019-09-28 19:32:41,307 root WARNING 05 logging.py 62 警告
  >>>2019-09-28 19:32:41,307 root ERROR 05 logging.py 63 错误
  >>>2019-09-28 19:32:41,308 root CRITICAL 05 logging.py 64 危险
  ```

+ **basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有：**

  - filename：用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中。
  - filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
  - format：指定handler使用的日志显示格式。
  - datefmt：指定日期时间格式。
  - level：设置记录日志的级别
  - stream：用指定的stream创建StreamHandler。可以指定输出到
  - sys.stderr,sys.stdout或者文件(f=open(‘test.log’,’w’))，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

+ **format参数中可能用到的格式化串**：

  - %(name)s Logger的名字
  - %(levelno)s 数字形式的日志级别
  - %(levelname)s 文本形式的日志级别
  - %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
  - %(filename)s 调用日志输出函数的模块的文件名
  - %(module)s 调用日志输出函数的模块名
  - %(funcName)s 调用日志输出函数的函数名
  - %(lineno)d 调用日志输出函数的语句所在的代码行
  - %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
  - %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
  - %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
  - %(thread)d 线程ID。可能没有
  - %(threadName)s 线程名。可能没有
  - %(process)d 进程ID。可能没有
  - %(message)s用户输出的消息