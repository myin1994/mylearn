## 自定义模块

+ 模块的分类

  + 内置模块--标准库  200+
  + 第三方模块
  + 自定义模块

+ 模块的作用

  + 开发效率高（使用内置函数和模块）
  + 减少重复代码，分文件管理，有助于修改和维护

+ 自定义模块的使用

  + import 导入（相当于将模块的整体内容全部放到当前文件中）

    ```
    import lib  #飘红不代表报错，单独使用  使用.操作
    print(globals())  #当前全局作用域中已包含lib模块
    
    lib.login()
    lib.register()
    a = 10
    print(lib.a) #通过模块调用打印模块中的a==5
    print(a)  #打印当前全局空间中的a==10
    ```

  + import  导入时发生的事情

    + 将模块存储到当前名称空间中
    + 开辟空间并以模块的名字命名
    + 通过模块名来使用模块中的功能

  + from 模块名 import 功能 as 别名  导入  （推荐使用）

    + 同一模块功能可在同一行写

    + ```
    from lib import * 将lib下所有的功能全部导入
       __all__=['name','read1'] #这样在另外一个文件中用from spam import *就只能导入列表中规定的两个名字
      ```
    
    + 也是将模块中内容全部导入，但只可使用导入的具体功能
    
      ```
      a = 10
    from lib import login,register,a   #从lib模块下将login函数导入
      login()
    register()
      print(a)  #这里模块中导入的a覆盖了原先的变量
      ```
    
    + 通过as重命名功能则不会覆盖
    
      ```
      a = 10
      from lib import a as b  #给模块中的变量临时取别名
      print(a)  #原先全局作用域的a
      print(b)  #模块中的a
      ```

+ 注意点

  + 同一模块，写多次只执行一次

+ 模块导入顺序：内存  --> 内置 --> sys.path

  + 查看内置模块及模块获取路径

    ```
    import sys
    print(sys.modules)  #查看内置模块----字典
    print(sys.path)  #获取模块查找路径----列表
    for i in sys.path:
        print(i)     #路径----字符串
    ```

  + 通过添加sys.path路径从而可以导入其他路径下的模块

    ```
    import sys
    sys.path.append(r"C:\Users\24479\Desktop\作业上传\Python基础\day014")
    print(sys.path)
    from lib import a
    print(a)
    ```

+ 模块的两种用法

  + 普通模块
  + 被当做脚本执行（终端下运行）

+ 在模块中通过if ____name___ == "____name__":设置调用模块时不执行的内容

  + ```
    在当前文件中执行__main__获取的值是"__name__"
    ```

  + ```
    当前文件被当做模块导入时，__name__获取的是当前文件名
    ```

+ 要避免的问题：循环导入

## time 模块

+ 获取当前时间戳（格林尼治时间-浮点型）

  ```
  print(time.time())  #1569489983.4301805
  ```

+ 休眠（秒）

  ```
  time.sleep(2)  #返回None
  ```

+ python中时间日期格式化符号： 

  ```
  常用：
  %Y 四位数的年份表示（000-9999） ***
  %m 月份（01-12）   ****
  %d 月内中的一天（0-31）  ***
  %H 24小时制小时数（0-23） *** 
  %M 分钟数（00=59）  ****
  %S 秒（00-59）   ****
  ```

  ```
  所有：
  %y 两位数的年份表示（00-99） 
  %Y 四位数的年份表示（000-9999） ***
  %m 月份（01-12）   ****
  %d 月内中的一天（0-31）  ***
  %H 24小时制小时数（0-23） ***
  %I 12小时制小时数（01-12） 
  %M 分钟数（00=59）  ****
  %S 秒（00-59）   ****
  %a 本地简化星期名称 
  %A 本地完整星期名称 
  %b 本地简化的月份名称 
  %B 本地完整的月份名称 
  %c 本地相应的日期表示和时间表示 
  %j 年内的一天（001-366） 
  %p 本地A.M.或P.M.的等价符 
  %U 一年中的星期数（00-53）星期天为星期的开始 
  %w 星期（0-6），星期天为星期的开始 
  %W 一年中的星期数（00-53）星期一为星期的开始 
  %x 本地相应的日期表示 
  %X 本地相应的时间表示 
  %Z 当前时区的名称 
  %% %号本身
  ```

+ 时间分类

  + 时间戳  --用于计算
  + 结构化时间 ---给程序员查看使用(命名元组)
  + 字符串时间 --- 给用户看查看

