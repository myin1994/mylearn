"""
s_26 day03 作业
"""

"""
1.有变量name = "aleX leNb" 完成如下操作：
"""
# 移除 name 变量对应的值两边的空格,并输出处理结果
# name = "   aleX leNb   "
# print(name.strip())

# 判断 name 变量是否以 "al" 开头,并输出结果
# name = "aleX leNb"
# print(name.startswith("al"))

# 判断name变量是否以"Nb"结尾,并输出结果
# name = "aleX leNb"
# print(name.endswith("Nb"))

# 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
# name = "aleX leNb"
# print(name.replace("l","p"))

# 将name变量对应的值中的第一个"l"替换成"p",并输出结果
# name = "aleX leNb"
# print(name.replace("l","p",1))

# 将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
# name = "aleX leNb"
# print(name.split("l"))

# 将name变量对应的值根据第一个"l"分割,并输出结果。
# name = "aleX leNb"
# print(name.split("l",1))

# 将 name 变量对应的值变大写,并输出结果
# name = "aleX leNb"
# print(name.upper())

# 将 name 变量对应的值变小写,并输出结果
# name = "aleX leNb"
# print(name.lower())

# 判断name变量对应的值字母"l"出现几次，并输出结果
# name = "aleX leNb"
# print(name.count("l"))

# 如果判断name变量对应的值前四位"l"出现几次,并输出结果
# name = "aleX leNb"
# print(name.count("l",0,5))

# 请输出 name 变量对应的值的第 2 个字符?
# name = "aleX leNb"
# print(name[1])

# 请输出 name 变量对应的值的前 3 个字符?
# name = "aleX leNb"
# print(name[0:3])

# 请输出 name 变量对应的值的后 2 个字符?
# name = "aleX leNb"
# print(name[-2:])

"""
2.有字符串s = "123a4b5c"

通过对s切片形成新的字符串s1,s1 = "123"
通过对s切片形成新的字符串s2,s2 = "a4b"
通过对s切片形成新的字符串s3,s3 = "1345"
通过对s切片形成字符串s4,s4 = "2ab"
通过对s切片形成字符串s5,s5 = "c"
通过对s切片形成字符串s6,s6 = "ba2"
"""
# s = "123a4b5c"
# s1 = s[:3]
# s2 = s[3:-2]
# s3 = s[::2]
# s4 = s[1:-2:2]
# s5 = s[-1:]
# s6 = s[-3::-2]
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)
# print(s6)

"""
3.使用while和for循环分别打印字符串s="asdfer"中每个元素。
"""
# s="asdfer"
# count = 0
# while count < len(s):
#     print(s[count])
#     count += 1
#
# for i in s:
#     print(i)

"""
4.使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"。
"""
# s="asdfer"
# for i in s:
#     print(s)

"""
5.使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb,...gsb。
"""
# s="abcdefg"
# for i in s:
#     print(i+"sb")

"""
6.使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
"""
# s="321"
# for i in s:
#     print(f"倒计时{i}秒")
# print("出发！")

"""
7.实现一个整数加法计算器(两个数相加)：
如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。
"""
# content = input("请输入内容:")
# splits1 = content.split("+")
# print(f"{int(splits1[0])}+{int(splits1[1])}={int(splits1[0])+int(splits1[1])}")

"""
8.选做题：实现一个整数加法计算器（多个数相加）：
如：content = input("请输入内容:") 用户输入：5+9+6 +12+ 13，然后进行分割再进行计算。
"""
# content = input("请输入内容:")
# splits1 = content.split("+")
# content_sum = 0
# for i in splits1:
#     content_sum += int(i)
# print(content.replace(" ","")+"="+str(content_sum))

"""
9.计算用户输入的内容中有几个整数（以个位数为单位）。
如：content = input("请输入内容：") # 如fhdal234slfh98769fjdla
"""
# content = input("请输入内容：")
# count = 0
# for i in content:
#     if i.isdecimal():
#         count += 1
# print(f"总共{count}个整数")

"""
10.写代码：计算 1 - 2 + 3 -4... + 99 中除了88以外所有数的总和？
"""
# s = 0
# for i in range(1,100):
#     if i % 2 == 1:
#         s += i
#     else:
#         if i == 88:
#             continue
#         s -= i
# print(s)

"""
11.选做题：写代码，完成下列需求：
用户可持续输入（用while循环），用户使用的情况：
输入A，则显示走大路回家，然后在让用户进一步选择：
是选择公交车，还是步行？
选择公交车，显示10分钟到家，并退出整个程序。
选择步行，显示20分钟到家，并退出整个程序。
输入B，则显示走小路回家，并退出整个程序。
输入C，则显示绕道回家，然后在让用户进一步选择：
是选择游戏厅玩会，还是网吧？
选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
"""
# while True:
#     select1 = input("请输入A、B、C:").upper()
#     if select1 == "A":
#         select2 = input("你选择了走大路回家\n请选择公交车或步行：")
#         if select2 == "公交车":
#             print("10分钟到家")
#             break
#         elif select2 == "步行":
#             print("20分钟到家")
#             break
#         else:
#             print("输入错误")
#     elif select1 == "B":
#         print("走小路回家")
#         break
#     elif select1 == "C":
#         select2 = input("你选择了绕道回家\n请选择游戏厅玩会或网吧：")
#         if select2 == "游戏厅玩会":
#             print("一个半小时到家，爸爸在家，拿棍等你")
#         elif select2 == "网吧":
#             print("两个小时到家，妈妈已做好了战斗准备。")
#         else:
#             print("输入错误")

"""
12.选做题：判断⼀句话是否是回⽂. 回⽂: 正着念和反着念是⼀样的. 例如, 上海⾃来⽔来⾃海上
"""
# content = input("请输入一句话：")
# if content == content[::-1]:
#     print("是回文")
# else:
#     print("不是回文")

"""
13.制作趣味模板程序(使用字符串格式化)需求：
等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进行任意现实 
如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
"""
# name = input("请输入姓名：")
# position = input("请输入地点：")
# hobby = input("请输入爱好：")
# print(f"敬爱可亲的{name}，最喜欢在{position}地⽅⼲{hobby}")