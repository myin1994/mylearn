"""
该服务器提供上传和下载的功能，文件存储位置可选
1.服务器启动后进入监听状态
2.客户端连接后自动分出一个进程
3.在进程中自动分出收发线程
"""
from multiprocessing import Process
from socket import socket
import threading
import struct
class Sever:
    def __init__(self,sever_ip,sever_port,file_path):

        self.__sever_ip = sever_ip
        self.__sever_port = sever_port
        self.__file_path = file_path
        self.s = socket()
        self.s.bind(self.addr)
        self.s.listen(5)
        self.run()

    @property
    def addr(self):
        addr = (self.__sever_ip,self.__sever_port)
        return addr

    def send(self):

        # with open(filepath, )
        pass

    def receice(self):
        pass

    def wr_con(self, client_s, client_addr):
        """
        服务器连接到客户端后收发客户端命令
        收：要求2字节 1-下载 2-上传
        发：要求2字节 3-请求正确 4-请求错误
        :return:
        """
        requet_data = struct.unpack("!H",client_s.recv(2))[0].decode()
        if requet_data == 1:
            t1 = threading.Thread(target=self.send)
            ack_data = struct.pack("!H", 3)
            client_s.send(ack_data)
            t1.start()
        if requet_data == 2:
            t2 = threading.Thread(target=self.receice)
            ack_data = struct.pack("!H", 3)
            client_s.send(ack_data)
            t2.start()
        if requet_data != 1 and requet_data != 2:
            ack_data = struct.pack("!H",4)
            client_s.send(ack_data)

    def run(self):
        """
        服务器启动后自动触发进入循环监听状态
        :return:
        """
        while True:
            print("服务器等待连接……")
            client_s, client_addr = self.s.accept()
            print(f"客户端{client_addr}已接入,分出进程处理")
            sever_Procss = Process(target=self.wr_con,args=(client_s,client_addr))
            sever_Procss.start()
            client_s.close()
