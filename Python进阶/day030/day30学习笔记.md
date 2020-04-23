## 硬件相关

+ 集线器（HUB）

  计算机网络中连接多个计算机或其他设备的连接设备，是对网络进行集中管理的最小单元。英文Hub就是中心的意思，像树的主干一样，它是各分支的汇集点。HUB是一个共享设备，主要提供信号放大和中转的功能，它把一个端口接收的所有信号向所有端口分发出去

+ 交换机(Switch)

  一种基于MAC（网卡的硬件地址）识别，能完成封装转发数据包功能的网络设备。交换机可以“学习”MAC地址，并把其存放在内部地址表中，通过在数据帧的始发者和目标接收者之间建立临时的交换路径，使数据帧直接由源地址到达目的地址。

+ 物理地址（实际地址）

  + 网络设备制造商生产时写在硬件内部
  + MAC地址是48位的（6个字节）
  + 前3组16进制数08:00:20代表网络硬件制造商的编号，它由IEEE（电气与电子工程师协会）分配
  + 后3组16进制数0A:8C:6D代表该制造商所制造的某个网络产品（如网卡）的系列号
  + MAC地址在世界是惟一的（可以直接理解为网卡的序列号）

+ 路由器

  + 确定一条路径的设备，路由器是连接因特网中用来链接网络号不同的、不同的网络，相当于中间人各局域网、广域网的设备，它会根据信道的情况自动选择和设定路由，以最佳路径，按前后顺序发送信号的设备。
  + 路由器的一个作用是连通不同的网络，另一个作用是选择信息传送的线路

  

## UDP广播

+ 概念

  + 当前网络上所有电脑的某个进程都收到同一个数据
  + 一般借助交换机分发数据

+ 实现

  + 修改套接字设置

    ```python
    from socket import *
    s = socket(AF_INET,SOCK_DGRAM)
    dest = ("<broadcast>",7788)
    s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)#设置套接字选项，允许s发送广播数据
    ```
  ```
  
  ```

+ 发送IP需要设置为255
  
    ```python
    s.sendto("hello".encode("GB2312"),("192.168.137.255",8080))
  ```
  
  + 一般使用while循环接收广播数据



## TFTP协议

TFTP（Trivial File Transfer Protocol,简单⽂件传输协议）是TCP/IP协议簇中的⼀个⽤来在客户端与服务器之间进⾏简单⽂件传输的协议。

+ 特点

  + 应用层协议，用于简单文件传输
  + 适合在局域网进行传递
  + 端口号固定为69---只用来接收读写请求
  + 基于UDP实现

+ TFTP下载器原理

  <img src="./day30学习笔记.assets/1571743672598.png">

  + 从服务器上将一个文件复制到本机上
  + 在本地创建一个空文件（与要下载的文件同名）
  + 向里面写数据（接收到一点就向空文件里写一点）
  + 关闭（接受完所有数据关闭文件）

+ TFTP格式要求

  + 读写请求包

    操作码（2Byte，1-下载\|2-上传）+文件名+0（1B）+传输模式（固定为octet-8位字节）+0（1B）

    | 操作码                  | 文件名 | 0     | 传输模式            | 0     |
    | ----------------------- | ------ | ----- | ------------------- | ----- |
    | 2Byte（1-下载\|2-上传） |        | 1Byte | 固定为octet-8位字节 | 1Byte |

  + 数据包

    操作码（2B，3-DATA）+块编号（2B，顺序0-65535）+数据（512B）

    客户端接收到小于516的数据时退出接收（发送时结束发送）

    | 操作码        | 块编号             | 数据    |
    | ------------- | ------------------ | ------- |
    | 2Byte(3-DATA) | 2Byte(顺序0-65535) | 512Byte |

  + 确认包（ACK）

    操作码（2B，4-ACK）+块编号（2B，顺序0-65535）

    | 操作码       | 块编号             |
    | ------------ | ------------------ |
    | 2Byte(4-ACK) | 2Byte(顺序0-65535) |

  + ERROR

    操作码（2B，5-error）+差错码（2B）+差错信息+0（1B）

    | 操作码         | 差错码 | 差错信息 | 0     |
    | -------------- | ------ | -------- | ----- |
    | 2Byte(5-error) | 2Byte  |          | 1Byte |

  <img src="./day30学习笔记.assets/1571744529192.png">

  

