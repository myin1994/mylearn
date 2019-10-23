# # TCP服务器
# 多进程中不允许绑定相同端口号（需要设置）
# 多线程也一样
# from socket import *
#
#
# def acc(news, clientaddr):
#
#
#     news.send("hello".encode("gb2312"))
#     recdata = news.recv(1024)
#     print(recdata.decode("gb2312"))
#
#
# import threading
#
# s = socket(AF_INET, SOCK_STREAM)
# addr = ("", 7878)
# s.bind(addr)
# s.listen(5)
# while True:
#     news, clientaddr = s.accept()
#     t = threading.Thread(target=acc,args=(news, clientaddr))
#     t.start()

# TCP服务器
# from socket import *
#
# s = socket(AF_INET, SOCK_STREAM)
# addr = ("192.168.34.170", 7878)
# print(s)
# s.bind(addr)
# print(s)
#
# s.listen(5)
# news, clientaddr = s.accept()
# news.send("hello".encode())
# recdata = news.recv(1024)
# print(recdata.decode())
# import threading
# from socket import *
# import time
# s =socket()
# s.bind(("",7788))
# def func1(s):
#     print("1",s)
#     time.sleep(3)
#     print("1",s)
#
# def func2(s):
#     print("2",s)
#     time.sleep(3)
#     print("2",s)
# t1 = threading.Thread(target=func1,args=(s,))
# s = socket()
# s.bind(("",7766))
# t2 = threading.Thread(target=func2,args=(s,))
# t1.start()
# t2.start()
# s.close()
# func(a)
# s.close()
# time.sleep(10)

# # 单进程TCP服务器
# from socket import *
# import threading
#
#
# def send(client_s, client_addr):
#     while True:
#         try:
#             send_data = input("服务器发送内容：")
#             client_s.send(send_data.encode())
#         except:
#             print("客户端已断开连接")
#             return
#         finally:
#             client_s.close()
#
# def receive(client_s, client_addr):
#     try:
#         while True:
#             receive_data = client_s.recv(1024)
#             if len(receive_data) > 0:
#                 print("\n服务器接收内容：",receive_data.decode())
#             else:
#                 print("客户端已断开连接")
#                 return
#     except:
#         print("客户端意外断开！")
#         return
#     finally:
#         client_s.close()
#
# s = socket()
# addr = ("",7878)
# s.bind(addr)
# s.listen(5)
# while True:
#     print("服务器等待客户端连接……")
#     client_s, client_addr = s.accept()
#     print(f"客户端{client_addr}已连接")
#     try:
#         while True:
#             # send_t = threading.Thread(target=send,args=(client_s, client_addr))
#             receive_t = threading.Thread(target=receive,args=(client_s, client_addr))
#             # send_t.start()
#             receive_t.start()
#     except:
#         print(f"客户端{client_addr}已断线")
#         continue
#     finally:
#         client_s.close()


# 多线程TCP服务器收发
# from socket import *
# import threading
#
#
# def send(client_s, client_addr):
#     try:
#         while True:
#             print(123)
#             send_data = input(f"服务器向客户端{client_addr}发送内容：")
#             client_s.send(send_data.encode())
#     except:
#         print(f"\n{client_addr}客户端意外断开，不能发送！")
#         return
#     finally:
#         client_s.close()
#
# def receive(client_s, client_addr):
#     try:
#         while True:
#             receive_data = client_s.recv(1024)
#             if len(receive_data) > 0:
#                 print(f"服务器收到{client_addr}消息：",receive_data.decode())
#             else:
#                 print(f"\n{client_addr}客户端已断开连接")
#                 return
#     except:
#         print(f"\n{client_addr}客户端意外断开,不能接收！")
#         return
#     finally:
#         client_s.close()
#
# s = socket()
# addr = ("",7880)
# s.bind(addr)
# s.listen(5)
# num = 0
# while True:
#     print("\n服务器等待客户端连接……")
#     client_s, client_addr = s.accept()
#     print(f"客户端{client_addr}已连接")
#     send_t = threading.Thread(target=send,args=(client_s, client_addr))
#     receive_t = threading.Thread(target=receive,args=(client_s, client_addr))
#     send_t.start()
#     receive_t.start()


# 多进程TCP服务器实现
# class Sever:
#     def __init__(self,addr=("",7878),lis=5):
#         import socket
#         self.s = socket.socket()
#         self.addr = addr
#         self.s.bind(self.addr)
#         self.lis = lis
#         self.s.listen(self.lis)
#         self.run()
#
#     def __send(self,client_s, client_addr):
#         try:
#             while True:
#                 send_data = input(f"服务器向客户端{client_addr}发送内容：")
#                 client_s.send(send_data.encode())
#         except:
#             print(f"\n{client_addr}客户端意外断开！")
#             return
#         finally:
#             client_s.close()
#
#     def receive(client_s, client_addr):
#         try:
#             while True:
#                 receive_data = client_s.recv(1024)
#                 if len(receive_data) > 0:
#                     print(f"\n服务器收到{client_addr}消息：",receive_data.decode())
#                 else:
#                     print(f"\n{client_addr}客户端已断开连接")
#                     return
#         except:
#             print(f"\n{client_addr}客户端意外断开！")
#             return
#         finally:
#             client_s.close()
#
#     def run(self):
#         while True:
#             print("服务器可连接")
#             client_s, client_addr = self.s.accept()


from socket import *
import threading
from multiprocessing import Process


def send(client_s, client_addr):
    try:
        while True:
            print(123)
            send_data = input(f"服务器向客户端{client_addr}发送内容：")
            client_s.send(send_data.encode())
    except:
        print(f"\n{client_addr}客户端意外断开，不能发送！")
        return
    finally:
        client_s.close()

def receive(client_s, client_addr):
    try:
        while True:
            receive_data = client_s.recv(1024)
            if len(receive_data) > 0:
                print(f"服务器收到{client_addr}消息：",receive_data.decode())
            else:
                print(f"\n{client_addr}客户端已断开连接")
                return
    except:
        print(f"\n{client_addr}客户端意外断开,不能接收！")
        return
    finally:
        client_s.close()

def main():
    s = socket()
    addr = ("",7880)
    s.bind(addr)
    s.listen(5)

    while True:
        print("\n服务器等待客户端连接……")
        client_s, client_addr = s.accept()
        print(f"客户端{client_addr}已连接")
        send_t = Process(target=send,args=(client_s, client_addr))
        receive_t = Process(target=receive,args=(client_s, client_addr))
        send_t.start()
        receive_t.start()
        client_s.close()

if __name__ == '__main__':
    main()