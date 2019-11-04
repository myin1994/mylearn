# TCP客户端
from socket import *
import threading
import time
s = socket()
# s.bind(("",1234))
addr = ("192.168.34.112",8001)
s.connect(addr)
def send():
    while True:
        try:
            send_data = input("客户端发送内容：")
            # send_data = "哈哈哈哈哈刀"
            s.send(send_data.encode())
        except ConnectionResetError:
            print("服务器已断开连接")
            break
    s.close()

def receive():
    while True:
        try:
            receive_data = s.recv(1024)
            print(receive_data)
            if len(receive_data) > 0:
                print("\n客户端接收内容：",receive_data.decode())
            else:
                print("服务器已断开！")
                break
        except ConnectionResetError:
            print("服务器已断开连接")
            break
    s.close()

send_t = threading.Thread(target=send)
receive_t = threading.Thread(target=receive)
send_t.start()
receive_t.start()