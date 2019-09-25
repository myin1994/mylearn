# 递归：精华  一递一归
# 递归需要有边界条件、递归前进段和递归返回段。
# 当边界条件不满足时，递归前进；当边界条件满足时，递归返回。


# 递归的定义：
# 1.不断调用自己本身   #死递归
# 2.有明确结束的条件

# 最大深度（层次）：官方-1000   实际测试-998/997/994/993
# def func(): #死递归
#     print(1)
#     func()
# func()

# import sys
# sys.setrecursionlimit(100000)  #调整递归最大深度
# def func():
#     print(1)
#     func()
# func()

# def age(n):
#     if n == 3:
#         return 18
#     return age(n+1) - 2
# print(age(1))

# def age(n):
#     if n == 3:
#         return 18
# def age1(n):
#     if n == 3:
#         return 18
#     return age(n + 1) - 2
#
# def age2(n):
#     if n == 3:
#         return 18
#     return age1(n+1) -2   #由返回值向深层寻找
#
# print(age2(1))

# 阶乘

# def jc(n):
#     if n == 1 :
#         return 1
#     else:
#         return n * jc(n-1)
# print(jc(5))

# lst = [1,1]
# for i in range(6):
#     lst.append(lst[-1] + lst[-2])
# print(lst)

# def feb(n):
#     n = n + 2
#     a ,b = 0, 1
#     for i in range(n):
#         a, b = b, a+b
#     return a
#
# print(feb(5))


# def feb(n):
#     if n <= 1:
#         return 1
#     else:
#         return feb(n-1) + feb(n-2)
#
# print(feb(5))

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))
print(list(map(fib,range(1,6))))

# 递归计算1+2+3……+100+n
# def func(n):
#     if n == 1:
#         return 1
#     else:
#         return func(n-1) + n
# print(func(100))

#上楼梯问题，一次可以上1或2阶，求上n阶有几种可能
# def fun(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return fun(n-1) + fun(n-2)
# print(fun(5))