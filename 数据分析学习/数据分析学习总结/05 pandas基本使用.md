## pandas安装与使用

+ 安装 

  ```
  pip install pandas
  ```

+ 引入

  ```
  import pandas as pd
  ```

## 两个常用数据类型

pandas提供两个常用的数据类型：

- Series
- DataFrame

## Series类型

Series类型类似于Numpy的一维数组对象，可以将该类型看做是一组数据与数据相关的标签（索引）联合而构成（带有标签的一维数组对象）。

+ 关于Series类型，我们可以认为是一组数据，每个数据带有一个标签。（可以简单的看成是一个带有标签的ndarray数组类型）
+ Series使用类似字典的方式，进行存储。其中，标签就是字典的key，数据就是字典的value。
+ Series只支持一维的数据结构。

### 创建方式

Series常用的创建（初始化）方式：

- 列表等可迭代对象（可通过index直接指定索引）

  ```python
  a = pd.Series([1,2,3])
  print(type(a))#<class 'pandas.core.series.Series'>
  print(a[0])#1
  #a = pd.Series(range(10))
  ```

- ndarray数组对象

  ```
  a = pd.Series(np.array([10,20,30]))
  ```

- 字典对象

  ```python
  a = pd.Series({'a':10,"b":20,"c":30})
  a
  >>>
  a    10
  b    20
  c    30
  dtype: int64
  ```

- 标量

  ```python
  a = pd.Series(100,index=(0,1,2))
  a
  >>>
  0    100
  1    100
  2    100
  dtype: int64
  ```

  

### 相关属性

- index

  - 可以通过index属性设置Series对象的标签。

    ```python
    a = pd.Series([1,2,3],index=(8,9,10))
    a
    >>>>
    8     1
    9     2
    10    3
    dtype: int64
    ```

  - 如果没有显式指定，则会自动生成0,1,2依次递增的标签。

    ```python
    a.index
    >>>
    Int64Index([8, 9, 10], dtype='int64')
    #RangeIndex(start=0, stop=3, step=1)-默认
    ```

  - 可通过属性进行修改

    ```python
    a = pd.Series([1,2,3])
    a.index = ['a','b','c']
    a.index
    ```

  - 我们也可以自己创建一个Index对象，传入给index参数（创建Series时）。

    ```python
    index = pd.Index([100,200,300])
    a = pd.Series([1,2,3],index=index)
    a
    >>>
    100    1
    200    2
    300    3
    dtype: int64
    ```

  - 创建Index对象的好处

    - 当多个Series都需要相同的index时，我们就可以把创建好的Index对象指派给每一个Series。
    - 不需要每个Series都单独去指定一个列表。
    - 在索引进行修改时，我们只需要修改Index对象，对于每个Series，不需要进行改动。

- values

  - values 类似与字典中的values方法。（但是，这里是属性）。返回Series中关联的数据。

  - 值为ndarry数组类型

    ```python
    a = pd.Series([1,2,3])
    print(a.values,type(a.values))
    #[1 2 3] <class 'numpy.ndarray'>
    ```

- shape

  - 返回Series数据的形状。

    ```python
    a.shape#(3,)
    ```

- size

  - 返回Series数据的个数。

- dtype

  - 返回Series数据的类型。

- Series与Series的index（标签对象）都具有name属性。

  - Series的name属性

    - 可以通过创建Series时，指定name参数来设置。

      ```python
      a = pd.Series([1,2,3],index=[5,7,7],name='Series属性')
      print(a.name)#Series属性
      ```

    - Series的name属性可以在输出Series对象时，能够体现。但是，其作用不仅仅只体现在输出中。

  - index的name属性

    - Series的Index属性（依然是一个对象）的name属性，可以在创建Index对象时指定。

      ```python
      index = pd.Index([1,2,3],name='Index属性')
      a = pd.Series([1,2,3],index=index,name='Series属性')
      print(index.name)#Index属性
      print(a.name)#(a.name)
      print(a.index.name)#Index属性
      print(a)
      >>>
      Index属性
      1    1
      2    2
      3    3
      Name: Series属性, dtype: int64
      ```

    - Index对象的name属性，也可以在创建Index对象之后进行设置（修改）

- head与tail

  - 最多显示前n/后n个数据。如果没有给定参数，则参数值默为5。

    ```python
    a = pd.Series(range(1,8))
    print(a.head(2))
    print(a.tail(2))
    ----------------
    0    1
    1    2
    dtype: int64
    5    6
    6    7
    dtype: int64
    ```

### Series相关操作

Series在操作上，与Numpy数据具有如下的相似性：

