# 多进程之间。默认不共享数据
# 栈：FILO
# 队列：FIFO

# 通过Queue（队列Q）实现进程间数据传递
# from multiprocessing import Queue
#
# q1 = Queue(3) #初始化一个Queue对象，最多可接受3条消息
# q1.put(1)
# q1.put("2")
# print(q1.get())
# print(q1.get())
#
# print("被阻塞前")
# q1.get()
# print("被阻塞后")
# print(q1.get())
# print(q1.qsize())
# print(q1.get()) #获取一个数据并从队列移除，若队列无数据则阻塞程序
# q1.put("4") #被阻塞
# print(2)

# from multiprocessing import Queue,Process
#
# def wite(q1):
#     for i in range(5):
#         q1.put(i)
#         print(f"放入{i}")
#
# def read(r,q1,q2 = None):
#     while True:
#         if q1.empty():
#             break
#         else:
#             a = q1.get()
#             print(r,"读取", a)
#             if q2:
#                 q2.put(a)
#
#
# if __name__ == "__main__":
#     q1 = Queue()
#     q2 = Queue()
#     w = Process(target=wite,args=(q1,))
#     r1 = Process(target=read,args=("r1",q1,q2))
#     r2 = Process(target=read,args=("r2",q2,q1))
#     w.start()
#     w.join()
#     r2.start()
#     r1.start()
#     r1.join()
#     r2.join()

#
# from multiprocessing import Queue,Process
#
# def wite(q1):
#     for i in range(5):
#         q1.put(i)
#         print(f"放入{i}")
#
# def read1(r,q1,q2):
#     while True:
#         a = q1.get()
#         print(r,"读取", a)
#         if q2:
#             q2.put(a)
# def read2(r,q1):
#     while True:
#         print(r,"读取",q1.get())
#
# if __name__ == "__main__":
#     q1 = Queue()
#     q2 = Queue()
#     w = Process(target=wite,args=(q1,))
#     r1 = Process(target=read1,args=("r1",q1,q2))
#     r2 = Process(target=read2,args=("r2",q2))
#     w.start()
#     w.join()
#     r2.start()
#     r1.start()
#     r1.join()
#     r2.join()

# 使用进程池
# from multiprocessing import Pool, Manager
# import time
#
# def write(p):
#     for i in range(10):
#         p.put(i)
#         print("写入",i)
#
# def read(p):
#     time.sleep(3)
#     for i in range(p.qsize()):
#         print("读取",p.get())
#
# if __name__ == "__main__":
#     po = Pool()
#     p = Manager().Queue()
#     po.apply_async(write,(p,))
#     po.apply_async(read,(p,))
#     po.close()
#     po.join()


# import threading
# import time
# class MyThread(threading.Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#
#     def run(self) -> None:
#         for i in range(5):
#             print(self.name,i)
#             time.sleep(3)
#
# t1 = MyThread("进程1")
# t2 = MyThread("进程2")
# t1.start()
# t2.start()



# from multiprocessing import Process
# import time
# def f1():
#
#     time.sleep(3)
#     print(1)
#
#
# if __name__ == "__main__":
#     p1 = Process(target=f1)
#     p1.start()
#
#     print("主进程")

# from multiprocessing import Queue
# import time
#
# q = Queue(3)
#
# q.put("消息一")
# q.put("消息二")
# # time.sleep(0.00000000000001)
# # print(q.get())
# # print(q.qsize())
# # print(q.empty())
# a = q.get()
# print(a)
# q.put("消息三")


"""
1，写一个程序，实现1个进程向n个进程通信，传递数据

一个数据写入者
n个用户同时接收
"""
from multiprocessing import Process, Queue
queue1 = Queue()
def write(num,queue):
    for i in range(num):
        a = queue.put(i)
        print("进程写入：",i)

def read(q1,q2):
    while True:
        try:
            a = q1.get()
            print("读取:",a)
            q2.put(a)
        except Exception:
            break

def receiver(n):
    return [Queue() for i in range(n)]

if __name__ == "__main__":
    def func(person):
        receiver_lst = receiver(person)

        sender_p = Process(target=write,args=(5,receiver_lst[0]))
        sender_p.start()
        sender_p.join()

        lst = [Process(target=read,args=(receiver_lst[i],receiver_lst[i+1])) for i in range(len(receiver_lst) -1)]
        for i in lst:
            i.start()
        for i in lst:
            i.join()
    func(6)