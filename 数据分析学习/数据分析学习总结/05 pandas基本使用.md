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

## DataFrame类型

+ DataFrame是一个多维数据类型。
+ 因为通常使用二维数据，因此，我们可以将DataFrame理解成类似excel的表格型数据，由多列组成，每个列的类型可以不同。
+ 因为DataFrame是多维数据类型，因此，DataFrame既有行索引，也有列索引。

### 创建方式

我们可以使用如下的方式创建（初始化）DataFrame类型的对象（常用）：

- 二维数组结构（列表,ndarray数组，DataFrame等）类型。

  - 使用display直接输出到控制台上（可多个）
    - display与print类似，不同的是，在jupyter中部分类型输出会有美化的效果
    - display是Ipython所扩展的函数，Python中没有
    - display方法输出的结果与直接对对象进行求值，展示在交互式控制台上的结果是相同的（Out中展示的内容），但是，直接求值的方式，只能显示最后一个结果。

  ```python
  a = pd.DataFrame([[11,22,33],[44,55,66]])
  print(a)
  a
  ------
      0   1   2
  0  11  22  33
  1  44  55  66
  ```

  ![image-20191231093528905](05 pandas基本使用.assets/image-20191231093528905.png)

- 字典类型，key为列名，value为一维数组结构（列表，ndarray数组,Series等）。

  ```python
  a = pd.DataFrame({'a':[1,2,3],'b':[3.1,4.2,5.3],'c':['b','d','e']})#标量可广播对齐
  print(a)
  -----------
     a    b  c
  0  1  3.1  b
  1  2  4.2  d
  2  3  5.3  e
  ```

  ![image-20191231103346139](05 pandas基本使用.assets/image-20191231103346139.png)

  - 字典的每组键值对表示DataFrame的一个列。键值对的key用来指定列索引（列标签）
  - 键值对的value用来指定该列的值。

- 如果没有显式指定行与列索引，则会自动生成以0开始的整数值索引。我们可以在创建DataFrame对象时，通过index与columns参数指定。

  ```python
  a = pd.DataFrame([[1,2,3],[4,5,6]],index=['row1','row2'],columns=['col1','col2','col3'])
  print(a)
  ------
        col1  col2  col3
  row1     1     2     3
  row2     4     5     6
  ```

  - 可以在创建DataFrame对象之后，通过修改DataFrame的index(columns)属性来指定行（列）索引。

    ```python
    a = pd.DataFrame([[1,2,3],[4,5,6]],index=['row1','row2'],columns=['col1','col2','col3'])
    a.index=['修正1','修正2']
    a.columns=['rcol1','rcol2','rcol3']
    print(a)
    -----------
         rcol1  rcol2  rcol3
    修正1      1      2      3
    修正2      4      5      6
    ```

- 可以通过head，tail访问前 / 后N行记录（数据）。

  ```python
  a = pd.DataFrame(np.random.random((20,100)))
  a.head()#默认5条
  a.tail()
  ```

- 随机抽样sample()-默认取一条

  ```python
  a = pd.DataFrame(np.random.random((20,100)))
  a.sample(2)
  ```

  - sample()默认为不放回抽样（抽样的数量不能大于样本的数量）

  - 将replace参数指定为True（放回抽样）。

    ```python
    a = pd.DataFrame(np.random.random((20,100)))
    a.sample(21,replace=True)
    ```

  - random_state参数指定随机种子（来重现抽样的序列）

    ```python
    a = pd.DataFrame(np.random.random((20,100)))
    a.sample(2,replace=True,random_state=1)
    ```

    

### 相关属性

- index

  DataFrame的行索引

  ```python
  a = pd.DataFrame(np.random.random((5,3)))
  print(a.index)
  ------
  RangeIndex(start=0, stop=5, step=1)
  ```

- columns

  DataFrame的列索引

- values

  DataFrame对象所关联的值。（二维的ndarray数组）

  ```python
  a = pd.DataFrame(np.random.random((5,3)))
  print(a.values)
  -------------
  [[0.64019771 0.13014219 0.65840082]
   [0.53474793 0.640329   0.98205557]
   [0.54784337 0.92901306 0.93270652]
   [0.35559662 0.80455353 0.70681247]
   [0.58433726 0.0772441  0.54943972]]
  ```

- shape

  DataFrame的形状(即values的形状)

- ndim

  DataFrame的维度---2

