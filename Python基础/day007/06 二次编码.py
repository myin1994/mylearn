# 回顾编码
# ascii：英文，数字，符号 8位
# gbk：英文，数字，符号，中文 英8，中：16
# unicode：英文，数字，符号，中文 英32，中：32
# utf-8:英文，数字，符号，中文 英8，中：24,欧洲：16

# 二次编码：
# python3内存中使用的是unicode
# 硬盘中存储时选择的编码方式：gbk，utf-8

# s = "你好啊啊"
# s1 = s.encode("utf-8") #编码
# print(s1)
# s2 = s1.decode("utf-8") #解码
# print(s2)

# b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe5\x93\x88\xe5\x93\x88'
# 存储
# 网络传输

# s = "你好"
# s1 = s.encode("utf-8") #编码 2个字--6字节
# # print(s1[0])
# print(s1)
# s2 = s1.decode("gbk") #解码 3个字--6字节
# print(s2)

# s = "hello"
# s1 = s.encode("ascii")
# # print(s1[0])
# print(s1)
# s2 = s1.decode("gbk")
# print(s2)

# encode #编码
# decode #解码
# 用什么编码就用什么解码

# 用处：
# 1.存储 -- 文件操作
# 2.传输 -- 网编
