class Client:

    def __init__(self):
        import socket
        self.s1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.s2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    def __down_thread(self,filename,ip,encode="gb2312"):
        import struct,os
        request = struct.pack(f"!H{len(filename.encode(encode))}sb5sb",1
                              ,filename.encode(encode),0,"octet".encode(),0)
        self.s1.sendto(request,(ip,69))
        f = open(filename,"ab")
        flag = True
        num1 = 0
        while True:
            datapack = self.s1.recvfrom(1024)
            oper, num = struct.unpack("!HH",datapack[0][:4])
            if oper == 5:
                print("查无此文件")
                flag = False
                f.close()
                break
            data = datapack[0][4:]
            num1 += len(data)
            f.write(data)
            print(f"文件：{filename}已下载{num1/(2**20)}MB")
            if len(data) < 512:
                print(f"文件：{filename}接收完毕")
                f.close()
                break
            ack = struct.pack("!HH",4,num)
            self.s1.sendto(ack,datapack[1])
        if not flag:
            os.remove(filename)

    def __up_thread(self,filename,ip,encode="gb2312"):
        import struct, os
        filesize = os.path.getsize(filename)
        request = struct.pack(f"!H{len(filename.encode(encode))}sb5sb", 2
                              , filename.encode(encode), 0, "octet".encode(), 0)
        self.s2.sendto(request, (ip, 69))
        f = open(filename, "rb")
        num1 = 0
        while True:
            datapack = self.s2.recvfrom(1024)
            oper, num = struct.unpack("!HH", datapack[0][:4])
            if oper != 4:
                print("文件重复")
                f.close()
                break
            data = f.read(512)
            num1 += 512
            print(f"文件：{filename}当前上传{num1/filesize:.2%}")
            if num == 65535:
                num = -1
            datapack2 = struct.pack("!HH512s",3,num+1,data)

            self.s2.sendto(datapack2,datapack[1])
            if len(data) < 512:
                print(f"文件{filename}发送完毕")
                f.close()
                break

    def up(self,filename,ip,encode="gb2312"):
        import threading
        t = threading.Thread(target=self.__up_thread,args=(filename,ip,encode))
        t.start()

    def down(self,filename,ip,encode="gb2312"):
        import threading
        t = threading.Thread(target=self.__down_thread,args=(filename,ip,encode))
        t.start()
client1 = Client()
# client1.up("LOL.jpg","127.0.0.1")
# client1.down("LOL.jpg","127.0.0.1")
client1.up("LOL.jpg","127.0.0.1")
# client1.up("梦想1.flv","127.0.0.1")
# client1.down("梦想.flv","127.0.0.1")
client1.down("001.png","127.0.0.1")