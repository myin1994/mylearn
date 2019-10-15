# 进程池：用来创建多个进程
from multiprocessing import Pool
import random
import time
def r1():
    print("r1",random.randint(1,10))
    time.sleep(10)
def r2():
    print("r2",random.randint(1,10))
    time.sleep(2)
if __name__ == "__main__":
    po = Pool(3)
    for i in range(100):
        po.apply_async(r1) #创建子进程并进入就绪状态
        po.apply_async(r2) #创建子进程并进入就绪状态
    po.close()
    print("主进程执行1")
    po.join()
    print("主进程执行2")

# from multiprocessing import Pool
# import random,time
#
# def work(num):
#     print(random.random()*num,num)
#     time.sleep(3)
#
# if __name__ == "__main__":
#     po = Pool(3)
#     for i in range(10):
#         po.apply_async(work,(i,))
#     po.close()
#     po.join()