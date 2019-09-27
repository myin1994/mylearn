import hashlib
import sys
import os
import json
def login(*args):
    """
    登录功能，记录登录状态，登录次数，登录用户名
    :return:
    """
    global name
    login_count = 3
    if user_dic["login_status"]:
        print("已登录！")
        return
    print("请登录！")
    while not user_dic["login_status"]:
        name = input("请输入用户名：")
        if lock_status(name):
            print("用户名被锁定,请联系管理员!")
            return
        psw = input("请输入密码：")
        md5 = hashlib.md5()  # 初始化加密算法
        md5.update(psw.encode("utf-8"))
        f = open("userinfo.txt", "r", encoding="utf-8")
        for i in f:
            if i.split(":")[0] == name and i.split(":")[1] == md5.hexdigest():
                print("登录成功！")
                user_dic["login_status"] = True
                break
        if not user_dic["login_status"] and not lock_status(name):
            lock_account(name)
            f3 = open(log_path, "r", encoding="utf-8")
            error_times = 0
            for i in f3:
                if json.loads(i).get(name) != None:
                    error_times = json.loads(i).get(name)
                    print(f"用户名或密码错误！登录失败！剩余次数{3-error_times}")
                    f3.close()
                    break
            if error_times == 3:
                print("用户名被锁定,请联系管理员!")
                break
        f.close()


def register(*args):
    """
    注册功能
    :return:
    """
    f = open("userinfo.txt", "a+", encoding="utf-8")
    f2 = open("userlog.txt", "a+", encoding="utf-8")
    while True:
        name = input("请输入注册用户名（不能有特殊字符）：")
        psw = input("请输入注册密码（6~14个字符之间）：")
        f1 = open("userinfo.txt", "r", encoding="utf-8")
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
        func()
    else:
        print(f"欢迎{name}进入文章页面")

def comment(func):
    """
    评论页面
    :return:
    """
    if user_dic["login_status"] == False:
        print("登录后可使用该功能！")
        func()
    else:
        print(f"欢迎{name}进入评论页面")

def diary(func):
    """
    日记页面
    :return:
    """
    if user_dic["login_status"] == False:
        print("登录后可使用该功能！")
        func()
    else:
        print(f"欢迎{name}进入日记页面")

def collect(func):
    """
    收藏页面
    :return:
    """
    if user_dic["login_status"] == False:
        print("登录后可使用该功能！")
        func()
    else:
        print(f"欢迎{name}进入收藏页面")

def cancel(func):
    """
    注销当前账号
    :return:
    """
    if user_dic["login_status"] == False:
        print("登录后可使用该功能！")
        func()
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

base_path = os.path.dirname(os.getcwd())
# log_path = os.path.join(base_path,"day016","blog_mayang",'userlog.txt')
# log_path2 = os.path.join(base_path,"day016","blog_mayang",'userlog2.txt')
log_path = r"C:\Users\24479\Desktop\作业上传\Python基础\day016\blog_mayang\userlog.txt"
log_path2 = r"C:\Users\24479\Desktop\作业上传\Python基础\day016\blog_mayang\userlog2.txt"

def lock_status(name):
    """
    检查用户是否被锁定
    :param name:
    :return: 被锁定返回True 没有返回False
    """
    f = open("userlog.txt","r",encoding="utf-8")
    for i in f:
        if json.loads(i).get(name) == 3:
            f.close()
            return True
    else:
        f.close()
        return False

def lock_account(name):
    with open("userlog.txt", "r", encoding="utf-8") as f1,open("userlog2.txt", "w", encoding="utf-8") as f2:
        for i in f1:
            j = json.loads(i)
            if j.get(name) == None:
                f2.write(json.dumps(j,ensure_ascii=False) + "\n")
            else:
                j[name] += 1
                f2.write(json.dumps(j,ensure_ascii=False) + "\n")
    os.rename("userlog.txt","userlog.txt.bak")
    os.rename("userlog2.txt","userlog.txt")
    os.remove("userlog.txt.bak")

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

user_dic = {"login_status":False,"logout_status":False}

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
run()
