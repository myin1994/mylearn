## 序列化

**将一个数据类型转化成另一个数据类型**

###  json模块

+ 支持字典和列表：转换为字符串

+ 网络传输

  + dumps   序列化：将字典或列表转换为字符串类型
  + loads    反序列化：将字符串类型的列表或字典转换为应有格式

  ```
  import json
  lst = [1,2,3,4,5]
  a = json.dumps(lst)
  print(a,type(a)) #[1, 2, 3, 4, 5] <class 'str'>
  
  s1 = json.loads(a)
  print(s1,type(s1)) #[1, 2, 3, 4, 5] <class 'list'>
  ```

  ```
  import json
  dic = {"key":"我爱","你":2}
  a = json.dumps(dic,ensure_ascii=False)#默认为True，转换时中文显示会为字节
  print(a,type(a)) #{"key": "\u6211\u7231", "\u4f60": 2} <class 'str'>
  
  b = json.loads(a)
  print(b,type(b)) #{'key': '我爱', '你': 2} <class 'dict'>
  ```

+ 文件存储

  + dump  序列化：将字典或列表转换为字符串写入文件（多次写入不支持换行）

    ```
    import json
    dic = {"alex":"alex123"}
    f = open("userinfo","a",encoding="utf-8")
    json.dump(dic,f)
    ```

  + load   反序列化：读取文件中字符串类型的列表或字典并转换为应有格式（多个时报错）

    ```
    import json
    f = open("userinfo","r",encoding="utf-8")
    a = json.load(f) #文件仅存一个字典型数据
    print(a,type(a)) #{'alex': 'alex123'} <class 'dict'>
    ```

+ 批量向文件中写入json数据并读取

  ```
  import json
  dic = {"alex":"alex123"}
  f = open("userinfo","a+",encoding="utf-8")
  for i in range(3):
      f.write(json.dumps(dic) + "\n") #逐行将转换格式后的数据写入
  
  f.seek(0)
  for i in f:
      print(json.loads(i),type(json.loads(i)))#逐行读取数据并转换为原有格式
  
  >>>{'alex': 'alex123'} <class 'dict'>
  >>>{'alex': 'alex123'} <class 'dict'>
  >>>{'alex': 'alex123'} <class 'dict'>
  ```

  或者将json数据整个提取出来后添加元素再写回

### pickle模块

+ 几乎支持python中所有的对象(不支持lambda)：转换为字节

+ 网络传输

  + dumps   序列化：将对象转换为字节
  + loads    反序列化：将字节转换为应有格式

  ```
  import pickle
  def func():
      print("函数被调用")
  
  a = pickle.dumps(func)
  print(a,type(a))  #b'\x80\x03c__main__\nfunc\nq\x00.' <class 'bytes'>
  a1 = pickle.loads(a)
  print(a1,type(a1)) #<function func at 0x0000020A24781EA0> <class 'function'>
  a1() #函数被调用
  ```

  ```
  import pickle
  tu = (1,2,3,4,5)
  a = pickle.dumps(tu)
  print(a,type(a))#b'\x80\x03(K\x01K\x02K\x03K\x04K\x05tq\x00.' <class 'bytes'>
  b = pickle.loads(a)
  print(b[0],type(b)) #1 <class 'tuple'>
  ```

+ 文件存储

  + dump  序列化：将对象转换为字节写入文件（多次写入不支持换行，但每次写入会自动加\n）

    ```
    import pickle
    dic ={"name":"alex","age":18,"hobby":1234}
    f = open("userinfo","ab")
    pickle.dump(dic,f)
    ```

  + load   反序列化：读取文件中的字节并转换为应有格式（类似生成器一次读取一个）

    ```
    import pickle
    f1 = open("userinfo","rb") #文件中有多个对象的字节
    a = pickle.load(f1)
    print(a,type(a))#{'name': 'alex', 'age': 18, 'hobby': 1234} <class 'dict'>
    ```

+ 批量向文件中写入pickle数据并读取

  ```
  import pickle
  dic ={"name":"alex","age":18,"hobby":1234}
  f = open("userinfo","ab+")
  for i in range(3):
      pickle.dump(dic,f)
  
  f.seek(0)
  while 1:
      try:
          print(pickle.load(f)) #一个一个的读取
      except EOFError:
          break
  ```

  

