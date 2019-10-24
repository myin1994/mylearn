"""
该客户端用于从对应服务器上进行下载和上传，保存位置可选
"""
class Client:
    def __init__(self,sever_ip,sever_port,file_path):
        import socket
        self.__sever_ip = sever_ip
        self.__sever_port = sever_port
        self.__file_path = file_path
        self.s = socket.socket()
        self.s.connect(self.addr)

    @property
    def addr(self):
        addr = (self.__sever_ip,self.__sever_port)
        return addr

    def upload(self):
        pass

    def download(self):
        pass