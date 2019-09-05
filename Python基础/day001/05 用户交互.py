# intput(提示语句)  #--程序交互 input --输入
# input() #坑--阻塞（不填内容的话）
# print(111)

# a = input('请输入：')
# print(a + '不好')

# qq_user = input('QQ账号：')
# qq_password = input('QQ密码：')
# print(qq_user,qq_password)

# num = input('请输入数字：')
# #python3中input获取的内容全都是字符串
# print(type(num)) #查看数据类型
# print(int(num) + 5)


a = '10'
b = int(a)
# str -> int (字符串转换整型)
# int -> str (整型转换字符串)
print(a,b) #print是给用户看的，输出值是经过加工的

# 总结：
# input() 输入，获取的内容是字符串
# type() 查看数据类型
# int('字符串') 字符串中的内容必须全是数字
# 还有一个