+ struct模块使用

  | **FORMAT** |     **C TYPE**     |  **PYTHON TYPE**   | **STANDARD SIZE** |
  | :--------: | :----------------: | :----------------: | :---------------: |
  |     x      |      pad byte      |      no value      |                   |
  |     c      |        char        | string of length 1 |         1         |
  |     b      |    signed char     |      integer       |         1         |
  |     B      |   unsigned char    |      integer       |         1         |
  |     ?      |       _Bool        |        bool        |         1         |
  |     h      |       short        |      integer       |         2         |
  |     H      |   unsigned short   |      integer       |         2         |
  |     i      |        int         |      integer       |         4         |
  |     I      |    unsigned int    |      integer       |         4         |
  |     l      |        long        |      integer       |         4         |
  |     L      |   unsigned long    |      integer       |         4         |
  |     q      |     long long      |      integer       |         8         |
  |     Q      | unsigned long long |      integer       |         8         |
  |     f      |       float        |       float        |         4         |
  |     d      |       double       |       float        |         8         |
  |     s      |       char[]       |       string       |                   |
  |     p      |       char[]       |       string       |                   |
  |     P      |       void *       |      integer       |                   |

  + q和Q只适用于64位机器;每个格式前可以有一个数字,表示这个类型的个数,如s格式表示一定长度的字符串,4s表示长度为4的字符串

  + pack() 将数据按一定格式打包

    ```python
    import struct
    #读写请求包
    pack = struct.pack("!H7sb5sb",1,"001.png".encode(),0,"octet".encode(),0)
    #!-大端模式（指数据的高字节保存在内存的低地址中，而数据的低字节保存在内存的高地址中）
    #H-将操作码1存储成2字节
    #7s-按文件名长度存储7字节
    #b-0存储为1字节
    #5s-传输模式长度存储5字节
    #b-0存储为1字节
    ```

  + unpack() 将数据包按给定格式解析成元组

    ```python
    opcode, block_number = struct.unpack("!HH",datapack[0][:4])#拆包出操作码和块编号
    ```

  + calcsize() 计算给定的格式(fmt)占用多少字节的内存

+ TFTP客户端上传下载总结

  + 下载

    + 客户端先给服务器（69端口）发送下载请求（读写请求包）
    + 以追加写字节模式创建文件句柄
    + 开始循环读取
    + 将服务器发回的数据包拆包，得到操作码、块编号、字节数据
    + 判断操作码是否为5（存在错误），正常应为3，有错则终止读取
    + 将拆包得到的数据写入文件
    + 判断数据长度是否小于512（小于则认为读取完毕退出）
    + 将拆包得到的块编号打包在ACK中并发回服务器

  + 上传

    + 客户端先给服务器（69端口）发送下载请求（读写请求包）
    + 以追读字节模式创建文件句柄
    + 开始循环上传
    + 将服务器发回的ACK确认包拆包，得到操作码、块编号
    + 判断操作码是否为4（允许上传），否则存在错误
    + 读取512字节，并按数据包格式将块编号加一（大文件需要注意判断块编号达到65535时需要重置为零），以及数据打包后发给服务器
    + 判断数据长度是否小于512（小于则认为发送完毕退出）

  + 程序实现（基础版）

    ```python
    #需要模拟服务器
    class Client:
    
        def __init__(self):
            import socket
            self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
        def down(self,filename,ip,encode="gb2312"):
            import struct,os
            request = struct.pack(f"!H{len(filename.encode(encode))}sb5sb",1
                                  ,filename.encode(encode),0,"octet".encode(),0)
            self.s.sendto(request,(ip,69))
            f = open(filename,"ab")
            flag = True
            while True:
                datapack = self.s.recvfrom(1024)
                oper, num = struct.unpack("!HH",datapack[0][:4])
                if oper == 5:
                    print("查无此文件")
                    flag = False
                    f.close()
                    break
                data = datapack[0][4:]
                f.write(data)
                if len(data) < 512:
                    print("接收完毕")
                    f.close()
                    break
                ack = struct.pack("!HH",4,num)
                self.s.sendto(ack,datapack[1])
            if not flag:
                os.remove(filename)
    
        def up(self,filename,ip,encode="gb2312"):
            import struct, os
            filesize = os.path.getsize(filename)
            request = struct.pack(f"!H{len(filename.encode(encode))}sb5sb", 2
                                  , filename.encode(encode), 0, "octet".encode(), 0)
            self.s.sendto(request, (ip, 69))
            f = open(filename, "rb")
            num1 = 0
            while True:
                datapack = self.s.recvfrom(1024)
                oper, num = struct.unpack("!HH", datapack[0][:4])
                if oper != 4:
                    print("文件重复")
                    f.close()
                    break
                data = f.read(512)
                num1 += 512
                print(f"当前上传{num1/filesize:.2%}")
                if num == 65535:
                    num = -1
                datapack2 = struct.pack("!HH512s",3,num+1,data)
    
                self.s.sendto(datapack2,datapack[1])
                if len(data) < 512:
                    print("发送完毕")
                    f.close()
                    break
    client1 = Client()
    client1.up("LOL.jpg","127.0.0.1")
    ```

    ```python
    #修正版
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
    client1.up("梦想.flv","127.0.0.1")
    # client1.up("梦想1.flv","127.0.0.1")
    # client1.down("梦想.flv","127.0.0.1")
    client1.down("梦想1.flv","127.0.0.1")
    ```

    