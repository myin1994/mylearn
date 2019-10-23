# 单进程服务器
# from socket import *
# s = socket()
# addr = ("192.168.34.170",8989)
# s.bind(addr)
# s.listen(5)
# while True:
#     print("主进程等待新客户端")
#     client_s, client_addr = s.accept()
#     print(f"主进程接下来负责处理,客户端ip：{client_addr[0]}客户端端口：{client_addr[1]}")
#     try:
#         while True:
#             recdata = client_s.recv(1024)
#             if len(recdata) > 0: #若收到数据为零，说明客户端已经调用close()
#                 print(f"接收到客户端ip：{client_addr[0]}客户端端口：{client_addr[1]}信息：{recdata.decode()}")
#             else:
#                 print(f"客户端ip：{client_addr[0]}客户端端口：{client_addr[1]}已关闭")
#                 break
#     except ConnectionResetError:
#         print("远程主机强迫关闭了一个现有的连接")
#     except:
#         print("其他未知错误")
#     finally:
#         client_s.close()
# s.close()


# from socket import *
# import json
# s = socket(AF_INET, SOCK_STREAM)
#
# s.bind(("192.168.34.170", 9999))
# s.listen(5)
# conn,addr = s.accept()
# # f = open("user", "r", encoding="utf-8")
#
# while True:
#     info = conn.recv(1024)
#     # if len(info) > 0:
#     print(info.decode())
#     # else:
#     #     s.close()
#     #     break

# TCP多进程服务器
from socket import *
from multiprocessing import *
from time import sleep
def dealWithClient(client_s,client_addr):
    try:
        while True:
            recdata = client_s.recv(1024)
            if len(recdata) > 0:
                print(f"接收到客户端ip：{client_addr[0]}客户端端口：{client_addr[1]}信息：{recdata.decode()}")
            else:
                print()
                print(f"客户端ip：{client_addr[0]}客户端端口：{client_addr[1]}已关闭")
                break
    except ConnectionResetError:
        print("远程主机强迫关闭了一个现有的连接")
        return
    except:
        print("其他未知错误")
        return
    finally:
        client_s.close()

def main():
    s = socket()
    # s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    addr = ("",7878)
    s.bind(addr)
    s.listen(5)
    try:
        while True:
            print("主进程等待新客户端")
            client_s, client_addr = s.accept()
            print("主进程创建新进程负责数据处理")
            client = Process(target=dealWithClient,args=(client_s,client_addr))
            client.start()
            client_s.close()
    finally:
        s.close()

if __name__ == '__main__':
    main()