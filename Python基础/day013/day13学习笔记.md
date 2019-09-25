## 闭包

+ 作用

  保护数据安全，保护数据的干净性

+ 定义

  + 在嵌套函数内，使用非全局变量（且不使用本层变量）--嵌套的这个函数是闭包的本质
  + 将嵌套函数返回

+ 理解：

  理解成定义在一个函数内部的函数。

  在本质上，闭包是将函数内部和函数外部连接起来的桥梁。

+ 基本结构

  ```
  def func():
      a = 10  #自由变量
      def foo():
          print(a)
      return foo
  f = func()
  f() #等价于func()()-->foo()
  print(f.__closure__) #验证是否是闭包(不是返回None)
  ```

  ```
  def buy_car():
      lst = []  #自由变量
      print(1)
      def func(price):
          lst.append(price)
          arg = sum(lst) /  len(lst)
          print(arg)
      return func
  
  f = buy_car() #只调用一次外层函数，后面相当于在buy_car函数的基础之上调用func
  f #相当于函数调用
  print(f.__closure__)
  print(f.__code__.co_freevars) #查看自由变量
  print(f.__code__.co_varnames) #查看局部变量
  f(1) #相当于buy_car()(1)
  f(2)
  f(3)
  ```

+ 注意点

  + 没有将嵌套的函数返回也是一个闭包，但是这个闭包不能使用

    理解为没有桥梁，嵌套的函数无法调用

    ```
    def func():
        a = 10
        print(1)
        def foo():
            print(a)
        print(foo.__closure__)
    func()
    ```

  + 函数的形参也属于自由变量

    ```
    def wrapper(a,b):
        #a = 2
        #b = 3  #隐性
        def inner():
            print(a)
            print(b)
        return inner
    a = 2
    b = 3
    ret = wrapper(a,b) #传参使用自由变量
    print(ret.__closure__)
    ret()
    ```

+ 闭包的应用场景

  + 装饰器
  + 防止数据被改动

## 装饰器

+ 开放封闭原则

  + 对扩展开放 ---支持增加新功能
  + 对修改源代码是封闭的,对调用方式是封闭的

+ 作用：在原有的基础上添加额外的功能

+ 初版装饰器

  ```
  import time #python中的标准库的模块
  def run_time(f): #接收目标函数
      def inner():
          starttime =time.time()  #被装饰函数之前
          f()
          print(time.time() - starttime) #被装饰函数之后
      return inner  #不能加括号
  
  def index():
      time.sleep(2)  #休眠--2秒
      print("is index xxxx")
  
  index = run_time(index) #理解为调用闭包,这个时候才定义inner()
  index() #实际为inner()
  ```

+ 使用语法糖@

  ```
  # 语法糖必须要放在被装饰函数的上方
  import time
  def run_time(f):
      def inner():
          starttime =time.time()
          f()
          print(time.time() - starttime)
      return inner  #不能加括号
  
  @run_time   #语法糖本质---> index = run_time(index)
  def index():
      time.sleep(2)  #休眠--2秒
      print("is index xxxx")
  @run_time   #语法糖  func = run_time(func)
  def func():
      time.sleep(2)  #休眠--2秒
      print("is index yyyy")
  
  index() #实际为inner()
  func()
  ```

+ 标准版装饰器

  ```
  def wrapper(func): #接收被装饰函数的函数名
      def inner(*args,**kwargs): #接收被装饰函数需要的参数
          """执行被装饰函数之前的操作"""
          func(*args,**kwargs)
          #ret = func(*args,**kwargs)
          """执行被装饰函数之后的操作"""
          #return ret #可接收被装饰函数的返回值
      return inner
  
  @wrapper
  def index():
      print("is index")
  
  index()
  ```

+ 不使用参数时的装饰器

  ```
  def func(args):  #不用参数时
      print("新加功能")
      return args
  
  @func  #index = func(index)
  def index():
      print(2)
  
  index()  #对应被装饰函数不能接收参数
  ```

+ 还原被装饰函数函数名

  ```
  import time
  import functools#
  def warpper(f):
      @functools.wraps(f)  #使用该命可让func函数返回其本身的函数名
      def inner():
          f1 = open("time.txt","a",encoding="utf-8")
          f1.write(f"函数名：{f.__name__} 当前时间节点：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")
          f1.flush()
          f1.close()
          f()
      return inner
  
  @warpper
  def func():
      print(func.__name__)  #不使用方法打印的是装饰器的名字
  
  func()
  ```

  