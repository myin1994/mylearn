#1.今日课上内容敲3遍以上
#注释的使用
"""
多行注释1
多行注释2
多行注释3
"""
'''
多行注释1
多行注释2
'''

#定义变量
# a = 1
# b = '字符串'
# c = True
# print(a,b,c)

#字符串整型相互转换
# int_1 = 1
# str_1 = '123'
# bool_1 = False
# str_2 = str(int_1)
# str_3 = str(bool_1)
# int_2 = int(str_1)
# print(str_2,type(str_2)) #整型转换为字符串
# print(str_3,type(str_3)) #布尔型转换为字符串
# print(int_2,type(int_2)) #字符串转换为整型

#输入输出+流程控制语句
# name = input('请输入姓名：')
# age = int(input('请输入年龄：'))
# sex = input('请输入性别：')
# hobby = input('请输入爱好：')
# if age <= 18:
#     print(name)
#     if sex == '女':
#         print(hobby)
#     elif sex == '男':
#         print('请离开')
#     else:
#         print('Are you sure?')
# elif age > 60:
#     print('您好')
# if age ==16 and sex == '女':
#     print('花一样的年龄')

# 2.name = input(“>>>”)通过代码来验证name变量是什么数据类型？
# name = input('>>>')
# print(type(name)) #name为字符串

# 3.if条件语句的基本结构？
"""
if  条件:
    执行语句
elif 条件：
    执行语句
elif 条件：
    执行语句
else：
    执行语句
    
根据具体情况使用if语句，可嵌套
"""
# 4.用print打印出下面内容：
# print('''
# 文能提笔安天下,
# 武能上马定乾坤.
# 心存谋略何人胜,
# 古今英雄唯世君.
# ''')

# 5.利用if语句写出猜大小的游戏：
# 设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。
# guess = int(input("请猜数字："))
# if guess > 66:
#     print('猜测的结果大了')
# elif guess < 66:
#     print('猜测的结果小了')
# else:
#     print('猜测结果正确')

#加入循环
# guess = -1
# while guess != 66:
#     guess = int(input("请猜数字："))
#     if guess > 66:
#         print('猜测的结果大了')
#     elif guess < 66:
#         print('猜测的结果小了')
#     else:
#         print('猜测结果正确')

# 6.提⽰⽤户输入他的年龄, 通过程序进⾏判断.
# 如果小于10,提示小屁孩,
# 如果大于10,小于20,提示青春期叛逆的小屁孩.
# 如果大于20,小于30.提示开始定性,开始混社会小屁孩儿,
# 如果大于30,小于40.提示看老老大不了,赶紧结婚小屁孩儿.
# 如果大于40,小于50.提示家里有个不听话的小屁孩儿.
# 如果大于50,小于60.提示自己马上变成不听话的老屁孩儿.
# 如果大于60,小于70.提示活着还不错的老屁孩儿.
# 如果大于70,小于90.提示人生就快结束了的一个老屁孩儿.
# 如果大于90以上.提示再见了这个世界.
# age = int(input('请输入年龄：'))
# if age < 10:
#     print('小屁孩')
# elif age >= 10 and age <20:
#     print('青春期叛逆的小屁孩')
# elif age >= 20 and age < 30:
#     print('开始定性,开始混社会小屁孩儿')
# elif age >= 30 and age < 40:
#     print('看老老大不了,赶紧结婚小屁孩儿')
# elif age >= 40 and age < 50:
#     print('家里有个不听话的小屁孩儿')
# elif age >= 50 and age < 60:
#     print('自己马上变成不听话的老屁孩儿')
# elif age >= 60 and age < 70:
#     print('活着还不错的老屁孩儿')
# elif age >= 70 and age < 90:
#     print('人生就快结束了的一个老屁孩儿')
# else:
#     print('再见了这个世界')


# 7.单行注释以及多行注释？
# 单行注释内容1
# 单行注释内容2
"""
多行注释内容1
多行注释内容2
……
多行注释内容n
"""
'''
多行注释内容1
多行注释内容2
……
多行注释内容n
'''

# 8.简述你所知道的Python3x和Python2x的区别？
"""
源码：python2-不统一且有重复代码    python3-统一，无重复代码
除法：python2-返回整型             python3-返回浮点型
input():python2-与输入类型相同,raw_input()获取到的都是字符串  python3-均返回字符串
"""

# 9.提示用户输入的麻花藤. 判断用户输入的是否正确. 如果对, 提示真聪明, 如果不对, 提示用户输入错误
# label = input('请输入“麻花藤”：')
# if label == '麻花藤':
#     print('真聪明')
# else:
#     print('输入错误')

# 10.用户输入一个月份.然后判断月份是多少月.根据不同的月份,打印出不用的饮食(根据个人习惯和老家习惯随意编写)
# month = int(input('请输入一个月份：'))
# if month == 1:
#     print('大米')
# elif month == 2:
#     print('小米')
# elif month == 3:
#     print('玉米')
# elif month == 4:
#     print('苹果')
# elif month == 5:
#     print('香蕉')
# elif month == 6:
#     print('榴莲')
# elif month == 7:
#     print('西瓜')
# elif month == 8:
#     print('南瓜')
# elif month == 9:
#     print('土豆')
# elif month == 10:
#     print('红薯')
# elif month == 11:
#     print('粉丝')
# elif month == 12:
#     print('馒头')
# else:
#     print('没听说过的月份')

# 11.用户输入一个分数.根据分数来判断用户考试成绩的输出不同的档次
# =90 A
# =80 B
# =70 C
# =60 D
# < 60 不及格
# score = int(input('请输入你的分数：'))
# if score >= 90:
#     print('RANK:A')
# elif score >= 80:
#     print('RANK:B')
# elif score >= 70:
#     print('RANK:C')
# elif score >= 60:
#     print('RANK:D')
# else:
#     print('不及格！')