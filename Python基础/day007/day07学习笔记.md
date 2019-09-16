## 基础数据类型补充-方法（不常用）

### int

+ `bit_length()` 求数字二进制最大位数 

  ```
  a = 25 #11001
  print(a.bit_length())    #5
  ```

### str

+  `capitalize()` 首字母大写

  ```
  s = "alsx hahah"
  s1 = s.capitalize()  #首字母大写
  print(s1)  #Alsx hahah
  ```

+ `title()` 每个单词首字母大写（可以空格，逗号等字符分隔单词）

  ```
  s = "alsx hahah"
  s1 = s.title()
  print(s1)  #Alsx Hahah
  ```

+ `index(元素名 )`  通过元素查找索引，返回第一个查到的元素 的索引，查不到报错

  ```
  s = "alsx hahah"
  s1 = s.index("h")
  print(s1)  #5
  ```

+ `find(元素名)`  通过元素查找索引，查找不到时返回-1

+ `join(列表，元组)`  使用链接符将元组列表转换为字符串

+ `center(number)`  设置居中

  ```
  s1 = s.center(20)  #居中，一共20个
  print(s1)  #     alsx hahah     
  s1 = s.center(20,"-")  #居中，填充，一共20个,可用符号代替空格
  print(s1)  #-----alsx hahah-----
  ```

+ `format()`  格式化

  ```
  s = "alsx{}ha{}hah"
  s1 = s.format("11","222")  #按照位置格式化
  ```

  ```
  s = "alsx{1}ha{0}hah"
  s1 = s.format("11","222")  #按照索引格式化
  ```

  ```
  s = "alsx{a}ha{b}hah"
  s1 = s.format(b = "11",a = "222")  #按照关键字格式化
  ```

+ `swapcase()` 大小写互相转换

  ```
  s = "alsx haHah"
  s1 = s.swapcase()
  print(s1)  #ALSX HAhAH
  ```

+ `translate()`  按照自定义模式进行替换

  ```
  intab = "aeiou" #需要被替换的内容
  outtab = "12345" #目标替换内容
  trantab = str.maketrans(intab, outtab) #maketrans()构建特殊字典
  print(trantab)  #{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
  str1 = "this is string example....wow!!!"
  print(str1.translate(trantab)) #th3s 3s str3ng 2x1mpl2....w4w!!!
  ```

### list

+ `reverse()`  反向列表

  ```
  lst = [1,2,3,5,6,4]
  print(lst[::-1])  #新开辟一个列表
  lst.reverse()  #原地修改
  print(lst)
  ```

+ `sort()`  排序（默认升序）

  ```
  lst = [1,2,3,5,6,4]
  lst.sort()  #升序(reverse=False)
  lst.sort(reverse=True)  #降序
  print(lst)
  ```

+ 列表相加  lst1+lst2  新开辟空间

+ 列表乘数字

  列表和元组进行乘法时元素都是共用的（内部可变数据类型会同步变化）

  ```
  lst1 = [1,2,3,[4]]
  lst3 = lst1 * 3
  print(id(lst3[3]),id(lst3[7]))  #地址相同
  ```

  ```
  lst = [1,2,[]]
  lst1 = lst * 2
  lst[-1].append(8)
  print(lst1)  #[1, 2, [8], 1, 2, [8]]
  print(lst)  #[1, 2, [8]]
  ```

### tuple

```
tu = (10)  #int
tu = (10,) #tuple
tu = () #tuple
```

### dict

+ `fromkeys("abc",12)`  快速创建键值对

  参数一：键（可迭代数据类型）  参数二：值（共用）

  ```
  dic = {}.fromkeys("abc",12) #该方法仅借用一个字典，并不会修改原字典
  dic = dict.fromkeys("abc",12)
  print(dic) #{'a': 12, 'b': 12, 'c': 12}
  ```

  ```
  dic = dict.fromkeys("abc",[])
  dic["c"].append(1) #全部变化,共用可变数据类型的地址，同步变化
  dic["c"] = [67] #用新列表替换
  print(dic)
  ```

+ 定义字典

  ```
  dic = {}
  dic  = dict()
  dic = dict(k1 = 1,k2 = 2,k3 = 3)
  dic = dict(([1,2],[4,5],[6,7]))
  print(dic)
  ```

## 数据类型转换

| 数据类型转换 |    int    |    str     |    bool    |    list     |    tuple    |    dict     |    set     |
| :----------: | :-------: | :--------: | :--------: | :---------: | :---------: | :---------: | :--------: |
|     int      |           |  int(str)  |            |             |             |             |            |
|     str      | str(int)  |            | str(bool)  |  str(list)  | str(tuple)  |  str(dict)  |  str(set)  |
|     bool     | bool(int) | bool(str)  | bool(bool) | bool(list)  | bool(tuple) | bool(dict)  | bool(set)  |
|     list     |           | list(str)  |            |             | list(tuple) | list(dict)  | list(set)  |
|    tuple     |           | tuple(str) |            | tuple(list) |             | tuple(dict) | tuple(set) |
|     dict     |           |            |            |             |             |             |            |
|     set      |           |  set(str)  |            |  set(list)  | set(tuple)  |  set(dict)  |            |

**注：可迭代数据类型可相互转换**



bool的False-----只要为空就是False

```
print(bool(0))
print(bool())
print(bool(None))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))
```

## 循环删除的坑

+ 列表

  列表删除时会自动补位，使用range或复制一份

  ```
  lst = [11,22,33,44,55]
  for i in range(len(lst)):  #第一种
      lst.pop()
  print(lst)
  ```

  ```
  lst1 = lst.copy()  #第二种
  for i in lst1:
      lst.remove(i)
  print(lst)
  ```

+ 字典和集合

  字典和集合在循环（迭代）中不可删除键值对，但可修改键的值

  ```
  dic = {"key":1,"key2":2}
  for i in dic:   #报错
      del dic[i]
  print(dic)
  ```

  ```
  dic = {"key":1,"key2":2}
  dic1 = dic.copy()
  for i in dic1:
      del dic[i]
  print(dic) #{}
  ```

  ```
  s = {1,2,3,4,5,6}
  for i in list(s):
      s.remove(i)
  print(s)
  ```

  删除奇数索引元素

  ```
  lst = [11,22,33,44,55,66]
  
  tu = tuple(lst)
  for i in range(len(tu)):
      if i % 2 != 0:
          lst.remove(tu[i])
  print(lst)
  
  print(lst[::2]) #切片取值
  
  del lst[1::2] #切片删除
  print(lst)
  ```

+ 总结：

  + 有序数据 类型需要考虑索引值的变化
  + 无序数据类型不能在循环中直接删除

## 二次编码

+ python3内存中使用的是unicode
+ 硬盘中存储时选择的编码方式：gbk，utf-8

```
s = "你好啊啊"
s1 = s.encode("utf-8") #编码
print(s1)
s2 = s1.decode("utf-8") #解码
print(s2)
```

注：用什么编码就用什么解码

+ 作用
  + 存储 -- 文件操作
  + 传输 -- 网编