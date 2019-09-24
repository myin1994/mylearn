# 1.闭包
# 闭包的作用：保护数据的安全性和干净性
# 闭包的定义：
#     1.在嵌套函数内使用非全局变量（且非本层变量）
#     2.并且将嵌套函数返回
def func(a):
    def foo():
        print(a)
    return foo
# func(2)()
a = func(3)
a()
# 2.装饰器
# 开放封闭规则：
# 1.对扩展功能开放
# 2.对修改源代码及调用方式封闭

# def wrapper(func):
#     def inner(*args,**kwargs):
#         """装饰前功能1"""
#         ret = func(*args,**kwargs)
#         """装饰后功能2"""
#         return ret
#     return inner
#
# @wrapper   #index = wrapper(index)
# def index():
#     print("is index")
#
# index()

def func(args):
    print("is func")
    return args

@func #index = func(index)
def index():
    print("is index")

index()