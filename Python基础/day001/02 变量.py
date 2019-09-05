# print() ---打印（输出）
# print(111)

# 变量：将程序中运行的中间值，临时存储起来以便再次使用
# 昵称
#
# 定义一个变量
# name = 'alex'
# 'alex':值（数据）
# = ：赋值操作
# name ：变量名
# print(name)  ##使用定义的变量名

# a = 'name1'
# print(a)
# b = 'name2'
# print(b)

# a1 = 'name3'
# print(a1)

# b1 = 'name4'
# print(b1)

# b_a = 'name5'
# print(b_a)

# a_b = 'name6'
# print(a_b)

# _a = 'name7'
# print(_a)

# 1a = 'name8'  #错误变量名
# print(1a)

#变量命名规范：
# 1.数字，字母，下划线组成
# 2.不能以数字开头
# 3.禁止使用python关键字（如下）

# ['False', 'None', 'True', 'and', 'as',
#
#  'assert', 'break', 'class', 'continue', 'def',
#
#  'del', 'elif', 'else', 'except', 'finally',
#
#  'for', 'from', 'global', 'if', 'import',
#
#  'in', 'is', 'lambda', 'nonlocal', 'not',
#
#  'or', 'pass', 'raise', 'return', 'try',
#
#  'while', 'with', 'yield']

# 4.变量名要具有可描述性
# 5.变量名要区分大小写
# name = 'alex'
# Name = 'name'
# print(name)
# print(Name)

# 6.不能使用中文和拼音
# https://unbug.github.io/codelf/  命名神器
# https://guobaoyuan.gitee.io/book/ 博客

# 7.推荐写法
# 驼峰体
# AlexOfOldboy = 89
# 下划线(官方推荐)
# alex_of_oldboy = 89


# a1 = 'alex'
# 1_a = 'sange'
# a_1_a = 'jiangyi'
# print(a1)
# print(a_1_a)
# print(1_a)

# age = 18
# age1 = age
# print(age,age1) #print可以打印多个内容，以,分隔

# age = 18
# age1 = age
# age2 = age1
# age = 20
# age1 = 19
# print(age,age1,age2) #20 19 18

# name = 'xx'
# name1 = name
# name2 = name1
# name1 = 'xxx'
# name2 =name1
# name = 'xxxx'
# print(name,name1,name2) ####xxxx,xxx,xxx