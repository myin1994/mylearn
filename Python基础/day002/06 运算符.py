# 1.比较运算符
"""
> <
>= <=
==
!=
"""
# 2.算术运算符
"""
+ - * / 
// 整除，向下取整(地板除)
** 幂
% 取余，取模
"""
# print(5 / 2) #2.5
# print(5 // 2) #2
# print(5 ** 2) #25
# print(5 % 2) #1

# 3.赋值运算符
"""
 =
 +=
 -=
 *=
 /=
 //=
 **=
 %=
"""
# a = 10
# b = 2
# b += 1  #b = b + 1
# a -= 1 #a = a -1
# a *= 2 #a = a *2
# a /= 2 #a = a / 2
# a //= 2 #a = a // 2
# a **= 2 #a = a ** 2
# a %= 2 #a = a % 2

# 4.逻辑运算符
# True 和 False 逻辑运算时
"""
与（and）：同真为真，有假为假
或（or）：有真为真，同假为假
非（not）：取反
优先级：() > not > and > or
查找顺序：从左向右
"""
# 数字逻辑运算时（面试用）：
# and数字不为0时和不为False：and运算选择and后面的内容
# and两边都为假时选择and左边
# 一真一假选假
# print(1 and 3)
# print(0 and 8)
# print(9 and 0)
# print(9 and True)
# print(True and 9)
# print(9 and False)
# print(2 or -2)



# or数字不为0时和不为False：or算选择or前面的内容
# or两边都为假时选择or左边
# 一真一假选真

# print(1 or 2)
# print(1 or 0)
# print(-2 or 0)

# 5.成员运算符
"""
in：在
not in：不在
"""
# name = 'name'
# msg = input('输入内容')
# if name in msg:
#     print("在")
# else:
#     print("不在")