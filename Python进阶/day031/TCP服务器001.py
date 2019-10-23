"""
该服务器提供上传和下载的功能，文件存储位置可选
"""
class Sever:
    def __init__(self,sever_ip,sever_port,file_path):
        import socket
        self.__sever_ip = sever_ip
        self.__sever_port = sever_port
        self.__file_path = file_path
        self.s = socket.socket()
        self.s.bind(self.addr)
        self.s.listen(5)
        self.run()

    @property
    def addr(self):
        addr = (self.__sever_ip,self.__sever_port)
        return addr

    def upload(self):
        pass

    def download(self):
        pass

    def run(self):
        while True:
            print("服务器等待连接……")
            client_s, client_addr = self.s.accept()
            rec_data = client_s.recv(1024)
            if rec_data.decode() == 1:
                self.upload()
            if rec_data.decode() == 2:
                self.download()
