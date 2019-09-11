# day05学习笔记

## 字典

+ 定义

  + 可变数据类型
  + 无序，显示时按照定义的顺序显示（python3.6版本以上）
  + Python中的数据类型之一(唯一一种 键 值 对的数据)
  + `dic = {"键":"值"}`

+ 作用

  + 存储大量的数据 （比列表存储的数据还要大）
  + 将数据和数据之间进行关联（键：值）
  + 查询方便且查询速度快

+ 哈希

  ​        一个对象能被称为 hashable ， 它必须有个 hash 值，这个值在整个生命周期都不会变化，而且必须可以进行相等比较，所以一个对象可哈希，它必须实现__hash__() 与 __eq__() 方法。

  ​		对于 Python 的内建类型来说，只要是创建之后无法修改的(immutable)类型都是 hashable 如字符串，可变动的都是 unhashable的比如：列表、字典、集合，**他们在改变值的同时却没有改变id,无法由地址定位值的唯一性,因而无法哈希**。我们自定义的类的实例对象默认也是可哈希的（hashable），而hash值也就是它们的id()。

  ​		简单总结：可变数据类型不可哈希，不可变数据类型可哈希。

+ 字典的键

  + 不可变数据类型（可哈希）
  + 唯一（重名则覆盖）

+ 字典的值：任意

+ 创建字典

  + `dict()`构造函数

    ```
    dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    ```

  + 字典推导式

    ```
    >>> {x: x**2 for x in (2, 4, 6)}
    {2: 4, 4: 16, 6: 36}
    ```

  + 直接通过关键字参数来指定键值对

    ```
    >>> dict(sape=4139, guido=4127, jack=4098)
    {'sape': 4139, 'guido': 4127, 'jack': 4098}
    ```

+ 字典的增

  + 直接增加 `dic["键"] = "值"`

    ```
    dic = {"key":1}
    dic["sss"] = 89
    dic[666] = "sss"
    print(dic)
    ```

  + `setdefault("键",值)`    设定字典的默认值（无加有不变）

    参数1：key 参数2：value  直接对字典增加，有返回值（返回默认值）

    逻辑：先通过键去字典中查找，返回值是None，才会将键和值添加到字典中

    ```
    dic = {"key":1,"key3":None}
    dic.setdefault("meet",18) #不存在，增加，返回值为18
    dic.setdefault("key1") #不存在，增加，返回值None
    dic.setdefault("key",18) #存在，不变，返回值1
    dic.setdefault("key3",18) #存在，不变，返回值None
    print(dic)
    ```

+ 字典的删除

  + clear（） 清空字典

    ```
    dic = {"key":1,"dd":"sss"}
    dic.clear()
    print(dic)
    ```

  + pop() 通过键删除，返回被删除的键对应的值

    ```
    dic = {"key":1,"dd":"sss"}
    print(dic.pop("key") ) #返回值为1
    print(dic)
    ```

  + popitem() 随机删除，python3默认删除最后一个，返回被删除的键值对（元组）

    ```
    dic = {"key":1,"dd":"sss"}
    print(dic.popitem() ) #返回值为('dd', 'sss')
    print(dic)
    ```

  + del 删除字典或通过删除键删除

    ```
    dic = {"key":1,"dd":"sss"}
    del dic #删除整个字典
    del dic["dd"]
    print(dic)
    ```

+ 字典的修改

  + 直接修改 `dic["键"] = "值"`  (暴力修改：有改无加)

    ```
    dic = {"key":1,"dd":"sss"}
    dic["dd"] = "666" #修改
    dic["ss"] = "666" #增加
    print(dic)
    ```

  + update(字典)  有改无加

    ```
    dic = {"key":1,"dd":"sss"}
    dic.update({"key":2,"meet":"sss"}) #相当于字典合并
    print(dic)
    ```

+ 字典的查询

  + `setdefault("键")`    通过返回值查询,没有返回None

    ```
    dic = {"key":1,"dd":"sss"}
    print(dic.setdefault("key")) #返回 1
    print(dic.setdefault("key1")) #返回 None
    ```

  + 通过键直接查找值

    ```
    dic = {"key":1,"dd":"sss"}
    print(dic["dd"]) #通过键查找值，暴力，键存在时返回对应的值
    print(dic["cdd"]) #通过键查找值，键不存在时报错
    ```

  + get()  通过键查找值

    键存在时返回对应的值，键不存在时返回None;

    可自定义键不存在时的返回值

    ```
    dic = {"key":1,"dd":"sss"}
    print(dic.get("dd")) #返回"sss"
    print(dic.get("cdd")) #键不存在,返回None
    print(dic.get("cdd","找不到")) #键不存在,返回自定义内容
    ```

  + `keys()`  获取字典的键,返回键类型，可迭代(不支持索引)

    ```
    print(dic.keys())  #高仿列表，可迭代,不支持索引
    print(list(dic.keys())[0]) #转为列表后可索引
    ```

  + `values()` 获取字典的值,返回值类型，可迭代(不支持索引)

    ```
    print(dic.values())
    ```

  + `items()` 获取字典的键和值,返回键值对类型，可迭代(不支持索引)

    迭代结果为元组类型

+ 字典的嵌套：通过键找值

## 解构的概念

+ 规则

  + 把线性结构（可迭代对象）的元素解开，并顺序的赋给其他变量

  + 左边接纳的要与右边解开的个数一致

+ 举例

  ```
  a,b,c = "你好啊" #字符串
  print(a)
  print(b)
  ```

  ```
  a,b,c = [1,2,3] #列表
  print(a)
  print(b)
  ```

  ```
  a,b,c = {"key1":1,"key2":2,"key3":3} #字典
  print(a)
  print(b)
  ```

  ```
  a,b,c = 10,20  #左右个数不一致时报错
  print(a)
  print(b)
  ```

+ 解构对象超限时：使用*变量名接受多余的全部数据（聚合）组成一个列表（不能单独使用）

  ```
  a,b,*c = [1,2,3,4,5,6]  #聚合
  print(a,b,c)
  ```

+ 应用于字典

  ```
  dic = {"key1":1,"key2":2,"key3":3}
  for k,v in dic.items():  # for i in dic.items():  k,v = i  对元组解构
      print(k,v)
  ```

+ 丢弃变量  _

  _仅会取到最后一次的赋值

  