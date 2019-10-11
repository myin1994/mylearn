# 多态/多态性
# 多态
# 1.python是一种多态语言，不关心对象的类型（不需要定义好）
# 可以在不同的时间引用不同的对象
# 2.一类事物，可以具有多种形态（类可以有多个子类,子类中有功能不同的同名的方法）
# class Person:
#     def sleep(self):
#         print("人需要休息")
#
# class alex(Person):
#     def sleep(self):
#         print("睡觉")
#
# class BigB(Person):
#     def sleep(self):
#         print("买沙发")

# 多态性(父类可以对子类进行约束)
# 在多态的基础上，定义统一的接口（类外定义单独的函数）
#  不同类的对象作为函数的参数时，得到的结果不同
# class Person:
#     def sleep(self):
#         print("人需要休息")
#
# class alex(Person):
#     def sleep(self):
#         print("睡觉")
#
# class BigB(Person):
#     def sleep(self):
#         print("买沙发")
#
# def abc(tool):
#     tool.sleep()
#
# a = alex()
# b = BigB()
# c = Person()
# abc(a)
# abc(b)
# abc(c)


# class Person:
#     def sleep(self):
#         print("子类未定义此方法")
#
# class alex(Person):
#     def sleep(self):
#         print("睡觉")
#
# class BigB(Person):
#     pass
#
# def abc(tool):
#     tool.sleep()
#
# a = alex()
# b = BigB()
# abc(a)
# abc(b)



# 鸭子类型
# 不关心类型，不需要继承，通过一个接口（外部函数）来调用方法，只关注方法实现，这种情况被称为鸭子类型
# 在鸭子类型中，关注的不是对象的类型本身，而是它是如何使用的
# class Person:
#     def swim(self):
#         print("人会游泳")
#
# class Duck:
#     def swim(self):
#         print("鸭子会游泳")
#
# class Fish:
#     def swim(self):
#         print("鱼会游泳")
#
# def swimming(tool):
#     tool.swim()
#
# xiaoming = Person()
# xiaohuang = Duck()
# xiaoli = Fish()
# swimming(xiaoli)

# 总结：Python本身就是支持多态性的
# • 增加了程序的灵活性（通用性），以不变应万变，不论对象千变万化， 使用者都是同一种形式去调用
# • 增加了程序的可扩展性，通过继承某个类创建了一个新的类，接口使用 者无需更改自己的代码，还是用原方法调用

"""
练习：
• 创建汽车类（Car）含实例属性颜色red,对象方法run，功能是打印XX颜 色小汽车在跑。
• 创建猫类（Cat）含实例属性名字name,对象方法run，功能是打印猫咪XX 在跑。
• 实例化汽车类颜色为红色，实例化猫类，使用公共函数调用对象方法
"""
# class Car:
#     def __init__(self, red):
#         self.red = red
#
#     def run(self):
#         print(f"{self.red}颜色小汽车在跑")
#
#
# class Cat:
#     def __init__(self, name):
#         self.__name = name
#
#     def run(self):
#         print(f"猫咪{self.__name}在跑")
#
# def run(a):
#     a.run()
# car1 = Car("红")
# cat1 = Cat("小咪")
# car1.run()
# run(car1)
# run(cat1)
