# 1.生成器的本质就是一个迭代器
# 最大的区别：
    # 迭代器：文件句柄，通过数据转换---python自带提供
    # 生成器：程序员自己实现

# lst = [1,2,3,4,5]
# l = lst.__iter__()  #同时占据空间

# 生成器目的：不再通过数据转换实现，而是通过代码编写实现

# 生成器的定义:
# 1.基于函数实现的生成器
# 2.表达式实现生成器

# 基于函数
# def func():
#     print(1)
#     return 5
# print(func())

#这是一个生成器
#当函数体中存在yield时就是定义一个生成器（语法分析识别到-全局）
# def func():
#     print(1)
#     yield 5
# print(func())  #创建一个生成器对象  <generator object func at 0x000001AA18B91CA8>


# def func():
#     print(foo)  #不报错
#
# def func():
#     if 3 > 2  #报错
# def func():
#     if 3 > 2  #报错

# 程序执行时：
    # 1.语法分析 --分析所有语法
    # 2.词法分析
    # 3.自己找


# 生成器的使用
# 特性：惰性机制
# yield 和 return的部分功能很像
# 版1
# def func():
#     yield 1  #记录最后一次的执行位置的
#     yield 2
#     yield 3
#
# g = func() #获取的是生成器的内存地址
# print(next(g)) #取值
# print(next(g))
# print(next(g))

# 版2
# def func():
#     yield 1  #记录最后一次的执行位置的
#     yield 2
#     yield 3
#
# g1 = func()
# g2 = func()
# g3 = func()
# print(g1,g2,g3)
# print(next(func())) #新定义生成器/迭代器
# print(next(func())) #新定义生成器/迭代器
# print(next(func()))

# def func():
#     yield
# print(next(func()))  #可返回None

# def func():
#     yield [1,2,3,4]
# print(next(func()))  #可返回列表，字典

# def func():
#     def foo():
#         print(1)
#     yield foo
#
# g = next(func()) #foo函数的内存地址
# print(g(),type(g))  #foo()

# def a(): #如果ruturn和yield同时存在
#     print(1)
#
#     yield 111
#     return 112
#     yield 113
# print(a)
# print(a())
# g = a()
# print(next(g))
# print(next(g))

# def func():
#     yield 1,2,3,4,5
#     print(123)
#     yield 111
# print(func)
# print(func())
# g = func()
# print(next(g))
# print(next(g))

# 时间 空间
# lst = list(range(1,50001))
# for i in range(50000):
#     lst.pop(0)
# print(lst)
#
# def func():
#     for i in range(1,50001):
#         yield i
# g = func()
# print(next(g))
# print(next(g))
# print(next(g))

# 区分迭代器和生成器
# lst = [1,2,3]
# print(lst.__iter__())
# def func():
#     yield 1
# print(func())
# func().send()
# 1.查看是否可用send()方法--func().send()  #具备send，生成器
# 看内存地址（推荐）

#生成器一定是一个迭代器，但迭代器不一定是一个生成器
# 生成器的本质就是一个迭代器

# 迭代器和生成器的优点：
# 1.节省空间
# 迭代器和生成器的缺点：
# 1.不能直接使用元素
# 2.不能直观查看元素
# 3.使用不灵活
# 4.稍微消耗时间
# 5.一次性的，不能逆行

# yield form
# def func():
#     # yield [1,2,23,44,3]
#     for i in [1,2,23,44,5]:
#         yield i
# g = func()
# for i in g:
#     print(i)

# def func():
#     # yield [1,2,23,44,3]  #将列表整体返回
#     yield from [1,2,3,4,4] #将列表中的元素逐个返回
#     yield from [44,5,3,4,4] #将列表中的元素逐个返回
# g = func()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

def func():
    yield [1,2,23,44,3]  #将列表整体返回、
    yield from "sddssssssssss"
    yield from {"k1":1,"k2":2,"k3":3}
    yield from {1,2,3,4}
    yield from [3,4,7,4,4] #将列表中的元素逐个返回
    yield from (44,5,3,4,4) #将列表中的元素逐个返回
g = func()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# yield：
    # yield 能返回多个，以元组的形式存储
    # yield 能返回各种数据类型（python的对象）
    # yield 能够写多个并且都执行
    # yield 能够记录执行的位置
    # yield 后面不写内容 默认返回None
    # yield 不会终止生成器
    # yield 都是将数据一次性返回

# yield from
# 将可迭代对象逐个返回


# 重点:
# 可迭代对象:
# python中规定只要是具有__iter__()方法的就是可迭代对象

# 迭代器:
# 具有__iter__()和__next__()方法的就是迭代器

# 生成器：
# 基于函数创建的生成器，函数体中必须存在yield
# 查看是否可用send()方法
# 地址
def foo():
    a = 1
    print(id(a))
    return 1
print(foo)
print(foo)


def func():
    a = [1]
    yield 1
    yield 2
g = func() #新创建并确定为g生成器
print(next(g))
print(next(g))
print(next(func())) #新创建，从头开始时
print(next(func())) #新创建，从头开始时
print(func())
print(func())


