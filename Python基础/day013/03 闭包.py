# 闭包：保护数据安全，保护数据的干净性
# # 闭包的定义：
    # 1.在嵌套函数内，使用非全局变量（且不使用本层变量）
    # 2.将嵌套函数返回

# def func():
#     a = 10  #自由变量
#     def foo():
#         print(a)
#     return foo
# f = func()
# f()
# print(f.__closure__) #验证是否是闭包

# 单价：12000
# 版本1
# lst = []
# def buy_car(price):
#     lst.append(price)
#     arg = sum(lst) /  len(lst)
#     print(arg)
#
# buy_car(12000)
# buy_car(24000)
# lst[1] = 10
# buy_car(12000)
# buy_car(12000)
# buy_car(12000)
# buy_car(50000)
# buy_car(50000)

# 版本2：闭包
# def buy_car():
#     lst = []
#     print(1)
#     def func(price):
#         lst.append(price)
#         arg = sum(lst) /  len(lst)
#         print(arg)
#     return func
#
# f = buy_car() #只调用一次外层函数
# f #相当于函数调用
# print(f.__closure__)
# print(f.__code__.co_freevars) #查看自由变量
# print(f.__code__.co_varnames) #查看局部变量
# f(1) #相当于buy_car()(1)
# f(2)
# f(3)
# f(4)
# f(5)
# f(6)

#没有将嵌套的函数返回也是一个闭包，但是这个闭包不能使用
# def func():
#     a = 10
#     print(1)
#     def foo():
#         print(a)
#     print(foo.__closure__)
# func()

# def func():
#     a = 10
#     def foo():
#         print(a)
#     return foo
# func()()  #相当于foo()

# def wrapper(a,b):
#     #a = 2
#     #b = 3  #隐性
#     def inner():
#         print(a)
#         print(b)
#     return inner
# a = 2
# b = 3
# ret = wrapper(a,b)
# print(ret.__closure__)
# ret()

# 闭包的应用场景：
# 1.装饰器
# 2.防止数据被改动