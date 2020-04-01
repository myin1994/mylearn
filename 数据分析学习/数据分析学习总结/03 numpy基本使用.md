## numpy基本使用

### numpy引入

```python
import numpy as np
print(np.__version__)#查看版本信息
print(np.show_config())#查看配置说明
```

### 数组的创建

+ numpy最核心的内容就是nd-array数组类型

+ 创建

  + array

    + 一维数组

      ```python
      a = np.array([1,2,3,4])
      print(a)
      
      >>>
      [1 2 3 4]
      ```

    + 二维数组（及多维）

      + 维度与元素个数一致时

        ```python
        b = np.array([[1,2],[3,4]])
        print(b)
        
        >>>
        [[1 2]
         [3 4]]
        ```

      + 维度与元素个数不一致时会被分别单独当做一条数据（塌陷为一维？）

        ```python
        c = np.array([[1,2],[3,4,5]])
        print(c)
        
        >>>
        [list([1, 2]) list([3, 4, 5])]
        ```
  
+ arange
  
  + 数组的元素通过arange区间（参数）指定，类似于python中的range
  
    ```python
      a = np.arange(1,10)
      print(a)
      
      >>>[1 2 3 4 5 6 7 8 9]
      a:array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ```
  
    
  
  + arange([start,] stop[, step,], dtype=None) 步长规则与range一致,但可以是小数
  
    ```python
      a = np.arange(1,10,0.5)
      print(a)
      
      >>>[1.  1.5 2.  2.5 3.  3.5 4.  4.5 5.  5.5 6.  6.5 7.  7.5 8.  8.5 9.  9.5]
    ```
  
+ ones/zeros/empty/full
  
  + 创建元素默认为1/0/不确定值/自定义值(指定形状后指定)的数组,指定形状
  
  + np.ones(shape, dtype=None, order='C')
  
    + shape-指定数组维度(通过元组指定维度)
  
      ```python
        a = np.ones(shape=5)#一维数组
        #a = np.ones(shape=(5,))
        print(a)
        >>>[1. 1. 1. 1. 1.]
        
        a = np.ones(shape=(5,3,))#二维指定行列（五行三列）
        print(a)
        >>>
        [[1. 1. 1.]
         [1. 1. 1.]
         [1. 1. 1.]
         [1. 1. 1.]
         [1. 1. 1.]]
      ```
  
    + dtype-默认为float64, 使用形式dtype=np.int;
  
      ```python
        a = np.ones(shape=(5,3,),dtype=np.int)
        print(a)
        
        >>>
        [[1 1 1]
         [1 1 1]
         [1 1 1]
         [1 1 1]
         [1 1 1]]
      ```
  
    + order-可选参数，c代表与c语言类似，行优先；F代表列优先
  
+ ones_like/zeros_like/empty_like/full_like
  
  + 创建元素默认为1/0/值不确定/自定义值的数组,根据参数数组形状
  
  + np.ones_like(i, dtype=None, order='K', subok=True)
  
    ```python
      c = np.ones_like([[1,2,3],[3,4,5],[5,6,7]])
      print(c)
      
      >>>
      [[1 1 1]
       [1 1 1]
       [1 1 1]]
    ```
  
+ eye/identity
  
  + 创建指定长度的单位矩阵（主对角线为1，其余为0）
  
  + np.eye(N, M=None, k=0, dtype=<class 'float'>, order='C')
  
    + N-行
      
    + M-列（不指定时默认等于行数）
      
    + k-基于对角线的偏移量（±）
      
      ```python
      a = np.eye(5)
      #a = np.identity(5)
      print(a)
      >>>
      [[1. 0. 0. 0. 0.]
       [0. 1. 0. 0. 0.]
       [0. 0. 1. 0. 0.]
       [0. 0. 0. 1. 0.]
       [0. 0. 0. 0. 1.]]
      ```
  
+ linspace
  
    线性空间，创建等差数列
  
    ```python
    np.linspace(
        start,#区间开始点
        stop,#区间结束点
        num=50,#元素个数
        endpoint=True,#是否包含终止点，默认为True-包含
        retstep=False,#为True会改变计算的输出，输出一个元组，而元组的两个元素分别是需要生成的数列和数列的步进差值。
        dtype=None,
      axis=0,
    )
  ```
  
  ![image-20191223141219345](.\asserts\image-20191223141219345.png)
  
  ​	
  
