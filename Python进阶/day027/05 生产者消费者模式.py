# 用于爬虫
# ⽣产者消费者模式是通过⼀个容器（缓冲区）来解决⽣产者和消费者的强耦合问题
# • 例如两个线程共同操作一个列表，一个放数据，一个取数据

# class queue.Queue(maxsize=0)
# – FIFO队列的构造器。maxsize为一个整数, 表示队列的最大条目数，可用来限制内存的使用。
# – 一旦队列满，插入将被阻塞直到队列中存在空闲空间。如果maxsize小于等于0，队列大小为无限。 maxsize默认为0

# import queue
# import threading
#
# def write():
#     while True:
#         if q1.qsize() <= 600:
#             for i in range(1,51):
#                 q1.put(f"新数据{i}")
#
# def read():
#     while True:
#         if q1.qsize() >= 100:
#             for i in range(20):
#                 print("读取",q1.get())
#
# q1 = queue.Queue()
# for i in range(1,500):
#     q1.put(f"初始数据{i}")
#
# t1 = threading.Thread(target=write)
# t2 = threading.Thread(target=read)
# t1.start()
# t2.start()


# 回调
# from  multiprocessing import Pool,Process
# import random
#
# def download(name):
#     import time
#     for i in range(1,4):
#         print(f"{name}下载文件{i}")
#         time.sleep(random.randint(1,3))
#     return f"{name}下载完成"
#
# def alterUser(msg):
#     print(msg)
#
# if __name__ == "__main__":
#     p = Pool(3)
#     p.apply_async(func=download,args=("进程1",),callback = alterUser)
#     p.apply_async(func=download,args=("进程2",),callback = alterUser)
#     p.apply_async(func=download,args=("进程3",),callback = alterUser)
#     p.close()
#     p.join()











# 协程
# from greenlet import greenlet
# def t1():
#     while True:
#         # sum = 0
#         print(sum([i for i in range(1,101)]))
#         gr2.switch()
#         a = input("输入1:")
#         print(a)
# def t2():
#     while True:
#         # sum = 0
#         print(sum([i for i in range(1,101)]))
#         gr1.switch()
#         a = input("输入2:")
#         print(a)
#
# gr1 = greenlet(t1)
# gr2 = greenlet(t2)
# gr1.switch()

import gevent
def t1():
    while True:
        # sum = 0
        print(sum([i for i in range(1,101)]))
        gevent.sleep(1)
        a = input("输入1:")
        print(a)
def t2():
    while True:
        # sum = 0
        print(sum([i for i in range(1,101)]))
        gevent.sleep(1)
        a = input("输入2:")
        print(a)

gr1 = gevent.spawn(t1)
gr2 = gevent.spawn(t2)
gr1.join()
gr2.join()