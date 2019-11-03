from socket import *

# while True:
#     data = input(">>>").encode()
#     s.send(data)
#     data1 = s.recv(1024).decode()
#     print(data1)
class Myclient:
    def __init__(self):
        self.status = False
        self.s = socket()
        self.server_addr = ("192.168.34.170",7878)
        self.s.connect(self.server_addr)
        msg1 = """
                  1.登录
                  2.注册
                  3.退出
                  请选择操作序号（1|2|3）："""
        dict1 ={"1":"login",
                "2":"sign_up",
                "3":"exit"}
        while not self.status:
            choice = input(msg1).strip()
            if hasattr(self,dict1[choice]):
                func = getattr(self,dict1[choice])
                func()
            else:
                print("输入错误请重新输入！")

    def login(self):
        while True:
            self.s.send("login".encode())
            ack = self.s.recv(1).decode()
            if ack == "1":
                print("开始登录")
                name = self.s.recv(1024).decode()
                self.s.send(input(name).encode())
                password = self.s.recv(1024).decode()
                self.s.send(input(password).encode())
                result = self.s.recv(1024).decode()
                if result == "1":
                    print("登录成功！")
                    return
                else:
                    print("登录失败！请重新注册！")

    def sign_up(self):
        while True:
            self.s.send("sign_up".encode())
            ack = self.s.recv(1).decode()
            if ack == "1":
                print("开始注册")
                name = self.s.recv(1024).decode()
                self.s.send(input(name).encode())
                password = self.s.recv(1024).decode()
                self.s.send(input(password).encode())
                result = self.s.recv(1024).decode()
                if result == "1":
                    print("注册成功！")
                    return
                else:
                    print("注册失败！请重新注册！")

            else:
                print("服务器未响应,请重试！")


    def exit(self):
        print("退出")
        exit()

myclient = Myclient()
