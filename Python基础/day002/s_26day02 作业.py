"""
s_26day02 作业
"""
"""
1.判断下列逻辑语句的结果,一定要自己先分析 (3<4这种是一体)
1）1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
2）not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6

1)分析：从左至右1 > 1为假，3 < 4为真，则第二个or前为真，则停止解析，结果为True
2）分析：从左至右 not 2 > 1为假则第一个and前为假，停止解析，返回值为False
"""
# 验证
# print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# 验证无误

"""
2.求出下列逻辑语句的值,一定要自己分析
1)8 or 3 and 4 or 2 and 0 or 9 and 7 --------8
2)0 or 2 and 3 and 4 or 6 and 0 or 3 --------4
3)1 and 0 or 8 and 9 and 5 or 2 -------------5
4)4 or 8 and not False and 8 or 9 -----------4
"""
# print(8 or 3 and 4 or 2 and 0 or 9 and 7)
# print(0 or 2 and 3 and 4 or 6 and 0 or 3)
# print(1 and 0 or 8 and 9 and 5 or 2)
# print(4 or 8 and not False and 8 or 9)
# 验证无误

"""
3.下列结果是什么? (2>1这种是一体)
6 or 2 > 1---6
3 or 2 > 1---3
0 or 5 < 4---False
5 < 4 or 3---3
2 > 1 or 6---True
3 and 2 > 1---True
0 and 3 > 1---0
2 > 1 and 3---3
3 > 1 and 0---0
3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2---2
"""
# print(6 or 2 > 1)
# print(3 or 2 > 1)
# print(0 or 5 < 4)
# print(5 < 4 or 3)
# print(2 > 1 or 6)
# print(3 and 2 > 1)
# print(0 and 3 > 1)
# print(2 > 1 and 3)
# print(3 > 1 and 0)
# print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)
# 验证无误

"""
4.简述ASCII、Unicode、utf-8编码

ASCII码：美国制造，只包含英文、数字及部分特殊字符的编码，不支持中文，一个字符占8位（1个字节）,总共可表示256个字符
Unicode:适用于中英文的编码集，一个字符均用4个字节表示（32位）
utf-8:目前最流行的编码集
    英文一个字符占8位（1个字节）
    欧洲一个字符占16位（2个字节）
    亚洲一个字符占24位（3个字节）
"""

"""
5.简述位和字节的关系？

1字节（byte） = 8位（bit）
即8位由0/1组成的编码段，如 0000 0001是一个字节
"""

"""
6.while循环语句基本结构？

while 条件:
    循环体（可添加break终止循环，continue跳至下次循环；可嵌套while）
else：#while的条件不满足时执行
    语句
"""

"""
7.利用while语句写出猜大小的游戏：
设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确，然后退出循环。
"""
# while True:
#     guess = int(input('请猜一个数字：'))
#     if guess > 66:
#         print('大了')
#     elif guess < 66:
#         print('小了')
#     else:
#         print('结果正确')
#         break

"""
8.在7题的基础上进行升级：
给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，如果三次之内没有猜测正确，则自动退出循环，并显示‘太笨了你....’。
"""
# count = 0
# while True:
#     count += 1
#     guess = int(input('请猜一个数字：'))
#     if guess > 66:
#         print('大了')
#     elif guess < 66:
#         print('小了')
#     else:
#         print('结果正确')
#         break
#     if count == 3:
#         print('太笨了你……')
#         break

"""
9.使用while循环输出 1 2 3 4 5 6 8 9 10
"""
# count = 1
# while count < 11:
#     print(count)
#     count += 1

"""
10.求1-100的所有数的和
"""
# count = 1
# sum = 0
# while count < 101:
#     sum += count
#     count += 1
# print(sum)

"""
11.输出 1-100 内的所有奇数
"""
# count = 1
# while count < 101:
#     if count % 2 != 0:
#         print(count)
#     count += 1

"""
12.输出 1-100 内的所有偶数
"""
# count = 1
# while count < 101:
#     if count % 2 == 0:
#         print(count)
#     count += 1

"""
13.求1-2+3-4+5 ... 99的所有数的和
"""
# count = 1
# sum = 0
# while count < 101:
#     if count % 2 != 0:
#         sum += count
#     else:
#         sum -= count
#     count += 1
# print(sum)

"""
14.⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）
"""
# count = 1
# while count < 4:
#     user_name = input("请输入用户名：")
#     user_psw = input("请输入密码：")
#     if user_name == '用户名' and user_psw == '密码':
#         print('登录成功')
#         break
#     else:
#         print('用户名或密码错误，剩余错误次数：%s'%(3-count)) #第一种方法
#         print(f'用户名或密码错误，剩余错误次数：{3 - count}') #第二种方法
#         print('用户名或密码错误，剩余错误次数：{}'.format(3 - count))  # 第三种方法
#     count += 1