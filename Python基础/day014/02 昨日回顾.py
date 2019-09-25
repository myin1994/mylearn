# 闭包
# 定义：
#     1.在嵌套函数内，使用非全局变量（且非本层变量）
#     2.将嵌套函数返回
# 作用：保护数据，保证数据干净性
# 应用场景：装饰器
# def func():
#     a = 10
#     def foo():
#         print(a)
#     return foo
#
# f = func()
# f()
# print(f.__closure__)

# 装饰器
# 开放封闭原则：
# 1.对扩展开放，可增加新功能
# 2.对修改源代码及调用方式封闭

def wrapper(func):
    def inner(*args,**kwargs):
        print(234)
        func(*args,**kwargs)
    return inner

@wrapper
def index(a,b,c):
    print(a,b,c)

index(1,2,3)