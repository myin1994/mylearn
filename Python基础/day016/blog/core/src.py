login_dic = {
    "username":None,
    "flag":False,  # 登录成功是True 登录不成功是False
    "count":3
}

from lib import commom
from conf import setting
login = commom.login

def register():
    """
    注册
    :return:
    """
    user = input("username:")
    pwd = input("password:")
    with open(setting.File_PATH, "a+", encoding="utf-8")as f:
        f.seek(0)
        if user.isalpha() and 14 > len(pwd) > 6:
            for i in f:
                file_user, file_pwd = i.strip().split(":")
                if file_user == user:
                    print("用户名已存在!")
                    return
            else:
                f.write(f"{user}:{pwd}\n")
                print("注册成功！")
        else:
            print("注册失败")

def comment():
    print(f"欢迎{login_dic['username']}登录评论区")

def log():
    print(f"欢迎{login_dic['username']}登录日志区")

def article():
    print(f"欢迎{login_dic['username']}登录文章区")

def collect():
    print(f"欢迎{login_dic['username']}登录收藏区")

def log_out():
    login_dic["username"] = None
    login_dic["flag"] = False
    print("注销成功！")

func_dict = {
    "1":login,
    "2":register,
    "3":comment,
    "4":log,
    "5":article,
    "6":collect,
    "7":log_out,
    "8":exit
}

msg = """
1.请登录
2.请注册
3.进入文章页面
4.进入评论页面
5.进入日记页面
6.进入收藏页面
7.注销账号
8.退出整个程序
请输入序号:
"""
def run():
    while True:
        choose = input(msg)
        if choose in func_dict:
            if choose == "1" or  choose == "2" or  choose == "8":
                func_dict[choose]()
            elif login_dic['flag']:
                func_dict[choose]()
            else:
                login(func_dict[choose])  # login(log)
        else:
            print("请重新输入!")