+ logspace
  
    创建对数（指数）的等比数列
  
    ```
    np.logspace(
        start,
        stop,
        num=50,
        endpoint=True,
        base=10.0,#底数值
        dtype=None,
      axis=0,
    )
    ```
  
    ```python
    a = np.logspace(1,10,10)
    print(a)
    
    >>>
    [1.e+01 1.e+02 1.e+03 1.e+04 1.e+05 1.e+06 1.e+07 1.e+08 1.e+09 1.e+10]
    
    
    a = np.logspace(1,10,10,base=2)
    print(a)
  >>>
    [   2.    4.    8.   16.   32.   64.  128.  256.  512. 1024.]
  ```
  
  + arange与linspace对比
  
    + 相同点：二者都可以产生等差数列
    + 不同点（侧重点）
      + arange，在指定区间，侧重于已知（确定）的步长值，而不太在意能产生多少个元素
      + linspace，在指定区间，侧重于产生多少个元素，而不太在意产生怎样的步长值

 

### 数组（ndarry）与列表（List） 

数组与列表类似，是具有相同类型的多个元素构成的整体

+ 局限

  + 数组：要求元素是相同的类型
  + 列表：不作限制

+ 优势（计算）

  + 数组可以与标量进行运算，数组直接也可以进行矢量化运算。【对应位置的元素进行运算，无需进行循环操作，这样就可以充分利用现代处理器SIMD Single Instruction,Multiple Data方式进行并行计算 】

    ![image-20191223144424916](.\asserts\image-20191223144424916.png)

  + 数组在运算时，具有广播能力【可根据需要进行元素的扩展（内存对齐-对位运算），完成运算】

    + 广播可以发生在标量与矢量之间，也可以发生在矢量与矢量之间
    + 沿着行进行广播

    ![image-20191223143928148](.\asserts\image-20191223143928148.png)

    ![image-20191223145400583](.\asserts\image-20191223145400583.png)

    + 沿着列进行广播

    ![image-20191223145916403](.\asserts\image-20191223145916403.png)

    + 广播并非在任何场景下都能进行，如果不能广播成相同的形状，就会出现错误

  + 数组底层使用C程序编写，运算速度快

  + 数组底层使用C中数组的存储方式（紧凑存储），节省内存空间

+ 应用对比

  + 时间

    + 创建（数组、列表）

      数组明显节省时间

      ![image-20191223164005359](.\asserts\image-20191223164005359.png)

    + 计算

      ![image-20191223164241121](.\asserts\image-20191223164241121.png)

  + 空间

    ![image-20191223165120602](.\asserts\image-20191223165120602.png)

### 数组的相关属性与操作

+ ndim-返回数组的维度(shape的长度)

  ```python
  a = np.array([[1,2,3],[2,3,3]])
  print(a.ndim)#2
  ```

+ shape-返回数组的形状，即数组的维度及对应长度（每个维度元素的个数,高→低）

  ```python
  x = np.array([[1],[1,2]])
  print(x)
  print(x.shape)
  
  >>>
  [list([1]) list([1, 2])]
  (2,)
  
  x = np.array([[1,2,3],[1,2,4]])
  print(x)
  print(x.shape)
  >>>
  [[1 2 3]
   [1 2 4]]
  (2, 3)----二维数组的行列
  ```

+ dtype-返回数组元素类型

  ```python
  x = np.array([[1,2,3],[1,2,4]])
  print(x.dtype)
  >>>int32
  
  x = np.array([[1,2,3.1],[1,2,4]])
  print(x.dtype)
  >>>
  float64
  ```

+ size-返回数组中元素的个数（最低维度）

  ```python
  x = np.array([[1,2,3],[1,2,4]])
  print(x.size)#6
  ```

+ itemsize-返回每个元素占用的空间大小（字节）

  ```python
  x = np.array([[1,2,3],[1,2,4],[1,2,3],[3,4,5]])
  print(x.itemsize)#4---int32对应
  ```

