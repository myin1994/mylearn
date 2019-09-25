"""
s_26 day14作业
"""

"""
1.请实现一个装饰器，限制该函数被调用的频率，如10秒一次（面试题）
"""
# import functools
# import time
# def foo(time_now):
#     f1 = open("time.txt","a+",encoding="utf-8")
#     f1.seek(0)
#     time_before = 0
#     for i in f1:
#         time_before = i.strip()
#     time_gap = time_now - float(time_before)
#     print(f"距离上次运行程序时间间隔：{time_gap}")
#     def wrapper(func):
#         @functools.wraps(func)
#         def inner():
#             if time_gap > 10:
#                 ret = func()
#                 f1.write(f"\n{time_now}")
#                 return ret
#             else:
#                 print("请10s后再运行程序！")
#                 f1.write(f"\n{time_now}")
#         return inner
#     return wrapper
#
#
# @foo(time.time())
# def index():
#     print("程序运行成功！")
#
#
# index()

"""
2.请写出下列代码片段的输出结果：

def say_hi(func):
  def wrapper(*args,**kwargs):
      print("HI")
      ret=func(*args,**kwargs)
      print("BYE")
      return ret
  return wrapper

def say_yo(func):
  def wrapper(*args,**kwargs):
      print("Yo")
      return func(*args,**kwargs)
  return wrapper
@say_hi
@say_yo
def func():
  print("ROCK&ROLL")
func()
HI
Yo
ROCK&ROLL
BYE
验证正确
"""

"""
3.编写装饰器完成下列需求:
用户有两套账号密码,一套为京东账号密码，一套为淘宝账号密码分别保存在两个文件中。
设置四个函数，分别代表 京东首页，京东超市，淘宝首页，淘宝超市。
启动程序后,呈现用户的选项为:
1,京东首页
2,京东超市
3,淘宝首页
4,淘宝超市
5,退出程序
四个函数都加上认证功能，用户可任意选择,用户选择京东超市或者京东首页,只要输入一次京东账号和密码并成功,则这两个函数都可以任意访问;
用户选择淘宝超市或者淘宝首页,只要输入一次淘宝账号和密码并成功,则这两个函数都可以任意访问.
相关提示：用带参数的装饰器。装饰器内部加入判断，验证不同的账户密码。
"""

# def login(flag,func,file_name="JDdata"):
#     """
#     登录函数
#     :param flag: 装饰器参数
#     :param func:
#     :param file_name: 文件名
#     :return:
#     """
#     username = input("请输入用户名：")
#     psw = input("请输入密码：")
#     f1 = open(file_name, "r", encoding="utf-8")
#     for i in f1:
#         if i.split(":")[0] == username and i.split(":")[1] == psw:
#             print("登录成功！")
#             flag[1] = False
#             flag[2] = True
#             return func()
#     else:
#         print("账号或密码错误！")
#
# def auth(flag):
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             if flag1[1] and not flag1[2]:
#                 return login(flag1,func)
#             elif flag1[1]:
#                 return func(*args, **kwargs)
#             if flag2[1] and not flag2[2]:
#                 return login(flag2,func,file_name="TBdata")
#             elif flag2[2]:
#                 return func(*args, **kwargs)
#         return inner
#     return wrapper
#
# flag1 ={1:True,2:False}
# flag2 ={1:True,2:False}
#
# @auth(flag1)
# def jd_home():
#     print("欢迎进入京东首页！")
#
# @auth(flag1)
# def jd_market():
#     print("欢迎进入京东超市！")
#
# @auth(flag2)
# def tb_home():
#     print("欢迎进入淘宝首页！")
#
# @auth(flag2)
# def tb_market():
#     print("欢迎进入淘宝超市！")
#
# def logout():
#     print("退出程序成功！")
#
#
# msg = """
# 1,京东首页
# 2,京东超市
# 3,淘宝首页
# 4,淘宝超市
# 5,退出程序
# 请选择序号（1~5）：
# """
#
# choice_dic = {"1":jd_home,
#               "2":jd_market,
#               "3":tb_home,
#               "4":tb_market,
#               "5":logout}
#
# while True:
#     choice = input(msg)
#     if choice in choice_dic:
#         if choice == "5":
#             choice_dic[choice]()
#             break
#         else:
#             if choice == "1" or choice == "2":
#                 flag2[1], flag1[1] = False, True
#             else:
#                 flag1[1], flag2[1] = False, True
#             choice_dic[choice]()
#     else:
#         print("请输入正确序号！")

"""
4.给l1 = [1,1,2,2,3,3,6,6,5,5,2,2]去重，不能使用set集合（面试题）。
"""
# l1 = [1,1,2,2,3,3,6,6,5,5,2,2]
# for i in l1.copy():
#     if l1.count(i) > 1:
#         l1.remove(i)
# print(l1)

# l1 = [1,1,2,2,3,3,6,6,5,5,2,2]
# l2 =[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)

"""
5.用递归函数完成斐波那契数列（面试题）：
斐波那契数列：1，1，2，3，5，8，13，21..........(第三个数为前两个数的和，但是最开始的1，1是特殊情况，可以单独讨论)
"""
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(6))
# print(list(map(fib,list(range(1,7)))))

"""
6.用户输入序号获取对应的斐波那契数字：比如输入6，返回的结果为8.
"""
# def fib(n):
#     lst = []
#     a, b =0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a
# print(fib(6))