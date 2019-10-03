import hashlib
import json
from core import src
from conf import setting

user_status = src.user_status
userinfo_path = setting.userinfo_path


def judge(user_status):
    """
    判断是否已登录
    :return:
    """
    def wrapper(func):
        def inner(*args,**kwargs):
            if user_status["login_status"] == True:
                if user_status["choice"] != "1":
                    func(user_status)
                else:
                    print("您已登录！")
                    return
            else :
                print("请先登录！")
                ret = login()
                return func(ret)
        return inner
    return wrapper




def login():
    """
    1.登录功能
    :return:
    """
    if user_status["login_status"]:
        print("您已登录！")
        return
    count = 3
    while count:
        user_name = input("请输入用户名：")
        user_pwd = input("请输入密码：")
        user_pwd_has = hashlib.md5((user_name + user_pwd).encode("utf-8"))
        with open(userinfo_path,"a+",encoding="utf-8") as f:
            f.seek(0)
            for i in f:
                if json.loads(i) == {"name": user_name, "pwd": user_pwd_has.hexdigest()}:
                    print("登录成功！")
                    user_status["login_status"] = True
                    user_status["username"] = user_name
                    return user_status
            else:
                count -= 1
                print(f"账号或密码错误！剩余错误次数：{count}")
                if count == 0:
                    exit()