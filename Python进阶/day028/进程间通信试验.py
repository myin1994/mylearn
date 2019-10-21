# from multiprocessing import Pool,Manager
# import time
# def sender(lst,content):
#     for i in content:
#         for j in lst:
#             j.put(i)
#     print("写入成功")
#
# def read(i,q):
#
#     while True:
#         print(i,"读取",q.get())
#         if q.empty():
#             break
#
# if __name__ == "__main__":
#
#     lst = [Manager().Queue() for i in range(5)]
#     po1 = Pool(len(lst)+1)
#     # sender(lst,"你好")
#     po1.apply_async(func=sender,args=(lst,"你好"))
#     time.sleep(1)
#     for i in lst:
#         po1.apply_async(func=read,args=(lst.index(i),i))
#     po1.close()
#     po1.join()

# from multiprocessing import Pool,Manager,Queue,Process
#
# import time
# def sender(lst,content):
#
#     print("sender",lst)
#     for i in content:
#         for j in lst:
#             j.put(i)
#     print("写入成功")
#     return lst
#
#
#
# if __name__ == "__main__":
#     def receiver(lst):
#         print("receicer",lst)
#         # for i in lst:
#         #     print(i.get())
#
#         def read(i, q):
#             print(3)
#             while True:
#                 print(i, "读取", q.get())
#                 if q.empty():
#                     break
#
#         po = Pool()
#         # sender(lst,"你好")
#         time.sleep(1)
#         for i in range(len(lst)):
#             print(1)
#             po.apply_async(func=read,args=(i,lst[i]))
#             time.sleep(1)
#
#         po.close()
#         po.join()
#
#     lst = [Manager().Queue() for i in range(5)]
#     po1 = Pool(1)
#     # sender(lst,"你好")
#     po1.apply_async(func=sender,args=(lst,"你好"),callback=receiver)
#     po1.close()
#     po1.join()