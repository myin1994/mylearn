# 多进程，多线程，协成

# 计算机程序-一段可执行的代码
# 进程-正在运行的代码
# 软件进程运行在操作系统之上

# 多任务处理：使得计算机可以同时处理多个任务
# 实现方式：多进程、多线程

# 一个或多个CPU实现时各个进程切换实现
# 系统调用机制

# 串行：一个CPU执行完一个进程结束后再执行下一个进程
# 并发：一个CPU处理多进程
# 并行：多个CPU处理不同的进程

# 多进程
# CPU切换的速度快-人感觉不出来
# 运行一个程序就产生一个进程
# 模拟
# def tiaowu():
#     print("正在跳舞")
#     changge()
#
# def changge():
#     print("正在唱歌")
#
# for i in range(20):
#     tiaowu()

#  程序开始运行时，首先会创建一个主进程
# 在主进程（父进程）下，我们可以创建新的进程（子进程），子进程依赖于主进程， 如果主进程结束，程序会退出
#  Python提供了非常好用的多进程包multiprocessing，借助这个包，可以轻松完成 从单进程到并发执行的转换
# multiprocessing模块提供了⼀个Process类来创建⼀个进程对象

# 子进程和主进程互不影响，主进程一般用于管理和创建子进程

# from multiprocessing import Process
#
# def zhandipan(a):
#     print("抢占铜锣湾",a)
#
# def qiangdipan():
#     print("抢占钵兰街")
# print(__name__)
#
# if __name__ == "__main__":
#     # windows 系统中需要用到它
#     # 把创建进程和调用进程的代码放到下面
#     print("主进程启动，帮派建立")
#
#     haonan = Process(target=zhandipan,args=("test",)) #创建子进程时会自动导入启动它的文件
#     # target表示调用对象，args表示调用对象的位置参数元组
#     # （注意：元组中只有一个元素时结尾要加，）
#     shisanmei = Process(target=qiangdipan,name="子进程2")
#     print(haonan.name,shisanmei.name) #进程名
#
#     haonan.start() #进程进入就绪状态
#     shisanmei.start()
#     print(haonan.pid,shisanmei.pid) #进程编号-系统分配后根据编号调用
#     haonan.join()
#     shisanmei.join()
#     print("程序结束")

"""
朋友眼中你是小明(__name__ == '小明'), 
你自己眼中你是你自己(__name__ == '__main__'),

你编程很好, 朋友调你去帮他写程序(import 小明, 这时你在朋友眼中: __name__ == '小明'),
但你晚上也会打开xx网站, 做一些自己的事情(直接运行小明.py, __name__ == '__main__')

所以，if __name__ == '__main__' 我们简单的理解就是： 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。

 python xxx.py 与 python -m xxx.py 的区别。两种运行 Python 程序的方式的不同点在于，一种是直接运行，一种是当做模块来运行。
"""

# from multiprocessing import Process
# import time
# import random
#
#
# def test():
#     for i in range(random.randint(1, 5)):
#         print("----子进程中%d___" % i)
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     p = Process(target=test)
#     p.start()
#     p.join()  # 这句话保证子进程结束后再向下执行
#     # p.join(2)#等待2s
#     # p.terminate() #进行结束
#     print("----等待子进程结束后进行-----")
#
#
# # 整个子进程结束后主进程才结束，p.join保证p进程结束后，才继续向下执行
# '''
# ----子进程中0___
# ----子进程中1___
# ----等待子进程结束后进行-----
# '''

# 全局变量在多个进程中不共享：进程之间的数据是独立的，默认情况下互不影响
# from multiprocessing import Process
# num = 10
#
# def r1():
#     global num
#     num += 5
#     print(f"在子进程一中：num={num}")
#
# def r2():
#     global num
#     num += 10
#     print(f"在子进程二中：num={num}")
#
# if __name__ == "__main__":
#     p1 = Process(target=r1)#理解为导入包不会影响包的数据
#     p2 = Process(target=r2)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print(f"在主进程中:num={num}")

# 创建新的进程还能够使⽤类的⽅式， 可以⾃定义⼀个类， 继承Process类， 每次实 例化这个类的时候， 就等同于实例化⼀个进程对象
# from multiprocessing import Process
# class Wodejincheng(Process):
#
#     def __init__(self,args = ()):
#
#     def run(self) -> None:
#         print(f"{self._args}固定执行这些代码")
#
# if __name__ == "__main__":
#     p1 = Wodejincheng((1,))
#     p2 = Wodejincheng((1,))
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()



# from multiprocessing import Pool
# import time
# def pr1():
#     print("进程1")
#     time.sleep(10)
#
# def pr2():
#     print("进程2")
#     time.sleep(5)
# if __name__ == '__main__':
#     pool = Pool(4)
#     for i in range(10):
#         pool.apply_async(pr1)
#         pool.apply_async(pr2)
#     pool.close()
#     pool.join()