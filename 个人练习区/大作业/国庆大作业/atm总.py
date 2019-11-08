import hashlib
import json
import os
import logging
import re
basepath = os.path.dirname(os.getcwd())

userinfo2_path = os.path.join(basepath,"db","userinfo.bak")
user_status = {"login_status":False,"choice":None,"username":"None","account_balance":0}

# def log_write(user_status,action):
#     log_path = os.path.join(basepath, "log",user_status["username"] + ".log")
#     print(log_path)
#     logging.basicConfig(
#         level=20,
#         format="%(asctime)s %(name)s %(filename)s %(lineno)s %(message)s",
#         datefmt="%Y-%m-%d %H:%M:%S",
#         filename=log_path,
#         filemode="a"
#         )
#     logging.info(f"用户：{user_status['username']} 操作：{action} 余额：{user_status['account_balance']}")

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

msg = """
1.登录（可支持多个账户（非同时）登录）
2.注册
3.查看余额
4.存钱
5.转账（给其他用户转钱）
6.查看账户流水
7.退出
请选择功能序号："""

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
            userinfo_path = os.path.join(basepath, "db", sign_in_name+".json")
            with open(userinfo_path,"a+",encoding="utf-8") as f:
                f.seek(0)
                for i in f:
                    if json.loads(i)["name"] == sign_in_name:
                        print("用户名重复！")
                        break
                else:
                    sign_in_pwd_has = hashlib.md5((sign_in_name+sign_in_pwd).encode("utf-8"))
                    f.write(json.dumps({"name":sign_in_name,"pwd":sign_in_pwd_has.hexdigest(),"account_balance":0},
                                       ensure_ascii=False))
                    print("注册成功！")
                    break

@judge(user_status)
def account_balance(user_status):
    """
    3.查看余额
    :return:
    """
    print(f"用户：{user_status['username']} 当前账户余额：{user_status['account_balance']}")
    log_write(user_status,"查看余额")

@judge(user_status)
def save_money(user_status):
    """
    4.存钱功能
    :return:
    """
    while True:
        save_money_now = input("请输入要存入的钱数：")
        if re.match("[0-9]+\.*[1-9]*", save_money_now):
            if re.match("[0-9]+\.*[1-9]*", save_money_now).group() == save_money_now and float(save_money_now) > 0:
                print(f"成功存入{save_money_now}元")
                break
            else:
                print("输入金额错误请重新输入！")
        else:
            print("输入金额错误请重新输入！")
    userinfo_path = os.path.join(basepath, "db", user_status["username"] + ".json")
    with open(userinfo_path, "a+", encoding="utf-8") as f, open(userinfo2_path, "w", encoding="utf-8") as f1:
        f.seek(0)
        for i in f:
            user_dic = json.loads(i)
            if user_dic["name"] == user_status["username"]:
                user_dic["account_balance"] += float(save_money_now)
                user_status['account_balance'] += float(save_money_now)
            f1.write(json.dumps(user_dic,ensure_ascii=False) + "\n")
    log_write(user_status, f"存钱{save_money_now}元")
    os.rename(userinfo_path,"bak")
    os.rename(userinfo2_path,userinfo_path)
    os.rename("bak",userinfo2_path)

@judge(user_status)
def accoun_trans(user_status):
    """
    5.转账功能
    :return:
    """
    flag = True
    while flag:
        trans_money_name = input("请输入要转账的用户名：")
        trans_money_now = input("请输入要转出的钱数：")
        if re.match("[0-9]+\.*[1-9]*", trans_money_now):
            if re.match("[0-9]+\.*[1-9]*", trans_money_now).group() == trans_money_now :
                if 0 < float(trans_money_now) < user_status['account_balance']:
                    userinfo_path = os.path.join(basepath, "db", trans_money_name + ".json")
                    with open(userinfo_path, "a+", encoding="utf-8") as f:
                        f.seek(0)
                        if f.read():
                            f.seek(0)
                            if json.load(f)["name"] == trans_money_name and trans_money_name != user_status["username"]:
                                print(f"成功向{trans_money_name}转入{trans_money_now}元")
                                flag = False
                                break
                            else:
                                print("不能向自己转账！")
                        else:
                            f.close()
                            os.remove(userinfo_path)
                            print("输入用户名错误请重新输入！")
                else:
                    print("输入金额错误请重新输入！")
            else:
                print("输入金额错误请重新输入！")
        else:
            print("输入金额错误请重新输入！")
    userinfo_path = os.path.join(basepath, "db", user_status["username"] + ".json")
    with open(userinfo_path, "a+", encoding="utf-8") as f, \
            open(userinfo2_path, "w", encoding="utf-8") as f1:
        f.seek(0)
        user_dic = json.load(f)
        user_dic["account_balance"] -= float(trans_money_now)
        user_status['account_balance'] -= float(trans_money_now)
        f1.write(json.dumps(user_dic,ensure_ascii=False))
    os.rename(userinfo_path, "bak")
    os.rename(userinfo2_path, userinfo_path)
    os.rename("bak", userinfo2_path)
    userinfo_path = os.path.join(basepath, "db", trans_money_name + ".json")
    with open(userinfo_path, "a+", encoding="utf-8") as f, \
            open(userinfo2_path, "w", encoding="utf-8") as f1:
        f.seek(0)
        user_dic = json.load(f)
        user_dic["account_balance"] += float(trans_money_now)
        money_now = user_dic["account_balance"]
        f1.write(json.dumps(user_dic,ensure_ascii=False))
    os.rename(userinfo_path,"bak")
    os.rename(userinfo2_path,userinfo_path)
    os.rename("bak",userinfo2_path)
    log_write(user_status, f"向{trans_money_name}转账{trans_money_now}元")
    log_write({"username": trans_money_name, "account_balance": money_now}, f"收到{user_status['username']}转账{trans_money_now}元")

@judge(user_status)
def account_log(user_status):
    """
    6.查看银行流水
    :return:
    """
    log_path = os.path.join(basepath, "log", user_status["username"] + ".log")
    with open(log_path,"a+",encoding="utf-8") as f:
        f.seek(0)
        print(f.read())
        f.seek(0)
        if not f.read():
            print("当前无操作记录！")

def exit_atm():
    """
    7.退出程序
    :return:
    """
    print("您已退出程序！")
    exit()

choice_dict = {"1":login,
               "2":sign_in,
               "3":account_balance,
               "4":save_money,
               "5":accoun_trans,
               "6":account_log,
               "7":exit_atm}

def run():
    while True:
        choice = input(msg)
        user_status[1] = choice
        if user_status[1] in choice_dict:
            choice_dict[user_status[1]]()
        else:
            print("输入有误，请重新选择！")

run()