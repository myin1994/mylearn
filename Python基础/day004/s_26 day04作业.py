"""
s_26 day04作业
"""
"""
1.写代码，有如下列表，按照要求实现每一个功能

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
"""
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]

# 计算列表的长度并输出
# print(len(li))

# 列表中追加元素"seven",并输出添加后的列表
# li.append("seven")
# print(li)

# 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# li.insert(0,"Tony")
# print(li)

# 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# li[1] = "Kelly"
# print(li)

# 请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# l2=[1,"a",3,4,"heart"]
# li.extend(l2)
# print(li)

# 请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# s = "qwert"
# li.extend(s)
# print(li)

# 请删除列表中的元素"ritian",并输出添加后的列表
# li.remove("ritian")
# print(li)

# 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# print(li.pop(1),li)

# 请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[1:4]
# print(li)

"""
2.写代码，有如下列表，利用切片实现每一个功能

li = [1, 3, 2, "a", 4, "b", 5,"c"]
"""
li = [1, 3, 2, "a", 4, "b", 5,"c"]

# 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# l1 = li[:3]
# print(l1)

# 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
# l2 = li[3:-2]
# print(l2)

# 通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
# l3 = li[:-1:2]
# print(l3)

# 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
# l4 = li[1:-2:2]
# print(l4)

# 通过对li列表的切片形成新的列表l5,l5 = ["c"]
# l5 = li[-1:]
# print(l5)

# 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
# l6 = li[-3::-2]
# print(l6)

"""
3.写代码，有如下列表，按照要求实现每一个功能。

lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
将列表中的字符串"1"变成数字101（用两种方式）。
"""
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]

# 将列表lis中的"tt"变成大写（用两种方式）。
# lis[3][2][1][0] = "TT"  #第一种
# lis[3][2][1][0] = lis[3][2][1][0].upper()  #第二种
# print(lis)

# 将列表中的数字3变成字符串"100"（用两种方式）。
# lis[1] = "100" #第一种
# lis[3][2][1][1] = "100"
# lis[1:2] = ["100"] #第二种
# lis[3][2][1][1:2] = ["100"]
# print(lis)

# 将列表中的字符串"1"变成数字101（用两种方式）。
# lis[3][2][1][-1] = 101 #第一种
# lis[3][2][1][-1:] = [101] #第二种
# print(lis)

"""
4.请用代码实现：
li = ["alex", "wusir", "taibai"]
利用下划线将列表的每一个元素拼接成字符串"alex_wusir_taibai"
"""
# li = ["alex", "wusir", "taibai"]
# lis = "_".join(li) #第一种
# print(lis)

# lis = li[0] + "_" + li[1] + "_" + li[2] #第二种
# print(lis)

# lis = "" #第三种
# for i in li:
#     lis += i + "_"
# print(lis.strip("_"))

"""
5.利用for循环和range打印出下面列表的索引。

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
"""
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in li:  #for循环
#     print(li.index(i))

# for i in range(len(li)): #for循环与range
#     print(i)

"""
6.利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
"""
# li = []  #第一种
# for i in range(2,101,2):
#     li.append(i)
# print(li)

# li = list(range(2,101,2))  #第二种
# print(li)
"""
7.利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
"""
# li = []
# for i in range(3,51):
#     if i % 3 == 0:
#         li.append(i)
# print(li)

"""
8.利用for循环和range从100~1，倒序打印。
"""
# for i in range(100,0,-1):
#     print(i)

"""
9.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
"""
# li = list(range(100,9,-2))
# for i in li:
#     if i % 4 != 0:
#         li.remove(i)
# print(li)

"""
10.利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成*。
"""
# li = list(range(1,31))
# for i in li:
#     if i % 3 == 0:
#         li[li.index(i)] = "*"
# print(li)

"""
11.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
"""
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
# lis = []
# for i in li:
#     if i.replace(" ","").upper().startswith("A") and i.replace(" ","").endswith("c"):
#         lis.append
#         (i.replace(" ",""))
# for i in lis:
#     print(i)

"""
12.开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
敏感词列表 li = ["老师苍", "东京比较热", "武兰", "波多"]
则将用户输入的内容中的敏感词汇替换成等长度的*（老师苍就替换***），并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
"""
# li = ["老师苍", "东京比较热", "武兰", "波多"]
# lis = []
# content = input("请输入评论内容：")
# for i in li:
#     if i in content:
#         content = content.replace(i,"*"*len(i))
# lis.append(content)
# print(lis)

"""
13.有如下列表（选做题）
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
我想要的结果是：
1
3
4
alex
3
7
8
taibai
5
ritian
"""
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# for i in li:
#     if type(i) == list:
#         for k in i:
#             if type(k) == str:
#                 print(k.lower())
#             else:
#                 print(k)
#     elif type(i) == str:
#         print(i.lower())
#     else:
#         print(i)