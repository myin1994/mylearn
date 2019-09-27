"""
第二周大作业
"""

"""
三.用代码模拟博客园系统

项目分析：
1．首先程序启动，显示下面内容供用户选择：

1.请登录
2.请注册
3.进入文章页面
4.进入评论页面
5.进入日记页面
6.进入收藏页面
7.注销账号
8.退出整个程序
2．必须实现的功能：

1.注册功能要求：
a.用户名、密码要记录在文件中。
b.用户名要求：不能有特殊字符并且确保用户名唯一。
c.密码要求：长度要在6~14个字符之间。

2.登录功能要求：
a.用户输入用户名、密码进行登录验证。
b.登录成功之后，才可以访问3 - 7选项，如果没有登录或者登录不成功时访问3 - 7选项，不允许访问,提示用户进行登录!
c.超过三次登录还未成功，则退出整个程序。
3.进入文章页面要求：
提示欢迎xx进入文章页面。(xx是当前登录的用户名)

4.进入评论页面要求：

​	提示欢迎xx进入评论页面

5.进入日记页面要求：
提示欢迎xx进入日记页面。

6.进入收藏页面要求：
提示欢迎xx进入收藏页面。

7.注销账号要求：
不是退出整个程序，而是将已经登录的状态变成未登录状态（在次访问3~7选项时需要重新登录）

8.退出整个程序要求：
就是结束整个程序
"""


# def login():
#     """
#     登录功能，记录登录状态，登录次数，登录用户名
#     :return:
#     """
#     global login_status,login_count,name
#     if login_status:
#         print("已登录")
#         return
#     print("请登录！")
#     name = input("请输入用户名：")
#     psw = input("请输入密码：")
#     f = open("userinfo.txt","r",encoding="utf-8")
#     for i in f:
#         if i.split(":")[0] == name and i.split(":")[1] == psw:
#             print("登录成功！")
#             login_status = True
#             login_count = 3
#             break
#     if not login_status:
#         login_count -= 1
#         print(f"用户名或密码错误！登录失败！剩余次数{login_count}")
#     f.close()
#
#
# def register():
#     """
#     注册功能
#     :return:
#     """
#     f = open("userinfo.txt", "a+", encoding="utf-8")
#     while True:
#         name = input("请输入注册用户名（不能有特殊字符）：")
#         psw = input("请输入注册密码（6~14个字符之间）：")
#         f1 = open("userinfo.txt", "r", encoding="utf-8")
#         for i in f1:
#             if i.split(":")[0] == name:
#                 print("用户名重复！请重新注册！")
#                 return
#         f1.close()
#         if name.isalnum():
#             if  5 < len(psw) < 15:
#                 print("注册成功！")
#                 f.write(f"\n{name}:{psw}")
#                 f.flush()
#                 f.close()
#                 break
#             else:
#                 print("密码长度不符合要求！")
#                 continue
#         else:
#             print("用户名不能有特殊字符！")
#
#
# def article():
#     """
#     文章页面
#     :return:
#     """
#     if login_status == False:
#         print("登录后可使用该功能！")
#     else:
#         print(f"欢迎{name}进入文章页面")
#
# def comment():
#     """
#     评论页面
#     :return:
#     """
#     if login_status == False:
#         print("登录后可使用该功能！")
#     else:
#         print(f"欢迎{name}进入评论页面")
#
# def diary():
#     """
#     日记页面
#     :return:
#     """
#     if login_status == False:
#         print("登录后可使用该功能！")
#     else:
#         print(f"欢迎{name}进入日记页面")
#
# def collect():
#     """
#     收藏页面
#     :return:
#     """
#     if login_status == False:
#         print("登录后可使用该功能！")
#     else:
#         print(f"欢迎{name}进入收藏页面")
#
# def cancel():
#     """
#     注销当前账号
#     :return:
#     """
#     global login_status
#     if login_status == False:
#         print("登录后可使用该功能！")
#     else:
#         print("注销成功")
#         login_status = False
#
# def logout():
#     """
#     退出程序
#     :return:
#     """
#     global logout_status
#     print("退出成功！")
#     logout_status = True
#
#
# msg = """
# 1.登录
# 2.注册
# 3.进入文章页面
# 4.进入评论页面
# 5.进入日记页面
# 6.进入收藏页面
# 7.注销账号
# 8.退出整个程序
# 请输入选择序号："""
#
#
# func_choice = {
#     "1":login,
#     "2":register,
#     "3":article,
#     "4":comment,
#     "5":diary,
#     "6":collect,
#     "7":cancel,
#     "8":logout
# }
# login_count = 3
# login_status = False
# logout_status = False
# name = None
# def system_choice():
#     """
#     功能选择
#     :return:
#     """
#     while True:
#         choice = input(msg)
#         if choice in func_choice:
#             func_choice[choice]()
#             if logout_status == True or login_count == 0:
#                 break
#         else:
#             print("输入错误！请重新选择！")
# system_choice()

