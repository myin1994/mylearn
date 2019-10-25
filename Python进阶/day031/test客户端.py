from socket import *
import time
s = socket()
s.bind(("192.168.34.170",7879))
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.connect(("192.168.34.170",7891))
num = 0

num += 1
# s.send(f"客户端连接中{num}".encode())
data1 = s.recv(1024).decode()

s.close()
print(data1)
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