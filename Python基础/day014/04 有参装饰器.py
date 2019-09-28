# 有参数的 装饰器（根据参数执行装饰内容）
# 开关-条件-函数
# def arg(argv):
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             if argv:
#                 print("开始装饰")
#             ret = func(*args,**kwargs)
#             if argv:
#                 print("装饰结束")
#             return ret
#         return inner
#     return wrapper
#
# @arg(False)  #或用此代替，@arg(False) -> @wrapper -> index = inner(index)
# def index():
#     print("is index")

# wrapper = arg(True)  #返回值为wrapper
# index = wrapper(index)  #返回值为inner
# index()

#多个函数使用相同装饰器时-1-定义多个装饰器，只是名字不相同
# def wrapper(func):
#     def inner(*args,**kwargs):
#         username = input("请输入用户名：")
#         pwd = input("请输入密码：")
#         if username == "alex" and pwd == "alex123":
#             func(*args,**kwargs)
#     return inner
#
#
# def wechat():
#     print("微信")
#
# def dy():
#     print("抖音")
#
# def email():
#     print("邮箱")
#
# msg = """
# 1.微信
# 2.抖音
# 3.邮箱
# 选择：
# """
# choice = input(msg)
# if choice == "1":
#     wechat()
# if choice == "2":
#     dy()
# if choice == "3":
#     email()


# def auth(arg):
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             username = input("请输入用户名：")
#             pwd = input("请输入密码：")
#             if arg == "1":
#                 if username == "alex" and pwd == "alex123":
#                     func(*args,**kwargs)
#             if arg == "2":
#                 if username == "alex" and pwd == "alex123":
#                     func(*args,**kwargs)
#             if arg == "3":
#                 if username == "alex" and pwd == "alex123":
#                     func(*args,**kwargs)
#         return inner
#     return  wrapper
#
# def wechat():
#     print("微信")
#
# def dy():
#     print("抖音")
#
# def email():
#     print("邮箱")
#
# msg = """
# 1.微信
# 2.抖音
# 3.邮箱
# 选择：
# """
# choice = input(msg)
# wrapper = auth(choice)
# if choice == "1":
#     wechat = wrapper(wechat)
#     wechat()
# if choice == "2":
#     dy = wrapper(dy)
#     dy()
# if choice == "3":
#     email = wrapper(email)
#     email()

msg = """
1.微信
2.抖音
3.邮箱
选择：
"""
choice = input(msg)

def auth(arg):
    def wrapper(func):
        def inner(*args,**kwargs):
            username = input("请输入用户名：")
            pwd = input("请输入密码：")
            if arg == "1":
                if username == "alex" and pwd == "alex123":
                    func(*args,**kwargs)
            elif arg == "2":
                if username == "alex" and pwd == "alex123":
                    func(*args,**kwargs)
            elif arg == "3":
                if username == "alex" and pwd == "alex123":
                    func(*args,**kwargs)
        return inner
    return wrapper
##看一下@的作用
@auth(choice)   #wechat = wrapper = auth(choice)
def wechat():
    print("微信")
# # wrapper = auth(choice)
# # wechat = wrapper(wechat)
wechat()
#
# @auth(choice)
# def dy():
#     print("抖音")
#
# @auth(choice)
# def email():
#     print("邮箱")
#
# if choice == "1":
#     wechat()
# elif choice == "2":
#     dy()
# elif choice == "3":
#     email()

# msg = """
# 微信
# 抖音
# 邮箱
# 选择：
# """
# choice = input(msg)
#
# def auth(arg):
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             username = input("请输入用户名：")
#             pwd = input("请输入密码：")
#             if arg == "微信":
#                 if username == "alex" and pwd == "alex123":
#                     func(*args,**kwargs)
#                 else:
#                     print("账号或密码错误")
#             elif arg == "抖音":
#                 if username == "alex" and pwd == "alex123":
#                     func(*args,**kwargs)
#                 else:
#                     print("账号或密码错误")
#             elif arg == "邮箱":
#                 if username == "alex" and pwd == "alex123":
#                     func(*args,**kwargs)
#                 else:
#                     print("账号或密码错误")
#         return inner
#     return wrapper
#
# @auth(choice)   #wechat = wrapper = auth(choice)
# def wechat():
#     print("微信")
# wechat()
#
# @auth(choice)
# def dy():
#     print("抖音")
# dy()
#
# @auth(choice)
# def email():
#     print("邮箱")
#
# email()


# 应用场景：flask框架的路由就是有参装饰器