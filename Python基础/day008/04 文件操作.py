# 文件操作---操作文件
# 文件操作的作用：持久化存储

# 三次登录锁定

# 文件操作怎么使用

# 联系电话.txt
# 1.file = 路径
# 2.mode = 操作文件的方式
    #r-只读文本  w-清空写文本  a-追加写文本
    # rb-只读字节  wb-清空写字节  ab-追加写字节
    # r+    w+  a+
# 3.encoding = 文件的编码
#         win -gbk
#         linux  mac  -utf-8
# f  文件句柄--操作文件使用的变量名

# f = open("联系电话.txt",mode="r",encoding="utf-8")  #打开--通过python向操作系统发送指令
# print(f.read()) #全部读取-只能读一遍
# f.close()
# f = open("联系电话.txt",mode="r",encoding="utf-8")  #打开--通过python向操作系统发送指令
# print(f.read()) #第二次读为空行（光标移动到末尾）
# print(f.read(3)) #模式是r的情况下按照字符读取，行末尾隐藏的换行符\n也算一个字符
#                        rb是字节
# print(f.readline())  #读取一行，读到末尾换行符会换行
# print(f.readline())  #读取一行
# print(f.readline().strip())  #读取一行(不换行)

# print(f.readlines())   #读取多行，以列表的形式存储
# f1 = open("test4.txt",mode="w",encoding="utf-8")  #打开--通过python向操作系统发送指令
# for i in f.readlines():
#     f1.write(i)
# for i in f:  #文件句柄可迭代 一行一行读取
#     print(i)

# 路径
# 相对路径：相当于当前运行的文件目录
# import os
# print(os.getcwd())  #工作路径
# . #当前路径
# .. #上一级路径(可嵌套..\..\=)

# f = open("..\day007\联系电话.txt","r",encoding="utf-8")
# f = open(".\联系电话.txt","r",encoding="utf-8")
# print(f.read())
# 绝对路径：从磁盘根部开始查找的就是绝对路径

# 转义：
# 1.\\ -- 普通的\
# f = open("C:\\Users\\24479\\Desktop\\作业上传\\Python基础\\day007\\联系电话.txt",mode="r",encoding="utf-8")
# a = f.read()
# print(a)
# 2. r  推荐使用
# f = open(r"C:\Users\24479\Desktop\作业上传\Python基础\day007\联系电话.txt",mode="r",encoding="utf-8")
# a = f.read()
# print(a)

# rb 读字节 --  爬虫
# f = open("联系电话.txt","rb")
# print(f.read())
# print(f.read().decode(encoding="utf-8"))

# w-清空写：有文件时清空文件，没文件时创建文件
# 1.清空文件内容(打开文件时)
# 2.写入内容
# f = open("test1","w",encoding="utf-8")
# f.write("hahahah")


# f.flush()  #刷新
# f.write("dddddddddddhah")

# f.close() #关闭文件

# f.write("今天\n")
# f.write("明天")
# f.write("后天")

# wb  清空写字节  -- 爬虫  没有时创建文件
# import requests
# ret = requests.get("https://guobaoyuan.gitee.io/book/assets/image-20190619205811650.png")
# ret_b = ret.text.encode("utf-8")
# print(ret_b)

# f = open("2.jpg","wb")  #清空写入新图片
# f1 = open("1.jpg","rb")  #源图片
# f.write(f1.read()) #将f1图片1写入f图片2

# a-追加写 没文件时创建文件 一直在文件的末尾进行添加
# f = open("test1","a",encoding="utf-8")
# f.write("444")
# f.write("555")
# f.write("666\n")
# f.write("\n777\n")
# f.write("555")
# f.write("555")
# f.write("\n555")  #换行在追加内容前加换行符

# ab：自己完善

# +操作
# r+ 读写 -- 可读可写

# f = open("test1","r+",encoding="utf-8")
# a = f.read()
# print(a)
# f.write("这是读写")
# print(f.read())

# 特殊的操作
# f = open("test1","r+",encoding="utf-8")
# f.write("这是读写")  #开头写入
# a = f.read() #光标移动到写入内容末尾，读取后面的内容
# print(a)

# w+  ：清空写，读
# f = open("test1","w+",encoding="utf-8")
# f.write("666")
# f.seek(0,0)  #光标移动到文件头部
# print(f.read())

# a+  ：追加写，读
# f = open("test1","a+",encoding="utf-8")
# f.write("333")
# f.seek(0,0)  #光标移动到文件头部
# print(f.read())

# 最常用 r,w,a  a+(没有文件时，实时显示)  r+(覆盖一些内容时)
# w，a可以创建文件
# 在不移动光标的情况下，文件内容只能读取一次

# 光标
# f = open("test1","r",encoding="gbk")
# f.tell()#查看光标 返回的是字节
# print(f.tell())
# f.seek(0,0)  #移动到文件头部
# f.seek(0,1)  #移动到光标当前位置
# print(f.tell())
# f.seek(0,2)  #移动到文件末尾
# print(f.tell())
# f.seek(8)  #移动3个字节，根据编码不同决定移动的字节的大小3
# print(f.tell())
# print(f.read())
# print(f.tell())

# a 追加-总是在文件末尾-不在光标后添加
# f = open("test2","a",encoding="gbk")
# f.write("嘿嘿嘿")
# f.seek(0,0)
# print(f.tell())
# f.write("哈哈哈")

# with open
# 1.自动关闭文件
# with open("test2","r",encoding="gbk") as f:
#     print(f.read())
# print(f.read()) #ValueError: I/O operation on closed file.

# 2.可以同时操作多个文件
# with open("test2","r",encoding="gbk") as f,open("test1","r",encoding="utf-8") as f1:
#     print(f.read())
#     print(f1.read())

# 文件的修改
# 1.打开文件，读取文件中所有的内容 一行一行读取 使用for
# 2.对每一行的内容进行替换
# 3.新建一个文件，将替换后的内容写入新文件
# 4.导入os模块，通过os模块修改文件名
# 文本中存储的都是字符串
# with open("test1","r",encoding="utf-8") as f,\
#         open("test2","w",encoding="utf-8") as f1:
#     for i in f:
#         f1.write(i.replace("nb","sb"))
#         f1.flush()
#
# import os #与操作系统做交互
# os.rename("test1","test3")
# os.rename("test2","test")

# 注意：
# 1.文件中存储的都是字符串
# 2.写入内容时只能写入字符串


