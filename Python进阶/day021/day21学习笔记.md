## 类之间的关系-继承关系

+ 概念

  + 实现继承之后，子类将继承父类的属性和方法（包含父类），可以直接使用

  + 支持扩展

  + 父类（基类）----->子类（派生类）

  + Python中，同时支持单继承与多继承

    + 单继承

      子类可以继承父类的属性和方法，修改父类，所有子类都会 受影响

      ```
      class Father(object):#不继承时，默认继承object类
          def __init__(self, name, sex, money):
              self.name = name
              self.sex = sex
              self.money = money
      
          def live(self):
              print("花钱")
      
      class Son(Father):
          pass
      
      xiaoming = Son("小明","男",100) #实例属性：子类中找不到就去父类中找（默认调用了父类的init方法）
      xiaoming.live() #方法：子类中找不到就去父类中找
      ```

    + 多继承

      + 有多个直接父类
      + 排在前面的父类中的方法会“遮蔽”排在后面的父类中的同名方法(根据查找顺序找到就OK了)

      ```
      class Person:
          pass
      
      class Driver:
          pass
      
      class Teacher(Person,Driver):#优先继承前者的属性和方法
          def teach(self):
              print("教书育人")
      ```

+  isinstance()及issubclass() 函数

  + Python与其他语言不同，当我们定义一个class的时候，我们实际上就定义了一种数据类型。即每个类就相当于一个数据类型-list-dict-str。

  + isinstance(对象,类型)    判断对象是否属于该数据类型

    ```
    class Teacher:
        def teach(self):
            print("教书育人")
    
    xiaoming = Teacher()
    a = isinstance(10.5,int) #判断是否是该数据类型
    print(a) #False
    b = isinstance(xiaoming,Teacher)  #判断是否是类的对象
    print(b) #True
    ```

  + issubclass(子类,父类)  检查类继承,判断是否子类

    ```
    class Driver:
        pass
    
    class Teacher(Driver):
        def teach(self):
            print("教书育人")
    
    c = issubclass(Teacher,Driver) #判断是否是类的子类
    print(c) #True
    ```

+ 方法重写（重构）

  + 子类可以重写父类中的方法 （根据方法的查找顺序）

    ```
    class Father(object):
        def __init__(self, name, sex, money):
            self.name = name
            self.sex = sex
            self.money = money
    
        def live(self):
            print("打人")
    
    class Son(Father):
        def live(self): #同名方法覆盖父类方法
            print("打妹妹")
    
    xiaoming = Son("小明","男",100)
    xiaoming.live() #打妹妹
    ```

  + super()关键字在当前类中调用父类父类方法（为了同时使用父类和子类属性或方法）

    + 使用方法及原理

      按照mro方法返回的是一个类的方法解析顺序表（顺序结构-从左至右的继承顺序，保证每个类在其中只出现一次） 

      + super(类名, self).func()  

        会在self的MRO列表上搜索类名的下一个类

        ```
        class Men:
            def __init__(self,sex):
                self.sex = sex
        
        class Women:
            def __init__(self, age):
                self.age = age
        
        class NvHanZi(Men, Women):
            def __init__(self, name, sex, age):
                self.name = name
                super(NvHanZi,self).__init__(sex)
                super(Men,self).__init__(age)
                与下面等价
                #Men.__init__(self,name)
                #Women.__init__(self,age)
        
        print(NvHanZi.mro())
        >>>[<class '__main__.NvHanZi'>, <class '__main__.Men'>, <class '__main__.Women'>, <class 'object'>]
        xiaoli = NvHanZi(1,2,3)
        print(xiaoli.name) #1
        print(xiaoli.sex) #2
        print(xiaoli.age) #3
        ```

        

      + super().func()--python3中默认当前类名

    + MRO列表获取方法

      + `类名.mro() `
      +  `对象名.__class__.mro()`
      
    + 单继承中，以上两种调用父类的方式无区别，多继承中使用super更好

+ 钻石继承问题(继承的父类来自相同的父类)

  ​	普通方法会调用两次爷爷类的方法

  + ```
    class YeYe:
        def __init__(self):
            print("初始化爷爷")
    class Qinba(YeYe):
        def __init__(self):
            print("进入亲爸类")
            YeYe.__init__(self)
            print("初始化亲爸")
    class GanDie(YeYe):
        def __init__(self):
            print("进入干爹类")
            YeYe.__init__(self)
            print("初始化干爹")
    class ErZi(Qinba,GanDie):
        def __init__(self):
            Qinba.__init__(self)
            GanDie.__init__(self)
            print("初始化儿子")
    bigB = ErZi()
    ```

  + 使用super()可避免该问题

    ```
    class YeYe:
        def __init__(self):
            print("初始化爷爷")
    class Qinba(YeYe):
        def __init__(self): #self 接收的是儿子对象
            super().__init__()
            print("初始化亲爸")
    class GanDie(YeYe):
        def __init__(self):
            super().__init__()
            print("初始化干爹")
    
    class ErZi(Qinba,GanDie):
        def __init__(self):
            super().__init__() #去上一层进行 查找（树中的左右左）
            print("初始化儿子")
    
    print(ErZi.mro()) #查找顺序
    >>>[<class '__main__.ErZi'>, <class '__main__.Qinba'>, <class '__main__.GanDie'>, <class '__main__.YeYe'>, <class 'object'>]
    bigB = ErZi()
    ```

    

+ 性质与作用

  + 增加了类的耦合性（耦合性不宜多，宜精）-慎用（可能会使逻辑复杂化）
  + 减少了重复代码
  +  使得代码更加规范化，合理化

+ 组合与继承的对比

  + 组合：在新类里面创建原有类的对象，重复利用已有类的功能 “has-a”关系
  + 继承：允许设计人员根据其它类的实现来定义一个类的实现 “is-a”关系

+ 注意点

  + 不要轻易地使用继承，除非两个类之间是“is-a”的关系 ----因为过多地使用继承会破坏代码 的可维护性，当父类被修改的时候，会影响到所有继承自它的子类，从而增加 程序的维护难度与成本
  + 组装的时候用组合，扩展的是时候用继承

