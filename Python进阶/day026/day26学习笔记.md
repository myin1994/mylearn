## 进程间通信

+ 概念

  多进程之间，默认是不共享数据的，因此需要通过一个中转数据的对象进行进程间通信

+ 进程间通信方法

  + 通过Queue（队列Q）实现（队列：FIFO-栈：FILO）

  + 创建消息队列Q

    ```python
    from multiprocessing import Queue
    
    q1 = Queue(3) #初始化一个Queue对象，最多可接受3条消息(空或负则为无上限)
    ```

    

  + 入队操作-添加消息

    +  `Queue.put(item,[block[, timeout]])`
      + 被添加数据类型不限
      + 默认block=True - 阻塞状态，队列满时再写入则会阻塞（时间根据timeout而定）----表现为程序停在该位置(非阻塞状态会抛出异常)
      + 默认timeout=None -阻塞时长
    + `Queue.put_nowait(item)`： 相当Queue.put(item, False)

    ```python
    from multiprocessing import Queue
    
    q1 = Queue(3) #初始化一个Queue对象，最多可接受3条消息
    q1.put(1)
    q1.put("2")
    q1.put("3")
    print("被阻塞前")
    q1.put("4")
    print("被阻塞后")
    >>>被阻塞前
    >>>……
    ```

  + 出队操作-读取消息

    + `Queue.get([block[, timeout]])`
      + 从队列中读取消息并删除（先进先出）
      + 默认block=True - 阻塞状态，队列空时再读取则会阻塞（时间根据timeout而定）----表现为程序停在该位置(非阻塞状态会抛出异常)
      + 默认timeout=None -阻塞时长
    +  `Queue.get_nowait()`： 相当Queue.get(False) -若无阻塞则可能报错

    ```python
    from multiprocessing import Queue
    
    q1 = Queue(3) #初始化一个Queue对象，最多可接受3条消息
    q1.put(1)
    q1.put("2")
    print(q1.get())
    print(q1.get())
    
    print("被阻塞前")
    q1.get()
    print("被阻塞后")
    >>>1
    >>>"2"
    >>>被阻塞前
    >>>
    ```

  + `Queue.qsize()`： 返回当前队列包含的消息数量

  +  `Queue.empty()`： 判断队列是否为空（若没有阻塞直接判断则可True可False）

  + `Queue.full()：` 判断队列是否已满

  + 具体实现

    ```python
    #一个输出多个接收方
    from multiprocessing import Queue,Process
    
    def wite(q1):
        for i in range(5):
            q1.put(i)
            print(f"放入{i}")
    
    def read1(r,q1,q2):
        while True:
            a = q1.get()
            print(r,"读取", a)
            if q2:
                q2.put(a)
    def read2(r,q1):
        while True:
            print(r,"读取",q1.get())
    
    if __name__ == "__main__":
        q1 = Queue()
        q2 = Queue()
        w = Process(target=wite,args=(q1,))
        r1 = Process(target=read1,args=("r1",q1,q2))
        r2 = Process(target=read2,args=("r2",q2))
        w.start()
        w.join()
        r2.start()
        r1.start()
        r1.join()
        r2.join()
    ```

+ 使用进程池创建

  ```python
  from multiprocessing import Pool, Manager
  import time
  
  def write(p):
      for i in range(10):
          p.put(i)
          print("写入",i)
  
  def read(p):
      time.sleep(3)  #加阻塞以确保数据全部写入队列
      for i in range(p.qsize()):
          print("读取",p.get())
  
  if __name__ == "__main__":
      po = Pool()
      p = Manager().Queue()
      po.apply_async(write,(p,))
      po.apply_async(read,(p,))
      po.close()
      po.join()
  ```

  

## 多线程

+ 线程概念

  + 实现多任务的另一种方式 （被包含在进程里）
  + 在进程中同时处理多个任务
  + 也叫轻量级进程----是更小的执行单元

+ 线程特性

  + 一个进程可拥有多个并行的(concurrent)线程，（主进程--->主线程--->子线程（共享空间）---只能有主线程能创建）
  + 主线程当中每一个线程，共享当前进程的资源--可直接进行通信（信息传递速度更快）
  + 同一时间只有一个线程能在同一个CPU上执行

