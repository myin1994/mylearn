## 面向对象

+ 面向过程（数学）：
  + 事件为中心：分析出解决问题所需的步骤，然后用函数将步骤实现并按顺序调用
  + 维护，复用，扩展性较差
+ 面向对象（上帝）
  + 与面向过程相辅相成，在软件开发过程中，宏观上，用面向对象来把握事物间复杂的关系
  + 性能低于面向过程
+ 面向对象与面向过程，不属于任何一种编程语言，是两种不同的编程思想



## 类和对象

+ 类是对象的抽象

  + 包含属性和方法

+ 对象是类的具象

  + 可通过类创建对象

+ 8种数据类型是数据的封装，函数是算法的封装

+ 类，数据和算法都能封装，更高一级

+ 类的命名规则：首字母大写

+ 定义类

  ```
  #class GirlFriend(object):
  class GirlFriend:
      sex = "女"
      age = 18
      height = 180
      weigh = 180
      money = 100000000
      l1 = [1,2,3,4,5,6]
  
      def chui_tui(self,num):  #在类里叫方法，self接收的是调用者
          print(f"捶腿{num}次")
  
      def get_money(self):
          print("给100元")
   
  xiaoli = GirlFriend()
  print(xiaoli.sex)
  xiaoli.chui_tui(20)
  # 引用计数为0时会被垃圾回收机制回收
  
  xiaoli1 = GirlFriend()
  print(xiaoli1.sex)
  xiaoli1.chui_tui(20)
  
  print(GirlFriend.__dict__) #查看类中内容
  
  xiaoli1.face_value = -5
  print(xiaoli1.face_value)
  ```

  ```
  class GirlFriend:
      num_eyes = 2  #类属性
  
      def __init__(self,color,height):  #实例属性
          self.eye_color = color
          self.height = height  #一般重名使用
  
      def chui_tui(self, num):  # 在类里叫方法，self接收的是调用者
          print(f"捶腿{num}次")
          self.abc = 50
  
      def get_money(self):
          print("给100元")
  
  xiaoli = GirlFriend("白色",180)
  print(xiaoli.eye_color)
  print(xiaoli.height)
  
  xiaoli.weight = 120
  print(xiaoli.weight)
  
  xiaoli.num_eyes = 3  #添加的是实例属性
  print(xiaoli.num_eyes) #此时会覆盖（不是真的覆盖）类属性
  # 访问属性的优先级：实例属性-类属性
  
  print(GirlFriend.num_eyes)  #通过类名来访问类属性
  # 类属性，实例（对象）属性
  ```

+ 类属性

  用来存放当前类所有对象所共有的特征，一般通过类名访问和修改（所有类的对象都会改变），用对象名也能访问，但不能修改

+ 实例属性（接收的参数）

  存放每个对象各自的特征，只能通过对象去访问，类名无法访问,可在对象内及其它对象内进行修改