+ ndarray.flags	ndarray 对象的内存信息

+ ndarray.real	ndarray元素的实部

+ ndarray.imag	ndarray 元素的虚部

+ ndarray.data	包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。

### 数组类型

+ 在创建数组时，也可以使用dtype来显示指定数组中的元素类型（通过numpy提供的类型进行指定）。

  ```python
  a = np.array([[1,2],[3,4]],dtype=np.int64)
  a = np.array([[1,2],[3,4.1]],dtype=float)
  ```

+ 如果没有指定，会根据元素的类型进行推断。

+ 如果元素的类型不同，则会选择一种兼容的类型

+ 在创建数组时，元素的顺序也可能影响数组的类型

  + 低端存储（低位在前）

    ```python
    a = np.array([1,2,'3'])
    a.dtype#dtype('<U11')
    
    a = np.array(["1",2,3])
    a.dtype#dtype('<U1')-根据开始识别的数据类型决定
    ```

  + 高端存储

### 类型转换

使用astype方法对数组对象进行转换，返回转换后的结果，但不会改变原数组（类似reversed函数-只提供结果）

```python
a = np.array([1,2,3,4.1])
print(a)#[1.  2.  3.  4.1]
print(a.dtype)#float64
b = a.astype(int)
print(a)#[1.  2.  3.  4.1]
print(a.dtype)#float64
print(b)#[1 2 3 4]
print(b.dtype)#int32
```

注：不能通过对象的dtype属性直接进行修改类型。在计算机中， 整数类型与浮点类型的存储机制是不同的。

### 改变形状

+ 方法实现

  + 数组对象的reshape方法
  + np的reshape函数

  ```python
  a = np.arange(24)
  print(a)
  #b = np.reshape(a,(4,6))
  b = a.reshape(4,6)
  print(b)
  >>>
  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
  [[ 0  1  2  3  4  5]
   [ 6  7  8  9 10 11]
   [12 13 14 15 16 17]
   [18 19 20 21 22 23]]
  ```

  + 如果改变形状是多维的，可以将其中一个的维度设置为-1，表示根据长度自动计算。（用于转换未知数组为行向量或列向量）

    ```python
    a = np.arange(24)
    print(a)
    b = np.reshape(a,(4,-1))
    #b = a.reshape(-1,24)
    print(b)
    ```

    

### 索引和切片

+ 相似点

  + 数组对象支持索引和切片操作，语法与Python中序列类型的索引与切片类似

  + 当数组是多维数组时，可以使用array[高维，低维，……]的方式按照维度进行索引和切片

    + 索引

      ```python
      a = np.arange(10)
      a = a.reshape(2,-1)
      print(a)
      print(a[1][0])
      print(a[1,0])
      >>>
      [[0 1 2 3 4]
       [5 6 7 8 9]]
      5
      5
      ```

    + 切片

      + 一维

        ```python
        a = np.arange(10)
        #a = a.reshape(2,-1)
        print(a)
        print(a[1:5])
        print(a[1:5:2])
        print(a[::-1])
        >>>
        [0 1 2 3 4 5 6 7 8 9]
        [1 2 3 4]
        [1 3]
        [9 8 7 6 5 4 3 2 1 0]
        ```

      + 多维-array[先切高维，再切低维，……]

        ```python
        b = np.arange(30).reshape(5,-1)
        print(b)
        print(b[1:4,1:4])
        >>>
        [[ 0  1  2  3  4  5]
         [ 6  7  8  9 10 11]
         [12 13 14 15 16 17]
         [18 19 20 21 22 23]
         [24 25 26 27 28 29]]
        [[ 7  8  9]
         [13 14 15]
         [19 20 21]]
        ```

