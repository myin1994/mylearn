# 匿名函数：一句话函数
# 匿名函数的名字叫做lambda
# def func(a,b):
#     c = a + b
#     return c
# print(func(1,2))

# 匿名函数的编写格式
# f = lambda a, b :a + b
# print(f(1,2))
# print((lambda a, b :a + b)(1,2))

# lambda 和 def 是一样的
# a,b 和 (a,b) 是一样的
# :a + b 和 return a+b 是一样的
# 形参：可以接收位置参数，动态位置，默认，动态关键字
# :返回值：只能返回一个数据
# f = lambda x,y:(x,y,x+y)
# print(f.__name__)

# f = lambda x,y: x if x > y else y

# print([lambda i:i+1 for i in range(3)]) #三个函数组成的列表（没有被调用），for仅决定个数

# g = [lambda i:i+1 for i in range(3)]
# print([em(3) for em in g])

# g = (lambda i:i+1 for i in range(3))
# print([em(3) for em in g])

# g = [lambda :i+1 for i in range(3)]
# print([em() for em in g])

# g = (lambda :i+1 for i in range(3))
# print([em() for em in g])

# g = [lambda x:x*i for i in range(3)]
# print([em(3) for em in g])

# g = (lambda x:x*i for i in range(3))
# print([em(3) for em in g])

# g = [lambda x:x*i for i in range(3)]
# for j in [2,10]:
#     g1 = (em(3) for em in g)
# print([e + j for e in g1])

# filter --过滤
# lst = [1,2,3,4,5,54,7,8,65]
# new_lst = []
# for i in lst:
#     if i > 4:
#         new_lst.append(i)
# print(new_lst)

# 模拟内置函数filter底层
# lst = [1,2,3,4,5,54,7,8,65]
# def foo(x): #规则函数
#     return x > 4   #Ture  和  False
#
# def f(func,iter):
#     lst = []
#     for i in iter:
#         if func(i):
#             lst.append(i)
#     return lst
#
# print(f(foo,lst))

# 使用
# lst = [1,2,3,4,5,54,7,8,65]
# def func(x):  #规则函数
#     return x>4 #Ture  和  False
# print(list(filter(func,lst)))


# lst = [1,2,3,4,5,54,7,8,65]
# print(list(filter(lambda x:x>4,lst)))


# lst = [{'id':1,'name':'alex','age':18},
#         {'id':1,'name':'wusir','age':17},
#         {'id':1,'name':'taibai','age':16},]
# print(list(filter(lambda x:x["age"] > 16,lst)))
#
# print(list(filter(lambda x:len(x["name"]) < 5,lst)))

# map() #映射，将可迭代对象中每一个元素执行函数功能

# lst = [1,2,3]
# print(list(map(str,lst)))

# lst1 = [1,2,3]
# lst2 = [3,2,1]
# lst3 = [1,2,3,4,5]
# print([lst1[i] + lst2[i] for i in range(len(lst1))])
# print(list(map(lambda  x,y :x+y,lst1,lst2)))
# print(list(map(lambda  x,y,z :x+y+z,lst1,lst2,lst3)))


# sorted()
# lst = [1,4,3,2,5,6,-7]
# print(sorted(lst)) #新建列表,升序
# print(lst)
# lst.sort()
# print(lst)  #原地修改


# print(sorted("alex,mdzz"))
# print(sorted("alex,mdzz",reverse=True)) #降序


# lst = ['天龙八部','西游记','红楼梦','三国演义']
# print(sorted(lst,key=len)) #key= 排序规则
# print(sorted(lst,key=lambda x:len(x)))
#
# lst = [{'id':1,'name':'alex','age':18},
#         {'id':2,'name':'wusir','age':17},
#         {'id':3,'name':'taibai','age':16},]
# print(sorted(lst,key=lambda x:x["age"]))

# print(max([12,3,4,5]))
# print(max([12,3,4,5,-15],key = abs))

# print(min([12,3,4,5]))
# print(min([12,3,4,5,-15],key = abs))

# dic = {"a":3,"b":2,"c":1}
# print(max(dic,key = lambda x:dic[x]))
# print(max(dic.values()))

# reduce() 累计
# from functools import reduce #python3
# # python2 reduce
#
# lst = [1,2,3,4,5]
# def func(x,y):
#     return x*y
# print(reduce(func,lst))
# print(reduce(lambda x,y:x*y,lst))
#
# # print()
# print("alex","wusir","太亮",sep="|",end="")  #分隔符可自定义
# print(111)
# f = open("a","a",encoding="utf-8")
# print("meet",file=f) #文件流

# zip()  拉链
# lst1 = [1,2,3,4,5,6]
# lst2 = [5,4,3,2,1]
# # print(list(map(lambda x,y:(x,y),lst1,lst2)))
# print(zip(lst1,lst2))
# print(dict(zip(lst1,lst2)))
# print(tuple(zip(lst1,lst2)))
# print(list(zip(lst1,lst2)))