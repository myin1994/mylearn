from socket import *
s = socket()
addr = ("192.168.34.170",7788)
s.connect(addr)
while True:
    action = input("请输入操作（登录/注册）").encode()
    s.send(action)
    reaction = s.recv(1024)
    action2 = input(reaction.decode()).encode()
    s.send(action2)
    result = s.recv(1024).decode()
    print(result)

