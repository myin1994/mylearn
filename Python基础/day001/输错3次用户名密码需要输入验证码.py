"""
实现输入三次错误的账号或密码后需要输入验证码
"""
"""
第一次实现
flag1 = True
flag2 = 0
while flag1:
    user_name = input('请输入用户名：')
    user_password = input('请输入密码：')
    if flag2 < 3:
        if user_name == '用户名' and user_password == '密码':
            print("用户名密码正确")
            flag1 = False
        else:
            print('用户名或密码错误')
            flag2 += 1
    else:
        verifycode = input('请输入验证码：')
        if verifycode == '验证码':
            if user_name == '用户名' and user_password == '密码':
                print("用户名密码正确")
                flag1 = False
            else:
                print('用户名或密码错误')
        else:
            print('验证码错误')
"""
###优化版
flag1 = True
flag2 = 0
while flag1:
    user_name = input('请输入用户名：')
    user_password = input('请输入密码：')
    if flag2 > 2:
        verifycode = input('请输入验证码：')
        if verifycode != '验证码':
            print('验证码错误')
            continue
    if user_name == '用户名' and user_password == '密码':
        print("用户名密码正确")
        flag1 = False
    else:
        print('用户名或密码错误')
        flag2 += 1
