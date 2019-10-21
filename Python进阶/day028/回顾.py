# import threading
#
# def func():
#     print(111)
#     print(t1.name)
#     print(threading.current_thread().name)
#
# t1 = threading.Thread(target=func,name="112")
# t1.start()

# class Person:
#     __age = 18
#
#     @property
#     def age(cls):
#         return cls.__age
#
#     @age.setter
#     def age(cls,num):
#         cls.__age = num
#
#
#     @age.deleter
#     def age(cls):
#         del cls.__age
#
# x1 = Person()
# x1.age = 19
# print(x1.age)
# print(x1.__dict__)
# print(Person.__dict__)

# class A():
#     def __init__(self,name):
#         self.name = name
#     def __eq__(self, other):
#         if self.name == other.name:
#             return True
#         else:
#             return False
# class B(A):
#     pass
#
# a = A("123")
# b = B("1234")
# print(a == b)

# class Person():
#     def __init__(self, name):
#         self.name = name
#
# def func():
#     print(123)
#
# x1 = Person("小明")
# x1.func = func
# print(x1.__dict__)
# x1.func()
# import types
# x1.func = types.MethodType(func,x1)
# print(x1.__dict__)
# x1.func()

# setattr(x1,"func",func)
# x1.func()

# 依赖关系的实质是在一个类的方法中实现对其他类对象的操作
# 组合关系的实质是在一个类中的实例化过程中将其他类的对象组合进来以便进行一系列操作

# class Yeye():
#     def __init__(self):
#         print("进入爷爷")
#
# class Qinba(Yeye):
#     def __init__(self):
#         # Yeye.__init__(self)
#         print("进入亲爸")
#
# class Gandie(Yeye):
#     name1 = 2
#     def __init__(self,name):
#         self.name = name
#         # Yeye.__init__(self)
#         print("进入干爹")
#     def func(self):
#         print(self.name)
#
# class Erzi(Qinba,Gandie):
#     def __init__(self,name):
#         # Qinba.__init__(self)
#         Gandie.__init__(self,name)
#         print("进入儿子")
#
# erzi = Erzi("张三")
# erzi.func()
# print(erzi.name)
# erzi.name

# from abc import abstractmethod,ABCMeta
# class Payment(metaclass=ABCMeta):
#     @abstractmethod
#     def pay(self,name):
#         pass
#
# class A(Payment):
#     def pay(self):
#         pass
#
# class B(Payment):
#     def pay(self):
#         pass
# a = B()

# class Danli:
#     flag = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.flag:
#             cls.flag = super().__new__(cls)
#         return cls.flag
#
# class A(Danli):
#     pass
#
# a = A()
# b = A()
# print(a is b)

# class A:
#     def func(self):
#         print(1)
#
# class B:
#     def func(self):
#         print(2)
#
# class C:
#     def func(self):
#         print(3)
#
# class D:
#     def func(self):
#         print(4)
#
# class Factory:
#     def func(self,attr):
#         if attr == 1:
#             return A()
#         if attr == 2:
#             return B()
#         if attr == 3:
#             return C()
#         else:
#             return D()
#
# x = Factory()
# y = x.func(1)
# y.func()


# import threading,queue,time
# q = queue.Queue()
#
# def put(q):
#     i = 0
#     while True:
#         i += 1
#         if q.qsize() < 100:
#             a = f"新添加元素{i}"
#             q.put(a)
#             print(a)
#         else:
#             i -= 1
#             time.sleep(1)
#             print("过会儿添加")
#
# def get(q):
#     while True:
#         if q.qsize() > 10:
#             print(f"读取{q.get()}")
#         else:
#             time.sleep(1)
#             print("过会儿读取")
#
# t1 = threading.Thread(target=put,args=(q,))
# t2 = threading.Thread(target=get,args=(q,))
# t1.start()
# t2.start()

# a = 1
# b = [1,2,3,4]
# try:
#     print(a/1)
#     print(b[9])
# except ZeroDivisionError:
#     print("除0错误")
# # except Exception as e:
# #     print("其他错误",e)
# else:
#     print("正常执行")
# finally:
#     print("必须执行")

# def func():
#
#     try:
#         print(1/0)
#         return "666"
#     finally:
#         print(111)
# func()

# class Myerror(Exception):
#     def __new__(cls, *args, **kwargs):
#         super().__new__(cls)
#         print("error")
#
# try:
#     if 1 < 2:
#         raise Myerror()
# except ZeroDivisionError:
#     print("YYY")

# from greenlet import greenlet
# import threading,queue,time
# q = queue.Queue()
#
# def put():
#     i = 0
#     print(i)
#     g2.switch()
#     while True:
#         i += 1
#         if q.qsize() < 100:
#             a = f"新添加元素{i}"
#             q.put(a)
#             print(a)
#         else:
#             i -= 1
#             # time.sleep(1)
#             print("过会儿添加")
#         g2.switch()
#
# def get():
#     j = 1
#     print(j)
#     g1.switch()
#     while True:
#         if q.qsize() > 10:
#             print(f"读取{q.get()}")
#         else:
#             # time.sleep(1)
#             print("过会儿读取")
#         print(q.qsize())
#         g1.switch()
#
# t1 = threading.Thread(target=put)
# t2 = threading.Thread(target=get)
# g1 = greenlet(put)
# g2 = greenlet(get)
# g1.switch()
# # print(1111)
# t1.start()
# t2.start()

# import gevent
# def t1():
#     while True:
#         # sum = 0
#         print(sum([i for i in range(1,101)]))
#         gevent.sleep(1)#用来模拟一个耗时操作
#         #gevent中：当一个协程遇到耗时操作会自动交出控制权给其他协程
#         a = input("输入1:")
#         print(a)
# def t2():
#     while True:
#         # sum = 0
#         print(sum([i for i in range(1,101)]))
#         gevent.sleep(1)
#         a = input("输入2:") #每当遇到耗时操作，会自用转到其他协程
#         print(a)
#
# gr1 = gevent.spawn(t1) # 创建一个gevent对象（创建了一个协程），此时就已经开始执行t1
# gr2 = gevent.spawn(t2)
# print(1)
# gr1.join()
# gr2.join()
import threading
import queue
import time
import random

class jdThread(threading.Thread):
    def __init__(self,index,queue):
        threading.Thread.__init__(self)
        self.index = index
        self.queue = queue

    def run(self):
        while True:
            time.sleep(1)
            if self.queue.empty():
                break
            item = self.queue.get()
            print("序号：",self.index,"任务",item,"完成")
            self.queue.task_done()#task_done方法使得未完成的任务数量-1

q = queue.Queue(0)
'''
初始化函数接受一个数字来作为该队列的容量，如果传递的是
一个小于等于0的数，那么默认会认为该队列的容量是无限的.
'''
for i in range(2):
    jdThread(i,q).start()#两个线程同时完成任务

for i in range(10):
    q.put(i)#put方法使得未完成的任务数量+1
