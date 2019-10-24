# from socket import *
# s1 = socket()
# s1.bind(("192.168.34.170",7878))
# s1.listen(5)
# s2, addr = s1.accept()
# s2.send("123".encode())
# s2.send("123".encode())
# s2.send("123".encode())

# 发送方将多条数据一起发送
# 接收方一次接受了少于长度的数据

# 解决方法
# strut模块
# import struct
# a = 1
# b = 4294967295
# c = struct.pack("!II",a,b)
# print(c)
# d = struct.unpack("!II",c)
# print(d)

from socket import socket
import subprocess
import struct
s = socket()
s.bind(("192.168.34.170",7879))
s.listen(5)
while True:
    s_new, addr = s.accept()
    print(addr)
    while True:
        try:
            cmd = s_new.recv(1024)
            ret = subprocess.Popen(cmd.decode(),shell= True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            a = ret.stdout.read()
            b = ret.stderr.read()
            total_size = len(a) + len(b)
            head_pack = struct.pack("!i",total_size)
            s_new.send(head_pack)
            s_new.send(a+b)
        except:
            print("有错！")
            break
    s_new.close()