- dtypes

  DataFrame与二维的数组ndarray在数据类型上不同

  - 对于ndarray，会根据数组中所有元素的类型，来决定一种兼容的类型。

  - 对于DataFrame，类似于数据库中的二维表（或Excel二维表），每一列都有单独的类型。列与列之间不受干扰。

  - dtypes 返回DataFrame中每一列的类型。(返回的数据类型是Series类型)

    ```python
    a = pd.DataFrame({'a':[1,2,3],'b':[3.1,4.2,5.3],'c':['b','d','e']})
    print(a.dtypes)
    print(a.dtypes['a'])#int64
    ---------------
    a      int64
    b    float64
    c     object
    dtype: object
    ```

- 注意事项

  - 可以通过index访问行索引，columns访问列索引，values访问数据，其中index与columns也可以进行设置（修改）。

  - 可以为DataFrame的index与columns属性指定name属性值。

    ```python
    a = pd.DataFrame({'a':[1,2,3],'b':[3.1,4.2,5.3],'c':['b','d','e']})
    a.index.name = '行索引名称'
    a.columns.name = '列索引名称'
    print(a)
    --------------
    列索引名称  a    b  c
    行索引名称           
    0      1  3.1  b
    1      2  4.2  d
    2      3  5.3  e
    ```

    

  - DataFrame的数据不能超过二维。

### DataFrame相关操作

假设df为DataFrame类型的对象。

```
df = pd.DataFrame({'a':[1,2,3],'b':[3.1,4.2,5.3],'c':['b','d','e']})
```

#### 列操作

- 获取DataFrame的某列

  - df[列索引]

    ```
    df['a']-----为Series类型
    ```

  - df.列索引---df.a

  - 建议使用第一种方式，因为第一种方式局限性更少，对于第二种方式，要求标签名必须是Python中合法的标示符才可以。

- 增加（修改）列：df[列索引] = 列数据(标量会广播) `df['d']=[5,6,7]`

  - 通常，不会人为的去指定数据增加或修改，而是都是通过现有的数据计算产生的。

    ```python
    df = pd.DataFrame({"苹果":[1, 2, 3], "香蕉":[2.0, 4, 5], "葡萄":[20, 3, 4]}, index=["1月", "2月", "3月"])
    df['总和']=df.sum(axis=1)
    print(df)
    -----------
        苹果   香蕉  葡萄    总和
    1月   1  2.0  20  23.0
    2月   2  4.0   3   9.0
    3月   3  5.0   4  12.0
    ```

- 删除列

  - del df[列索引]

  - df.pop(列索引)----原地修改，返回被删除的列

  - df.drop(列索引或数组)----返回删除后的拷贝

    - axis-0-删除行

    - axis-1-删除列

      ```python
      df.drop('苹果',axis=1)
      df.drop(['苹果','香蕉'],axis=1)#axis='columns'
      ```

    - inplace指定为True则原地修改

#### 行操作

- 获取行

  - df.loc 根据标签进行索引。

    - DataFrame列标签→查询数据Series行标签
    - DataFrame行标签name属性→查询数据Series行标签name属性

    ```python
    df = pd.DataFrame({"苹果":[1, 2, 3], "香蕉":[2.0, 4, 5], "葡萄":[20, 3, 4]}, index=["1月", "2月", "3月"])
    df.loc['1月']
    ------------
    苹果     1.0
    香蕉     2.0
    葡萄    20.0
    Name: 1月, dtype: float64
    ```

  - df.iloc 根据位置进行索引。`df.iloc[0]`

  - df.ix 混合索引。先根据标签索引，如果没有找到，则根据位置进行索引（前提是标签不是数值类型）。【已不建议使用】