"""
四.用代码实现三次用户登录及锁定(选做题,这是一个单独的程序)
项目分析:
一.首先程序启动,显示下面内容供用户选择:
1.注册
2.登录

a.用户选择登录的时候,首先判断用户名在userinfo.txt表中存在不在,存在就不能进行注册
b.当注册的用户名不存在的时候将用户名和密码写入到userinfo.txt文件中
c.用户选择登录的时候,判断用户输入的账号和密码是否userinfo.txt存储的一致
d.用户名和密码一致就终止循环,并提示用户登录成功!
e.用户名和密码不一致,只有三次登录机会,三次过后提示用户名被锁定,请联系管理员!并终止循环
f.当用户名错误三次,再次运行程序.登录锁定的账号继续提示用户名被锁定,请联系管理员!
"""
def login():
    """
    登录功能，记录登录状态，登录次数，登录用户名
    :return:
    """
    global login_status,name
    login_count = 3
    if login_status:
        print("已登录！")
        return
    print("请登录！")
    while not login_status:
        name = input("请输入用户名：")
        if lock_status(name):
            print("用户名被锁定,请联系管理员!")
            return
        psw = input("请输入密码：")
        f = open("userinfo.txt", "r", encoding="utf-8")
        for i in f:
            if i.split(":")[0] == name and i.split(":")[1] == psw:
                print("登录成功！")
                login_status = True
                break
        if not login_status:
            login_count -= 1
            print(f"用户名或密码错误！登录失败！剩余次数{login_count}")
            if login_count == 0:
                lock_account(name)
                print("用户名被锁定,请联系管理员!")
                break
        f.close()



def register():
    """
    注册功能
    :return:
    """
    f = open("userinfo.txt", "a+", encoding="utf-8")
    while True:
        name = input("请输入注册用户名（不能有特殊字符）：")
        psw = input("请输入注册密码（6~14个字符之间）：")
        f1 = open("userinfo.txt", "r", encoding="utf-8")
        for i in f1:
            if i.split(":")[0] == name:
                print("用户名重复！")
                return
        f1.close()
        if name.isalnum():
            if  5 < len(psw) < 15:
                print("注册成功！")
                f.write(f"\n{name}:{psw}:")
                f.flush()
                f.close()
                break
            else:
                print("密码长度不符合要求！")
                continue
        else:
            print("用户名不能有特殊字符！")
def cancel():
    """
    注销当前账号
    :return:
    """
    global login_status
    if login_status == False:
        print("登录后可使用该功能！")
    else:
        print("注销成功")
        login_status = False

def logout():
    """
    退出程序
    :return:
    """
    global logout_status
    print("退出成功！")
    logout_status = True

def lock_status(name):
    """
    检查用户是否被锁定
    :param name:
    :return: 被锁定返回True 没有返回False
    """
    f = open("userinfo.txt","r",encoding="utf-8")
    for i in f:
        if i.split(":")[0] == name and i.split(":")[-1].strip() == "Y":
            f.close()
            return True
    else:
        f.close()
        return False

def lock_account(name):
    f = open("userinfo.txt", "r+", encoding="utf-8")
    for i in f:
        if i.split(":")[0] == name:
            f.write("Y")
            f.close()
            return
    else:
        f.write(f"\n{name}:{'None'}:Y")
msg = """
1.登录
2.注册
3.注销
4.退出
请输入选择序号："""

func_choice = {
    "1":login,
    "2":register,
    "3":cancel,
    "4":logout
}

login_status = False
logout_status = False
def system_choice():
    """
    功能选择
    :return:
    """
    while True:
        choice = input(msg)
        if choice in func_choice:
            func_choice[choice]()
            if logout_status == True:
                break
        else:
            print("输入错误！请重新选择！")
system_choice()