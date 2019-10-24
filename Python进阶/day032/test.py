import socket
import subprocess
import struct
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8080))
phone.listen(5)
while 1:  # 循环连接客户端
    conn, client_addr = phone.accept()
    print(client_addr)
    while 1:
        try:
            cmd = conn.recv(1024)
            ret = subprocess.Popen(cmd.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            correct_msg = ret.stdout.read()
            error_msg = ret.stderr.read()
            # 1.获取总长度
            total_size = len(correct_msg) + len(error_msg)  # 7865
            # 2. 制作等长度的报头
            # 将一个数字（不定长的int类型）转化成等长度的bytes类型。# total_size int数据类型。--->bytes
            ret = struct.pack('i', total_size)
            # 3. 发送固定长度的报头
            conn.send(ret)
            # 4. 发送数据
            conn.send(correct_msg + error_msg)
            conn.send(ret)
            conn.send(correct_msg + error_msg)

        except ConnectionResetError:
            break
    conn.close()
phone.close()