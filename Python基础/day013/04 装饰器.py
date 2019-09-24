# 装饰器
# 开放封闭原则：
# 1.对扩展开放 ---支持增加新功能
# 2.对修改源代码是封闭的,对调用方式是封闭的

# 装饰器：在原有的基础上添加额外的功能

# 版1
# import time #python中的标准库的模块
# # print(time.time())  #--时间戳  浮点数（秒）
# starttime = time.time()
# def index():
#     time.sleep(2)  #休眠--2秒
#     print("is index xxxx")
# index()
# print(time.time()-starttime)

# # 版2
# import time #python中的标准库的模块
# def run_time(f):
#     starttime =time.time()
#     f()
#     print(time.time() - starttime)
#
# def index():
#     time.sleep(2)  #休眠--2秒
#     print("is index xxxx")
#
# run_time(index)
#
# ff = index
# index = run_time
# index(ff)


# # 版3-初版装饰器
# import time #python中的标准库的模块
# def run_time(f): #接收目标函数
#     def inner():
#         starttime =time.time()  #被装饰函数之前
#         f()
#         print(time.time() - starttime) #被装饰函数之后
#     return inner  #不能加括号
#
# def index():
#     time.sleep(2)  #休眠--2秒
#     print("is index xxxx")
#
# index = run_time(index)
# index()

# 版4
# 语法糖必须要放在被装饰函数的上方
# import time #python中的标准库的模块
# def run_time(f):
#     def inner():
#         starttime =time.time()  #被装饰函数之前
#         f()
#         print(time.time() - starttime) #被装饰函数之后
#     return inner  #不能加括号
#
# @run_time   #语法糖本质---> index = run_time(index)
# def index():
#     time.sleep(2)  #休眠--2秒
#     print("is index xxxx")
# @run_time   #语法糖  func = run_time(func)
# def func():
#     time.sleep(2)  #休眠--2秒
#     print("is index yyyy")
#
# index()
# func()

# import time
# def run_time(f):
#     def foo():
#         starttime = time.time()
#         f()
#         print(time.time()-starttime)
#     return foo

# def add_func(f):
#     def foo():
#         f()
#         print("哈哈")
#     return foo
#
# @add_func
# @run_time
# def func():
#     print([i for i in range(9)])
#
# func()

import time #python中的标准库的模块
# def run_time(f):# f接收的是被装饰函数的函数名
#     def inner(*args,**kwargs): #被装饰的函数需要的参数
#         print("外挂开启")
#         f(*args,**kwargs)
#         print("外挂关闭")
#     return inner  #不能加括号
#
# @run_time   #语法糖本质---> index = run_time(index)
# def index(user,pwd,hero):
#     print("打开游戏")
#     print(f"登录{user}和{pwd}")
#     print(f"选择英雄{hero}")
#     print("游戏中")
#     print("游戏结束")
# index("ma","12345","目的地")


# def run_time(f):# f接收的是被装饰函数的函数名
#     def inner(*args,**kwargs): #被装饰的函数需要的参数
#         print("外挂开启")
#         ret = f(*args,**kwargs)
#         print("外挂关闭")
#         return ret #可接收返回值
#     return inner  #不能加括号
#
# @run_time   #语法糖本质---> index = run_time(index)
# def index(user,pwd,hero):
#     print("打开游戏")
#     print(f"登录{user}和{pwd}")
#     print(f"选择英雄{hero}")
#     print("游戏中")
#     return "游戏结束"
# print(index("ma","12345","目的地"))  #其实index是inner

# # 标准版装饰器：
# def wrapper(func):
#     def inner(*args,**kwargs):
#         """执行被装饰函数之前的操作"""
#         func(*args,**kwargs)
#         """执行被装饰函数之后的操作"""
#     return inner
#
# @wrapper
# def index():
#     print("is index")
#
# index()

# def func(args):  #不用参数时
#     print("新加功能")
#     return args
#
# @func  #index = func(index)
# def index():
#     print(2)
#
# index()