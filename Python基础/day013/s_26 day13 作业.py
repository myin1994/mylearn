"""
s_26 day13 作业
"""

"""
2.都完成的做一下作业（下面题都是用内置函数或者和匿名函数结合做出）：

1).用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
l=[{'name':'alex'},{'name':'y'}]
"""
l=[{'name':'alex'},{'name':'y'}]
# print(list(map(lambda x:{"name":x["name"] + "sb"},l)))

"""
2)用filter来处理,得到股票价格大于20的股票名字

shares={
 'IBM':36.6,
 'Lenovo':23.2,
 'oldboy':21.2,
 'ocean':10.2,
         }
"""
# shares={
#  'IBM':36.6,
#  'Lenovo':23.2,
#  'oldboy':21.2,
#  'ocean':10.2,
#          }
# print(list(filter(lambda x:shares[x] > 20,shares)))

"""
3)有下面字典，得到购买每只股票的总价格，并放在一个迭代器中。
结果：list一下[9110.0, 27161.0,......]

portfolio = [
  {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}]
"""
# portfolio = [
#   {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# g = (i["shares"] * i["price"] for i in portfolio)
# print(list(g))

"""
4)还是上面的字典，用filter过滤出单价大于100的股票。
"""
# portfolio = [
#   {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# print(list(filter(lambda x:x["price"] > 100,portfolio)))

"""
5)有下列三种数据类型，

 l1 = [1,2,3,4,5,6]
 l2 = ['oldboy','alex','wusir','太白','日天']
 tu = ('**','***','****','*******')
写代码，最终得到的是（每个元组第一个元素>2,第三个*至少是4个。）

 [(3, 'wusir', '****'), (4, '太白', '*******')]
这样的数据。
"""
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = ['oldboy', 'alex', 'wusir', '太白', '日天']
# tu = ('**', '***', '****', '*******')
# print(list(zip(list(filter(lambda x:x > 2,l1)),l2,list(filter(lambda x:len(x) > 3,tu)))))

"""
6)有如下数据类型(实战题)：

 l1 = [{'sales_volumn': 0},
       {'sales_volumn': 108},
       {'sales_volumn': 337},
       {'sales_volumn': 475},
       {'sales_volumn': 396},
       {'sales_volumn': 172},
       {'sales_volumn': 9},
       {'sales_volumn': 58},
       {'sales_volumn': 272},
       {'sales_volumn': 456},
       {'sales_volumn': 440},
       {'sales_volumn': 239}]
将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
"""
# l1 = [{'sales_volumn': 0},
#       {'sales_volumn': 108},
#       {'sales_volumn': 337},
#       {'sales_volumn': 475},
#       {'sales_volumn': 396},
#       {'sales_volumn': 172},
#       {'sales_volumn': 9},
#       {'sales_volumn': 58},
#       {'sales_volumn': 272},
#       {'sales_volumn': 456},
#       {'sales_volumn': 440},
#       {'sales_volumn': 239}]
# print(sorted(l1,key=lambda x:x['sales_volumn']))

"""
3.有如下数据结构,通过过滤掉年龄大于16岁的字典

lst = [{'id':1,'name':'alex','age':18},
        {'id':1,'name':'wusir','age':17},
        {'id':1,'name':'taibai','age':16},]
"""
# lst = [{'id':1,'name':'alex','age':18},
#         {'id':1,'name':'wusir','age':17},
#         {'id':1,'name':'taibai','age':16},]
# print(list(filter(lambda x:x["age"] > 16,lst)))

"""
4.有如下列表,按照元素的长度进行升序

lst = ['天龙八部','西游记','红楼梦','三国演义']
"""
# lst = ['天龙八部','西游记','红楼梦','三国演义']
# print(sorted(lst,key=lambda x:len(x)))

