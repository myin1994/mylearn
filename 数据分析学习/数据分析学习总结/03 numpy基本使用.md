## numpy基本使用

### numpy引入

```python
import numpy as np
print(np.__version__)#查看版本信息
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
  
  ![image-20191223141219345](.\imag\image-20191223141219345.png)
  
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

    ![image-20191223144424916](.\imag\image-20191223144424916.png)

  + 数组在运算时，具有广播能力【可根据需要进行元素的扩展（内存对齐-对位运算），完成运算】

    + 广播可以发生在标量与矢量之间，也可以发生在矢量与矢量之间
    + 沿着行进行广播

    ![image-20191223143928148](.\imag\image-20191223143928148.png)

    ![image-20191223145400583](.\imag\image-20191223145400583.png)

    + 沿着列进行广播

    ![image-20191223145916403](.\imag\image-20191223145916403.png)

    + 广播并非在任何场景下都能进行，如果不能广播成相同的形状，就会出现错误

  + 数组底层使用C程序编写，运算速度快

  + 数组底层使用C中数组的存储方式（紧凑存储），节省内存空间

+ 应用对比

  + 时间

    + 创建（数组、列表）

      数组明显节省时间

      ![image-20191223164005359](.\imag\image-20191223164005359.png)

    + 计算

      ![image-20191223164241121](.\imag\image-20191223164241121.png)

  + 空间

    ![image-20191223165120602](.\imag\image-20191223165120602.png)