+ 不同点

  + 数组的切片返回的是原数组的视图（底层数据），切片对象与原数组对象共享底层数据，如果一个对象修改了底层数据，另一个对象也会受到影响

    ```python
    a = np.array([1,2,3,4])
    print(a)#[1 2 3 4]
    b = a[:]
    b[0] = 100
    print(a)#[100   2   3   4]
    ```

  + python中返回的是浅拷贝对象

  + 实现数组的对象的拷贝，可以使用copy方法

    ```python
    a = np.array([1,2,3,4])
    print(a)#[1 2 3 4]
    b = a.copy()
    b[0] = 100
    print(a)#[1 2 3 4]
    ```

  + 通过整数数组进行索引

    当要选取的元素不连续时，可以提供一个索引数组来选择（或修改）对应索引位置的元素（可用于打乱顺序）

    ```python
    a = np.array([1,3,5,10,-2,6])
    print(a)#[ 1  3  5 10 -2  6]
    index = [1,2,4]#索引数组
    print(a[index])#[ 3  5 -2]
    #print(a[[1,2,4]]) 
    ```

    + 通过整数数组索引，返回的是原数组的拷贝，而不是视图

    + 可以提供多个一维数组索引，此时会将每个数组的对应位置元素作为索引，返回对应的元素。

      ```python
      a = np.arange(24).reshape(2,3,4)
      print(a)
      print(a[[0],[1],[2]])
      print(a[[0,1],[1,2],[2,3]])#0,1,2一组，1,2,3一组
      >>>
      [[[ 0  1  2  3]
        [ 4  5  6  7]
        [ 8  9 10 11]]
      
       [[12 13 14 15]
        [16 17 18 19]
        [20 21 22 23]]]
      [6]
      [ 6 23]
      ```

  + 通过布尔数组进行索引

    + 对应位置为True则选取，False则不选

      ```python
      bool_array = [True,True,False,False,True]
      a = np.array([1,3,5,7,9])
      print(a[bool_array])#[1 3 9]
      ```

    + 返回值是数组视图

    + 用于索引的布尔数组通常通过现有数组计算得出

    + 可以通过`~`对条件进行取反操作（不能使用not）

      ```python
      a = np.array([1,2,101,901,66])
      a[~(a>100)] = 100
      print(a)#[100 100 101 901 100]
      ```

    + 当存在多个条件时，可以使用&，|符号（不能使用and or），同时每个条件要使用()包裹

      ```python
      age = np.array([33,13,42,23,6,99])
      print(age[(age>15)&(age<34)])#[33 23]
      ```

    + 实用操作（元素过滤）

      + 选择年龄大于15的

        ```python
        age = np.array([33,13,42,23,6,99])
        age_gt_15 = age > 15
        print(age_gt_15)
        age_result = age[age_gt_15]
        print(age_result)
        #print(age[age>15])
        >>>
        [ True False  True  True False  True]
        [33 42 23 99]
        ```

      + 选择两个数组中对应位置相同的元素

        ```python
        a = np.array([33,13,42,23,6,99])
        b = np.array([31,13,42,23,7,99])
        print(a[a == b])#[13 42 23 99]
        ```

      + 将大于100的元素设置为100

        ```python
        a = np.array([1,2,101,901,66])
        a[a>100] = 100
        print(a)#[  1   2 100 100  66]
        ```

### 数组扁平化

转换为一维数组

+ np.ravel/ravel

  返回的是原数组的视图

  ```python
  a = np.arange(10).reshape(2,5)
  print(a)#[[0 1 2 3 4]
   		  [5 6 7 8 9]]
  b = a.ravel()
  print(b)#[0 1 2 3 4 5 6 7 8 9]
  b[0]=100
  print(a)#[[100   1   2   3   4]
   		  [  5   6   7   8   9]]
  ```

+ flatten

  返回的是原数组的拷贝

  ```python
  a = np.arange(10).reshape(2,5)
  print(a)#[[0 1 2 3 4]
   		  [5 6 7 8 9]]
  b = a.flatten()
  print(b)#[0 1 2 3 4 5 6 7 8 9]
  b[0]=100
  print(a)#[[0 1 2 3 4]
   		  [5 6 7 8 9]]
  ```

  

### 数组的存储顺序

通过order参数指定

+ C-行优先存储（一行存满再存下一行）

+ F-列优先存储（一列存满再存下一列）

