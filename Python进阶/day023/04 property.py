# property
# 是一种特殊的属性，访问它时会执行一段功能（方法）然 后返回值
# 作用：可以把方法伪装成属性去调用，提供获得返回值 的功能




# 为什么要用property：
# • 将一个类的方法定义成属性以后，对象再去使用的时候obj.name,根本无 法察觉自己的name是执行了一个函数然后计算出来的
# • 这种特性的使用方式**遵循了统一访问的原则**
# class Person:
#     def __init__(self, age):
#         self.__age = age
#
#     @property
#     def get_age(self):
#         return self.__age
#
# xiaoM = Person(18)
# # print(xiaoM.get_age())
# print(xiaoM.get_age)

# 属性一般具有三种访问方式，获取、修改、删除
# • 我们可以根据这几个属性的访问特点，分别将三个方法定义为对同一个属性的 获取、修改、删除
# • 只有在属性定义property后才能定义setter,deleter
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,num):
        if 0 < num <150:
            self.__age = num
    @age.deleter
    def age(self):
        del self.__age

xiaoM = Person(18)
# print(xiaoM.age)
# xiaoM.age = 20
# print(xiaoM.age)
#
# del xiaoM.age
# print(xiaoM.age)

# 第二种写法
# class Person:
#     def __init__(self, age):
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self,num):
#         if 0 < num <150:
#             self.__age = num
#         else:
#             raise Exception("年龄设置错误")
#
#     def del_age(self):
#         del self.__age
#
#     age = property(fget=get_age,fset=set_age,fdel=del_age)
#
# xiaoM = Person(18)
# print(xiaoM.age)
# xiaoM.age = 220
# print(xiaoM.age)
#
# del xiaoM.age
# print(xiaoM.age)