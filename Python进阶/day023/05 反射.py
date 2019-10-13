# 反射
# • 反射的概念是由Smith在1982年首次提出的，主要是指程序可以 访问、检测和修改它本身状态或行为的一种能力（自省）
# • python面向对象中的反射：通过字符串的形式操作对象相关的属 性。python中的一切事物都是对象（都可以使用反射）
# • 有四个可以实现自省的函数： hasattr,getattr,setattr,delattr

# 应用于对象的反射

# class Foo:
#     f = '类变量'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def say_hi(self):
#         print('hi,%s' % self.name)
#
# obj = Foo('小明', 73)
# 检测是否含有某属性
# print(hasattr(Foo,'name'))
# print(hasattr(obj,'name'))
# print(hasattr(obj,'age1'))
# print(hasattr(obj,'f'))

# print(hasattr(obj,'say_hi'))
# print(obj.__dict__)
# print(Foo.__dict__)

# print(getattr(obj,"name"))
# b = getattr(obj,"say_hi")
# b()


# setattr(obj,"sex","男")
# # print(Foo.sex)
# print(obj.sex)
# def eat1():
#     print("吃")
# setattr(obj,"eat",eat1)
#
# obj.eat()
# print(hasattr(obj,'eat'))
# delattr(obj,'name')
# print(obj.name) #被删除后报错

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def run(self):
#         print("pao")
# xiaom = Person("小明",18)
# print(hasattr(xiaom,"name"))

#获取属性的值
# b = getattr(xiaom,"age")
# b = getattr(xiaom,"run")
# print(b())
#设置属性,该属性不一定是存在的
# setattr(xiaom,"sex",123)
# print(xiaom.sex)
# def eat1():
#     print("吃")
# setattr(xiaom,"eat",eat1)
# xiaom.eat()

#综合用法
# b = getattr(xiaom, "age123", setattr(xiaom, "age123", "20"))
# print(b)

#删除属性
# delattr(xiaom,'name')
# print(xiaom.name) #被删除后报错



class User:
    def login(self):
        print('欢迎来到登录页面')
    def register(self):
        print('欢迎来到注册页面')
    def save(self):
        print('欢迎来到存储页面')

user = User()
while True:
    choose = input('>>>').strip()
    if hasattr(user,choose):
        func = getattr(user,choose)
        func()
    else:
        print('输入错误。。。。')
