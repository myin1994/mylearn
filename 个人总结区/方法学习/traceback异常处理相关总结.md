# traceback模块

+ 作用

  + traceback模块被用来跟踪异常返回信息
  + 可在控制台输出结果
  + 可将结果传入文件中记录

+ 常用方法

  + print_exc([limit[, file]]): 会自动处理当前 except 块所捕获的异常,将异常传播轨迹信息输出到控制台或指定文件中
    + limit: 用于限制显示异常传播的层数，比如函数 A 调用函数 B，函数 B 发生了异常，如果指定 limit=1，则只显示函数 A 里面发生的异常。不设置 limit 参数的话，默认全部显示。
    + file: 指定将异常传播轨迹信息输出到指定文件中。不指定该参数，则输出到控制台。
  + traceback.format_exc([limit]): 将异常传播轨迹信息转换成字符串

  ```python
  import traceback
  try:
      raise SyntaxError("traceback test")
  except Exception as e:
      fp = open("test1.txt", "w", encoding="utf-8")  # 创建内存文件对象
      traceback.print_exc(file=fp)
      traceback.print_exc()
      print(traceback.format_exc())
  ```

## 异常测试

+ 异常信息获取 sys.exc_info() 

  ```python
  import traceback
  import sys
  try:
      raise SyntaxError("traceback test")
  except Exception as e:
      exc_type, exc_value, exc_traceback = sys.exc_info()#元组
      print(exc_type, exc_value, exc_traceback)
      print(sys.exc_info())
  
  #<class 'SyntaxError'> traceback test <traceback object at 0x000001F8306BA988>
  #(<class 'SyntaxError'>, SyntaxError('traceback test',), <traceback object at 0x000001F8306BA988>)
  ```

  + exc_type： except 块内的异常类型
  + exc_value：except 块内的异常值（ 异常错误的信息 ）
  + exc_traceback： 跟踪回溯的对象 （异常传播轨迹）

+  打印栈的跟踪信息 `traceback.print_tb(traceback[, limit[, file]])`

  +  tb: 这个就是traceback object, 是我们通过sys.exc_info获取到的
  + limit: 这个是限制stack trace层级的，如果不设或者为None，就会打印所有层级的stack trace (limit=-1 打印最开始的错误信息)

  +  file: 这个是设置打印的输出流的，可以为文件，也可以是stdout之类的file-like object。如果不设或为None，则输出到sys.stderr

  ```python
  import traceback
  import sys
   
  def traceback_test():
      try:
          raise SyntaxError('traceback_test')
      except Exception as e:
          traceback.print_tb(e, limit=1, file=sys.stdout)
   
  if __name__ == '__main__':
      traceback_test()
  
  #错误信息
  Traceback (most recent call last):
    File "D:/MH_code/test_flask_project/app/traceback.py", line 14, in <module>
      traceback_test()
    File "D:/MH_code/test_flask_project/app/traceback.py", line 11, in traceback_test
      traceback.print_tb(e, limit=1, file=sys.stdout)
    File "C:\Python27\lib\traceback.py", line 61, in print_tb
      f = tb.tb_frame
  AttributeError: 'exceptions.SyntaxError' object has no attribute 'tb_frame'
  
  ```

+  打印异常信息 `traceback.print_exception(type, value, traceback[, limit[, file]])`

  +  (type, value, traceback)为sys.exc_info()返回的元组 
  +  如果traceback不为空, 打印栈头信息(即最近被调用的信息) 
  +  在栈的信息后打印异常类型和参数（错误信息）
  +  如果是语法错误, 会打印对应的代码行数, 用”^”指明语法错误的位置  

  ```python
  import traceback
  import sys
  
  
  def traceback_test():
      try:
          raise SyntaxError('traceback_test')
      except Exception as e:
          exc_type, exc_value, exc_traceback = sys.exc_info()
          traceback.print_exception(exc_type, exc_value, exc_traceback,limit=2,file=sys.stdout)
  
  
  if __name__ == '__main__':
      traceback_test()
  
  #错误信息
  Traceback (most recent call last):
    File "C:/Users/24479/Desktop/作业上传/个人总结区/方法学习/test.py", line 7, in traceback_test
      raise SyntaxError('traceback_test')
    File "<string>", line None
  SyntaxError: traceback_test
  ```

+ 简写，常用`traceback.print_exc([limit[, file]])`

  自动执行exc_info()来帮助获取这三个参数


## 异常处理规则

成功的异常处理应该实现如下4个目标

+ 使程序代码混乱最小化
+ 捕获并保留诊断信息
+ 通知合适的人员
+ 采用合适的方式结束异常活动

###  不要过度使用异常

滥用异常机制会带来负面影响，过度使用异常体现在两个方面：

+ 把异常和普通错误混淆在一起，不再编写任何错误处理代码，而是以简单的引发异常来代替所有的错误处理。
+ 使用异常处理来代替流程控制

要注意的是：异常处理机制的初衷是将不可预期异常的处理代码和正常的业务逻辑处理代码分离，因此绝不要使用异常处理来代替正常的业务逻辑判断。另外，异常机制的效率比正常的流程控制效率差，所以不要使用异常处理来代替正常的程序流程控制。

### 不要使用太庞大的 try 块

​		try 块的代码过于庞大会造成 try 块中出现异常的可能性大大增加，导致分析异常原因的难度也大大增加。try 块很庞大时，后面需要大量的 except 块才可针对不同的异常提供不同的处理逻辑，在同一个 try 块后使用大量的 except 块则需要分析它们之间的逻辑关系，反而增加编程复杂度。

​		所以大的 try 块可分割成多个可能出现异常的程序段落，并将其放在单独的 try 块中，从而分别捕获并处理异常。

###  不要忽略捕获到的异常

当产生异常时，在 except 块里应做一些有用的事情，如处理并修复异常，不能将 except 块设置为空或者简单的打印异常信息。对异常采取适当的措施，例如

+ 处理异常。对异常进行合适的修复，然后绕过异常发生的地方继续运行；或者用别的数据进行计算，以代替期望的方法返回值；或者提示用户重新操作等等，总之，程序应尽量修复异常，使程序能恢复运行。
+ 重新引发新异常。把当前运行环境下能做的事情尽量做完，然后进行异常转译，把异常包装成当前层的异常，重新上传给上层调用者。
+ 在合适的层处理异常。如果当前层不清楚如何处理异常，就不要在当前层使用 except 语句来捕获该异常，让上层调用者来负责处理该异常。