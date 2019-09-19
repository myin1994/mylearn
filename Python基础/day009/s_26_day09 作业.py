"""
s_26_day09 作业
"""

"""
2.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
"""
# def get_uneven(lst_tu):
#     return lst_tu[1::2]
# a = get_uneven((0,1,2,3,4,5,6,7,8,9))
# print(a)

"""
3.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
"""
# def l_5(a):
#     return len(a) > 5
# print(l_5("555555"))
# print(l_5([1,2,3,4,5,6]))
# print(l_5((1,2,3,4,5,6)))
# print(l_5((1,2,3,4,5)))

"""
4.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
"""
# def l_2(a):
#     if len(a) > 2:
#         return a[:2]
#     else:
#         return a
# print(l_2([1,2,3,4,5]))
# print(l_2([1]))

"""
5.写函数，计算传入函数的字符串中,[数字]、[字母和中文]以及 [其他]的个数，并返回结果。
"""
# def count_str(s):
#     count1 = count2 = count3 = 0
#     for i in s:
#         if i.isdecimal():
#             count1 += 1
#         elif i.isalpha():
#             count2 += 1
#         else:
#             count3 += 1
#     return f"数字:{count1}个 字母和中文:{count2}个 其他:{count3}个 "
# print(count_str("weow我1234@#11"))

"""
6.写函数，接收两个数字参数，返回比较大的那个数字。
"""
# def bigger(a,b):
#     if a < b:
#         a = b
#     return a
# print(bigger(6,55))

# def bigger(a,b):
#     return a if a > b else  b
# print(bigger(6,55))
"""
7.写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
PS:字典中的value只能是字符串或列表
"""
# def dic_2(dic):
#     for k,v in dic.items():
#         if len(v) > 2:
#             dic[k] = v[:2]
#     return dic
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# print(dic_2(dic))

"""
8.写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
"""
# def lst_dic(lst):
#     dic = {}
#     if type(lst) != list:
#         return "传入数据类型错误！"
#     else:
#         for i in lst:
#             dic[lst.index(i)] = i
#     return dic
# print(lst_dic([11,22,33,44]))

# lst = [11,22,33]
# def func(lst):
#     dic = {}
#     for k,v in enumerate(lst):  #枚举，计数 默认从0开始
#         dic[k] = v
#     return  dic
# print(func(lst))

"""
9.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。
用户通过输入这四个内容，然后将这四个内容传入到函数中，
此函数接收到这四个内容，将内容追加到一个student_msg文件中。
"""
# def student_info(name,sex,age,grade):
#     f = open("student_msg","a",encoding="utf-8")
#     f.write(f"{name}-{sex}-{age}-{grade}\n")
# name = input("请输入姓名：")
# sex = input("请输入性别：")
# age = input("请输入年龄：")
# grade = input("请输入学历：")
# student_info(name,sex,age,grade)


"""
10.对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。

"""
# def student_info(name,age,grade,sex = "男"):
#     f = open("student1_msg","a",encoding="utf-8")
#     f.write(f"{name}-{sex}-{age}-{grade}\n")
#     f.flush()
#     f.close()
#
# while True:
#     name = input("请输入姓名(输入Q/q退出)：")
#     if name.upper() == "Q":
#         break
#     sex = input("请输入性别：")
#     age = input("请输入年龄：")
#     grade = input("请输入学历：")
#     student_info(name,age,grade,sex)

"""
写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（选做题）。
"""
# def re_file(file_name,file_content,file_recontent):
#     import os
#     with open(file_name,"r",encoding="utf-8") as f1 ,\
#         open("file_name2","w",encoding="utf-8") as f2:
#         for i in f1:
#             f2.write(i.replace(file_content,file_recontent))
#             f2.flush()
#     os.rename(file_name,"file_name3")
#     os.rename("file_name2",file_name)
#     os.remove("file_name3")
#
# re_file("student1_msg","nb","sb")

# def re_file(file_name,file_rname,file_content,file_recontent):
#     import os
#     with open(file_name,"r",encoding="utf-8") as f1 ,\
#         open(file_rname,"w",encoding="utf-8") as f2:
#         for i in f1:
#             f2.write(i.replace(file_content,file_recontent))
#             f2.flush()
#     os.rename(file_name,file_name+"bak")
#
# re_file("student1_msg","userinfo","nb","sb")