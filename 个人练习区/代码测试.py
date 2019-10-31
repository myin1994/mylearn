import gevent
def t1():
    while True:
        # sum = 0
        print(sum([i for i in range(1,101)]))
        # gevent.sleep(1)#用来模拟一个耗时操作
        #gevent中：当一个协程遇到耗时操作会自动交出控制权给其他协程
        a = input("输入1:")
        print(a)
def t2():
    while True:
        # sum = 0
        print(sum([i for i in range(1,101)]))
        gevent.sleep(1)
        a = input("输入2:") #每当遇到耗时操作，会自用转到其他协程
        print(a)

gr1 = gevent.spawn(t1) # 创建一个gevent对象（创建了一个协程），此时就已经开始执行t1
gr2 = gevent.spawn(t2)
gr1.join()#等待协程执行结束
gr2.join() #会等待协程运行结束后再退出