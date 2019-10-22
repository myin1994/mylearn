# TFTP
# 69端口只用于接收读写请求
# 将文件切分发送，长度小于固定值时就认为下载完成

# 读写请求
# import struct
# from socket import *
# cmb = struct.pack("!H7sb5sb",1,b"001.png",0,b"octet",0)
# udps = socket(AF_INET,SOCK_DGRAM)
# udps.sendto(cmb,("127.0.0.1",69))
# udps.close()

# import struct
# from socket import *
# request = struct.pack("!H7sb5sb",1,"LOL.jpg".encode(),0,"octet".encode(),0)
# s = socket(AF_INET,SOCK_DGRAM)
# s.sendto(request,("192.168.34.28",69))
# filename = open("LOL.jpg","ab")
# while True:
#     datapack = s.recvfrom(1024)
#     print(datapack)
#     caozuoma, kuainum = struct.unpack("!HH",datapack[0][:4])
#     print(type(caozuoma))
#     if caozuoma == 5:
#         break
#     data = datapack[0][4:]
#     filename.write(data)
#     if len(data) < 512:
#         break
#     ack = struct.pack("!HH",4,kuainum)
#     s.sendto(ack,datapack[1])

# class Client:
#
#     def __init__(self,filename,ip,encode="gb2312"):
#         import socket
#         self.filename = filename
#         self.ip = ip
#         self.encode = encode
#         self.s = s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#
#     def down(self):
#         import struct
#         request = struct.pack(f"!H{len(self.filename.encode(self.encode))}sb5sb",1
#                               ,self.filename.encode(self.encode),0,"octet".encode(),0)
#         self.s.sendto(request,(self.ip,69))
#         f = open(self.filename,"ab")
#         while True:
#             datapack = self.s.recvfrom(1024)
#             oper, num = struct.unpack("!HH",datapack[0][:4])
#             print(num)
#             if oper == 5:
#                 print("查无此文件")
#                 break
#             data = datapack[0][4:]
#             f.write(data)
#             if len(data) < 512:
#                 print("接收完毕")
#                 break
#             ack = struct.pack("!HH",4,num)
#             self.s.sendto(ack,datapack[1])
#
#     def up(self):
#         import struct
#         import os
#         filesize = os.path.getsize(self.filename)
#         request = struct.pack(f"!H{len(self.filename.encode(self.encode))}sb5sb", 2
#                               , self.filename.encode(self.encode), 0, "octet".encode(), 0)
#         self.s.sendto(request, (self.ip, 69))
#         f = open(self.filename, "rb")
#         num1 = 0
#         while True:
#             datapack = self.s.recvfrom(1024)
#             oper, num = struct.unpack("!HH", datapack[0][:4])
#             if oper != 4:
#                 print("文件重复")
#                 break
#             data = f.read(512)
#             num1 += 512
#             print(f"当前上传{num1/filesize:.2%}")
#             if num == 65535:
#                 num = -1
#             datapack2 = struct.pack("!HH512s",3,num+1,data)
#
#             self.s.sendto(datapack2,datapack[1])
#             if len(data) < 512:
#                 print("发送完毕")
#                 break
# down1 = Client("梦想.flv","127.0.0.1")
# down1.up()

