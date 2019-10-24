from socket import socket
import time
s = socket()
s.bind(("192.168.34.170",7879))
s.connect(("192.168.34.170",7891))
num = 0
while True:
    # try:
    time.sleep(5)
    num += 1
    data = s.recv(1024)
    print(len(data))
    print(num)
        # while True:
        #     num += 1
        #     s.send(f"客户端连接中{num}".encode())
        #     data = s.recv(1024)
        #     print(data)
        #     if num == 199:
        #         s.close()
        #         # break


        # num += 1
        # # s.send(f"客户端连接中{num}".encode())
        # data1 = s.recv(1024).decode()
        # print(data1)
        # s.close()
        # # time.sleep(2)
        # print(s.recv(1024))
        # time.sleep(3)
        # print("端口正常了")
        # break
        # if len(data) == 0:
        #     print("结束位",data)
        #     s.close()
        #     break
        # print(data)
        # if num == 199:
        #     s.close()
            # break
    # except Exception as e:
    #     print(e)