"""
5.有如下数据,按照元素的年龄进行升序

lst = [{'id':1,'name':'alex','age':18},
    {'id':2,'name':'wusir','age':17},
    {'id':3,'name':'taibai','age':16},]
"""
# lst = [{'id':1,'name':'alex','age':18},
#     {'id':2,'name':'wusir','age':17},
#     {'id':3,'name':'taibai','age':16},]
# print(sorted(lst,key=lambda x:x["age"]))

"""
6.看代码叙说,两种方式的区别

lst = [1,2,3,5,9,12,4]
lst.reverse()
print(lst) #lst本身进行了修改

print(list(reversed(lst))) #相当于新创建了一个反向后的列表
"""

"""
7.求结果(面试题)

v = [lambda :x for x in range(10)]
print(v) #[lambda,lambda,lambda……]列表里是10个匿名函数的内存地址
print(v[0]) # lambda匿名函数的内存地址
print(v[0]()) #  9
验证正确
"""

"""
8.求结果(面试题)

v = (lambda :x for x in range(10))
print(v) #生成器的内存地址
print(v[0]) #报错
print(v[0]()) #报错
print(next(v)) #匿名函数的内存地址
print(next(v)()) #1
验证正确
"""

"""
9.map(str,[1,2,3,4,5,6,7,8,9])输出是什么? (面试题)
函数的内存地址，加list()后输出是所有数字转换成字符串的列表
验证正确
"""

"""
10.有一个数组[34,1,2,5,6,6,5,4,3,3]请写一个函数，找出该数组中没有重复的数
的总和（上面数据的么有重复的总和为1+2+34=40)(面试题)
"""
# lst = [34,1,2,5,6,6,5,4,3,3]
# print(sum(list(filter(lambda x:lst.count(x) == 1,lst))))

"""
11.求结果：（面试题）

def num():
    return [lambda x:x**i for i in range(4)]
print([m(2) for m in num()]) #[m(2) for m in [lambda x:x**i for i in range(4)]]  [8,8,8,8]
验证正确
"""

"""
13.看代码写结果：
def wrapper(f):
    def inner(*args, **kwargs):
        print(111)
        ret = f(*args, **kwargs)
        print(222)
        return ret
    return inner

def func():
    print(333)

print(444) #444
func() #333
print(555) #55
验证正确

补充语法糖后继续
def wrapper(f):
    def inner(*args, **kwargs):
        print(111)
        ret = f(*args, **kwargs)
        print(222)
        return ret
    return inner

@wrapper
def func():
    print(333)

print(444) #444
func() #111 333 222
print(555) #55
验证正确
"""

"""
14.编写装饰器, 在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里’。
"""
# def warpper(func):
#     def inner():
#         print("每次执行被装饰函数之前都得先经过这里")
#         func()
#     return inner
#
# @warpper
# def index():
#     print("is 被装饰函数")
#
# index()

"""
15为函数写一个装饰器，把函数的返回值 + 100然后再返回。

@wrapper
def func():
    return 7


result = func()
print(result)
"""
# def wrapper(f):
#     def inner():
#         ret = f()
#         return ret + 100
#     return inner
#
# @wrapper
# def func():
#     return 7
#
# result = func()
# print(result)

"""
16.请实现一个装饰器，通过一次调用使被装饰的函数重复执行5次。
"""
# def warpper(f):
#     def inner():
#         for i in range(5):
#             f()
#     return inner
#
# @warpper
# def func():
#     print("执行一次了")
#
# func()

"""
17.请实现一个装饰器，每次调用函数时，将被装饰的函数名以及调用被装饰函数的时间节点写入文件中。

可用代码：
import time
struct_time = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", struct_time))  # 获取当前时间节点


def func():
    print(func.__name__)


函数名通过： 函数名.__name__获取。
"""
# import time
#
# def warpper(f):
#     def inner():
#         f1 = open("time.txt","a",encoding="utf-8")
#         f1.write(f"函数名：{f.__name__} 当前时间节点：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")
#         f1.flush()
#         f1.close()
#         f()
#     return inner
#
# @warpper
# def func():
#     print(func.__name__)
#
# func()