+ 线程和进程的区别

  | 区别                                               | 进程                                                         | 线程                                                         |
  | -------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | 根本区别                                           | 是系统进⾏资源分配和调度的⼀个独⽴单位                       | CPU调度和执行的单位                                          |
  | 开销【空间（内存耗用）和时间（运行时的执行性能）】 | 每个进程都有独立的代码和数据空间（进程上下文），进程间的切换会有较大的开销 | 轻量级的进程，同一类线程共享代码和数据空间，每个线程有独立的运行栈和程序计数器（PC）,线程切换开销小。 |
  | 所处环境                                           | 在操作系统中能同时运行多个任务                               | 在同一应用程序中有多个顺序流同时执行                         |
  | 分配内存                                           | 系统在运行时为每个进程分配不同的内存区域                     | 除了CPU之外，不会为线程分配内存（线程所使用的资源是它所属的进程的资源），线程组只能共享资源 |
  | 包含关系                                           | 没有额外线程的进程-->单线程；有多个线程的进程-->执行过程是多条线（线程）共同完成的 | 线程是进程的一部分                                           |

+ 多线程使用

  + 获取线程名

    ```python
    import threading
    
    a = threading.current_thread() #获取当前主线程对象
    print(a.ident)
    print(a.name) #当前线程名
    print(a)
    >>>20736
    >>>MainThread
    >>><_MainThread(MainThread, started 20736)>
    ```

    ```python
    import threading
    if __name__ == "__main__":
        a = threading.current_thread()
        a.name = "我取的名字"
        print(f"主线程启动：{threading.current_thread().name}")
    ```

  + 查看当前线程数量

    `threading.enumerate()` 返回当前运行中的Thread对象列表 

  + 创建线程

    + 通过 `threading.Thread` 直接在线程中运行函数

      ```python
      import threading
      import time
      def sing():
          for i in range(3):
              print("唱歌",i)
              time.sleep(1)
      
      def dance():
          for i in range(3):
              print("跳舞",i)
      
      
      t1 = threading.Thread(target=sing)
      t2 = threading.Thread(target=dance)
      t1.start()
      t2.start()
      print(threading.enumerate())
      
      >>>唱歌 0
      >>>跳舞 0
      >>>[<_MainThread(MainThread, started 19756)>, <Thread(Thread-1, started 18684)>, <Thread(Thread-2, started 5716)>]
      >>>3 #根据系统情况不确定数量
      >>>跳舞 1
      >>>跳舞 2
      >>>唱歌 1
      >>>唱歌 2
      ```

    + 通过继承 `threading.Thread `类来创建线程 (类似创建进程-重写run方法)

      ```python
      import threading
      import time
      class MyThread(threading.Thread):
          def __init__(self,name):
              super().__init__()
              self.name = name
      
          def run(self) -> None:
              for i in range(5):
                  print(self.name,i)
                  time.sleep(3)
      
      t1 = MyThread("进程1")
      t2 = MyThread("进程2")
      t1.start()
      t2.start()
      ```

+ 线程的五种状态

  + 新状态：线程对象已经创建，还没有在其上调用start()方法。 
  + 可运行状态：当线程有资格运行，但调度程序还没有把它选定为运行线程时线程所处的状态。当start()方法调用时，线程首先进入可运行状态。在线程运行之后或者从阻塞、等待或睡眠状态回来后，也返回到可运行状态。 
  + 运行状态：线程调度程序从可运行池中选择一个线程作为当前线程时线程所处的状态。这也是线程进入运行状态的唯一一种方式。 
  + 等待/阻塞/睡眠状态：这是线程有资格运行时它所处的状态。实际上这个三状态组合为一种，其共同点是：线程仍旧是活的（可运行的），但是当前没有条件运行。 但是如果某件事件出现，他可能返回到可运行状态。 
  + 死亡态：当线程的run()方法完成时就认为它死去。这个线程对象也许是活的， 但是，它已经不是一个单独执行的线程。线程一旦死亡，就不能复生。如果在一个死去的线程上调用start()方法，会抛出异常

+ 线程的优缺点

  + 数据使用方便
+ 因为线程直接共享全局变量，多个线程同时修改一个变量（即线程非安全），可能造成混乱
  
  ```python
  #执行1000000次的bug
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
  >>>r2执行后的num 11905960
  >>>r1执行后的num 12126074
  >>>全局中的num 12126074 #同名全局变量会因为线程的切换出现重复赋值的现象
  ```