+ 时间格式转换

  ![img](http://crm.pythonav.com/media/uploads/2019/04/17/IMAGE.PNG)

  + 时间戳转换结构化时间

    ```
    print(time.localtime(time.time()))
    
    print(time.localtime())  #默认转换当前时间戳为结构化时间
    ```

  + 结构化时间转换为时间戳

    ```
    print(time.mktime(time.localtime())) 
    ```

  + 结构化时间转换成字符串时间

    ```
    t = time.localtime()
    print(time.strftime("%Y-%m-%d  %H:%M:%S",t)) #2019-09-26  17:42:24
    ```

  + 字符串时间转换为结构化时间

    ```
    str_time = "2019-09-26  12:23:36"
    print(time.strptime(str_time,"%Y-%m-%d  %H:%M:%S"))
    ```

+ 其他使用

  + 获取当前年份

    ```
    print(time.localtime().tm_year) #2019
    ```

## datetime模块

+ **from datetime import datetime**

+ 获取到当前时间----对象

  ```
  print(datetime.now())   #2019-09-26 17:40:32.701035
  ```

+ 时间转换

  + 时间戳转对象

    ```
    print(datetime.fromtimestamp(time.time())) #2019-09-26 17:44:41.319778
    ```

  + 对象转换成时间戳

    ```
    print(datetime.timestamp(datetime.now())) #1569491152.17481
    ```

  + 对象转换成字符串

    ```
    print(datetime.strftime(datetime.now(),"%Y-%m-%d  %H:%M:%S"))
    >>>2019-09-26  17:46:12
    print(str(datetime.now()))
    >>>2019-09-26 17:47:15.366736
    ```

  + 字符串转换为对象

    ```
    print(datetime.strptime("2019/10/14","%Y/%m/%d"))
    >>>2019-10-14 00:00:00
    print(datetime.strptime("2019/10/14 13:25:26","%Y/%m/%d %H:%M:%S"))
    >>>2019-10-14 13:25:26
    ```

+ 计算时间

  + 计算时间间隔--天，时，分，秒

    ```
    print(datetime.now() - datetime(2019,9,1,12,13))
    >>>25 days, 5:37:34.237109
    ```

  + 加减时间间隔--天

    ```
    from datetime import datetime,timedelta
    print(datetime.now()-timedelta(days=365)) #加减时间间隔
    >>>2018-09-26 17:52:13.034312
    print(datetime.now()+timedelta(days=365))
    >>>2020-09-25 17:52:13.034312
    ```

## os 模块

**与操作系统做交互**

+ 文件

  + 重命名

    ```
    os.rename("旧名字","新名字") 
    ```

  + 删除文件（慎用）

    ```
    os.remove("要删除的文件名")
    ```

+ 文件夹

  + 递归创建文件夹

    ```
    os.makedirs("a/b/c/d/e")
    ```

  + 递归删除文件夹

    ```
    os.removedirs("a/b/c/d/e")
    ```

  + 单独创建文件夹

    ```
    os.mkdir("a")
    ```

  + 单独删除文件夹（必须是空文件夹才能删除）

    ```
    os.rmdir("a")
    ```

  + 查看当前路径下所有的文件

    ```
    print(os.listdir(r"C:\Users\24479\Desktop\作业上传"))
    ```

+ 路径

  + 获取当前工作路径

    ```
    print(os.getcwd())
    ```

  + 改变当前脚本工作目录，相当于终端里的cd

    ```
    os.chdir(r"C:\Users\24479\Desktop\作业上传\Python基础\day014")
    print(os.getcwd()) #当前工作目录已改变
    ```

  + 获取到当前文件的绝对路径

    ```
    print(os.path.abspath("lib")) #获取的是当前工作路径的文件绝对路径
    ```

  + 分割路径为父级目录和文件名组成的元组

    ```
    print(os.path.split(r"C:\Users\24479\Desktop\作业上传\一些git命令.md"))  #路径分割从右往左只切一刀，以元组的形式保存
    >>>('C:\\Users\\24479\\Desktop\\作业上传', '一些git命令.md')
    ```

  + 获取父级目录与获取文件名

    ```
    print(os.path.dirname(r"C:\Users\24479\Desktop\作业上传"))
    >>>C:\Users\24479\Desktop
    ```

    ```
    print(os.path.basename(r"C:\Users\24479\Desktop\作业上传"))
    >>>作业上传
    ```

  + is系列

    + 判断路径是否存在

      ```
      print(os.path.exists(r"C:\Users\24479\Desktop\作业上传"))  #True
      print(os.path.exists(r"C:\Users\24479\Desktop\作业上传1")) #False
      ```

    + 判断是否绝对路径

      ```
      print(os.path.isabs(r"C:\Users\24479\Desktop\作业上传"))  #True
      print(os.path.isabs("lib1")) #False
      ```

    + 判断是否是一个文件

      ```
      print(os.path.isfile(r"C:\Users\24479\Desktop\作业上传\一些git命令.md")) 
      >>>True
      print(os.path.isfile(r"C:\Users\24479\Desktop\作业上传\lib1.py"))
      >>>False
      ```

    + 判断目录是否存在

      ```
      print(os.path.isdir(r"C:\Users\24479\Desktop\作业上传")) 
      >>>True
      print(os.path.isdir(r"C:\Users\24479\Desktop\作业上传\一些git命令.md")) #是文件夹而非文件
      >>>False
      ```

  + 重要

    + 组合路径

      将多个路径组合后返回，第一个绝对路径之前的参数将被忽略

      ```
      print(os.path.join("l1","l2","C:\\Users","24479","Desktop","作业上传","一些git命令.md"))
      >>>C:\Users\24479\Desktop\作业上传\一些git命令.md
      ```

    + 返回path的大小（不准）

      ```
      print(os.path.getsize(r"C:\Users\24479\Desktop\作业上传\一些git命令.md"))
      >>>892
      ```

+ 其他（了解）

  + 运行shell命令，直接显示

    ```
    os.system("dir")
    ```

  + 运行shell命令，获取执行结果

    ```
    print(os.popen("dir").read())
    ```

  + 获取系统环境变量

    ```
    print(os.environ)
    ```

## sys 模块

**与python解释器做交互**

+ 通过添加sys.path路径从而可以导入其他路径下的模块

  ```
  import sys
  sys.path.append(r"C:\Users\24479\Desktop\作业上传\Python基础\day014")
  print(sys.path)
  from lib import a
  print(a)
  ```

+ 查看操作系统平台 win-win32  mac-darwin

  ```
   print(sys.platform)
  ```

+ 命令行参数List，第一个元素是程序本身路径

  ```
  print(sys.argv)
  >>>['C:/Users/24479/Desktop/作业上传/Python基础/day015/07 os模块.py']
  sys.argv.append(input("请输入:"))#输入1
  print(sys.argv)
  >>>['C:/Users/24479/Desktop/作业上传/Python基础/day015/07 os模块.py', '1']
  ```

+ 获取python版本

  ```
  print(sys.version)
  ```

+ 退出程序

  正常退出时exit(0),错误退出sys.exit(1)

  ```
  sys.exit()
  ```

+ 获取所有模块

  ```
  print(sys.modules)
  ```

## random 模块

**随机数**

+ 随机获取0~1之间的小数

  ```
  print(random.random())
  ```

+ 随机获取某个范围内的整数，包括边界

  ```
  print(random.randint(1,5))
  ```

+ 随机按范围与步长获取整数

  ```
  print(random.randrange(0,10,2)) #随机偶数
  print(random.randrange(1,11,2)) #随机奇数
  ```

+ 从可迭代对象随机获取一个元素

  ```
  print(random.choice([1,2,"ww",22,33]))
  print(random.choice("12345"))
  ```

  从可迭代对象随机获取多个元素（可重复）

  ```
  print(random.choices([1,2,"ww",22,33],k=2))
  ```

+ 从可迭代对象随机获取多个元素（不会重复）

  ```
  print(random.sample([1,2,3,4,5,6,7],k=2))
  ```

+ 将有序数据类型顺序打乱

  ```
  lst = [1,2,3,4,5,6,7,8,3]
  random.shuffle(lst) #原地打乱顺序
  print(lst)
  ```

+ 实现任意位数的验证码生成（字母，数字）

  + ASCII中大写字母：65-90，通过chr()获取对应的内容
  + ASCII中小写字母：97-122

  ```
  方法1：
  import random
  print("".join(random.choices([chr(i) for i in range(122) if chr(i).isalnum()],k=5)))
  ```

  ```
  方法2：
  import random
  s = ""
  for i in range(5):
      s += str(random.choice([chr(random.randint(65,90)),chr(random.randint(97,122)),random.randint(0,9)]))
  print(s)
  ```

  ```
  方法3：
  lst = list()
  lst.extend(list(range(65, 91)))
  lst.extend(list(range(48, 58)))
  lst.extend(list(range(97, 123)))
  s = ""
  for i in range(5):
      s = s + str(chr(random.choice(lst)))
  print(s)
  ```

  