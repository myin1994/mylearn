import json
import time
import hashlib
user_status = {"login_status":False,"choice":None,"username":None}

from conf import setting
from lib import common

judge = common.judge
login = common.login

userinfo_path = setting.userinfo_path
comment_path = setting.comment_path
diary_path = setting.diary_path

def sign_in():
    """
    2.注册功能
    :return:
    """
    while True:
        sign_in_name = input("请输入注册名（只能含有字母中文或者数字，不能含有特殊字符）：")
        sign_in_pwd = input("请输入注册密码（6~14个字符）：")
        if not sign_in_name.isalnum():
            print("无效用户名，请重新输入！")
            continue
        elif len(sign_in_pwd) < 6 or len(sign_in_pwd) > 14:
            print("密码长度错误，请重新输入！")
            continue
        else:
            with open(userinfo_path,"a+",encoding="utf-8") as f:
                f.seek(0)
                for i in f:
                    if json.loads(i)["name"] == sign_in_name:
                        print("用户名重复！")
                        break
                else:
                    sign_in_pwd_has = hashlib.md5((sign_in_name+sign_in_pwd).encode("utf-8"))
                    f.write("\n" + json.dumps({"name":sign_in_name,"pwd":sign_in_pwd_has.hexdigest()}))
                    print("注册成功！")
                    break

@judge(user_status)
def article(user_status):
    """
    3.文章页面
    :return:
    """
    print(f"欢迎{user_status['username']}进入文章页面")

@judge(user_status)
def comment(user_status):
    """
    4.评论页面
    :return:
    """
    print(f"欢迎{user_status['username']}进入评论页面")
    while True:
        with open(comment_path,"a+",encoding="utf-8") as f:
            f.seek(0)
            line = 0
            for i in f:
                line += 1
                comment_dic = json.loads(i)
                print(f"{comment_dic['line']}楼 -{comment_dic['username']}：{comment_dic['comment']}")
            comment_choice = input("请选择是否需要评论（Y-是|其他任意-否）：")
            if comment_choice.upper() == "Y":
                user_comment = input("请输入评论内容：")
                f.write("\n" + json.dumps({"line":line + 1,"username":user_status["username"],"comment":user_comment}))
            else:
                break

@judge(user_status)
def diary(user_status):
    """
    5.日记页面
    :return:
    """
    print(f"欢迎{user_status['username']}进入日记页面")
    while True:
        dipath = diary_path + "\\" + user_status['username']+".txt"
        with open(dipath,"a+",encoding="utf-8") as f:
            f.seek(0)
            for i in f:
                diary_dic = json.loads(i)
                print(f"记录时间：{diary_dic['time']}\n日记内容：{diary_dic['content']}")
            diary_choice = input("请选择是否需要记录日记（Y-是|其他任意-否）：")
            if diary_choice.upper() == "Y":
                user_diary = input("请输入日记内容：")
                f.write(json.dumps({"time": time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime()),
                                           "content": user_diary}) + "\n")
            else:
                break

@judge(user_status)
def collect(user_status):
    """
    6.收藏页面
    :return:
    """
    print(f"欢迎{user_status['username']}进入收藏页面")

@judge(user_status)
def logout(user_status):
    """
    7.注销功能
    :return:
    """
    user_status["login_status"] = False
    print("您已注销当前账户！")

def exit_blog():
    """
    8.退出程序
    :return:
    """
    print("您已退出程序！")
    exit()

choice_dict = {"1":login,
               "2":sign_in,
               "3":article,
               "4":comment,
               "5":diary,
               "6":collect,
               "7":logout,
               "8":exit_blog}

msg = """
1.请登录
2.请注册
3.进入文章页面
4.进入评论页面
5.进入日记页面
6.进入收藏页面
7.注销账号
8.退出整个程序
请选择序号："""

def run():
    while True:
        choice = input(msg)
        user_status[1] = choice
        if user_status[1] in choice_dict:
            choice_dict[user_status[1]]()
        else:
            print("输入有误，请重新选择！")

