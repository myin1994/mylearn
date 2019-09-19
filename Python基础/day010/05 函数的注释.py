# 函数的注释：给别人看的，
# def func(a,b,c):
#     """
#     函数功能
#     :param a: 参数 int
#     :param b: int
#     :param c: int
#     :return:
#     """
#     return

def add(a:int,b:int): #提示，没有做到约束
    """

    :param a:
    :param b:
    :return:
    """
    return a + b
# print(add(1,2))
# print(add("1","2"))
# print(add.__doc__)  #查看函数的注释
# print(add.__name__)  #查看函数的名字(原始)
a = add
print(a.__name__)  #查看函数的名字(原始)
print(a.__doc__)