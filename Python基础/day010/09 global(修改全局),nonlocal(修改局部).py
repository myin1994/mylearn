#global(修改全局),nonlocal(修改局部)


# global只修改全局空间中的变量
# 在局部空间中可以使用全局中的变量，但是不能修改，如果需要强制修改需要添加global
# a = 10
# def func():
#     #a = 1
#     # print(a)    可以使用
#     #a = a +1
#     global a
#     #当变量在全局存在时，申明要修改全局的变量
#     #当变量在全局不存在时，申明要在全局创建一个变量，并且会在局部开辟这个变量,但需要定义该变量
#     a = a + 1  #不声明且函数体内无定义不能修改
#     print(a)
# func()
# print(a) #11

# def func():
#     global a
#     a = 100
#     a = a + 1
#     print(a)
# func()
# print(a) #101

# a = 1000
# def func(a):
#     a = 100
#     a = a + 1
#     print(a)  #101
# func(a)
# print(a)  #1000

# nonlocal  只修改局部空间中的变量,最外层的一个函数
# 只修改距离nonlocal最近的一层，如果这一次没有就往上一层查找，只能在局部
# nonlocal不能创建变量
# a = 15
# def func():
#     a = 10
#     def foo():
#         a = 5
#         def f():
#             nonlocal a
#             a = a +1
#             print(a)
#         print(a)
#         f()
#         print(a)
#     foo()
#     print(a)
# func()
# print(a)

# 传参的时候相当于在当前函数体中进行了赋值操作
# def func(a):
#     #相当于 a = 100 操作
#     print(locals())
# func(100)

# a = 15
# def func():
#     a = 10
#     def foo():
#         def f():
#             # a = 1
#             nonlocal a
#             a = a +1
#             print(a)
#         print(a)
#         f()
#         print(a)
#     foo()
#     print(a)
# func()
# print(a)

# lst = [1,2,3,4,5,6]
# print(id(lst))
# def func():
#     lst.pop()
#     print(lst)
#     print(id(lst))
#     return lst
# print(func())
# print(id(lst))
# print(lst)