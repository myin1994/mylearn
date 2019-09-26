# 1.有参装饰器：
# 给装饰器额外增加一个参数，来控制装饰器的行为

# def auth(flag):
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             if flag:
#                 print(111)
#                 ret = func(*args,**kwargs)
#                 print(222)
#                 return ret
#             else:
#                 return func(*args,**kwargs)
#         return inner
#     return wrapper
#
# @auth(False)
# def index():
#     print("is index")
#
# index()

# 2.多个装饰器装饰一个函数
# def wrapper1(func):
#     def inner(*args,**kwargs):
#             print(111)
#             ret = func(*args,**kwargs)
#             print(222)
#
#     print("go1")
#     return inner
#
# def wrapper2(func):
#     def inner(*args,**kwargs):
#             print(111)
#             ret = func(*args,**kwargs)
#             print(222)
#     print("go2")
#     return inner
#
# @wrapper1
# @wrapper2
# def fun():
#     print(1)
#
# fun()

# 3.递归
# 1.不断调用自己本身
# 2.有明确的结束的条件

# 递归的最大深度：官方-1000  实际测试-993~998

# 修改递归最大深度：
# import sys
# sys.setrecursionlimit(10000)