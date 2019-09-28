user_dic = {"name":None,"login_status":False,"logout_status":False}
import hashlib
import json
from lib import common
from conf import setting
login = common.login

userinfo_PATH = setting.userinfo_PATH
userlog_PATH = setting.userlog_PATH
userlog2_PATH = setting.userlog2_PATH
name = user_dic["name"]
def register(*args):
    """
    注册功能
    :return:
    """
    f = open(userinfo_PATH, "a+", encoding="utf-8")
    f2 = open(userlog_PATH, "a+", encoding="utf-8")
    while True:
        name = input("请输入注册用户名（不能有特殊字符）：")
        psw = input("请输入注册密码（6~14个字符之间）：")
        f1 = open(userinfo_PATH, "r", encoding="utf-8")
        for i in f1:
            if i.split(":")[0] == name:
                print("用户名重复！请重新注册！")
                return
        f1.close()
        if name.isalnum():
            if  5 < len(psw) < 15:
                print("注册成功！")
                md5 = hashlib.md5()  # 初始化加密算法
                md5.update(psw.encode("utf-8"))
                f.write(f"\n{name}:{md5.hexdigest()}")
                f2.write(json.dumps({name:0},ensure_ascii=False) + "\n")
                f.flush()
                f.close()
                break
            else:
                print("密码长度不符合要求！")
                continue
        else:
            print("用户名不能有特殊字符！")


def article(func):
    """
    文章页面
    :return:
    """
    if user_dic["login_status"] == False:
        print("登录后可使用该功能！")
        func(fun = article)
    else:
        print(f"欢迎{name}进入文章页面")

def comment(func):
    """
    评论页面
    :return:
    """
    if user_dic["login_status"] == False:
        print("登录后可使用该功能！")
        func(fun = comment)
    else:
        print(f"欢迎{name}进入评论页面")

def diary(func):
    """
    日记页面
    :return:
    """
    if user_dic["login_status"] == False:
        print("登录后可使用该功能！")
        func(fun = diary)
    else:
        print(f"欢迎{name}进入日记页面")

def collect(func):
    """
    收藏页面
    :return:
    """
    if user_dic["login_status"] == False:
        print("登录后可使用该功能！")
        func(fun = collect)
    else:
        print(f"欢迎{name}进入收藏页面")

def cancel(func):
    """
    注销当前账号
    :return:
    """
    if user_dic["login_status"] == False:
        print("登录后可使用该功能！")
        func(fun = cancel)
    else:
        print("注销成功")
        user_dic["login_status"] = False

def logout(*args):
    """
    退出程序
    :return:
    """
    print("退出成功！")
    user_dic["logout_status"] = True




msg = """
1.登录
2.注册
3.进入文章页面
4.进入评论页面
5.进入日记页面
6.进入收藏页面
7.注销账号
8.退出整个程序
请输入选择序号："""


func_choice = {
    "1":login,
    "2":register,
    "3":article,
    "4":comment,
    "5":diary,
    "6":collect,
    "7":cancel,
    "8":logout
}



def run():
    """
    功能选择
    :return:
    """
    while True:
        choice = input(msg)
        if choice in func_choice:
            func_choice[choice](login)
            if user_dic["logout_status"] == True:
                break
        else:
            print("输入错误！请重新选择！")