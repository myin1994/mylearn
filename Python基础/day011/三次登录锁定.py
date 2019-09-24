login_dict = {
    "count": 3
}

user_info_path = "user_info.txt"
error_path = "error_user.txt"


def login():
    """
    登录函数
    :return:
    """
    user = input("username:")
    pwd = input("password:")
    with open(user_info_path, "a+", encoding="utf-8")as f, \
            open(error_path, "a+", encoding="utf-8")as f1:
        f.seek(0)
        f1.seek(0)
        dic = {}
        for i in f1:
            i = i.strip()
            dic[i] = dic.get(i, 0) + 1

        if user in dic and dic[user] >= 3:
            print(f"{user}用户已锁定,请联系管理员!")
            return

        else:
            login_dict['count'] -= 1
            for em in f:
                file_user, file_pwd = em.strip().split(":")
                if file_user == user and file_pwd == pwd:
                    print("登录成功!")
                    login_dict['count'] = 0
                    return

            else:
                f1.write(f"{user}\n")
                f1.flush()
                print(f"账号或密码错误,剩余次数:{login_dict['count']}")


def register():
    """
    注册函数
    :return:
    """
    user = input("username:")
    pwd = input("password:")
    with open(user_info_path, "a+", encoding="utf-8")as f:
        f.seek(0)
        for i in f:
            file_user, file_pwd = i.strip().split(":")
            if user == file_user:
                print("用户名已注册!")
                return
        else:
            f.write(f"{user}:{pwd}\n")
            print("账号注册成功!")


func_dict = {
    "1": login,
    "2": register
}

msg = """
1.登录
2.注册
请输入您要选择的序号:
"""

while login_dict['count']:
    choose = input(msg)
    if choose in func_dict:
        func_dict[choose]()
    else:
        print("请重新输入!")