+ 在构建数组时过程

  + 首先按照指定的存储方式（C或F）来对数组进行扁平化处理
  + 然后再按照指定的存储方式进行插值

  ```python
  a = np.array([[1,2],[3,4]],order="C")
  print(a)
  b = np.array([[1,2],[3,4]],order="F")
  print(b)
  >>>
  [[1 2]
   [3 4]]
  [[1 2]
   [3 4]]
  ```

  ```python
  a = np.array([[1,2,3],[4,5,6]],order="C")
  print(a)
  
  b = a.reshape((3,2),order='F')#扁平化1,4,2,5,3,6
  print(b)
  >>>
  [[1 2 3]
   [4 5 6]]
  [[1 5]
   [4 3]
   [2 6]]
  ```

  

### 通用函数ufunc（universal function）

与python中提供的计算规则是相同的，只不过Python中是对标量，numpy中针对矢量（不需要循环）

+ abs/fabs  绝对值

  ```python
  a = np.array([-1.5,-4,5,-6])
  b = np.abs(a)
  print(b)#[1.5 4.  5.  6. ]
  ```

+ cell/floor 向上取整/向下取整

+ exp  e的次幂

+ log/log2/log10

+ modf 返回整数和小数部分-元组(小数数组,整数数组)

  ```
  a = np.array([-1.5,-4,5,-6])
  b = np.modf(a)
  print(b)
  >>>
  (array([-0.5, -0. ,  0. , -0. ]), array([-1., -4.,  5., -6.]))
  ```

+ sin/sinh/cos/cosh……

+ sqrt

### 统计函数

+ mean/sum 平均值/求和
+ max/min 最大值/最小值
+ argmax/argmin 最大值/最小值对应的索引
+ std/var 标准差/方差
+ cumsum/cumprod 累积和/累积乘积

```python
x = np.arange(1,11)
print(x)
print(x.mean(),np.mean(x))#平均值
print(x.sum(),np.sum(x))#求和
print(x.max(),x.min())#求最大值/最小值
print(x.argmax(),x.argmin())#求最大值/最小值对应的索引
print(x.std(),x.var())#求标准差/方差
print(np.cumsum(x),np.cumprod(x))#求累积和/累积乘积
>>>
[ 1  2  3  4  5  6  7  8  9 10]
5.5 5.5
55 55
10 1
9 0
2.8722813232690143 8.25
[ 1  3  6 10 15 21 28 36 45 55] [      1       2       6      24     120     720    5040   40320  362880
 3628800]
```

+ 轴（axis） 

  + 可以指定axis参数来改变统计的轴，轴的取值为0,1,2……其中0表示的是最高的维度，1表示次高的维度，以此类推。

  + 轴也可以为负值，表示倒数第n个维度，例如-1表示最后（低）一个维度。

  + 在二维数组中，0表示沿竖直方向（行）进行操作，1表示沿着水平方向（列）进行操作。

    ```python
    x = np.arange(1,11).reshape(2,5)
    print(x)
    print(x.mean(axis=0))
    print(x.mean(axis=1))
    >>>
    [[ 1  2  3  4  5]
     [ 6  7  8  9 10]]
    [3.5 4.5 5.5 6.5 7.5]
    [3. 8.]
    ```

  + 在多维数组中，轴相对复杂一些，可以认为，是沿着轴所指定的下标变化的方向进行操作，例如，如果轴是1，则根据第1个下标变化的方向进行操作。(理解为对应维度变化方向)
  
    ```python
    a = np.arange(24).reshape(2,3,4)
    print(a)
    >>>
    [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]
    
     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]
    print(a.mean(axis=0))#对应高维度2下对应坍塌
    >>>
    [[ 6.  7.  8.  9.]
     [10. 11. 12. 13.]
     [14. 15. 16. 17.]]
    print(a.mean(axis=1))#对应维度3在高维2下坍塌
    >>>
    [[ 4.  5.  6.  7.]
     [16. 17. 18. 19.]]
    print(a.mean(axis=2))#对应维度4在高维3、2下坍塌
    >>>
    [[ 1.5  5.5  9.5]
     [13.5 17.5 21.5]]
    ```
  
  + 如果不指定轴，则对所有元素进行统计（无论数组是几维的）
  
  

### 随机函数

+ np.random.rand(d1,d2,…,…)

  产生0-1之间的随机（伪随机）浮点值，包括0，不包括1，可指定维度

  ```python
  np.random.rand()
  >>>0.44233543242736795
  np.random.rand(2,3)
  >>>
  array([[0.19279456, 0.33962678, 0.99085615],
         [0.87212213, 0.48307793, 0.41183068]])
  ```

