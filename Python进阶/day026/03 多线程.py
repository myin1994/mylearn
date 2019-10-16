# 线程：实现多任务的另一种方式（包含在进程中）

# 主进程---》主线程---》子线程（共享空间）-只能有主线程创建

# 子进程--》子进程中的线程(理解为就是子线程)

# 子线程--分块处理问题？-节省空间

# 轻量级-线程-共享当前进程的资源-不需要额外的通信机制

# python中子进程不可再创建线程因此一个子进程就是一个单线程
# import threading
#
# a = threading.current_thread() #获取当前主线程对象
# print(a.ident)
# print(a.name) #当前线程名
# print(a)

# import threading
# if __name__ == "__main__":
#     a = threading.current_thread()
#     a.name = "我取的名字"
#     print(f"主线程启动：{threading.current_thread().name}")
#     print(threading.enumerate())



# import threading
# import time
# def sing():
#     for i in range(3):
#         print("唱歌",i)
#         time.sleep(1)
#
# def dance():
#     for i in range(3):
#         print("跳舞",i)
#
#
# t1 = threading.Thread(target=sing)
# t2 = threading.Thread(target=dance)
# t1.start()
# t2.start()
# print(threading.enumerate())
# print(len(threading.enumerate()))














# 线程非安全
# import threading
# num = 1
# def r1():
#     global num
#     num += 1
#     print(num)
#
# for i in range(10):
#     t1 = threading.Thread(target=r1)
#     t1.start()

# flag = True
# while flag:
#     num = 0
#     def r1():
#         global num
#         for i in range(100000):
#             num += 1
#
#     def r2():
#         global num
#         for i in range(100000):
#             num += 1
#
#     p1 = threading.Thread(target=r1)
#     p2 = threading.Thread(target=r2)
#     p1.start()
#     p2.start()
#     if num == 200000:
#         flag = False
#         print(num)

import threading
import time
num = 0
def r1():
    global num
    for i in range(10000000):
        num += 1
    print("r1执行后的num",num)

def r2():
    global num
    for i in range(10000000):
        num += 1
    print("r2执行后的num", num)

p1 = threading.Thread(target=r1)
p2 = threading.Thread(target=r2)
p1.start()
# time.sleep(2)
p2.start()
# time.sleep(2)
p1.join()
p2.join()
print("全局中的num",num)