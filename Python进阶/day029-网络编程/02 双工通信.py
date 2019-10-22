class Message:

    def __init__(self,addr1:tuple, addr2:tuple):
        import socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr1 = addr1
        self.addr2 = addr2
        self.s.bind(addr1)

    def send(self):
        while True:
            a = input("输入内容：")
            self.s.sendto(a.encode("GB2312"), self.addr2)
            if a == "886":
                print("退出聊天")
                break

    def receive(self):
        while True:
            data = self.s.recvfrom(1024)
            data_decode = data[0].decode("GB2312")
            print("\n接收内容：", data_decode)
            if data_decode == "886":
                print("对方已退出")
                break

    def start(self):
        import threading
        t1 = threading.Thread(target=self.send)
        t2 = threading.Thread(target=self.receive)
        t1.start()
        t2.start()
message1 = Message(("",8181),("192.168.34.170", 8080))
message1.start()


# class Message:
#
#     def __init__(self,addr1:tuple, addr2:tuple):
#         import socket
#         self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         self.addr1 = addr1
#         self.addr2 = addr2
#         self.s.bind(addr1)
#
#     def send(self):
#         while True:
#             a = input("输入内容：")
#             self.s.sendto(a.encode("GB2312"), self.addr2)
#             if a == "886":
#                 print("退出聊天")
#                 exit()
#
#     def receive(self):
#         while True:
#             data = self.s.recvfrom(1024)
#             data_decode = data[0].decode("GB2312")
#             print("\n接收内容：", data_decode)
#             if data_decode == "886":
#                 print("对方已退出")
#                 break
#
#
#     def start(self):
#         import threading
#         t1 = threading.Thread(target=self.send,name="发线程 ")
#         t2 = threading.Thread(target=self.receive,name="收线程")
#         t1.start()
#         t2.start()
# message1 = Message(("",8181),("192.168.137.1", 8080))
# message1.start()


# from multiprocessing import Process
# import threading
#
# class Send(threading.Thread):
#     def __init__(self,s, addr):
#         super().__init__()
#         self.s = s
#         self.addr = addr
#
#     def run(self) -> None:
#         while True:
#             a = input("输入内容：")
#             self.s.sendto(a.encode("GB2312"), self.addr)
#             if a == "886":
#                 print("退出聊天")
#                 self.s.close()
#                 break
#
# class Receive(Process):
#     def __init__(self,s):
#         self.s = s
#         super().__init__()
#     def run(self) -> None:
#         while True:
#             data = self.s.recvfrom(1024)
#             data_decode = data[0].decode("GB2312")
#             print("\n接收内容：", data_decode)
#             if data_decode == "886":
#                 print("对方已退出")
#                 self.s.close()
#                 break
#
# if __name__ == "__main__":
#     from socket import *
#     s = socket(AF_INET,SOCK_DGRAM)
#     s.bind(("",8181))
#     p1 = Send(s,("192.168.34.170", 8080))
#     p2 = Receive(s)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()



# from socket import *
# import threading
# s = socket(AF_INET,SOCK_DGRAM)
# addr = ("127.0.0.1",8081)
# s.bind(addr)
#
# def jieshou():
#     while True:
#         data = s.recvfrom(1024)
#         print(data[0].decode())
#         if data[0] == "886":
#             s.close()
#
# def fasong():
#     while True:
#         r = input(":")
#         s.sendto(r.encode(), ("", 8082))
#         if r == "886":
#             s.close()
#
#
# t1 = threading.Thread(target=jieshou)
# t2 = threading.Thread(target=fasong)
# t1.start()
# t2.start()