+ np.random.random()

  与rand方法功能相同，维度通过元组指定

  ```python
  np.random.random((2,3))
  ```

+ np.random.randn(d1,d2,…,…)

  产生标准正态分布的随机值（均值为0，标准差为1）

+ np.random.normal(size=(维度),loc=均值,scale=标准差)

  产生标准正态分布的随机值，可自定义均值及标准差（默认标准正态分布）

+ np.random.randint(low，high=None,size=(维度))

  产生指定范围内的随机整数，包括起始点，不包括终止点

  ```python
  np.random.randint(2,9,(2,3))
  >>>
  array([[8, 8, 2],
         [7, 7, 3]])
  ```

+ np.random.seed()

  播种种子，相同的种子一定会产生相同的随机序列（为了产生相同的随机序列）

+ np.random.shuffle(x)

  对参数序列进行洗牌操作（影响原数组）

+ np.random.uniform(low=0.0, high=1.0, size=None)

  产生在指定范围内的随机小数值（包含起始点，不包含终止点）



### 连接与拆分函数

+ 连接

  + concatenate((a1, a2, ...), axis=0, out=None)

    合并两个或多个数组，axis指定合并的方向

    + 二维（0-纵向/1-横向）

      ```python
      x = np.arange(1,10).reshape(3,3)
      y = np.arange(10,19).reshape(3,3)
      print(x)
      print(y)
      >>>
      [[1 2 3]
       [4 5 6]
       [7 8 9]]
      [[10 11 12]
       [13 14 15]
       [16 17 18]]
       
       np.concatenate((x,y),axis=0)
       >>>
       array([[ 1,  2,  3],
             [ 4,  5,  6],
             [ 7,  8,  9],
             [10, 11, 12],
             [13, 14, 15],
             [16, 17, 18]])
      
      np.concatenate((x,y),axis=1)
      >>>
      array([[ 1,  2,  3, 10, 11, 12],
             [ 4,  5,  6, 13, 14, 15],
             [ 7,  8,  9, 16, 17, 18]])
      ```

  + np.vstack((x,y))

    按照竖直方向进行堆叠，相当于concatenate中axis为0

  + np.hstack((x,y))

    按照水平方向进行堆叠，相当于concatenate中axis为1

+ 拆分

  + np.split(ary, indices_or_sections, axis=0)

    +  indices_or_sections-指定拆分数量

      + 整数-均分（不能会报错）

      + 列表-列表中每个元素指定拆分的具体位置（索引）

        例如，指定拆分列表参数[a,b,c,d],则按照：

        [:a] [a:b] [b:c] [c:d]进行拆分

        ```python
        a = np.array([0,1,2,3,4,5])
        np.split(a,[2,4,5],axis=0)
        >>>
        [array([0, 1]), array([2, 3]), array([4]), array([5])]
        ```

    + axis=0，默认按竖直方向进行拆分（拆成若干行）

    + axis=1，按照水平方向进行拆分（若干列）

    + 返回值为列表

### 其他函数

+ np.any/np.all

  any任意一个元素为True，则结果为True，否则为False

  all所有元素为True，则结果为True，否则为False

  ```python
  a = np.array([0,1,2,3,4,5])
  print(np.any(a))#True
  print(np.all(a))#False
  ```

+ transpose/T 返回数组的转置(shape倒序)

  + 对于T属性，或者是无参的transpose方法，就是将轴的顺序进行颠倒
  + 如果需要进行其他的交换方式，可以使用含有参数的transpose指定
    + 规则：用以前的1轴充当现在的0轴，用以前的0轴，充当现在的1轴，用以前的2轴，充当现在的2轴

  ```python
  a = np.array([[1,2],[3,4],[5,6]])
  print(a)
  print(a.T)
  print(a.transpose())
  >>>
  [[1 2]
   [3 4]
   [5 6]]
  [[1 3 5]
   [2 4 6]]
  [[1 3 5]
   [2 4 6]]
  ```

