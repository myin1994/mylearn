## 函数的动态参数

+ 作用

  + 接收不固定长度的参数
  + 位置参数过多时使用

+ 函数参数的优先级：位置参数 > 动态位置参数 > 默认参数 > 动态关键字参数

+ 变量不能重复对同一形参传参

+ 动态参数类型

  + *args  动态位置参数-聚合为元组

    约定变量名，只接受多余的位置参数（任意数据类型）

    ```
    def func(*args):  #放在形参位置上的*是聚合(理解为接收数据时)
        print(*args)  #函数体中的*就是打散（理解为使用数据时） 1 2 3 4 5
        print(args)  #直接使用为元组  (1, 2, 3, 4, 5)
    func(1,2,3,4,5)
    ```

    

  + **kwargs  动态关键字参数-聚合为字典

    约定变量名，只接受多余的关键字参数（a=1，b=2……）

    ```
    def func(a,b,*args,m=9,**kwargs): #位置参数，动态位置参数，默认参数，动态关键字参数
        print(a,b,args,kwargs,m)  #聚合为字典 1 2 (3, 4) {'k': 3, 'hh': 10} 5
    func(1,2,3,4,m=5,k=3,hh=10) #与形参对应
    ```

+ 动态参数的应用（聚合的应用）

  + 万能传参

    ```
    def func(*args,**kwargs):  #万能传参
        print(args,kwargs)
        print(*args) #将元组打散
        print(**kwargs)  #报错
        print(*kwargs)  #获取字典的键
    func(11,22,33,44,55,666,a=1,b=2)
    ```

  + 将数据分离传入（一个一个的）

    + 列表

      ```
      lst = [1,2,3,4,5,6,7]
      def func(*args): #聚合
      	print(args)  #聚合结果 (1, 2, 3, 4, 5, 6, 7)
          print(*args)  #打散    1 2 3 4 5 6 7
      func(*lst)  #打散  func(1,2,3,4,5,6,7)
      ```

    + 字典（用于josn 数据）

      ```
      dic = {"key1":1,"key2":2}
      def func(**kwargs): #聚合
          print(kwargs)  #聚合为字典  {'key1': 1, 'key2': 2}
          print(*kwargs)  #打散为键  key1 key2
      func(**dic)  #打散  func(key=1,key2=2)
      print(*dic)  #打散为键  key1 key2
      ```

  + *聚合与打散的个人理解

    + 函数外聚合为列表（不能单独使用），函数形参上聚合为元组（**聚合关键字实参为字典）
    + 函数内外打散的结果都是单独的数据（其中字典只有键）

## 函数的注释

意义---方便理解函数功能

+ 注释方法

  + ```
    def func(a,b,c):
        """
        函数功能
        :param a: 参数 int
        :param b: int
        :param c: int
        :return:
        """
        return
    ```

  + ```
    def add(a:int,b:int): #提示，没有做到约束
        """
    
        :param a:
        :param b:
        :return:
        """
        return a + b
    ```

+ 查看注释

  ```
  print(add.__doc__)  #查看函数的注释
  ```

  ```
  print(add.__name__)  #查看函数的名字(原始名)
  ```

  函数名可作为作为变量赋值给其他变量（函数的内存地址）

  ```
  a = addprint(a.__name__)  #查看函数的名字(原始)
  print(a.__doc__)
  ```

## 函数的名称空间

+ 空间分类

1. 内置空间 -- 存放python自带的一些函数
2. 全局空间 -- 当前py文件定格编写代码开辟的空间
3. 局部空间 -- 函数体



+ 程序加载顺序（从外向内）

  ```
  内置空间 > 全局空间 > 局部空间
  ```

+ 程序取值顺序（从内向外）

  ```
  局部空间 > 全局空间 > 内置空间
  ```

  ```
  a = 10
  b = 10
  def func():
      a = 6
      print(a) #6--从局部
      print(b) #10--从全局
  func()
  ```

+ 作用域

  + 全局作用域：内置 + 全局

    使用globals()查看全局作用域--查看的是之前定义的内容（函数不被查看）

    ```
    a = 10
    b = 15
    def func():
        b = 5
        print(locals())
        print(globals())
    print(globals())  #不包含d的内容
    d = 10 
    print(globals())  #包含d的内容
    ```

    ```
    a = 10
    b = 15
    def func():
        b = 5
        print(locals()) #第一次调用：{'b': 5} 第二次调用：{'b': 5}
        print(globals()) #第一次调用：不包含d的内仍然  第二次调用包含d的内容
    func() #第一次调用
    d = 10
    func() #第二次调用
    ```

  + 局部作用域：局部

    使用locals()查看当前作用域（在局部-查看局部作用域；在全局-查看全局作用域）--查看的是之前定义的内容（函数不被查看）

    ```
    a = 10
    b = 15
    def func():
        b = 5
        print(locals()) #仅包含b的内容
    func()
    print(locals())  #不包含d的内容
    d = 10
    print(locals())  #包含a，b，func，d的内容
    ```

## 函数名的第一类对象及使用

**在这里将函数名理解为变量名，变量能做到的事情函数名也能做到**

