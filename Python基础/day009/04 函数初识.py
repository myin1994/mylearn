# 函数的作用：封装代码，大量的减少重复代码，重用性高
# 过程式编程  vs  函数式编程
# s = "alexdsb"
# # 不使用len()
# count =  0
# for i in s:
#     count += 1
# print(count)

# 全局空间（当前py文件无缩进时）
# def my_len():#函数下函数体是被封装内容，被调用时才执行
#     count = 0
#     for i in s:
#         count += 1
#     print(count)
#
# s = "alexdsb"
# my_len()
# s = [1,2,3,4,5,6,7,8]
# my_len()

#函数的定义
# def --关键字，声明要定义一个函数
# my_len 函数名，遵循变量命名规则
# () 固定结构 ，用于传参
# : 表示语句结束
# 缩进
# 函数体

# 定义结构
# def 函数名():
#     #函数体

# def func():
#     msg = input(">>>>")
#     print(msg)

# 函数的调用
# 函数名()
    #调用函数
    #接收返回值
# func()
# print()
# list.append()

# print(print("a"))
# print(input("a"))

# 返回值
# return  --返回
# return "aaa"
# 返回      值
# def func():
#     a = 10
#     return a
# print(func())

# 存在意义：是因为函数被调用后，函数体中开辟的空间会被自动销毁
# 函数创建局部空间
# 查找顺序：局部-->全局-->内置空间
# def func():
#     a = 10
#     b = 20
#     return a,b
# a,b = func() #拆包，解包，平行赋值
# print(a,b)
# print(func())


# def func():
#     for i in range(10):
#         return i # 切记：终止函数不是终止循环
# print(func())
# 函数体中不写return默认返回None，或者写了return不写返回值返回的也是None
# return 能够返回任意、多个数据类型（python中所有对象）
# return将返回值返回给调用者--func()
# retun 能够终止函数，return下方的代码不执行