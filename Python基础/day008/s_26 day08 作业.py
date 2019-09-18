"""
s_26 day08 作业
"""

"""
1.有如下文件，a1.txt，里面的内容为：
老男孩是最好的学校，
全心全意为学生服务，
只为学生未来，不为牟利。
我说的都是真的。哈哈
分别完成以下的功能：
a,将原文件全部读出来并打印。
b,在原文件后面追加一行内容：信不信由你，反正我信了。
c,将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。
d,将原文件全部清空，换成下面的内容：
每天坚持一点，
每天努力一点，
每天多思考一点，
慢慢你会发现，
你的进步越来越大。
"""
# with open("a1.txt","r",encoding="utf-8") as f:
#     print(f.read())

# with open("a1.txt","a",encoding="utf-8") as f:
#     f.write("\n信不信由你，反正我信了。")

# with open("a1.txt","a+",encoding="utf-8") as f:
#     f.seek(0,0)
#     print(f.read())
#     f.write("\n信不信由你，反正我信了。")

# with open("a1.txt","w",encoding="utf-8") as f:
#     f.write("每天坚持一点，\n每天努力一点，\n每天多思考一点，\n慢慢你会发现，\n你的进步越来越大。")

"""
2.有如下文件，t1.txt,里面的内容为：
葫芦娃，葫芦娃，
一根藤上七个瓜
风吹雨打，都不怕，
啦啦啦啦。
我可以算命，而且算的特别准:
上面的内容你肯定是心里默唱出来的，对不对？哈哈
分别完成下面的功能：
a,以r的模式打开原文件，利用for循环遍历文件句柄。
b,以r的模式打开原文件，以readlines()方法读取出来，并循环遍历 readlines(),并分析a,与b 有什么区别？深入理解文件句柄与 readlines()结果的区别。
c,以r模式读取‘葫芦娃，’前四个字符。
d,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
e,以a+模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将 原内容全部读取出来。
"""
# with open("t1.txt","r",encoding="utf-8") as f:
#     for i in f:
#         print(i)

# f = open("t1.txt","r",encoding="utf-8")
# for i in f.readlines():
#     print(i)
# f.close()
# a,b两种方式在输出内容上没有区别，但是遍历的对象不同，a是对句柄，b是对列表,并且列表 占据内存更多

# with open("t1.txt","r",encoding="utf-8") as f:
#     print(f.read(4))

# with open("t1.txt","r",encoding="utf-8") as f:
#     print(f.readline().strip())

# with open("t1.txt","a+",encoding="utf-8") as f:
#     f.write("\n老男孩教育")
#     f.seek(0,0)
#     print(f.read())

"""
3.文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3
通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
"""
# dic = dict()
# f = open("a.txt","r",encoding="utf-8")
# lst =f.readlines()
# price_sum = 0
# for i in lst:
#     lst2 = i.strip().split()
#     lst2[-1] = int(lst2[-1])
#     lst2[-2] = int(lst2[-2])
#     price_sum += lst2[-2] * lst2[-1]
#     dic["name"],dic["price"],dic["amount"] = lst2
#     lst[lst.index(i)] = dic.copy()
# print(f"总价钱：{price_sum}")
# print(lst)

# lst = []
# f = open("a.txt","r",encoding="utf-8")
# price_sum = 0
# for i in f:
#     a,b,c = i.split()
#     price_sum += int(b) * int(c)
#     dic = {"name":a,"price":int(b),"amount":int(c)}
#     lst.append(dic)
# print(lst)
# print(f"总价钱：{price_sum}")
"""
4.有如下文件b.txt：
alex是老男孩python发起人，创建人。
alex其实是人妖。
谁说alex是sb？
你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
将文件中所有的alex都替换成大写的SB（文件的改的操作）。
"""
# with open("b.txt","r",encoding="utf-8") as f1,open("b_1.txt","w",encoding="utf-8") as f2:
#     content = f1.readlines()
#     for i in content:
#         f2.write(i.replace("alex","SB"))
#         f2.flush()
# import os
# os.rename("b.txt","b_2.txt")
# os.rename("b_1.txt","b.txt")

# with open("b.txt","r",encoding="utf-8") as f1,open("b_1.txt","w",encoding="utf-8") as f2:
#     for i in f:
#         f2.write(i.replace("alex","SB"))
#         f2.flush()
# import os
# os.rename("b.txt","b_2.txt")
# os.rename("b_1.txt","b.txt")
"""
5.文件c1.txt内容(选做题)

name:apple price:10 amount:3 year:2012
name:tesla price:100000 amount:1 year:2013
.......

通过代码，将其构建成这种数据类型：
[{'name':'apple','price':10,'amount':3,year:2012},
{'name':'tesla','price':1000000,'amount':1}......]
并计算出总价钱。
"""
# dic = dict()
# price_sum = 0
# f = open("c1.txt","r",encoding="utf-8")
# lst = f.readlines()
# for i in lst:
#     lst2 = i.strip().split()
#     for j in lst2:
#         lst3 = j.split(":")
#         if lst3[-1].isdecimal():
#             lst3[-1] = int(lst3[-1])
#         dic[lst3[0]] = lst3[1]
#     price_sum += dic["price"] * dic["amount"]
#     lst[lst.index(i)] = dic.copy()
# print(f"总价钱：{price_sum}")
# print(lst)

# lst = []
# f = open("c1.txt","r",encoding="utf-8")
# for i in f:
#     dic = {}
#     for j in i.split():
#         k,v = j.split(":")
#         dic[k] = v
#     lst.append(dic)
# print(lst)
"""
6.文件d1.txt内容(选做题)
序号 部门 人数 平均年龄 备注
1 python 30 26 单身狗
2 Linux 26 30 没对象
3 运营部 20 24 女生多
.......

通过代码，将其构建成这种数据类型：
[{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},
......]
"""
# dic = dict()
# price_sum = 0
# f = open("d1.txt","r",encoding="utf-8")
# lst = f.readlines()
# lst_result = list()
# for i in lst:
#      lst2 = i.strip().split()
#      for j in lst2:
#          if lst.index(i) == 0:
#             dic[j] = None
#          else:
#              if j.isdecimal():
#                  j = int(j)
#              dic[list(dic)[lst2.index(str(j))]] = j
#      if lst.index(i) != 0:
#         lst_result.append(dic.copy())
# print(lst_result)

# lst = []
# f = open("d1.txt","r",encoding="utf-8")
# a,b,c,d,e = f.readline().split()
# # print(a,b,c,d,e)
# for i in f:
#     num,depart,peolpe,age,mark = i.split()
#     dic = {a:num,b:depart,c:peolpe,d:age,e:mark}
#     lst.append(dic)
# print(lst)