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
a = 1
b = '字符串'
c = True
print(a,b,c)

#字符串整型相互转换
int_1 = 1
str_1 = '123'
bool_1 = False
str_2 = str(int_1)
str_3 = str(bool_1)
int_2 = int(str_1)
print(str_2,type(str_2)) #整型转换为字符串
print(str_3,type(str_3)) #布尔型转换为字符串
print(int_2,type(int_2)) #字符串转换为整型

#输入输出+流程控制语句
name = input('请输入姓名：')
age = int(input('请输入年龄：'))
sex = input('请输入性别：')
hobby = input('请输入爱好：')
if age <= 18:
    print(name)
    if sex == '女':
        print(hobby)
    elif sex == '男':
        print('请离开')
    else:
        print('Are you sure?')
elif age > 60:
    print('您好')
if age ==16 and sex == '女':
    print('花一样的年龄')