## hashlib模块

**摘要算法，加密算法**

+ 功能：加密，校验一致性

+ 加密规则

  + 算法：md5  sha1   sha256  sha512
  + 规则
    + 内容相同，密文一定相同
    + 加密的密文是不可逆的 -- 但是md5已被破解
    + 明文转换为字节，再从字节转换为密文

+ 加密方法（md5  sha1   sha256  sha512互相替换）

  + 常规

    ```
    import hashlib
    s = "1234567"
    md5 = hashlib.md5()  #初始化加密算法
    md5.update(s.encode("utf-8"))
    print(md5.hexdigest())
    ```

  + 固定加盐

    实质是将加的盐与加密拼接成一个字符串后进行加密

    ```
    import hashlib
    user = input("user:")
    pwd = input("pwd:")
    md5 = hashlib.md5("oldboy".encode("utf-8")) #初始化时加盐
    md5.update(pwd.encode("utf-8"))
    print(md5.hexdigest())
    ```

  + 动态加盐

    ```
    import hashlib
    user = input("user:")
    pwd = input("pwd:")
    md5 = hashlib.md5(user.encode("utf-8"))#可多次加盐
    md5.update(pwd.encode("utf-8"))
    print(md5.hexdigest())
    ```

+ 一致性校验

  ```
  import hashlib
  s = '宝元 is a old driver'
  print(s.split())
  import hashlib
  # 直接 update
  md5obj = hashlib.md5()
  for i in s.split():
      md5obj.update(i.encode("utf-8")) #大文件时可切割后进行加密对比
  print(md5obj.hexdigest())  #213a4a0e2f69ac56db1ff6295f468e7d
  
  
  s1 = '宝元 is a old driver'
  s1 = s1.replace(" ","")
  md5 = hashlib.md5()
  md5.update(s1.encode("utf-8"))
  print(md5.hexdigest())
  ```

  

## collections 模块

+ 统计-统计可迭代数据类型中每个元素的个数，以字典的形式存储

  ```
  lst = [11,2,2,11,2,3]
  from collections import Counter
  print(dict(Counter(lst))) #{11: 2, 2: 3, 3: 1}
  print(Counter(lst)) #Counter({2: 3, 11: 2, 3: 1})
  ```

+ 有序字典-python2中使用

  ```
  from collections import OrderedDict
  a = OrderedDict({"key":1,"key2":2})
  print(a) #OrderedDict([('key', 1), ('key2', 2)])
  print(a["key"]) #1
  ```

+ 默认字典-可规定字典值的规则（可为函数）

  ```
  from collections import defaultdict
  dic = defaultdict(list) #列表值默认设置为列表
  dic["key"].append(1) #增加价值对
  dic["key1"]  #增加键值对，值默认空列表
  print(dic) #defaultdict(<class 'list'>, {'key': [1], 'key1': []})
  ```

  ```
  from collections import defaultdict
  dic = defaultdict(list)
  lst = [11,22,33,44,55,77,88,99]
  for i in lst:
      if i > 66:
          dic["key2"].append(i)
      else:
          dic["key1"].append(i)
  print(dic)
  ```

+ 双端队列

  + 队列：先进先出

  + 栈：先进后出

  + 双端队列的实现

    ```
    from collections import deque
    lst = deque([11,22,33,44,55])
    print(lst)
    lst.append(66)
    print(lst)
    lst.appendleft(44)  #从头添加元素
    print(lst)
    lst.pop()
    print(lst)
    lst.popleft()
    print(lst)
    ```

  + gc：垃圾回收机制-以引用计数为主，标记清除和分带回收为辅

+ 命名元组

  ```
  from collections import namedtuple
  dg = namedtuple("dg",["jd","wd","gd"])
  a = dg(111,222,8888)
  print(a) #dg(jd=111, wd=222, gd=8888)
  print(a.jd) #111,支持通过名称取值
  print(a[2]) #8888 支持索引
  ```



## 软件开发规范

**分文件管理**

+ bin -- 启动文件
+ lib -- 公共模块
+ core -- 主逻辑
+ db -- 相关数据
+ log -- 日志，记录程序运行情况
+ conf --配置文件(静态文件)
+ 导出文件夹的目录树
  1. cmd下cd到目标文件路径下
  2. tree /f >treefile.txt