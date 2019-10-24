import socket
import struct

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))  # 与客户端建立连接， 拨号

while 1:
    cmd = input('>>>')
    phone.send(cmd.encode('utf-8'))
    # 1. 接收固定长度报头
    data_head = phone.recv(4)

    # 2. 获取数据总长度
    total_size = struct.unpack('i', data_head)[0]
    total_data = b''
    while len(total_data) < total_size:
        total_data += phone.recv(1024)
    print(total_data.decode('gbk'))

phone.close()