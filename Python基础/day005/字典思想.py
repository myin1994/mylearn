# 输入A:打印A
# 输入B:打印B
# 输入C:打印C


dic = {"A":"我是A","B":"我是B","C":"我是C"}
choice = input(">>>").upper()
if choice in dic:
    print(dic[choice])
else:
    print("输入错误")