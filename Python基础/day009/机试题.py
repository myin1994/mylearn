"""
机试题
"""

"""
1.lis = [['哇',['how',{'good':['cd',1000,'99']},'大帅哥'],'I']] （总分2分）

- 列表lis中的'cd'全部变成大写。(1分)
- 列表中的1000通过数字相加在转换成字符串的方式变成'10086'。(1分)
"""
# lis = [['哇',['how',{'good':['cd',1000,'99']},'大帅哥'],'I']]
# lis[0][1][1]["good"][0] = lis[0][1][1]["good"][0].upper()
# print(lis)
# lis[0][1][1]["good"][1] = str(lis[0][1][1]["good"][1] + 9086)
# print(lis)

"""
2.dic = {'k1':'v1','k2':['alex','sb'],(1,2,3,):{'k3':['2',100,'wer']}}  （总3分）

- 将'k3'对应的值的最后面添加一个元素(1,2,3)。(1分)
- 将'k2'对应的值的第2个位置前插入元素{'a'}。(1分)
- 将(1,2,3,)对应的值添加一个键值对key:(1,)。(1分)
"""
# dic = {'k1':'v1','k2':['alex','sb'],(1,2,3,):{'k3':['2',100,'wer']}}
#
# dic[(1,2,3,)]["k3"].append((1,2,3))
#
# dic["k2"].insert(1,{'a'})
#
# dic[(1,2,3,)]["key"] = (1,)
# print(dic)

"""
3.敲七游戏. 从1开始数数. 遇到7或者7的倍数(包含17,27,这种数）要在桌上敲⼀下. 
编程来完成敲七. 给出⼀个任意的数字n. 从1开始数. 数到n结束. 
把每个数字都放在列表中, 在数的过程中出现7或 者7的倍数（包含17,27,这种数）.则向列表中添加⼀个'咣' 例如, 输⼊20. 
lst = [1, 2, 3, 4, 5, 6, '咣', 8, 9, 10,11,12,13,'咣',15,16,'咣',18,19,20]
"""
num = int(input("请输入一个整数："))
lst = list()
for i in range(1,num+1):
    if i % 7 == 0 or "7" in str(i)[-1]:
        lst.append("咣")
    else:
        lst.append(i)
print(lst)

"""
4.完成36选7的操作, 1- 37之间随机产生36个数,从这36个数中选择7个不重复的数添加到列表中(5分)
"""
# from random import randint
# s = set()
# while len(s) < 7:
#     s.add(randint(1,36))
# lst = list(s)
# print(lst)

"""
5.有文件t1.txt里面的内容为:（5分）
1,alex,22,13651054608,IT
2,wusir,23,13304320533,Tearcher
3,taibai,18,1333235322,IT

利用文件操作，将其构造成如下数据类型。
[{'id':'1','name':'alex','age':'22','phone':'13651054608','job':'IT'},
{'id':'2','name':'wusir','age':'23','phone':'13304320533','job':'Tearcher'},
{'id':'3','name':'taibai','age':'18','phone':'1333235322','job':'IT'}]
"""
# lst = []
# with open("t1.txt","r",encoding="utf-8") as f:
#     for i in f:
#         a,b,c,d,e = i.strip().split(",")
#         dic = {'id':a,'name':b,'age':c,'phone':d,'job':e}
#         lst.append(dic)
# print(lst)

"""
6.有如下车牌和车辆归属地,形成一个新的字典,显示每个归属地的车辆共有多少：(8分)
cars = ['鲁A32444','鲁A12333','湘B8989M','⿊A49678','⿊B46555','沪B25044','冀A11111',"京A01101"]
locals = {'冀':{"A":"石家庄","B":"唐山"},
          '⿊':{"A":"哈尔滨","B":"齐齐哈尔"},
          '鲁':{"A":"济南","B":"青岛"},
          '鄂':{"A":"武汉","B":"黄石"},
          '湘':{"A":"长沙","B":"株洲"},
          }

结果: {'济南':2, '株洲': 1, '哈尔滨': 1,'齐齐哈尔':1,'石家庄':1}
"""
# cars = ['鲁A32444','鲁A12333','湘B8989M','⿊A49678','⿊B46555','沪B25044','冀A11111',"京A01101"]
# locals = {'冀':{"A":"石家庄","B":"唐山"},
#           '⿊':{"A":"哈尔滨","B":"齐齐哈尔"},
#           '鲁':{"A":"济南","B":"青岛"},
#           '鄂':{"A":"武汉","B":"黄石"},
#           '湘':{"A":"长沙","B":"株洲"},
#           }
# result = {}
# for i in cars:
#     if i[0] in locals:
#         if i[1] in locals[i[0]]:
#             result[locals[i[0]][i[1]]] = result.get(locals[i[0]][i[1]],0) + 1
# print(result)

"""
7.有如下值li 将所有的数字保存至字典的第一个key对应的值中，将所有的字符串保存至第二个key对应的值中(4分)
li= ["a","b",11,22,33,44,55,"66",["alex","baoyuan","taibai"],"77","88","99"]
"""
# li= ["a","b",11,22,33,44,55,"66",["alex","baoyuan","taibai"],"77","88","99"]
# lst1 = []
# lst2 = []
# dic = {}
# for i in li:
#     if type(i) == list:
#         for j in i:
#             if type(j) == int:
#                 lst1.append(j)
#             else:
#                 lst2.append(j)
#     else:
#         if type(i) == int:
#             lst1.append(i)
#         else:
#             lst2.append(i)
# dic["key1"],dic["key2"] = lst1,lst2
# print(dic)


"""
8. userinfo.txt 文件中存放以下结构:(总分8分)

alex:alex3714
wusir:123456
meet:meet123


1.让用户选择:

1.注册
2.登录

2.用户选择注册就将账号和密码添加到userinfo.txt中,如果用户名存在就提示用户名存在,不存在就进行添加(2分)
3.用户选择登录,就验证用户的账号和密码是否与userinfo.txt一致,如果一致终止循环提示登录成功(3分)
4.让用户登录三次,三次错误将用户进行锁定提示用户名已锁定,并打印错误次数(使用字符串格式化)(3分)
"""
# while True:
#     choice = input("请选择（1-注册|2-登录）：")
#     if choice == "1" or choice == "2":
#         break
#     else:
#         print("输入错误")
# if choice == "1":
#     with open("userinfo.txt","r+",encoding="utf-8") as f1:
#         name = input("请输入用户名：")
#         psw = input("请输入密码：")
#         add_name = True
#         for i in f1:
#             if name == i.split(":")[0]:
#                 print("用户名存在")
#                 add_name = False
#                 break
#         if add_name:
#             f1.write(f"\n{name}:{psw}")
#             print("注册成功！")
# elif choice == "2":
#     with open("userinfo.txt", "r", encoding="utf-8") as f2:
#         count = 3
#         while count:
#             name = input("请输入用户名：")
#             psw = input("请输入密码：")
#             status = True
#             for j in f2:
#                 a,b = j.strip().split(":")
#                 if name == a and psw == b:
#                     print("登录成功")
#                     count = False
#                     status = False
#                     break
#             if status:
#                 print("用户名或密码错误！")
#                 count -= 1
#         if status == True:
#             print(f"输入错误{count + 3}次！用户名已锁定！")
