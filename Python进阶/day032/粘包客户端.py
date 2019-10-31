from socket import socket
import struct
s = socket()
s.connect(("192.168.34.170",7879))
while True:
    try:
        s.send(input("输入指令").encode())
        data1 = s.recv(4)
        print(data1)
        head_len1 = struct.unpack("!i",data1)
        print(head_len1)
        head_len = struct.unpack("!i",data1)[0]
        print(head_len)
        rec_data = b""
        while len(rec_data) < head_len:
            gap = head_len - len(rec_data)
            if gap <= 1024:
                rec_data += s.recv(gap)
                break
            else:
                rec_data += s.recv(1024)
        print(rec_data.decode("gbk"))
    except:
        print("有错")
        break
s.close()