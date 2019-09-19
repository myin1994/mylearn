# 函数的嵌套
# 1.交叉嵌套


# def func(foo): #相当于foo = a
#     print(2)
#     foo()  #调用函数a，接收返回值
#     print(3)
#
# def foo():
#     print(4)
#     a()
#     print(5)
#
# def a():
#     print(1)
#
# func(a)  #print时才是使用None

# def func():
#     print(1)
#     print("难啊")
#     print(2)
#
# def foo(b):
#     print(3)
#     ss = b()
#     print(ss)
#     print(4)
#
# def f(a,b):
#     a(b)
#
# f(foo,func)

# 2.嵌套
# def func(a,b):
#     def foo(b,a):
#         print(b,a)
#     foo(a,b)
# func(4,7) #4 7

# def func(a,b):
#     def foo(b,a):
#         print(b,a)
#     foo(b,a)
# func(4,7) #7 4

# def func(a,b):
#     def foo(a,b):
#         print(b,a)
#     foo(b,a)
# func(4,7) #4 7

# 接收参数按顺序（位置），使用参数按名字

# def func(a,b):
#     def foo(b,a):
#         print(b,a) #4 7
#     return foo(a,b)  #先执行函数调用 返回None
# a = func(4,7)
# print(a) #None

# def func(a,b):
#     def foo(b,a):
#         print(a,b) #7 4  使用时按变量名
#     return foo(a,b)  #先执行函数调用
# a = func(4,7)
# print(a) #None

# def func():
#     print(1) # 1
#
# def foo(a,b):
#     def f(a,b):
#         print(a,b) #2 1
#         func()
#     f(b,a)
# foo(1,2)

# def func(a,b):
#     a = a + b
#     b = a + 10
#     def foo(a,d):
#         def f(e,f):
#             print(f,e)
#             return "难"
#         f(d,a)
#     foo(b,a)
# print(func(2,3))

# def func(a,b):
#     a = a + b
#     b = a + 10
#     def foo(a,d):
#         def f(e,f):
#             print(f,e)
#             return "难"
#         return f(d,a)
#     return foo(b,a)
# print(func(2,3))







































# def a():
#     print(1)
#     b()
# def b():
#     print(2)
#     a()
# a()  #执行一段时间后报错
# b()