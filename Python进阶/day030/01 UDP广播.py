# from socket import *
# import gevent
# import threading
# s = socket(AF_INET,SOCK_DGRAM)
# s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
#
# s.bind(("",7788))
# lst1 = [i for i in range(1024,5000)]
# lst2 = [i for i in range(5000,10000)]
# r = "哈哈哈哈哈哈哈"*3000
# r1 = r.encode()
#
# def func1():
#     while True:
#         for i in lst1:
#             s.sendto(r1, ("192.168.34.255", i))
#             print(i)
#
# def func2():
#     while True:
#         for i in lst2:
#             s.sendto(r1, ("192.168.34.255", i))
#             print(i)
#
# g1 = threading.Thread(target=func1)
# g2 = threading.Thread(target=func2)
# g1.start()
# g2.start()
# # time.sleep(1)
# # data = s.recvfrom(1024)
# # print(data[0].decode())
# g1.join()
# g2.join()


from socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.sendto("hello".encode("GB2312"),("192.168.137.255",8080))