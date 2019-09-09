# 常用
# 万能的点
# name = "xYzd"
# name1 = name.upper() #全部大写
# name2 = name.lower() #全部小写
# print(name)
# print(name1)
# print(name2)

# 应用场景：
# yzm = "10jQkA"
#
# my_yzm = input(f'请输入验证码{yzm}：')
# if yzm.upper() == my_yzm.upper():
#     print("正确")
# else:
#     print("错误")

# name = "xyzd"
# # 以什么开头
# print(name.startswith("x",1,3)) #判断是否以"x"开头，返回bool;支持切片
# print(name.endswith("d",0,)) #判断是否以"d"结尾，返回bool;支持切片

# name = "aaaeeeccbb"
# print(name.count("e")) #计数（统计）,返回整型
# print(name.count("ee")) #计数（统计）

# name = "  你\n好   "  #\n 换行
# name1 = "  你\t好   \t"  #\n 制表符（tab）
# print(name1.strip())  #去除头尾两端及换行符，制表符
# name = "aa  33a"
# print(name.strip("a"))  #去除头尾两端指定字符串（全部，直到没有）

# 应用场景：
# account = input("账号：").strip()
# psw = input("密码：").strip()
# if account == "zhanghao" and psw == "12345":
#     print("OK")
# else:
#     print("NO")

# 分割：
a = "alex:alex1234"
print(a.split())  #默认按照空格及换行符，制表符进行分割(同时；返回值为列表
print(a.split(":"))  #可指定，被选中的分割符消失
b = "alex: a\nlex\t1234"
print(b.split())

# 替换：
# name = "alexcnb"
# print(name.replace("n","s")) #替换（参数1--旧值，参数2--新值，参数3--替换次数（默认全部替换））
# name = "alex_namee"
# print(name.replace("e","s",2)) #从左向右

#is系列 判断系列
# name = "alex"
# print(name.isalnum()) #判断是否由字母，中文，数字组成，返回bool
# print(name.isalpha()) #判断是否由字母，中文组成，返回bool
# print(name.isdigit()) #判断是否是阿拉伯数字（① ②也算-bug），返回bool
# print(name.isdecimal()) #判断是否是十进制，返回bool
