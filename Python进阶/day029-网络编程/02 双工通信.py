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