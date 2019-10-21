from  multiprocessing import Pool,Process
import random

def download(name):
    import time
    for i in range(1,4):
        print(f"{name}下载文件{i}")
        time.sleep(random.randint(1,3))
    return f"{name}下载完成"

def alterUser(msg):
    print("-->",msg)

if __name__ == "__main__":
    p = Pool(3)
    # 当func执行完毕后，return的东西会给到回调函数callback
    p.apply_async(func=download,args=("进程1",),callback = alterUser)
    # p.apply_async(func=download,args=("进程2",),callback = alterUser)
    # p.apply_async(func=download,args=("进程3",),callback = alterUser)
    p.close()
    p.join()