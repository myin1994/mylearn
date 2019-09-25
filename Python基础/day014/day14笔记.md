## 有参装饰器

+ 定义：根据参数执行装饰内容

+ 作用：设置装饰器的开关的函数

+ 推导版1-对单个函数的装饰器设置开关

  ```
  def arg(argv):
      def wrapper(func):
          def inner(*args,**kwargs):
              if argv:  #满足装饰器函数条件执行
                  print("开始装饰")
              ret = func(*args,**kwargs)
              if argv: #满足装饰器函数条件执行
                  print("装饰结束")
              return ret
          return inner
      return wrapper
  
  #@arg(False)  #或用此代替，@arg(False) -> @wrapper -> index = inner(index)
  def index():
      print("is index")
  
  wrapper = arg(True)  #返回值为wrapper
  index = wrapper(index)  #返回值为inner
  index()
  ```

+ 推导版2-对多个函数使用的同一装饰器设置开关

  ```
  def auth(arg):
      def wrapper(func):
          def inner(*args,**kwargs):
              username = input("请输入用户名：")
              pwd = input("请输入密码：")
              if arg == "1":
                  if username == "alex" and pwd == "alex123":
                      func(*args,**kwargs)
              if arg == "2":
                  if username == "alex" and pwd == "alex123":
                      func(*args,**kwargs)
              if arg == "3":
                  if username == "alex" and pwd == "alex123":
                      func(*args,**kwargs)
          return inner
      return  wrapper
  
  def wechat():
      print("微信")
  
  def dy():
      print("抖音")
  
  def email():
      print("邮箱")
  
  msg = """
  1.微信
  2.抖音
  3.邮箱
  选择：
  """
  choice = input(msg)
  wrapper = auth(choice)
  if choice == "1":
      wechat = wrapper(wechat)
      wechat()
  if choice == "2":
      dy = wrapper(dy)
      dy()
  if choice == "3":
      email = wrapper(email)
      email()
  ```

+ 实际使用-语法糖

  ```
  msg = """
  微信
  抖音
  邮箱
  选择：
  """
  choice = input(msg)
  
  def auth(arg):
      def wrapper(func):
          def inner(*args,**kwargs):
              username = input("请输入用户名：")
              pwd = input("请输入密码：")
              if arg == "微信":
                  if username == "alex" and pwd == "alex123":
                      func(*args,**kwargs)
                  else:
                      print("账号或密码错误")
              elif arg == "抖音":
                  if username == "alex" and pwd == "alex123":
                      func(*args,**kwargs)
                  else:
                      print("账号或密码错误")
              elif arg == "邮箱":
                  if username == "alex" and pwd == "alex123":
                      func(*args,**kwargs)
                  else:
                      print("账号或密码错误")
          return inner
      return wrapper
  
  @auth(choice)   #@auth(choice) -> @wrapper ->wechat = inner(wechat)
  def wechat():
      print("微信")
  wechat()
  
  @auth(choice)
  def dy():
      print("抖音")
  dy()
  
  @auth(choice)
  def email():
      print("邮箱")
  
  email()
  ```

+ 应用场景

  flask框架的路由就是有参装饰器

## 多个装饰器装饰一个函数

+ 执行顺序

  ```
  多个装饰器装饰一个函数时，先执行离被装饰函数最近的装饰器
  ```

+ 示例

  ```
  def f1(func): #func = index
      def f2(*args,**kwargs):
          print("f1装饰开始")
          func(*args,**kwargs)
          print("f1装饰结束")
      return f2
  
  def foo1(func):
      def foo2(*args,**kwargs):
          print("foo1装饰开始")
          func(*args,**kwargs)
          print("foo1装饰结束")
      return foo2
  
  @foo1  # index = foo1(index)  index = foo1(f2) =foo2 调用后回推
  @f1  #index = f1(index)   index = f2
  def index():
      print("is index")
  index()
  ```

+ 输出顺序-U型法则

  由上至下-按顺序输出每个装饰器在被装饰函数之前的内容

  中间-函数内容

  由下往上-按顺序输出每个装饰器在被装饰函数之后的内容

## 递归

+ 定义

  + 不断调用自己本身
  + 有明确结束的条件

+ 理解

  递归需要有边界条件、递归前进段和递归返回段。当边界条件不满足时，递归前进；当边界条件满足时，递归返回。

+ 最大深度

  ```
  官方-1000
  实际测试-998~993
  ```

+ 调整递归最大深度

  ```
  import sys
  sys.setrecursionlimit(100000)  #调整递归最大深度
  def func():
      print(1)
      func()
  func()
  ```

+ 递归三大要素

  + 明确函数功能
  + 寻找递归结束条件-递归出口
  + 找出函数的等价关系式

+ 举例

  + 例1

    ```
    #函数功能-计算阶乘
    def jc(n):
        if n == 1 :#递归结束条件
            return 1
        else:
            return n * jc(n-1)  #等价关系式为 jc(n) = jc(n-1) * n
    print(jc(5))
    ```

  + 例2

    ```
    #函数功能-计算斐波那契数列第n个值（从1开始数）
    def fib(n):
        if n <= 2: #递归结束条件 n=1，n=2结果都为1
            return 1
        else:
            return fib(n-1) + fib(n-2) #等价关系式 fib(n) = fib(n-1) + fib(n-2)
    
    print(fib(4))
    print(list(map(fib,range(1,6))))
    ```

  + 例3

    ```
    # 函数功能-递归计算1+2+3……+100+n
    def func(n):
        if n == 1:#递归结束条件 n = 1，结果为1
            return 1
        else:
            return func(n-1) + n #等价关系式 f(n) = f(n-1) + n
    print(func(100))
    ```

  + 例4

    ```
    #上楼梯问题，一次可以上1或2阶，求上n阶有几种可能
    def fun(n):
        if n == 0: #递归出口
            return 0
        elif n == 1: #递归出口
            return 1
        elif n == 2: #递归出口
            return 2
        else:
            return fun(n-1) + fun(n-2)#等价关系式 fun(n) = fun(n-1) + fun(n-2)
    print(fun(5))
    ```

+ 递归缺点：递归的效率比较低，其中效率最高的是尾递归