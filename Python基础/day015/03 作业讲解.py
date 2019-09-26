"""
1.请实现一个装饰器，限制该函数被调用的频率，如10秒一次（面试题）
"""
# import time
# def wrapper(func):
#     s_time = 0
#     def inner(*args,**kwargs):
#         nonlocal s_time
#         if time.time() - s_time >= 3:
#             func(*args,**kwargs)
#             s_time = time.time()
#         else:
#             print("被限制了")
#     return inner
#
# @wrapper
# def index():
#     print("is index")
#
# while True:
#     index()
#     time.sleep(1)
msg = """
1,京东首页
2,京东超市
3,淘宝首页
4,淘宝超市
5,退出程序
>>>
"""

choose = input(msg)
login_dic = {"JD":False,"TB":False}
def auth(arg):
    def wrapper(func):
        def inner(*args,**kwargs):
            user = input("user")
            pwd = input("pwd")
            if arg == "1" or arg == "2":
                with open("jd","a+",encoding="utf-8") as f:
                    f.seek(0)
                    for i in f:
                        u,p =i.strip().split(":")
                        if user == u and p == pwd:
                            login_dic["JD"]  = True
                            func(*args,**kwargs)
                    else:
                        print("账号密码错误")
            elif arg == "1" or arg == "2":
            func()
        return inner
    return wrapper

@auth(choose)
def jd_shopping():
    print("京东商城")

@auth(choose)
def jd_index():
    print("京东首页")

@auth(choose)
def tb_shopping():
    print("淘宝商城")

@auth(choose)
def tb_index():
    print("京东")

if choose == "1":
    jd_index()
