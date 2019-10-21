"""
s_26 day28作业
"""

"""
1，简述线程和协程的异同?

线程：多个线程并发执行时，同一时间只有一个线程在一块CPU上运行

协程：生存于线程之中,是比线程更小的执行单元，可以用来辅助线程的执行
"""

"""
2，什么是并行，什么是并发？

并行：多个进程同时在不同CPU上运行
并发：多个进程或线程在系统调度机制下在CPU上切换执行
"""

"""
3，请解释同步和异步这两个概念？

同步：多个任务按固定顺序执行，在时间上是线性的
异步：非固定顺序执行任务
"""

"""
4，GIL锁是怎么回事?

GIL锁是指在解释器层面加在每个线程前的一个互斥锁，它决定了每个CPU同一时间只能有一个线程执行
"""

"""
5，什么叫死锁？如何产生？如何解决

死锁是指多个线程或进程由于互斥锁的存在，在互相需要对方资源（释放锁）的情况下才可继续执行，双方互斥造成死锁。
可以使用非阻塞的锁避免死锁。
"""

"""
6，写一个程序，利用queue实现进程间通信；
"""
# from multiprocessing import Queue,Process
# def write(q):
#     for i in range(10):
#         q.put(i)
#         print("放入：",i)
#
# def read(q):
#     for i in range(q.qsize()):
#         print("获取",q.get(i))
#
# if __name__ == "__main__":
#     q = Queue()
#     p1 = Process(target=write,args=(q,))
#     p1.start()
#     p1.join()
#     p2 = Process(target=read, args=(q,))
#     p2.start()
#     p2.join()

"""
7，写一个程序，包含十个线程，同时只能有五个子线程执行
"""
# import threading,time
# def func():
#     lock.acquire()
#     print("当前线程：",threading.current_thread().name)
#     print("当前线程数量：",len(threading.enumerate()))
#     time.sleep(1)
#     lock.release()
#
# lock = threading.Semaphore(5)
# lst = [threading.Thread(target=func,name=f"线程{i}") for i in range(10)]
# for i in lst:
#     i.start()
