## 什么是上下文管理器

### 基本语法

```python
with EXPR as VAR:
    BLOCK
```

### 概念

+ 上下文表达式：with open('test.txt') as f:
+ 上下文管理器：open('test.txt')
+ f 不是上下文管理器，应该是资源对象



### 作用

+ with语句就是简洁版的try/finally语句
+ 代码块前后必然会执行的内容



### 原理

 **上下文管理器是内部实现了__enter__和__exit__方法的对象** 

```python
class Foo:
    def __init__(self):
        print("实例化一个对象")

    def __enter__(self):
        print("进入")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出")
        return True

    def func(self):
        print("被执行的方法")


with Foo() as f:
    f.func()

    
>>>实例化一个对象
>>>进入
>>>被执行的方法
>>>退出
```



+  `__enter__`方法说明 

  ```
  上下文管理器的__enter__方法是可以带返回值的，默认返回None，这个返回值通过with...as...中的 as 赋给它后面的那个变量，所以 with EXPR as VAR 就是将EXPR对象__enter__方法的返回值赋给 VAR,VAR可以是单个变量，或者由“()”括起来的元组（不能是仅仅由“,”分隔的变量列表，必须加“()”）。
  
  with...as...并非固定组合，单独使用with...也是可以的，上下文管理器的__enter__方法还是正常执行，只是这个返回值并没有赋给一个变量，with下面的代码块也不能使用这个返回值。
  ```

+  `__exit__`方法说明 

  ```
  上下文管理器的__exit__方法接收3个参数exc_type、exc_val、exc_tb，如果代码块BLOCK发生了异常e并退出，这3个参数分别为type(e)、str(e)、e.__traceback__，否则都为None。
  
  同样__exit__方法也是可以带返回值的，这个返回值应该是一个布尔类型True或False，默认为None（即False）。如果为False，异常会被抛出，用户需要进行异常处理。如果为True，则表示忽略该异常。
  ```

  

## 上下文管理器的使用

### 异常处理

​	  处理异常，通常都是使用 `try...execept..` 来捕获处理的。这样做一个不好的地方是，在代码的主逻辑里，会有大量的异常处理代理，这会很大的影响我们的可读性。

好一点的做法呢，可以使用 `with` 将异常的处理隐藏起来。

仍然是以上面的代码为例，我们将`1/0` 这个`一定会抛出异常的代码`写在 `func` 里

 `__exit__` 函数的三个参数 

+  exc_type：异常类型 
+  exc_val：异常值 
+ exc_tb：异常的错误栈信息

```python
class Foo:
    def __init__(self):
        print("实例化一个对象")

    def __enter__(self):
        print("进入")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import traceback
        if exc_val:
            print("异常类型：",exc_type)
            print("异常值：",exc_val)
            traceback.print_tb(exc_tb,-1)#打印最开始的错误信息，可设置错误栈数以及写入文件
        print("退出")
        return True

    def func(self):
        print(1 / 0)
        print("被执行的方法")

with Foo() as f:
    f.func()

---------------------------------------------    
实例化一个对象
进入
  File "F:/PyProgram/test98/test1.py", line 62, in func
    print(1 / 0)
异常类型： <class 'ZeroDivisionError'>
异常值： division by zero
退出
```



### 资源管理

​	 在我们日常使用场景中，经常会操作一些资源，比如文件对象、数据库连接、Socket连接等，资源操作完了之后，不管操作的成功与否，最重要的事情就是关闭该资源，否则资源打开太多而没有关闭，程序会报错 。

### 常见的上下文管理器

```
file
decimal.Context
thread.LockType
threading.Lock
threading.RLock
threading.Condition
threading.Semaphore
threading.BoundedSemaphore
```



## 理解并使用 contextlib

​	 Python还提供了一个contextmanager装饰器，允许用户将一个生成器定义为上下文管理器，该装饰器将生成器中的代码通过yield语句分成两部分，yield之前的代码为`__enter__`方法，yield之后的代码为`__exit__`方法，yield的返回值即`__enter__`方法的返回值，用于赋给as后的变量。 

### 实现资源管理

```python
import contextlib

@contextlib.contextmanager
def open_func(file_name):
    # __enter__方法
    print('open file:', file_name, 'in __enter__')
    file_handler = open(file_name, 'r')

    # 【重点】：yield
    yield file_handler

    # __exit__方法
    print('close file:', file_name, 'in __exit__')
    file_handler.close()
    return

with open_func('userinfo.txt') as file_in:
    for line in file_in:
        print(line)
```



### 实现异常捕获

```python
import contextlib
import traceback
import sys
@contextlib.contextmanager
def open_func(file_name):
    # __enter__方法
    print('open file:', file_name, 'in __enter__')
    file_handler = open(file_name, 'r')

    try:
        yield file_handler
    except Exception as exc:
        exc_type, exc_val, exc_tb = sys.exc_info()
        print("异常类型：", exc_type)
        print("异常值：", exc_val)
        traceback.print_tb(exc_tb, -1)
        print('the exception was thrown')
    finally:
        print('close file:', file_name, 'in __exit__')
        file_handler.close()

        return

with open_func('userinfo.txt') as file_in:
    for line in file_in:
        print(1/0)
        print(line)
```

