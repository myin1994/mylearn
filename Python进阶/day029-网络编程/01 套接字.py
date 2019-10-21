# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #不确定对方是否能收到
# # s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# from socket import *
# s = socket(AF_INET,SOCK_DGRAM)
# s.sendto("你好啊".encode("GB2312"),("192.168.137.1",8080))
# # 飞秋
# s.sendto("1:2020年12月30日:MY:MY-pc:32:你好啊".encode("GB2312"),("192.168.34.170",2425))

# from socket import *
# import time
# s = socket(AF_INET, SOCK_DGRAM) #创建套接字
# s.bind(('', 2425))   #绑定一个端口，ip地址和端⼝号，ip⼀般不⽤写
# addr = ('192.168.34.170', 2425) #准备接收方地址
# data = input("请输入：")
# s.sendto(("1:2020年12月30日:MY:MY-pc:32:"+data).encode("GB2312"),addr)
# time.sleep(20)
# #等待接收数据
# redata = s.recvfrom(1024)
# #1024表示本次接收的最大字节数
# print(redata)
# print("消息:",redata[0].decode("GB2312"))
# s.close()
# b'1_lbt80_11#128#E86A64026400#2046#20978#0#4000#9:1571664885:24479:LAPTOP-BJF4Q6NL:121:\x00'
# a = b'\xc2\xed\xd1\xf3\x00\x00'
# print(a.decode("GB2312"))


# from socket import *
# s = socket(AF_INET,SOCK_DGRAM)
# s.bind(("",8181))#为当前进程绑定一个ip地址和端口号，放到元组中(若不绑定则每次发生消息是随机端口)
# data = s.recvfrom(1024) #收到的数据是元组，显示数据需要访问其中第一个元素并解码
# print(data)
# print(data[0].decode("GB2312"))

# from socket import *
# s = socket(AF_INET,SOCK_DGRAM)
# addr = ("",8181)
# s.bind(addr)
# while True:
#     data = s.recvfrom(1024)
#     s.sendto(data[0],data[1])
#     print(data[0].decode("GB2312"))

# from socket import *
# s = socket(AF_INET,SOCK_DGRAM)
# addr = ("",8181)
# s.bind(addr)#为当前进程绑定一个ip地址和端口号，放到元组中
 #收到的数据是元组，显示数据需要访问其中第一个元素并解码
# while True:
#
#     a = input("输入内容")
#
#     s.sendto(a.encode("GB2312"), ("192.168.34.28", 6712))
#     # time.sleep(5)
#
#     data = s.recvfrom(1024)
#     print(data[0].decode("GB2312"))

# def send(addr):
#     while True:
#         a = input("输入内容：")
#         s.sendto(a.encode("GB2312"), addr)
#
# def receive():
#     while True:
#         data = s.recvfrom(1024)
#         data_decode = data[0].decode("GB2312")
#         print("\n接收内容：",data_decode)
#         if data_decode == "886":
#             print("对方已退出")
#             break
#
#
#
# t1 = threading.Thread(target=send,args=(("192.168.34.170", 8080),))
# t2 = threading.Thread(target=receive)
# t1.start()
# t2.start()
# import time
# def send_h():
#     while True:
#         s = socket(AF_INET, SOCK_DGRAM)
#         a = input("请输入要发送的信息:")
#         s.sendto(f"{a}".encode("gb2312"), ("192.168.34.170", 8080))
#
# def connect_h():
#
#     while True:
#         s = socket(AF_INET, SOCK_DGRAM)
#         time.sleep(10)
#         s.bind(("",8089))
#         a = s.recvfrom(1024)
#         print(f"对方IP{a[1]},对方发送内容:{a[0].decode('gb2312')}")
#
# a = threading.Thread(target=send_h)
# b = threading.Thread(target=connect_h)
# a.start()
# b.start()
