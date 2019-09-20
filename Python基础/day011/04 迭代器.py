# 迭代器：一个一个取值
# 可迭代对象：
# python中规定只要是具有__iter__()方法的就是可迭代对象

# str.__iter__()
# s = "1234"
# print(s.__iter__())
# list.__iter__()
lst = [1,2,3]
# print(lst.__iter__())
# tuple.__iter__()
# dict.__iter__()
# set.__iter__()
# 可迭代对象可重复取值

# for循环就一个迭代器
# 将可迭代对象转换为迭代器
# 有多少个元素就只能next多少次
# lst = [1,2,3,4]
# l = lst.__iter__()   #定义（创建）迭代器
# print(l)
# print(l.__next__())  #1 从内存地址出发，基于上一次停留的位置取下一位
# print(l.__next__())  #2 从内存地址出发，基于上一次停留的位置取下一位
# print(l.__next__())  #3 从内存地址出发，基于上一次停留的位置取下一位
# print(l.__next__())  #4 从内存地址出发，基于上一次停留的位置取下一位
# print(l.__next__())  #  取值超过范围，报错

# lst = [1,2,3,4]
# l = iter(lst)  #定义（创建）迭代器
# print(l)
# print(next(l))  #1 从内存地址出发，基于上一次停留的位置取下一位
# print(next(l))  #1 从内存地址出发，基于上一次停留的位置取下一位
# print(next(l))  #1 从内存地址出发，基于上一次停留的位置取下一位
# print(next(l))  #1 从内存地址出发，基于上一次停留的位置取下一位
# print(next(l))  #1 取值超过范围，报错



# 可迭代对象：str……………………
# python中规定只要是具有__iter__()方法的就是可迭代对象
# 优点
    #1.使用灵活（每个可迭代对象都有自己的方法）
    #2.能够直接查看元素的个数
# 缺点：占内存

# 迭代器：
# 具有__iter__()和__next__()方法的就是迭代器
# 优点：节省内存
# 缺点
     #1.只能向一个方向执行
     #2.一次性的
     #3.不能灵活操作，不能直接查看元素个数
# 文件句柄就是一个迭代器
# f = open("test1","a",encoding="utf-8")

# 应用：当内存空间大、数据量比较少时，建议使用可迭代对象
# 应用：当内存空间小、数据量比较大时，建议使用迭代器

# 注意点：
lst =[1,2,3,4,5]
print(lst.__iter__())
print(lst.__iter__()) #不一样，不一样的生成器
print(lst.__iter__().__next__())  #1
print(lst.__iter__().__next__())  #1  新定义的迭代器
#
# lst = [1,2,3,4]
# l = lst.__iter__()   #只定义一次
# print(l.__next__())  #1
# print(l.__next__())  #2

# for循环的本质
# s = "balablala"
# # for i in s:
# s1 = s.__iter__()
# while True:
#     try: #异常捕获---尝试运行一下缩进体的代码
#         print(s1.__next__())
#     except StopIteration: #接收错误（try有错误且满足异常条件时）
#         print("报错啦")
#         break
#
# #... == pass

# python2和python3的区别
# python2 没有__iter__方法 有iter(lst)
# python3 有

# 方法一
# lst =[1,2,3,4,5,6]
# l = lst.__iter__()
# print(l.__next__())

# 方法二
# lst =[1,2,3,4,5,6]
# l = iter(lst)
# print(next(l))

# 时间换空间：迭代器，生成器，用大量的时间来节省空间的使用
# 空间换时间：可迭代对象，使用大量的空间来节省时间

# lst = [1,2,3,4,5,6]
# l = iter(lst)
# l1 = iter(l) #迭代器转换迭代器视为无效
# print(l,l1)
# for i in l:
#     print(i)

# 迭代器也是一个可迭代对象