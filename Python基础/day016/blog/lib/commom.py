from core import src
from conf import setting
login_dic = src.login_dic
def login(func=None):
    """
    登录
    :return:
    """
    while login_dic["count"]:
        user = input("username:")
        pwd = input("password:")
        with open(setting.File_PATH,"a+",encoding="utf-8")as f:
            f.seek(0)
            for i in f:
                file_user,file_pwd = i.strip().split(":")
                if file_user == user and file_pwd == pwd:
                    login_dic["count"] = 3
                    login_dic["username"] = user
                    login_dic["flag"] = True
                    print("登录成功!")
                    if func:
                        func() # log()
                    return
            else:
                login_dic["count"] -= 1
                print("账号或密码错误!")
                if login_dic["count"] == 0:
                    exit()
