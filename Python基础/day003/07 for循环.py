# for循环：有限循环
# while循环 ：死循环

# for循环的结构：
# for i in xxx：
# for 关键字
# i 变量
# in 关键字
# xxx 可迭代对象（int，bool不可迭代）：
# str --字符串
# list --列表
# tuple --元祖
# set --集合
# dict --字典
# range --范围


# while 循环实现
# name = "alex"
"""
a
l
e
x
"""
# len(name) #len() 公共方法，获取长度
# count = 0
# while count < len(name):
#     print(name[count])
#     count += 1

# for 循环实现
# for i in name: #内部for进行赋值,按顺序进行迭代，最后返回值为最后的值
#     print(i)

# 面试题：
# name = "alex"
# for i in name:
#     pass #占位（当行）
# print(i)

# num = 5
# count = 1
# while num:
#     for i in "abc":
#         print(i + str(count))
#     count += 1
#     num -= 1