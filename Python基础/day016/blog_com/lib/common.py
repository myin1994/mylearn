import hashlib
import sys
import os
import json

from core import src
from conf import setting
user_dic = src.user_dic
userinfo_PATH = setting.userinfo_PATH
userlog_PATH = setting.userlog_PATH
userlog2_PATH = setting.userlog2_PATH

def login(*args,fun = None):
    """
    登录功能，记录登录状态，登录次数，登录用户名
    :return:
    """
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
        f = open(userinfo_PATH, "r", encoding="utf-8")
        for i in f:
            if i.split(":")[0] == name and i.split(":")[1] == md5.hexdigest():
                print("登录成功！")
                user_dic["login_status"] = True
                user_dic["name"] = name
                lock_clear(name)
                if fun:
                    return fun(login)
                break
        if not user_dic["login_status"] and not lock_status(name):
            lock_account(name)
            f3 = open(userlog_PATH , "r+", encoding="utf-8")
            error_times = 0
            for i in f3:
                if json.loads(i).get(name) != None:
                    error_times = json.loads(i).get(name)
                    print(f"用户名或密码错误！登录失败！剩余次数{3-error_times}")
                    f3.close()
                    break
            else:
                f3.write(json.dumps({name:1},ensure_ascii=False) + "\n")
                print(f"用户名或密码错误！登录失败！剩余次数{2}")
                f3.close()
            if error_times == 3:
                print("用户名被锁定,请联系管理员!")
                break
        f.close()

def lock_status(name):
    """
    检查用户是否被锁定
    :param name:
    :return: 被锁定返回True 没有返回False
    """
    f = open(userlog_PATH,"r",encoding="utf-8")
    for i in f:
        if json.loads(i).get(name) == 3:
            f.close()
            return True
    else:
        f.close()
        return False
def lock_account(name):
    with open(userlog_PATH, "r", encoding="utf-8") as f1,open(userlog2_PATH, "w", encoding="utf-8") as f2:
        for i in f1:
            j = json.loads(i)
            if j.get(name) == None:
                f2.write(json.dumps(j,ensure_ascii=False) + "\n")
            else:
                j[name] += 1
                f2.write(json.dumps(j,ensure_ascii=False) + "\n")
    os.rename(userlog_PATH,"userlog.txt.ba")
    os.rename(userlog2_PATH,userlog_PATH)
    os.rename("userlog.txt.ba",userlog2_PATH)

def lock_clear(name):
    with open(userlog_PATH, "r", encoding="utf-8") as f1,open(userlog2_PATH, "w", encoding="utf-8") as f2:
        for i in f1:
            j = json.loads(i)
            if j.get(name) == None:
                f2.write(json.dumps(j,ensure_ascii=False) + "\n")
            else:
                j[name] = 0
                f2.write(json.dumps(j,ensure_ascii=False) + "\n")
    os.rename(userlog_PATH, "userlog.txt.ba")
    os.rename(userlog2_PATH, userlog_PATH)
    os.rename("userlog.txt.ba", userlog2_PATH)