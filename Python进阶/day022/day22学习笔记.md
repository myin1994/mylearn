## 封装

将抽象得到的数据和行为相结合，形成一个有机的整体-----抽象得到类的过程

+ 数据的封装：元组，列表，字典-通过引用去使用数据

+ 算法的封装: 函数

+ 封装的目的：简化编程和增强安全性

  + 使用者不必关心如何实现
  + 通过接口调用（点）
  + 可以设置特定的访问权限给对象使用
  + 明确区分内外
    + 类的实现者：内-可以修改内部封装的东西而不影响外部调用者 
    + 类的使用者（外部调用）：外-只需要知道自己可以使用该类对象的哪些功能

+  私有属性，私有方法 

  + 创建：在创建的私有属性及私有方法前使用双下划线`__` 

    + 将不需要对外提供的内容都隐藏起来 
    +  把属性都隐藏，提供公共方法对其访问

    ```
    class Person:
        def __init__(self, name, age):
            self.__name = name  #私有属性,实际上自动变成当前类的类名_Person__name
            self.__age = age
    
        def __play(self): #私有方法
            print(f"{self.__name}喜欢玩儿手机")
        #提供外界访问的接口
        #类内可以访问私有属性和私有方法
        def get_name(self): #访问私有属性的接口
            return self.__name
    
        def set_name(self, name):
            self.__name = name
        def set_age(self,num):
            if 0 < num < 150:#对传入的属性设限
                self.__age = num
            else:
                print("输入不合法！")
        def get_play(self):
            self.__play()
    ```

  + 调用：提供外界访问的接口（类的内部）,类的对象不能直接访问

    ```
    xiaoming = Person("小明",18)
    print(xiaoming.get_name()) #小明
    #xiaoming.play() #报错
    xiaoming.set_name("马云") #调用接口修改私有属性
    print(xiaoming.get_name()) #马云
    ```

  + 破解： 在名称前加上` _类名，即 _类名__名称（例如a._A__N）`

  ```
  xiaoming._Person__name = "张飞" #修改
  print(xiaoming._Person__name) #直接调用  张飞
  print(xiaoming.get_name()) #张飞
  ```

  + 继承：原样继承

    ```
    class Boy(Person):
        pass
    
    xiaoli = Boy("小刚",20)
    print(xiaoli.get_name())
    print(xiaoli._Person__name)
    print(xiaoli.__dict__)
    ```

## 多态与多态性

+ python中多态的体现

  + python是一种多态语言，不关心对象的类型（不需要提前声明对象的数据类型）可以在不同的时间引用不同的对象

  + 一类事物，可以具有多种形态（类可以有多个子类,子类中均重写了父类的某个功能）

  ```
  class Person:
      def sleep(self):
          print("人需要休息")
  
  class alex(Person):
      def sleep(self):
          print("睡觉")
  
  class BigB(Person):
      def sleep(self):
          print("买沙发")
   
   实例化后的对象根据指向可执行功能不同的同名方法（呈现不同的行为特征）
  ```

+ 多态性

  + 在多态基础上，定义统一的接口（类外定义单独的函数） 

  + 不同类的对象作为函数的参数时，得到的结果不同

    ```
    class Person:
        def sleep(self):
            print("人需要休息")
    
    class alex(Person):
        def sleep(self):
            print("睡觉")
    
    class BigB(Person):
        def sleep(self):
            print("买沙发")
    
    def abc(tool):
        tool.sleep()#根据传入的对象调用方法
    
    a = alex()
    b = BigB()
    c = Person()
    abc(a)
    abc(b)
    abc(c)
    ```

  + 父类可以对子类进行约束（如要求必须使用子类的方法）

    ```
    class Person:
        def sleep(self):
            print("子类未定义此方法")
    
    class alex(Person):
        def sleep(self):
            print("睡觉")
    
    class BigB(Person):
        pass
    
    def abc(tool):
        tool.sleep()
    
    a = alex()
    b = BigB()
    abc(a)
    abc(b)
    ```

+ 多态性的优点

  + 增加了程序的灵活性（通用性），以不变应万变，不论对象千变万化， 使用者都是同一种形式去调用
  + 增加了程序的可扩展性，通过继承某个类创建了一个新的类，接口使用者无需更改自己的代码，还是用原方法调用

+ 鸭子类型

  + 不关心类型，不需要继承，只关注方法实现
  + 关注的不是对象的类型本身，而是它是如何使用的（有没有对应的方法）

  ```
  class Person:
      def swim(self):
          print("人会游泳")
  
  class Duck:
      def swim(self):
          print("鸭子会游泳")
  
  class Fish:
      def swim(self):
          print("鱼会游泳")
  
  def swimming(tool):
      tool.swim()
  
  xiaoming = Person()
  xiaohuang = Duck()
  xiaoli = Fish()
  swimming(xiaoli)
  ```

  

## 常见设计模式

### 单例模式

+ 类实例化对象时发生的事

  + 首先=右边，开始实例化后先调用 `__new__(cls)` 基于当前类获取内存地址（为返回值）
  + 然后调用 `__init__` (self)方法，将上一步的内存地址传入进行实例化
  + 最后将内存地址绑定对象----此时对象的实质是内存地址，且初始化了实例属性

+ 单例模式概念：一个类只有一个对象

  ```
  class Singletion(object):
      isin = None
      def __new__(cls, *args, **kwargs): #cls 代表当前类
          if cls.isin == None:
              cls.isin = super().__new__(cls)#获取了基于当前类的内存地址
              print(cls)
          return cls.isin  #第一次时新获取内存地址，第二次直接使用第一次的地址
  xiaoming = Singletion()
  xiaoli = Singletion()
  print(id(xiaoming),id(xiaoli)) #内存地址相同
  ```

  ```
  第二次使用单例模式时直接继承即可，无序重新设置
  class Mother(Singletion):
      def __init__(self, msg = ""):
          self.msg = msg
      def get_food(self, new_food):
          self.msg += new_food
      def food(self):
          print('做菜: ', self.msg)
  mother1 = Mother()
  mother2 = Mother()
  mother1.get_food('西红柿')
  mother2.get_food('鸡蛋')
  print('儿子的妈妈id：', id(mother1))
  mother1.food()
  print('女儿的妈妈id：', id(mother2))
  mother2.food()
  ```

### 工厂模式

+ 通过管理者（类），创建对象 

  + 工厂模式是不直接暴露对象创建细节，而是通过一个共用类创建 对象的设计模式，需要4步-创建基类-创建子类---创建工厂类---使用工厂模式创建基类

  ```
  python中省略了前两步（特性绝对）
  class Girl1:
      def xiyinli(self):
          print("我腿长")
  class Girl2:
      def xiyinli(self):
          print("我美")
  class Girl3:
      def xiyinli(self):
          print("我有钱")
  class Girl4:
      def xiyinli(self):
          print("不存在")
  class Factory:
      def get_girl(self,choice):
          if choice == "腿长":
              return Girl1()
          if choice == "美":
              return Girl2()
          if choice == "有钱":
              return Girl3()
          return Girl4()
  f1 = Factory()
  my_girl = f1.get_girl("脱发")
  my_girl.xiyinli()
  ```

  + 理解为将要创建的类封装在一个管理者类中（工厂类），通过条件判断使用哪个类来创建对象