+ swapaxes

  将参数指定的两个轴进行交换，其他轴不变（参数的顺序不重要）

  ```python
  a = np.array([[1,2],[3,4]])
  print(a)
  print(a.swapaxes(1,0))
  >>>
  [[1 2]
   [3 4]]
  [[1 3]
   [2 4]]
  ```

+ dot(@) 向量的乘法

  + 当其中一个操作数是数组，而另一个操作数是标量。此时会将标量进行广播，然后对位相乘（相当于*）

    ```python
    a = np.array([[1,2],[3,4]])
    b = 10
    print(np.dot(a,b))
    >>>
    [[10 20]
     [30 40]]
    ```

  + 当两个操作数都是一维数组时，进行对位相乘，然后相加，得到一个结果

    ```python
    a = np.array([1,2,3])
    b = np.array([3,2,1])
    print(np.dot(a,b))#10
    ```

  + 当两个数组都是二维数组时，执行属性上的矩阵点积运算（此时可以使用@符号来进行点积运算）-即横乘纵相加

    ```python
    a = np.array([[1,2],[3,4]])
    b = np.array([[5,6],[7,8]])
    print(a)
    print(b)
    print(np.dot(a,b))
    #print(a@b)
    >>>
    [[1 2]
     [3 4]]
    [[5 6]
     [7 8]]
    [[19 22]
     [43 50]]
    ```

  + 当其中一个数组是多维矩阵，而另一个操作数的一维矩阵时，此时，会使用左侧（多维）的最后一维与右侧（一维）进行对位相乘再相加的运算（此时要保证左侧数组的最低维与右侧数组的长度相同）

    ```python
    a = np.arange(24).reshape(2,3,4)
    b = np.array([1,2,3,4])
    print(a)
    print(b)
    print(np.dot(a,b))
    >>>
    [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]
    
     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]
    [1 2 3 4]
    [[ 20  60 100]
     [140 180 220]]
    ```

  + 当两个操作数都是多维（不都是二维）时，会使用左侧操作数的最后一维，与右侧操作数的倒数第二维进行对位相乘再相加的运算（此时要保证左侧数组的最低维与右侧数组的倒数第二维长度相同）

    ```python
    a = np.arange(12).reshape(2,3,2)
    b = np.arange(4).reshape(2,2)
    print(a)
    print(b)
    print(np.dot(a,b))
    >>>
    [[[ 0  1]
      [ 2  3]
      [ 4  5]]
    
     [[ 6  7]
      [ 8  9]
      [10 11]]]
    [[0 1]
     [2 3]]
    [[[ 2  3]
      [ 6 11]
      [10 19]]
    
     [[14 27]
      [18 35]
      [22 43]]]
    ```

+ sort/np.sort 排序

  + np.sort() 不改变视图

    ```python
    a = np.array([5,-2,4,-9,8])
    print(np.sort(a))#[-9 -2  4  5  8]
    print(a)#[ 5 -2  4 -9  8]
    ```

  + sort 改变原视图

    ```python
    a = np.array([5,-2,4,-9,8])
    a.sort()
    print(a)#[-9 -2  4  5  8]
    ```

+ unique 去除重复元素并返回排序之后的结果

  ```python
  a = np.array([1,2,3,-2,2,9])
  print(np.unique(a))#[-2  1  2  3  9]
  ```

+ np.where 类似三元运算

  第一个参数为条件，如果条件为True，则返回第2个参数，否则返回第三个参数

  ```python
  a = np.array([2,3,4,8,9])
  b = np.array([4,2,-1,10,20])
  print(np.where(a>b,a,b))
  ```

+ np.save/np.load

  + np.save(file, arr, allow_pickle=True, fix_imports=True)以二进制形式保存ndarray数组，如果没有指定扩展名，则补充.npy作为扩展名

+ np.savetxt/np.loadtxt

  + np.savetxt以文本的形式保存ndarray数组（只允许一、二维数组）

    ```python
    np.savetxt(
        fname,
        X,
        fmt='%.18e',#指定格式
        delimiter=' ',
        newline='\n',#换行
        header='',#头标记
        footer='',#尾标记
        comments='# ',#标记符
        encoding=None,
    )
    ```

  + np.loadtxt 读取时可指定数据类型