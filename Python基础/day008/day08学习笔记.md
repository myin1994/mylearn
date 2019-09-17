## 文件操作

### 作用

持久化存储

注意事项：

```
1.文件中存储的都是字符串
2.写入内容时只能写入字符串
```

### 打开文件方法

+ open:通过python向操作系统发送指令

  f-文件句柄：操作文件时使用的文件名

  `f = open("filepath",mode="操作模式",encoding="编码格式")`

+ with open  

  优点：自动关闭文件；可同时操作多个文件

  `with open("filepath","操作模式",encoding="编码方式") as f:`

  with open("file1","mode1",encoding="code1") as f1,open("file2","mode2",encoding="code2") as f2:

  **注意**：with open下需要在缩紧内进行操作，外部不支持使用

+ 路径

  + 相对路径：当前运行的文件目录

    ```
    import os
    print(os.getcwd())  #获取当前工作路径
    ```

    + `.\`   当前路径

      ```
      f = open(".\联系电话.txt","r",encoding="utf-8")
      print(f.read())
      ```

    + `..\ ` 上一级路径（可嵌套..\\..\）

      ```
      f = open("..\day007\联系电话.txt","r",encoding="utf-8")
      print(f.read())
      ```

  + 绝对路径：从磁盘根部开始查找

+ 转义：

  + \\ \  --普通的\

    ```
    f = open("C:\\Users\\24479\\Desktop\\作业上传\\Python基础\\day007\\联系电话.txt",mode="r",encoding="utf-8")
    a = f.read()
    print(a)
    ```

  + r  ---推荐使用

    ```
    f = open(r"C:\Users\24479\Desktop\作业上传\Python基础\day007\联系电话.txt",mode="r",encoding="utf-8")
    a = f.read()
    print(a)
    ```

+ 编码

  ```
  win      gbk
  linux    utf-8
  mac      utf-8
  ```

  

### 操作模式

    r 只读
    w 清空写
    a 追加写
    rb 只读字节
    wb 清空写字节
    ab 追加写字节
    r+ 读写
    w+ 清空写读
    a+ 追加写读
+ r 只读

  读取时，读取光标后的内容(在不移动光标的情况下，文件内容只能读取一次)

  ```
  f = open("联系电话.txt",mode="r",encoding="utf-8")
  print(f.read()) #全部读取-只能读一遍
  print(f.read()) #第二次读为空行（光标移动到末尾）  可使用f.close()关闭文件后重新读取内容
  ```

  ```
  print(f.read(6)) #模式是r的情况下按照字符读取（rb是字节），行末尾隐藏的换行符\n也算一个字符,读到后会换行
  
  print(f.readline())  #读取一行，读到末尾换行符会换行
  print(f.readline())  #读取一行，同文件操作下会读取下一行
  print(f.readline().strip())  #读取一行(不换行)
  ```

  ```
  print(f.readlines())  #读取多行，以列表的形式存储(行末的换行符会被输出-最后一行除外)，\会被读取为\\--为了重新写回文件时转义为一个\
  
  f1 = open("test4.txt",mode="w",encoding="utf-8")  #打开--通过python向操作系统发送指令
  for i in f.readlines():
      f1.write(i)
  ```

  ```
  for i in f:  #文件句柄可迭代 一行一行读取
      print(i)
  ```

+ rb 读字节 --爬虫中使用-默认二进制编码

  python中默认utf-8

  ```
  f = open("联系电话.txt","rb")
  print(f.read())  #读取二进制
  print(f.read().decode(encoding="utf-8"))  #可转换编码
  ```

+ w  清空写 ：文件存在时清空文件，不存在时创建文件（适应所有w模式）

  + 流程：清空文件内容（打开时）--->写入内容

  ```
  f = open("test1","w",encoding="utf-8")
  f.write("hahahah")
  ```

+ wb 清空写字节----常用于爬虫

  ```
  f = open("2.jpg","wb")  #清空写字节建立新图片
  f1 = open("1.jpg","rb")  #读取源图片字节
  f.write(f1.read()) #将f1图片1写入f图片2
  ```

+ a 追加写：一直在文件的末尾进行添加，不存在时创建文件（适应所有a模式）

  ```
  f = open("test1","a",encoding="utf-8")
  f.write("444")
  f.write("666\n")
  f.write("\n777\n")
  f.write("555")
  f.write("\n555")  #换行在追加内容前加换行符
  ```

+ ab 追加写字节  

+ `+` 操作

  + r+  读写  可读可写 指针在文件开头

    ```
    f = open("test1","r+",encoding="utf-8")
    a = f.read() #移动指针末尾
    print(a)
    f.write("这是读写") #在末尾添加内容
    print(f.read())
    ```

    ```
    f = open("test1","r+",encoding="utf-8")
    f.write("这是读写")  #开头写入-会覆盖之前的内容（根据编码）
    a = f.read() #光标移动到写入内容末尾，读取后面的内容
    print(a)
    ```

  + w+ 清空写 读

    ```
    f = open("test1","w+",encoding="utf-8")
    f.write("666")
    f.seek(0,0)  #光标移动到文件头部
    print(f.read())
    ```

  + a+ 追加写 读

    ```
    f = open("test1","a+",encoding="utf-8")
    f.write("333")
    f.seek(0,0)  #光标移动到文件头部
    print(f.read())
    ```

+ 光标

  ```
  f = open("test1","r",encoding="utf-8")
  f.tell()#查看光标 返回的是字节(根据编码)
  f.seek(0,0)  #移动到文件头部
  f.seek(0,1)  #移动到光标当前位置
  f.seek(0,2)  #移动到文件末尾
  f.seek(3)  #移动3个字节，根据编码不同决定移动的字节的大小3
  print(f.read())
  print(f.tell())
  ```

### 文件的修改

1. 打开文件，读取文件中所有的内容，使用for一行一行读取
2. 对每一行的内容进行替换
3. 新建一个文件，将替换后的内容写入新文件
4. 导入os模块，通过os模块修改文件名

```
with open("test1","r",encoding="utf-8") as f,\
        open("test2","w",encoding="utf-8") as f1:
    for i in f:
        f1.write(i.replace("nb","sb"))
        f1.flush()

import os #与操作系统做交互
os.rename("test1","test3")
os.rename("test2","test")
```