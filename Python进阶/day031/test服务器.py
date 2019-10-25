from socket import socket
import time
s = socket()
s.bind(("192.168.34.170",7891))
s.listen(5)
# s.setsockopt()
client_s, addr = s.accept()
num = 0

client_s.send(f"服务器连接中{num}".encode())


time.sleep(2)
client_s.close()

