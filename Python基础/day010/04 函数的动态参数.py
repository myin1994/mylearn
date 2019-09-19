# 1.函数的动态参数
# 位置参数，默认参数
# 动态参数的作用：
    # 1.能够接收不固定长度的参数
    # 2.位置参数过多时可以使用动态参数

# 函数参数的优先级 ：#位置参数>动态位置参数>默认参数>动态关键字参数
# def func(*args,**kwargs):  #万能传参
#     print(args,kwargs)
# func(11,22,33,44,55,666,a=1,b=2)

# def func(*args,**kwargs):  #万能传参
#     print(args,kwargs)
#     print(*args) #将元组打散
#     print(**kwargs)  #报错
#     print(*kwargs)  #获取字典的键
# func(11,22,33,44,55,666,a=1,b=2)

# lst = [1,2,3,4,5,6,7]
# def func(*args): #聚合
#     print(args)  #聚合结果
#     print(*args)  #打散
# func(*lst)  #打散  func(1,2,3,4,5,6,7)

# s ="ssssdddd"
# print(*s)
#
# a,*b = 1,2,3,4,5
# print(b)


# dic = {"key1":1,"key2":2}
# def func(**kwargs): #聚合
#     print(kwargs)  #聚合为字典
#     print(*kwargs)  #打散为键
# func(**dic)  #打散  func(key=1,key2=2)
# print(*dic)

# josn 数据  和字典长得一模一样


# 动态参数的使用
# def func(a,b,c):
#     print(a,b,c)
# func(1,2,3)

# *args  程序员之间约定俗成（可更换但不建议）,只接受多余的位置参数（任意数据类型）
# **kwargs  程序员之间约定俗成（可更换但不建议），只接受多余的关键字参数（a=1，b=2……）
# def func(*args):  #放在形参位置上的*是聚合
#     print(*args)  #函数体中的*就是打散
#     print(args)  #直接使用为元组
# func(1,2,3,4,5)

# def food(a,b,*args):  #位置参数+动态位置参数
#     print(a,b,args)
# food("1","2","3","4")

# 动态关键字参数（动态默认参数）
# def func(a,b,*args,c=2): #位置参数+动态位置参数+默认参数 #默认值可放数据类型
#     print(a,b,args,c)  #聚合为元组
# func(1,2,3,4,5,6,7,8,9,)


# 变量不能重复对同一形参传参
# def func(a,b,*args,m=9,**kwargs): #位置参数，动态位置参数，默认参数，动态关键字参数
#     print(a,b,args,kwargs,m)  #聚合为字典
# func(1,2,3,4,m=5,k=3,hh=10)

# def func(a,b,*args,m=9,**kwargs): #位置参数，动态位置参数，默认参数，动态关键字参数
#     print(a,b,args,kwargs,m)  #聚合为字典
# func(1,2,4,"m",5,6,7,8,9,hh=10,m= 10)

