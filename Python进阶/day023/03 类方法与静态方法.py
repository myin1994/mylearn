# 类方法

# 指一个类中通过 @ classmethod修饰的方法
# • 第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）
# • 调用：实例对象和类对象都可以调用
# • 类方法是将类本身作为对象进行操作的方法

# class Person:
#     @classmethod
#     def abc(cls):  #类方法，为当前类服务
#         print("类方法")
#
#     def adc(self):
#         print("实例方法")
#
# Person.abc()
# Person().abc()
# Person().adc()

"""
练习
使用场景分析： 
• 假设我有一个学生类和一个班级类，想要实现的功能为： 
• 执行班级人数增加的操作、获得班级的总人数 
• 学生类继承自班级类，每实例化一个学生，班级人数都能增加 
• 最后，我想定义一些学生，获得班级中的总人数
• 因为我实例化的是学生，但是如果我从学生这一个实例中获得班级总人数，在逻辑 上显然是不合理的 
• 同时，想要获得班级总人数，如果生成一个班级的实例也是没有必要的
"""
# class Class:
#     __student_num = 0
#     def __new__(cls, *args, **kwargs):
#         if cls != Class:
#             Class.add_student()
#         return super().__new__(cls)
#
#     def get_num(self):
#         print(self.__student_num)
#     @classmethod
#     def add_student(cls):
#         cls.__student_num += 1
#
# class Student(Class):
#     def __init__(self, name):
#         self.name = name
#
# class1 = Class()
# class1.add_student()
# class1.add_student()
# class1.get_num()
#
#
# student1 = Student("张三")
# student2 = Student("李四")
# student3 = Student("王五")
# Class().get_num()

# class Class:
#     __student_num = 0
#     def __new__(cls, *args, **kwargs):
#         if cls != Class:
#             Class.__student_num += 1
#         return super().__new__(cls)
#
#     def get_num(self):
#         print(self.__student_num)
#
# class Student(Class):
#     def __init__(self, name):
#         self.name = name
#
# student1 = Student("张三")
# student2 = Student("李四")
# student3 = Student("王五")
# Class().get_num()

#老师版
# class Cla:
#     num = 0
#     def __new__(cls, *args, **kwargs):
#         Cla.add()
#         return super().__new__(cls)
#     @classmethod
#     def add(cls):
#         cls.num += 1
# class Student(Cla):
#     def __init__(self, name):
#         self.name = name
#
# xiaoming = Student("小明")
# print(Cla.num)

# 静态方法-存放逻辑性函数
# 使用@staticmethod修饰的方法
# • 参数随意，没有“self”和“cls”参数，方法体中不能使用类或实例的 任何属性和方法
# • 实例对象和类对象都可以调用
# • 详解：静态方法是类中的函数，不需要实例。静态方法主要是用来存放 逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静 态方法中，不会涉及到类中的属性和方法的操作。可以理解为，静态方 法是个独立的、单纯的函数，它仅仅托管于某个类的名称空间中，便于 使用和维护

# class Person:
#     def run(self):
#         print("人在跑")
#     @staticmethod
#     def jump():
#         print("独立的跳")
#
# Person.jump()
# Person().jump()
# xiaoming = Person()
# xiaoming.jump()

import time
class TimeTest:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def show_time(self):
        return self.showTime()

    @classmethod
    def show_time2(cls):
        return cls.showTime()

    @staticmethod #声明创建普通函数
    def showTime():
        return time.strftime("%H:%M:%S",time.localtime())


print(TimeTest.showTime())
print(TimeTest.show_time2())
t = TimeTest(1,2,3)
print(t.showTime())
print(t.show_time())

#  上页中使用了静态方法（函数），然而方法体中并没使用（也不能使用） 类或实例的属性（或方法）
# • 若要获得当前时间的字符串时，并不需要实例化对象，此时对于静态方 法而言，所在类更像是一种名称空间
# • 其实，我们也可以在类外面写一个同样的函数来做这些事，但是这样做 就打乱了逻辑关系，也会导致以后代码维护困难
