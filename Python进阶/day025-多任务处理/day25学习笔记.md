## 多任务处理

+ 概念：使得计算机可以同时处理多个任务
+ 实现方式
  + 多进程
  + 多线程
+ CPU处理进程的方式
  + 串行：一个CPU执行完一个进程结束后再执行下一个进程
  + 并发：一个CPU处理多进程（通过系统调用机制轮流让各个任务交替执⾏）
  + 并行：多个CPU处理不同的进程（可以兼顾并发）
+ 同步与异步
  + 同步执行：一个进程在执行某个任务时，另外一个进程必须等待其执行完毕，才能继续执行。
  + 异步执行：一个进程在执行某个任务时，另外一个进程无需等待其执行完毕，就可以继续执行，当有消息返回时，系统会通知进行处理，这样可以提高执行效率。
  + 如，打电话时就是同步通信，发短信时就是异步通信。



## 多进程

+ 程序：一个指令的集合

+ 进程：正在执行的程序

  + 编写完的代码，没有运行时，称为程序，正在运行的代码，称为进程
  + 程序是死的(静态的)，进程是活的(动态的)

+ 多进程实现

  + 程序开始运行时，首先会创建一个主进程

  + **操作系统**轮流让各个任务交替执⾏ ，由于CPU的执⾏速度实在是太快了， 我们感觉就像所有任务都在同时执⾏⼀样

  + 在主进程（父进程）下，我们可以创建新的进程（子进程），子进程依赖于主进程，如果主进程结束，程序会退出

  + multiprocessing模块提供了⼀个Process类来创建⼀个进程对象 

  + 多进程中， 每个进程中所有数据（包括全局变量）都各有拥有⼀份， 进程之间的数据是独立的，默认情况下互不影响（理解为每一个进程相当于单独运行的程序）

    ```python
    from multiprocessing import Process
    num = 10
    
    def r1():
        global num
        num += 5
        print(f"在子进程一中：num={num}")
    
    def r2():
        global num
        num += 10
        print(f"在子进程二中：num={num}")
    
    if __name__ == "__main__":
        p1 = Process(target=r1)#理解为导入包不会影响包的数据
        p2 = Process(target=r2)
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print(f"在主进程中:num={num}")
    >>>在子进程一中：num=15
    >>>在子进程二中：num=20
    >>>在主进程中:num=10
    ```

+ `if __name__ == “__main__”:`说明

  + python的文件有两种使用的方法，第一是直接作为程序执行，第二是import到其他的python程序中被调用（模块重用）执行
  + 此`if __name__ == 'main': `的作用就是控制这两种情况执行代码的过程，`__name__` 是内置变量，用 于表示当前模块的名字 
  + 在`if __name__ == 'main': `下方代码只有在文件作为程序直接执行才会被执行，而import到其他程序中是不会被执行的

  ```python
  直观的理解
  朋友眼中你是小明(__name__ == '小明'), 
  你自己眼中你是你自己(__name__ == '__main__'),
  
  你编程很好, 朋友调你去帮他写程序(import 小明, 这时你在朋友眼中: __name__ == '小明'),
  但你晚上也会打开xx网站, 做一些自己的事情(直接运行小明.py, __name__ == '__main__')
  
  所以，if __name__ == '__main__' 我们简单的理解就是： 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
  
   python xxx.py 与 python -m xxx.py 的区别。两种运行 Python 程序的方式的不同点在于，一种是直接运行，一种是当做模块来运行。
  ```

+ Process类常⽤⽅法

  + p.start()：启动进程，并调用该子进程中的p.run() 
  + p.run():进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法 
  + p.terminate()（了解）强制终止进程p，不会进行任何清理操作 
  +  p.is_alive():如果p仍然运行，返回True.用来判断进程是否还在运行 
  + p.join([timeout]):主进程等待p终止，timeout是可选的超时时间

  ```python
  from multiprocessing import Process
  import time
  import random
  
  
  def test():
      for i in range(random.randint(1, 5)):
          print("----子进程中%d___" % i)
          time.sleep(1)
  
  
  if __name__ == '__main__':
      p = Process(target=test)
      p.start()
      p.join()  # 这句话保证子进程结束后再向下执行
      # p.join(2)#等待2s
      # p.terminate() #进行结束
      print("----等待子进程结束后进行-----")
  
  
  # 整个子进程结束后主进程才结束，p.join保证p进程结束后，才继续向下执行
  '''
  ----子进程中0___
  ----子进程中1___
  ----等待子进程结束后进行-----
  '''
  ```

  