- 增加行

  - append(others) ------返回新数据

    `other : DataFrame or Series/dict-like object, or list of these The data to append.`

    + append加入Series时，Series对象需要具有name属性(同时指定对应index)。

      ```python
      row = pd.Series([50,60,70],name='4月',index=['苹果','葡萄','香蕉'])
      df.append(row)
      ```

    + 指定参数-ignore_index=True，会重新生成从0开始，依次增1的索引（默认形式的索引）。此时，Series可以没有name属性。这样可以避免因为拼接产生重复的标签。

      ```python
      row = pd.Series([50,60,70],name='4月',index=['苹果','葡萄','香蕉'])
      df.append(row,ignore_index=True)
      --------------
      苹果	香蕉	葡萄
      0	1	2.0	20
      1	2	4.0	3
      2	3	5.0	4
      3	50	70.0	60
      ```

    + append 加入另外一个DataFrame(加多行)。

      ```python
      rows = pd.DataFrame(np.random.random((3,3)),columns=['苹果','葡萄','香蕉'],index=["1月", "2月", "3月"])
      df.append(rows,ignore_index=True)
      ```

  - pd.concat

    在增加多行的时候，建议大家使用concat。【concat在性能方面会比append好些】

    - axis-0-按行拼

      ```
      rows = pd.DataFrame(np.random.random((3,3)),columns=['苹果','葡萄','香蕉'],index=["1月", "2月", "3月"])
      pd.concat((df,rows),axis=0,ignore_index=True,sort=False)
      ```

    - axis-1-按列拼

      ```python
      pd.concat((df,rows),axis=1,ignore_index=False,sort=False)
      ```

- 删除行（操作同删除列）

  - df.drop(行索引或数组)

#### 行列混合操作：

- 先获取行，再获取列。

  ```python
  df = pd.DataFrame({"苹果":[1, 2, 3], "香蕉":[2.0, 4, 5], "葡萄":[20, 3, 4]}, index=["1月", "2月", "3月"])
  df.loc['1月'].loc['苹果']#df['苹果'].loc['1月']
  ```

- 先获取列，在获取行。

- 取多行多列

  ```python
  df[['苹果','葡萄']].loc[['1月','2月']]
  ```

- 注意获取行列时，数据的返回类型。

  - 索引---Series
  - 切片---DataFrame

- 注意点
  - 通过df[索引]访问是对列进行操作。

    索引**只支持**标签索引，不支持位置索引。因此，这样访问方式不会产生歧义。

  - 通过df[切片]访问是对行进行操作。【先按标签，然后按索引访问。如果标签是数值类型，则仅会按标签进行匹配。】

    切片既支持标签索引，也支持位置索引。故这样方式，行为容易混淆，**不建议**使用。

  - 通过布尔索引是对行进行操作。

    通过布尔数组提取元素，可以访问（返回）多个行。

    ```python
    df = pd.DataFrame({"苹果":[1, 2, 3], "香蕉":[2.0, 4, 5], "葡萄":[20, 3, 4]}, index=["1月", "2月", "3月"])
    df[[True,False,True]]
    ```

  - 通过数组索引是对列进行操作。

    通过标签数组提取元素，可以访问（返回）多个列。

### DataFrame结构

+ DataFrame的一行或一列，都是Series类型的对象。
+ 对于行来说，Series对象的name属性值就是行索引名称，其内部元素的值，就是对应的列索引名称。
+ 对于列来说，Series对象的name属性值就是列索引名称，其内部元素的值，就是对应的行索引名称。

### DataFrame运算

DataFrame的一行或一列都是Series类型的对象。因此，DataFrame可以近似看做是多行或多列Series构成的，Series对象支持的很多操作，对于DataFrame对象也同样适用，可以参考之前Series对象的操作。

- 转置--矩阵的转置

  ```python
  df = pd.DataFrame(np.arange(12).reshape(3,4))
  df.T
  ```

- DataFrame进行运算时，会根据行索引与列索引进行对齐。

  - 当索引无法匹配时，产生空值（NaN）。

    ```python
    df1 = pd.DataFrame(np.arange(12).reshape(3,4))
    df2 = pd.DataFrame(np.arange(12,24).reshape(3,4))
    print(df1+df2)
    ------------------
        0   1   2   3
    0  12  14  16  18
    1  20  22  24  26
    2  28  30  32  34
    ```

    ```python
    df1 = pd.DataFrame(np.arange(12).reshape(3,4))
    df2 = pd.DataFrame(np.arange(12,24).reshape(3,4),index=[0,1,3],columns=[0,1,2,4])
    print(df1+df2)
    -----------------
          0     1     2   3   4
    0  12.0  14.0  16.0 NaN NaN
    1  20.0  22.0  24.0 NaN NaN
    2   NaN   NaN   NaN NaN NaN
    3   NaN   NaN   NaN NaN NaN
    ```

  - 如果不想产生空值，可以使用DataFrame提供的运算函数来代替运算符计算，通过fill_value参数来指定填充值(只能补充缺失一项的情况)。

    ```python
    df1 = pd.DataFrame(np.arange(12).reshape(3,4))
    df2 = pd.DataFrame(np.arange(12,24).reshape(3,4),index=[0,1,3],columns=[0,1,2,4])
    print(df1.add(df2,fill_value=0))
    ------------
          0     1     2     3     4
    0  12.0  14.0  16.0   3.0  15.0
    1  20.0  22.0  24.0   7.0  19.0
    2   8.0   9.0  10.0  11.0   NaN
    3  20.0  21.0  22.0   NaN  23.0
    ```

