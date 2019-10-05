import logging
import os
import json
import hashlib

from core import src
from conf import setting

user_status = src.user_status
basepath = setting.basepath

def log_write(user_status,action):
    logger = logging.getLogger() #创建一个空架子，与logging独立
    log_path = os.path.join(basepath, "log", user_status["username"] + ".log")
    fh = logging.FileHandler(log_path,"a",encoding="utf-8")  #创建一个文件句柄用来记录日志（文件流）
    formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)s %(message)s") #定义一个记录文件的格式
    fh.setFormatter(formater)  #给文件句柄设置记录内容的格式
    logger.addHandler(fh)  #将文件句柄添加到logger对象中

    logger.level = 20  #设置警告级别
    logger.info(f"用户：{user_status['username']} 操作：{action} 余额：{user_status['account_balance']}")
    logger.removeHandler(fh)


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
    error_name = []
    while count:
        user_name = input("请输入用户名：")
        user_pwd = input("请输入密码：")
        user_pwd_has = hashlib.md5((user_name + user_pwd).encode("utf-8"))
        userinfo_path = os.path.join(basepath, "db", user_name+".json")
        with open(userinfo_path,"a+",encoding="utf-8") as f:
            f.seek(0)
            if not f.read():
                error_name.append(user_name)
            f.seek(0)
            for i in f:
                if json.loads(i)["name"] == user_name and json.loads(i)["pwd"] == user_pwd_has.hexdigest():
                    print("登录成功！")
                    user_status["login_status"] = True
                    user_status["username"] = user_name
                    user_status["account_balance"] = json.loads(i)["account_balance"]
                    return user_status
            else:
                count -= 1
                print(f"账号或密码错误！剩余错误次数：{count}")
    for i in error_name:
        os.remove(os.path.join(basepath, "db", i + ".json"))
    if count == 0:
        exit()