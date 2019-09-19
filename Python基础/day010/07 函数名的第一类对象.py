# 函数名的  第一类对象（称呼）及使用

# 1.函数名可以当做值，被赋值给一个变量

# def func():
#     print(1)
#
# print(func)  #函数的内存地址
# a = func
# print(a)
# a()


# 2.函数名可以当做另一个函数的参数来使用
# def func():
#     print(1)
#
# def fo(a): #a = func
#     print(a) #打印func函数的内存地址
#     a()
#
# fo(func)

# 3.函数名可以当做另一个函数的返回值
# 不管在什么位置，只要是看到函数名+()就是调用函数
# def func():
#     print(1)
#
# def fo(a): #a = func
#     return a #return  func函数的内存地址
#
# c = fo(func)
# print(c)  #func函数的内存地址

# 4.函数名可以当做元素存储在容器中

# def func():
#     print(1)
#
# def foo():
#     print(2)
#
# def fo():
#     print(3)
#
# lst = [func,foo,fo]
# for i in lst:
#     i()

# def login():
#     print("登录")
#
# def register():
#     print("注册")
#
# def shopping():
#     print("逛")
#
# def add_shopping_car():
#     print("加")
#
# def buy():
#     print("买")
#
# msg = """
# 1.注册
# 2.登录
# 3.逛
# 4.加
# 5.买
# 请输入您要选择的序号："""
#
# fun_dic={"1":register,
#          "2":login,
#          "3":shopping,
#          "4":add_shopping_car,
#          "5":buy}
# while True:
#     choice = input(msg)
#     if choice in fun_dic:
#         fun_dic[choice]()
#     else:
#         print("走你")