+  Process类常⽤属性

  + name： 当前进程实例别名， 默认为Process-N， N为从1开始递增的整数
  + pid： 当前进程实例的PID值

+ 创建子进程的方法

  + 方法一：通过Process直接创建

    ```python
    from multiprocessing import Process
    
    def zhandipan(a):
        print("抢占铜锣湾",a)
    
    def qiangdipan():
        print("抢占钵兰街")
    print(__name__)
    
    if __name__ == "__main__":
        # windows 系统中需要用到它
        # 把创建进程和调用进程的代码放到下面
        print("主进程启动，帮派建立")
    
        haonan = Process(target=zhandipan,args=("test",)) #创建子进程时会自动导入启动它的文件
        # target表示调用对象，args表示调用对象的位置参数元组 
        # （注意：元组中只有一个元素时结尾要加，） 
        shisanmei = Process(target=qiangdipan,name="子进程2")
        print(haonan.name,shisanmei.name) #进程名
    
        haonan.start() #进程进入就绪状态
        shisanmei.start()
        print(haonan.pid,shisanmei.pid) #进程编号-系统分配后根据编号调用
        haonan.join()
        shisanmei.join()
        print("程序结束")
    >>>__main__
    >>>主进程启动，帮派建立
    >>>Process-1 子进程2
    >>>39648 31320
    >>>__mp_main__
    >>>抢占铜锣湾 test
    >>>__mp_main__
    >>>抢占钵兰街
    >>>程序结束
    ```

  + 方法二：使⽤类的⽅式， 可以⾃定义⼀个类

    继承Process类， 每次实例化这个类的时候，就等同于实例化⼀个进程对象

    ```python
    from multiprocessing import Process
    class Wodejincheng(Process):
        def run(self) -> None:
            print("固定执行这些代码")
    
    if __name__ == "__main__":
        p1 = Wodejincheng()
        p2 = Wodejincheng()
        p1.start()
        p1.join()
        p2.start()
        p2.join()
    >>>固定执行这些代码
    >>>固定执行这些代码
    ```

  + 方法三：使用进程池创建多个进程

    + 导入multiprocessing模块提供的Pool
    + 初始化Pool时，可以指定⼀个**最⼤进程数**，当有新的请求提交到Pool中时， 如果池还没有满， 那么就会创建⼀个新的进程⽤来执⾏该请求
    + 但如果池中的进程数已经达到指定的最⼤值，那么该请求就会等待， 直到池中有进程结束， 才会创建新的进程来执⾏

    ```python
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
        po = Pool(3) #定义一个进程池，最大进程数为3，默认大小为CPU核数 
        for i in range(100):
            po.apply_async(r1) #创建子进程并进入就绪状态,进程池空闲时才创建新进程
            po.apply_async(r2) #创建子进程并进入就绪状态
        po.close()  #进程池关闭之后不再接收新的请求
        po.join() #等待po中所有子进程结束，必须放在close后面
    ```

    + multiprocessing.Pool常⽤函数解析
      +  apply_async(func[, args[, kwds]]) ： 使⽤⾮阻塞⽅式调⽤func（并⾏执⾏） ， args为传递给func的参数列表， kwds为传递给func的关键字参数列表（主进程可最先执行）
      +  apply(func[, args[, kwds]])使⽤阻塞⽅式调⽤func：必须等待上⼀个进程退出才能执⾏下⼀个进程（主进程最后执行）-类似串行
      +  close()： 关闭Pool， 使其不再接受新的任务
      +  join()： 主进程阻塞等待⼦进程的退出，必须在close或terminate之后使⽤；