- DataFrame与Series混合运算。

  - 默认Series索引匹配DataFrame的列索引，然后进行行广播。

    ```python
    df = pd.DataFrame(np.arange(12).reshape(3,4))
    a = pd.Series([100,200,300],index=[0,1,2])
    print(df + a)
    -----------------
           0      1      2   3
    0  100.0  201.0  302.0 NaN
    1  104.0  205.0  306.0 NaN
    2  108.0  209.0  310.0 NaN
    ```

  - 通过DataFrame对象的运算方法的axis参数，指定匹配方式（匹配行索引还是列索引）

    ```python
    df = pd.DataFrame(np.arange(12).reshape(3,4))
    a = pd.Series([100,200,300],index=[0,1,2])
    print(df.add(a,axis=0))#axis='index'
    -------------
         0    1    2    3
    0  100  101  102  103
    1  204  205  206  207
    2  308  309  310  311
    ```

    

### 排序

#### 索引排序

Series与DataFrame对象可以使用`sort_index`方法对索引进行排序(默认升序)。

+ DataFrame对象在排序时，还可以通过axis参数来指定轴（行索引-0还是列索引-1）。
+ 可以通过ascending参数指定升序还是降序。

```python
df = pd.DataFrame([[1,-5,3],[-5,2,4],[9,6,-3]],index=[-2,1,-3],columns=[-2,1,-3])
display(df)
print(df.sort_index(axis=1,ascending=False))
------------
     1  -2  -3
-2  -5   1   3
 1   2  -5   4
-3   6   9  -3
```

#### 值排序

Series与DataFrame对象可以使用`sort_values`方法对值进行排序。

+ axis=0,按某一列进行排序

  ```python
  df = pd.DataFrame([[1,-5,3],[-5,2,4],[9,6,-3]],index=[-2,1,-3],columns=[-2,1,-3])
  display(df)
  print(df.sort_values(-2,axis=0))
  --------------
      -2   1  -3
   1  -5   2   4
  -2   1  -5   3
  -3   9   6  -3
  ```

+ axis=1,按某一列进行排序

+ 指定inplace=True原地修改

### 索引对象

Series(DataFrame)的index或者DataFrame的columns就是一个索引对象。

- 索引对象可以向数组那样进行索引访问。

  ```
  df = pd.DataFrame([[1,2],[3,4]])
  print(df.index)#RangeIndex(start=0, stop=2, step=1)
  print(df.index[0])#0
  print(df.columns)#RangeIndex(start=0, stop=2, step=1)
  print(df.columns[1])#1
  ```

- 索引对象是不可修改的（可以换绑定）。

### 统计相关方法（参考数值中的使用--针对行列）

- mean / sum / count/median---均值/求和/计数/中位数

- max / min---最大值/最小值

- cumsum / cumprod---累积和/累积乘积

- argmax / argmin---最大值/最小值对应索引（Series，DataFrame）

- idxmax / idxmin---最大值/最小值对应索引（DataFrame）

  ```python
  df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
  a = pd.Series([1,2,3,5,6,4,6])
  print(a.idxmax())#4
  print(df.idxmax())
  -------------
  0    2
  1    2
  2    2
  dtype: int64
  ```

- var / std---方差/标准差

- corr / cov---相关系数（越大越贴近）/协方差

### 其他

- unique---去重但不会排序(与numpy中ndarray数组的方法行为不太一样)

  ```python
  a = pd.Series([1,2,3,3,2,10])
  a.unique()
  ------------
  array([ 1,  2,  3, 10], dtype=int64)
  ```

- value_counts

  返回Series中每个值出现的次数。

  + 默认降序排列
  + 可以通过指定ascending参数来指定升序排列。`ascending=True`

  ```python
  a = pd.Series([1,2,3,3,2,10])
  a.value_counts()
  --------------
  3     2
  2     2
  10    1
  1     1
  dtype: int64
  ```

  
