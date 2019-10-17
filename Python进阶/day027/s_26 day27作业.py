"""
s_26 day27作业
"""

"""
1，写一个程序，线程C在线程B后执行，线程B在线程A之后进行
"""
# import threading
# def A():
#     lock1.acquire()
#     print("执行A")
#     lock2.release()
#
# def B():
#     lock2.acquire()
#     print("执行B")
#     lock3.release()
#
# def C():
#     lock3.acquire()
#     print("执行C")
#
# lock1 = threading.Lock()
# lock2 = threading.Lock()
# lock2.acquire()
# lock3 = threading.Lock()
# lock3.acquire()
# t1 =threading.Thread(target=A)
# t2 =threading.Thread(target=B)
# t3 =threading.Thread(target=C)
# t1.start()
# t2.start()
# t3.start()

"""
2，编写一个程序，开启3个线程，这3个线程的name分别为A、B、C，每个线程将自己的name在屏幕上打印10遍，
要求输出结果必须按ABC的顺序显示；如：ABCABC….依次递推
"""
# import threading
# def A():
#     for i in range(10):
#         lock1.acquire()
#         print("执行A:",i+1,threading.current_thread().name)
#         lock2.release()
#
# def B():
#     for i in range(10):
#         lock2.acquire()
#         print("执行B:",i+1, threading.current_thread().name)
#         lock3.release()
#
# def C():
#     for i in range(10):
#         lock3.acquire()
#         print("执行C:",i+1, threading.current_thread().name)
#         lock1.release()
#
# lock1 = threading.Lock()
# lock2 = threading.Lock()
# lock2.acquire()
# lock3 = threading.Lock()
# lock3.acquire()
# t1 =threading.Thread(target=A,name="线程A")
# t2 =threading.Thread(target=B,name="线程B")
# t3 =threading.Thread(target=C,name="线程C")
# t1.start()
# t2.start()
# t3.start()

"""
3，简述生产者与消费者模式（用自己的话默写）

生成者与消费者模式是在两者之间增加一个缓冲区，产生后消费数据都是从与缓冲区交互，从而降低了两者的耦合，
通过阻塞队列去协调生产者与消费者的执行效率，通过设置动态条件，使得对CPU的运用效率最高
"""
