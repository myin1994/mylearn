# 序列化
# 1、json（重点）支持字典和列表 转换为字符串
# 2.pickle

# dump  load  用于文件写入存储
# dumps loads  用于网络传输(网络编程)

# dumps：序列
# loads：反序列

# 序列化：将一个数据类型转化成另一个数据类型

# lst = [1,2,3,4,5]
# a = str(lst)
# print(a)
# print(list(a))

# import json
# lst = [1,2,3,4,5]
# a = json.dumps(lst)
# print(a,type(a))
# b = str(lst)
# print(b,type(b))
# s1 = json.loads(a)
# print(s1,type(s1))
# s2 = json.loads(b) #不能转换字符串元素
# print(s2,type(s2))


# import json
# lst = [1,2,3,4,5]
# a = json.dumps(lst)
# print(a,type(a))
#
# s1 = json.loads(a)
# print(s1,type(s1))






# import json
# dic = {"key":"我爱","你":2}
# a = json.dumps(dic,ensure_ascii=True)
# print(a,type(a))
#
# b = json.loads(a)
# print(b,type(b))

# lst = ["元宝","中文","22","dd",4]
# a = json.dumps(lst,ensure_ascii=True)  #默认为True
# a1 =str(lst)
#
# print(a,type(a))
# print(a1,type(a1))
# b = json.loads(a)
# print(b,type(b))
#
# b1 = json.loads(a1)
# print(b1)

# dump
import json
# dic = {"alex":"alex123"}
# f = open("userinfo","a",encoding="utf-8")
# json.dump(dic,f)

# f = open("userinfo","r",encoding="utf-8")
# a = json.load(f)
# print(a,type(a))

# dic = {"alex":"alex123"}
# f = open("userinfo","a+",encoding="utf-8")
# for i in range(3):
#     f.write(json.dumps(dic) + "\n")
# # f = open("userinfo","r",encoding="utf-8")
# f.seek(0)
# for i in f:
#     print(json.loads(i),type(json.loads(i)))

import pickle
# pickle 几乎支持python中所有的对象(不支持lambda)
# 转换为字节写入
# 写入多行时自动带有换行，转换时可以多次转换
# def func():
#     print(111)
#
# a = pickle.dumps(func)
# print(a,type(a))  #转换成了字节
# a1 = pickle.loads(a)
# print(a1,type(a1))
# a1()

# tu = (1,2,3,4,5)
# a = pickle.dumps(tu)
# print(a,type(a))
# b = pickle.loads(a)
# print(b[0],type(b))
# # import pickle
# dic ={"name":"alex","age":18,"hobby":1234}
# f = open("userinfo","ab")
# pickle.dump(dic,f)
# f1 = open("userinfo","rb")
# a = pickle.load(f1)
# print(a,type(a))

# import pickle
# dic ={"name":"alex","age":18,"hobby":1234}
# f = open("userinfo","ab")
# pickle.dump(dic,f)
# pickle.dump(dic,f)
# f1 = open("userinfo","rb")
# for i in f1.readline().split():
#     print(pickle.loads(i))

# import pickle
# dic ={"name":"alex","age":18,"hobby":1234}
# dic1 ={"name":"meet","age":19,"hobby":12345}
# f = open("userinfo","rb+")
# pickle.dump(dic,f)
# pickle.dump(dic1,f)
# f.seek(0)
# print(pickle.load(f))
# print(pickle.load(f))

# import pickle
# dic ={"name":"alex","age":18,"hobby":1234}
# f = open("userinfo","ab+")
# for i in range(3):
#     pickle.dump(dic,f)
#
# f.seek(0)
# for i in range(3):
#     print(pickle.load(f))

# import pickle
# dic ={"name":"alex","age":18,"hobby":1234}
# f = open("userinfo","ab+")
# for i in range(3):
#     pickle.dump(dic,f)
#
# f.seek(0)

# while 1:
#     try:
#         print(pickle.load(f))
#     except EOFError:
#         break



# json 和 pickle的区别
# json 序列后是字符串  只支持字典和列表
# pickle 序列后是字节  支持python中大部分对象