# 同步调用：确定调用的顺序
# 提交一个任务, 自任务开始运行直到此任务结束, 我再提交下一个任务
# – 按顺序购买四大名著

# 异步调⽤：不确定顺序
# – 一次提交多个任务,然后我就直接执行下一行代码
# – 你喊你朋友吃饭 ，你朋友说知道了 ， 待会忙完去找你 ，你就去做别的了

# import threading
# def run1():
#     while True:
#         lock1.acquire()
#         print(1)
#         lock2.release()
# def run2():
#     while True:
#         lock2.acquire()
#         print(2)
#         lock3.release()
# def run3():
#     while True:
#         lock3.acquire()
#         print(3)
#         lock1.release()
#
# lock1 = threading.Lock()
# lock2 = threading.Lock()
# lock2.acquire()
# lock3 = threading.Lock()
# lock3.acquire()
# t1 = threading.Thread(target=run1)
# t2 = threading.Thread(target=run2)
# t3 = threading.Thread(target=run3)
# t1.start()
# t2.start()
# t3.start()

import threading,time
class Task1(threading.Thread):
    def run(self) -> None:
        while True:
            lock1.acquire()
            print("task1")
            time.sleep(1)
            lock2.release()

class Task2(threading.Thread):
    def run(self) -> None:
        while True:
            lock2.acquire()
            print("task2")
            time.sleep(1)
            lock3.release()
class Task3(threading.Thread):
    def run(self) -> None:
        while True:
            lock3.acquire()
            print("task3")
            time.sleep(1)
            lock1.release()

lock1 = threading.Lock()


lock2 = threading.Lock()
lock2.acquire() #先将两个进程锁住（提前获取锁）
lock3 = threading.Lock()
lock3.acquire()
t1 = Task1()
t2 = Task2()
t3 = Task3()
t1.start()
t2.start()
t3.start()





# 线程同步-消息队列