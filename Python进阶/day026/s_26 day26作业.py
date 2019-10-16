"""
s_26 day26作业
"""

"""
1，写一个程序，实现3个进程间通信，传递一个字符串
"""
# from multiprocessing import Pool, Manager
# import time
#
# def write(p):
#     for i in range(10):
#         print("进程1写入",i)
#         p.put(i)
#
# def read1(p1,p2):
#     while True:
#         if p1.empty():
#             break
#         else:
#             a = p1.get()
#             p2.put(a)
#             print("进程2读取",a)
#
# def read2(p):
#     while True:
#         time.sleep(0.0002)
#         if p.empty():
#             break
#         else:
#             print("进程3读取",p.get())
#
# if __name__ == "__main__":
#     po = Pool(3)
#     q1 = Manager().Queue()
#     q2 = Manager().Queue()
#     po.apply_async(write,(q1,))
#     time.sleep(0.001)
#     po.apply_async(read1,(q1,q2))
#     po.apply_async(read2,(q2,))
#     po.close()
#     po.join()

"""
2，写一个包含10个线程的程序，，每一个子线程执行的时候都需要打印当前线程名、当前活跃线程数量
"""
# import threading
# import time
# import random
#
# def func():
#     time.sleep(random.randint(1, 3))
#     print(threading.current_thread().name,f"当前活跃线程数量{len(threading.enumerate())}")
#
#
#
# lst = [threading.Thread(target=func,name=f"线程{i}") for i in range(10)]
# for i in lst:
#     i.start()

"""
3，已知列表 info = [1,2,3,4,55,233]生成6个线程对象,每次线程输出一个值，最后输出："the end"
"""
# import threading
# info = [1,2,3,4,55,233]
# def func():
#     print(threading.current_thread().name,"取值：",info.pop(0))
#
# lst = [threading.Thread(target=func,name=f"线程{i}") for i in range(6)]
# for i in lst:
#     i.start()

"""
4，有10个刷卡机，代表建立10个线程，每个刷卡机每次扣除用户一块钱进入总账中，每个刷卡机每天一共刷100次。
账户原有500块。所以当天最后的总账应该为1500
"""
# import threading
# account = 500
# def func():
#     global account
#     a = account
#     for i in range(100):
#         account += 1
#     print(threading.current_thread().name,account-a)
# lst = [threading.Thread(target=func,name=f"刷卡机{i}:") for i in range(1,11)]
# for i in lst:
#     i.start()
# print("总账：",account)