+ 函数名可以当做值，被赋值给另一个变量

  ```
  def func():
      print(1)
  
  print(func)  #函数的内存地址
  a = func  #a和func有相同的作用
  print(a)
  a() #可调用原func函数
  ```

+ 函数名可以当做另一个函数的参数来使用

  ```
  def func():
      print(1)
  
  def fo(a): #a = func
      print(a) #打印func函数的内存地址
      a() #相当于func()
  
  fo(func) #调用函数并传参
  ```

+ 函数名可以当做另一个函数的返回值

  ```
  def func():
      print(1)
  
  def fo(a): #a = func
      return a #return  func函数的内存地址
  
  c = fo(func)
  print(c)  #func函数的内存地址
  ```

+ 函数名可以当做元素存储在容器中

  ```
  def func():
      print(1)
  
  def foo():
      print(2)
  
  def fo():
      print(3)
  
  lst = [func,foo,fo]
  for i in lst:
      i()  #实现迭代调用函数
  ```

  作用-可将函数名存放在字典中，更方便调用(编程思想)

  栗子

  ```
  def login():
      print("登录")
  
  def register():
      print("注册")
  
  def shopping():
      print("逛")
  
  def add_shopping_car():
      print("加")
  
  def buy():
      print("买")
  
  msg = """
  1.注册
  2.登录
  3.逛
  4.加
  5.买
  请输入您要选择的序号："""
  
  fun_dic={"1":register,
           "2":login,
           "3":shopping,
           "4":add_shopping_car,
           "5":buy}
  while True:
      choice = input(msg)
      if choice in fun_dic:
          fun_dic[choice]()
      else:
          print("走你")
  ```

## 函数的嵌套

```
接收参数按顺序（位置），使用参数按名字
传参的时候相当于在当前函数体中进行了赋值操作
```

+ 交叉嵌套

  ```
  def func(foo): #相当于foo = a
      print(2)
      foo()  #调用函数a，接收返回值
      print(3)
  
  def foo():
      print(4)
      a()
      print(5)
  
  def a():
      print(1)
  
  func(a)  #print时才是使用None
  >>>2
  >>>1
  >>>3
  ```

  ```
  def func():
      print(1)
      print("难啊")
      print(2)
  
  def foo(b):
      print(3)
      ss = b()
      print(ss)
      print(4)
  
  def f(a,b):
      a(b)
  
  f(foo,func)
  >>>3      1      难啊     2    None    4
  ```

+ 嵌套

  ```
  def func(a,b):
      def foo(b,a):
          print(b,a)
      foo(a,b)
  func(4,7) #4 7
  ```

  ```
  def func(a,b):
      def foo(b,a):
          print(b,a)
      foo(b,a) #使用参数时交换了位置（按变量名使用）
  func(4,7) #7 4
  ```

  ```
  def func(a,b):
      def foo(b,a):
          print(b,a) #4 7
      return foo(a,b)  #先执行函数调用 返回None
  a = func(4,7)
  print(a) #None
  ```

  ```
  def func(a,b):
      def foo(b,a):
          print(a,b) #7 4  使用时按变量名
      return foo(a,b)  #先执行函数调用
  a = func(4,7)
  print(a) #None
  ```

  ```
  def func():
      print(1) # 1
  
  def foo(a,b):
      def f(a,b):
          print(a,b) #2 1
          func()
      f(b,a)
  foo(1,2)
  >>>>2 1       1
  ```

  ```
  def func(a,b):
      a = a + b
      b = a + 10
      def foo(a,d):
          def f(e,f):
              print(f,e)
              return "难"
          f(d,a)
      foo(b,a)
  print(func(2,3))
  >>>15 5        None
  ```

## 全局变量与局部变量的修改

+ `global`  只修改全局空间中的变量

  + 注意：当使用global时，关键字前面不能对全局变量进行操作（所有数据类型）

  + 功能

    + 当变量在全局存在时，申明要修改的全局变量

      ```
      a = 10
      def func():
      	#a = a +1  #不声明且函数体内无定义不能修改
      	#a = 1     #也是修改，不可存在
      	print(a)    #可以使用
          global a
          a = a + 1  #声明后可进行修改
          print(a)
      func()   #11
      print(a) #11
      ```

    + 当变量在全局不存在时，申明要在全局创建一个变量，并且会在局部开辟这个变量，但需要定义该变量

      ```
      def func():
          global a
          a = 100  #不定义会报错
          a = a + 1
          print(a)
      func()   #101
      print(a) #101
      ```

    + 未申明时，局部空间中对变量的修改不会影响全局空间（但是可变数据类型在全局中会被函数中的常规操作同步修改）

+ `nonlocal`  只修改局部空间中的变量,最外层的一个函数（最大的局部空间）

  只修改距离nonlocal最近的一层（非所在函数内），如果这一次没有就往上一层查找，只能在局部

  注意：在使用nonlocal时，当前函数体局部空间nonlocal之前不可对声明局部变量进行操作

  ```
  a = 15
  def func():
      a = 10
      def foo():
          a = 5
          def f():
              nonlocal a
              a = a +1
              print(a) # 6
          print(a) # 5
          f()
          print(a) # 6
      foo()
      print(a) # 10
  func()
  print(a) #15
  ```

  