- 支持广播与矢量化运算。

  - 广播

    ```python
    a = pd.Series([1,2,3])
    print(a+1)
    >>>
    0    2
    1    3
    2    4
    dtype: int64
    ```

  - 矢量化运算(根据索引对位计算)

    ```python
    a = pd.Series([1,2,3])
    b = pd.Series([1,2,3],index=[1,2,3])
    print(a+b)#a.add(b)
    >>>
    0    NaN
    1    3.0
    2    5.0
    3    NaN
    dtype: float64
    ```

  - Series提供了用于计算的方法，例如add，multiply等。方法没有运算符简便，但是，方法可以提供更多的行为。可以指定fill_value参数，当索引无法匹配时，使用fill_value进行填充。

    ```python
    a = pd.Series([1,2,3])
    b = pd.Series([1,2,3],index=[1,2,3])
    print(a.add(b,fill_value=10))#补充NaN部分数据
    >>>
    0    11.0
    1     3.0
    2     5.0
    3    13.0
    dtype: float64
    ```

  - 对比

    - Series也能进行标量或矢量化运算。但是,Series的计算规则与ndarray是不太相同的。
    - 对于ndarray，是进行对位的计算（根据元素的位置进行计算），对于Series，会根据索引进行对齐计算。如果索引无法进行匹配，则会产生空值。（NaN）

  - 我们可以通过pandas或Series的isnull与notnull来判断数据是否缺失。

    - isnull 空返回True
    - notnull 空返回False

    ```
    a = pd.Series([1,float("NaN"),None,np.nan])
    print(a.notnull())
    >>>
    0     True
    1    False
    2    False
    3    False
    dtype: bool
    ```

  - Numpy的一些函数，也适用于Series类型，例如，np.mean，np.sum等

    - ndarray数组与Series在计算时，对空值的处理，不太相同。

      - 对于ndarray数组，会产生空值。
      - 对于Series，会忽略空值。

      ```python
      a = pd.Series([1,2,3,4,np.NaN])
      b = np.array([1,2,3,4,np.NaN])
      print(np.mean(a))#2.5
      print(np.max(a))#4.0
      print(np.mean(b))#nan
      print(np.max(b))#nan
      ```

- 支持索引与切片，返回原数组数据的视图。（不建议使用）

  - a[key]
  - a[0:1]

- 支持整数数组与布尔数组提取元素。(拿到的是Series的拷贝，非视图)

  - 根据标签数组提取

    ```python
    a = pd.Series([1,2,3,4])
    a[[0,2]]
    >>>
    0    1
    2    3
    dtype: int64
    ```

  - 根据布尔数组提取

    ```python
    a = pd.Series([1,2,3,4])
    a[a>2]
    >>>
    2    3
    3    4
    dtype: int64
    ```

- ndarray与Series都可以通过索引来访问元素，但是，二者是有区别的。

  - 对于ndarray，类似于Python中的列表的形式，是基于位置进行的访问。在创建对象后，每个元素的位置就固定了，我们不能自行去改变元素的索引。
  - 对于Series，类似于Python中的字典的形式，是基于key值访问元素的。我们可以自行去改变（指定）key值。

### 索引

#### 标签索引与位置索引

+ 标签索引

  在创建Series时，我们通过index指定的标签（索引），就是标签索引。

+ 位置索引

  每个元素在创建时，都有对应的位置，该位置的顺序就是位置索引。(类似与ndarray数组的索引)

  ```python
  a = pd.Series([1,2,3],index=['a','b','c'])
  print(a['a'])#通过标签索引1
  print(a[0])#通过位置索引1
  ```

+ 当Series标签是数值类型时，位置索引会失效。

+ 当Series标签不是数值类型时，通过Series对象**索引**访问元素，索引既可以是标签索引，也可以是位置索引。这会造成极大的混淆。因此，不建议使用Series对象[索引]的方式访问元素。我们可以通过：

  + loc 仅通过标签索引访问。（不能通过位置访问元素）

  + iloc 仅通过位置索引访问。（不能通过标签访问元素）

    ```python
    a = pd.Series([1,2,3],index=['a','b','c'])
    print(a.loc['a'])#通过标签索引1
    print(a.iloc[0])#通过位置索引1
    ```

  + 不建议！老版本中，会使用ix访问元素。我们不要再去使用了。ix的意思是先通过标签索引寻找元素，如果不存在，再通过位置索引寻找元素。

### 切片对比

+ 对于Series切片，标签索引与位置索引是存在区别的。

  + 对于位置索引切片，包含起始点，不包含终止点（这点与ndarray的切片方式相同）。

  + 对于标签索引切片，包含起始点，也包含终止点。

    ```python
    a = pd.Series([1,2,3],index=['a','b','c'])
    print(a.loc['a':'c'])
    ------------
    a    1
    b    2
    c    3
    dtype: int64
    ```

    

### Series的CRUD

Series索引-数值CRUD操作（因为Series内部也是基于Mapping映射的形式，因此，其与字典的特征类似。）：

- 获取值

  ```python
  a =pd.Series([1,2,3],index=list('abc'))
  print(a.loc['a'])
  ```

- 修改值

  ```python
  a =pd.Series([1,2,3],index=list('abc'))
  a.loc['a'] = 100
  ```

- 增加索引-值

  ```python
  a =pd.Series([1,2,3],index=list('abc'))
  a.loc['d'] = 100#键不存在就是增加
  ```

- 删除索引-值

  - 方式一:返回一个新的对象

    ```python
    a =pd.Series([1,2,3],index=list('abc'))
    b = a.drop('a')#b = a.drop(['a','b'])
    print(b)
    ---------
    b    2
    c    3
    dtype: int64
    ```

  - 方式二：原地修改

    + 如果需要就地修改对象，而不是创建一个新的对象，可以将inplace参数设置为True。（默认为False）

      ```python
      a =pd.Series([1,2,3],index=list('abc'))
      a.drop('a',inplace=True)#返回值为None
      print(a)
      ------
      b    2
      c    3
      dtype: int64
      ```

    + 所有API中，只要含有inplace，该参数的默认值一律为False。

    + 如果方法（函数）含有inplace，并且，我们将inplace参数值指定为True，则该方法（函数）返回值为None。