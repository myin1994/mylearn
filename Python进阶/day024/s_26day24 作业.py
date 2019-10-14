"""
s_26day24 作业
"""

"""
1，编写一个计算减法的方法，当第一个数小于第二个数时，抛出“被减数不能小于减数"的异常
"""
# def subtract(a,b):
#     return a - b
# a = 1
# b = 5
# if a < b:
#     raise Exception("被减数不能小于减数")
# else:
#     print(subtract(a,b))


# def subtract(a,b):
#     if a < b:
#         raise Exception("被减数不能小于减数")
#     else:
#         return a - b
# print(subtract(5,3))

"""
2，info = ['http://xxx.com','http:///xxx.com','http://xxxx.cm'....]任意多的网址.
定义一个方法get_page(listindex) listindex为下标的索引，类型为整数。 
函数调用：任意输入一个整数，返回列表下标对应URL的内容，用try except 捕获列表下标越界
"""
# info = ['http://xxx.com','http:///xxx.com','http://xxxx.cm']
# def get_page(listindex):
#     return info[listindex]
#
#
# try:
#     print(get_page(int(input("任意输入一个整数:"))))
# except IndexError:
#     print("列表下标越界")
# except ValueError:
#     print("输入不为整数")
# except Exception as e:
#     print(e)

"""
3，让一个人类对象，可以使用len（）方法获得一个整数值
"""
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def __len__(self):
#         return len(self.name)
# xiaoming = Person("小明")
# print(len(xiaoming))

"""
4，定义人类对象，用print直接打印时可以获得该对象的属性信息
"""
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"姓名：{self.name},年龄：{self.age}"
#
# xiaoming = Person("小明",18)
# print(xiaoming)


"""
5，尝试捕获IOError
"""
# f = open("1","a",encoding="utf-8")
# try:
#     f.read()
# except IOError:
#     print("文件操作有误！")

"""
6,尝试捕获keyError
"""
# dic = {1:2,2:3,3:4}
# try:
#     print(dic[5])
# except KeyError:
#     print("不存在的键")
