## iter()的特殊用法

+ 常规使用

   iter(obj)，会返现一个迭代器，如果 obj 不是可迭代对象，则会报错。

+ 特殊用法（哨兵模式）

  + `iter(object[, sentinel])` sentinel 英文翻译为 哨兵。
  + sentinel 参数是可选的，当它存在时，object 不再传入一个可迭代对象，而是一个可调用对象，通俗点说就是可以通过()调用的对象，而 sentinel 的作用就和它的翻译一样，是一个“哨兵”，当时可调用对象返回值为这个“哨兵”时，循环结束，且不会输出这个“哨兵”。

+ 实例

  + 实例1

    心里想一个[1, 10]范围的数，然后代码开始随机，当随机到想的数时停止，看每次代码需要随机几次。

    ```python
    from random import randint
    def guess():
        return randint(0, 10)
    
    num = 1  # 这里先写死心里想的数为5
    for i in iter(guess, 5):
        print("第%s次猜测，猜测数字为: %s" % (num, i))
        num += 1  # 当 guess 返回的是 5 时，会抛出异常 StopIteration，但 for 循环会处理异常，即会结束循环
    ```

  + 实例2

    构造分块读取数据的生成器

    ```python
    from functools import partial
    def chunked_file_reader(file, block_size=1024 * 8):
        """
        生成器函数：分块读取文件内容，使用 iter 函数
        @param file: 文件句柄
        @param block_size: 字节数
        @return:
        """
        # 首先使用 partial(fp.read, block_size) 构造一个新的无需参数的函数
        # 循环将不断返回 fp.read(block_size) 调用结果，直到其为 '' 时终止
        for chunk in iter(partial(file.read, block_size), ''):
            yield chunk
     
    #利用该函数统计含有9的个数
    def count_nine_v3(fname):
        count = 0
        with open(fname) as fp:
            for chunk in chunked_file_reader(fp):
                count += chunk.count('9')
        return count
    ```



## 偏函数functools.partial

+ 概念

  + 在Python的functools模块众多的功能中，其中有一个就是偏函数，我们称之为 partial function
  + 偏函数，其实是函数的辅佐，可以理解成绑定了一部分参数的函数。作用就是少传参数，更短，更简洁。

+ partial的组成

  + 第一部分也就是第一个参数，是一个函数，这个函数可以是你定义的，也可以是Python内置函数
  + 第二部分是一个可变参数，*args
  + 第三部分是一个关键字参数

+ 偏函数的使用

  偏函数的第二个部分(可变参数)，按原有函数的参数顺序进行补充，参数将作用在原函数上，最后偏函数返回一个新函数

  + 实例1

    ```python
    from functools import partial
    def mysum(*args,**kwargs):
        """
        对传入的位置参数及关键字参数求和
        """
        s = 0
        print('args',args)
        print('kwargs',kwargs)
        for i in args:
            s += i
        for value in kwargs.values():
            s += value
        return s
    
    print(mysum(1,2,3,a=4,b=5))
    
    mysum2 = partial(mysum,3,a=4,b=5,)
    print(mysum2(1,2))
    
    >>>args (1, 2, 3)
    >>>kwargs {'a': 4, 'b': 5}
    >>>15
    >>>args (3, 1, 2)
    >>>kwargs {'a': 4, 'b': 5}
    >>>15
    ```

  + 实例2

    ```python
    #选择某一天，然后以这天为准，次日留存，3日留存，7日留存，14日留存，30日留存。
    #已有一个获取第几天后的函数
    from functools import partial
    from datetime import datetime,timedelta
    def GetNextDay(baseday,n):
        return str((datetime.strptime(str(baseday),'%Y-%m-%d')+timedelta(days=n)).date())
    selected_day = '2019-11-11'
    print(GetNextDay(selected_day, 1))
    print(GetNextDay(selected_day, 2))
    print(GetNextDay(selected_day, 6))
    print(GetNextDay(selected_day, 13))
    print(GetNextDay(selected_day, 29))
    #简化
    nday = partial(GetNextDay,selected_day)
    print('>>>>>>>>>>>>>')
    print(nday(1))
    print(nday(2))
    print(nday(6))
    print(nday(13))
    print(nday(29))
    ```

+ 总结

  当函数的参数个数太多，需要简化时，使用 functools.partial 可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。