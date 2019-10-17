# 线程同步

# 原子性-整体
# 一个操作整体做完
# 进行数据修改添加时使用

# 会降低效率

# 互斥锁-锁定代码以保证完全执行完
#  创建锁 mutex = threading.Lock()
# • 锁定 mutex.acquire()
# 中间代码
# • 释放 mutex.release() #解锁
# import threading
# import time
# num = 0
# def f1():
#     global num
#     for i in range(1000000):
#         mutex.acquire()
#         num += 1
#         mutex.release()
#
# def f2():
#     global num
#     for i in range(1000000):
#         mutex.acquire()
#         num += 1
#         mutex.release()
#
#
# mutex = threading.Lock()
#
# t1 = threading.Thread(target=f1)
# t2 = threading.Thread(target=f2)
# t1.start()
# t2.start()
# time.sleep(2)
# print(num)


# import threading
# import time
# num = 0
# def f1():
#     global num
#     mutex.acquire()
#     print("进入锁",num)
#     time.sleep(2)
#     for i in range(1000000):
#         num += 1
#     print("f1操作后",num)
#     mutex.release()
#
# def f2():
#     global num
#     print("f2中",num)
#     mutex.acquire() #如果后被调度到此会被阻塞
#     for i in range(1000000):
#         num += 1
#     print("f2操作后",num)
#     mutex.release()
#     num += 88
#
#
# mutex = threading.Lock()
#
# t1 = threading.Thread(target=f1)
# t2 = threading.Thread(target=f2)
# t1.start()
# t2.start()
# time.sleep(3)
# print(num)
# 线程可以从锁中切出，但是其他线程的锁中内容必须等当前锁完全执行完才能继续获取锁（被阻塞）

# 死锁，多个线程多个锁互相需要但多个线程抢到了不同的锁


# 信号量Semaphore ：控制一个时间点内线程进入数量的锁，信号量用来控制线程并发数
import threading
import time

s1 = threading.Semaphore(2)

def f1():
    s1.acquire()
    print("123")
    time.sleep(1)
    s1.release()

for i in range(10):
    t = threading.Thread(target=f1)
    t.start()