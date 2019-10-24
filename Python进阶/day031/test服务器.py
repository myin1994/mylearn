from socket import socket
import time
s = socket()
s.bind(("192.168.34.170",7891))
s.listen(5)
client_s, addr = s.accept()
num = 0
while True:
    num += 1
    client_s.send(f"服务器连接中{num}".encode())
    print(num)
# data = client_s.recv(1024)
# num += 1
# time.sleep(2)
# client_s.close()
# client_s.close()
# client_s.send(f"服务器连接中{num}".encode())
# print(data)
# client_s.send(f"服务器连接中{num}".encode())
# client_s.send(f"服务器连接中{num}".encode())
# client_s.send(f"服务器连接中{num}".encode())
# client_s.send(f"服务器连接中{num}".encode())
# client_s.send(f"服务器连接中{num}".encode())
# client_s.send(f"服务器连接中{num}".encode())
# client_s.send(f"服务器连接中{num}".encode())
# client_s.send(f"服务器连接中{num}".encode())
# client_s.send(f"服务器连接中{num}".encode())
# client_s.send(f"服务器连接中{num}".encode())
# client_s.send(f"服务器连接中{num}".encode())
# client_s.send(f"服务器连接中{num}".encode())
# client_s.send(f"服务器连接中{num}".encode())
# client_s.send(f"服务器连接中{num}".encode())


    # if len(data) == 0:
    #     client_s.close()
    #     time.sleep(5)
        # break