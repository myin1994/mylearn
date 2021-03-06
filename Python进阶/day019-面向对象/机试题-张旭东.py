"""
1.有列表
a = ["7net.cn", "www.7net", "www.septnet7", "7net", "www.6net", 7nte.org]
现需要从中将包含字符7net的元素给删掉，请以最少代码量实现。（3分）
"""

# a = ["7net.cn", "www.7net", "www.septnet7", "7net", "www.6net", "7nte.org"]
# print(list(filter(lambda x: "7net" not in x, a)))

"""
2.l = ['班级4', '班级1', '班级3', '班级5', '班级8']，按照数字的顺序从大到小排序，不改变原列表，请以最少代码量实现。（3分）
"""

# l = ['班级4', '班级1', '班级3', '班级5', '班级8']
# print(sorted(l,key=lambda x:x[2],reverse=True))

"""
3.现在有两元祖tu1 = ('a', 'b')，tu2 = ('cc', 'dd')，请使用python中的匿名函数和内置函数生成列表[{'a': 'cc'}, {'b': 'dd'}] （3分）
"""

# tu1 = ('a', 'b')
# tu2 = ('cc', 'dd')
# print(list(map(lambda x,y:{x:y}, tu1,tu2)))

"""
4.写一个生成器, 里面的元素是20以内所有奇数的平方减2, 并且调用生成器(2分)
"""

# g = (i**2-2 for i in range(1,20,2))
# for i in g:
#     print(i)

"""
5.lst = [{"a": 6, "b": 22}, {"a": 12, "b": 28}, {"a": 18, "b": 21}]
请写出以键b的值对lst进行从小到大排序的表达式（3分）
"""

# lst = [{"a": 6, "b": 22}, {"a": 12, "b": 28}, {"a": 18, "b": 21}]
# print(list(sorted(lst,key=lambda x:x["b"])))

"""
6.用filter函数过滤出单价大于100的股票。（3分）

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
​    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
​    {'name': 'FB', 'shares': 200, 'price': 21.09},
​    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
​    {'name': 'YHOO', 'shares': 45, 'price': 116.35},
​    {'name': 'ACME', 'shares': 75, 'price': 115.65}]
"""

# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 116.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}]
#
# print(list(filter(lambda x: x["price"] > 100, portfolio)))

"""
7.求出l1列表中成绩最高的学生的姓名。（3分）
l1 = [('王大锤', 59), ('乔碧萝', 67), ('宝哥哥', 99), ('铁蛋'，47)]
"""

# l1 = [('王大锤', 59), ('乔碧萝', 67), ('宝哥哥', 99), ('铁蛋', 47)]
# print(max(l1, key=lambda x: x[1])[0])

"""
8. 有一个lst = ["This", "is", "a", "Boy", "!"]
所有元素都是字符串, 使用sorted对它进行小写排序(3分)
"""

# lst = ["This", "is", "a", "Boy", "!"]
# print(sorted(lst, key=lambda x: x.lower()))

"""
9.将lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
转换成[1, 2, 3, 4, 5, 6, 7, 8, 9](5分)
"""

# l = list()
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for em in lst:
#     l.extend(em)
# print(l)

"""
10.写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
例如：[(‘红心’，2), (‘草花’，2), ('方片', 2)(‘黑桃’，‘2’)] (5分)
"""

# # 推导式
# lst1 = ["红心", "草花", "方片", "黑桃"]
# lst2 = ["1","2","3","4","5","6","7","8","9","10","J","Q","K"]
# print([(x,y) for y in lst2 for x in lst1])

# # 函数
# def func():
#     lst1 = ["红心", "草花", "方片", "黑桃"]
#     lst2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#     lst = list()
#     for el in lst2:
#         for em in lst1:
#             lst.append((em,el))
#     return lst
#
# print(func())

"""
11.将列表内的元素, 根据位数合并成字典(7分)

lst = [1, 2, 3, 4, 12, 23, 34, 45, 111, 222, 333, 1234, 2345, 34567, 456789]
# 输出如下字典:
{
    1: [1, 2, 3, 4],
    2: [12, 23, 34, 45],
    3: [111, 222, 333],
    4: [1234, 2345],
    5: [34567],
    6: [456789]
}
"""

# lst = [1, 2, 3, 4, 12, 23, 34, 45, 111, 222, 333, 1234, 2345, 34567, 456789]
# dic = dict()
# for el in lst:
#     if dic.get(len(str(el))):
#         dic[len(str(el))].append(el)
#     else:
#         dic[len(str(el))] = [el]
# print(dic)

"""
12.把s = "aaaabbbcc"
这种形状式中特定的字符串压缩成a4b3c2这种字符串的格式(10分)
"""

# 方法一:顺序不固定
# s = "aaaabbbcc"
# print("".join([el+str(s.count(el)) for el in set(s)]))

# 方法二:顺序固定
# from collections import Counter
# s = "aaaabbbcc"
# print("".join([k+str(v) for k,v in Counter(s).items()]))

"""
13.有两个字符串列表a和b, 每个字符串是由逗号分隔的一些字符: (10分)
a = [
    "a:1",
    "b:2:3",
    "c:5:7"
]
b = [
    "a:2:3",
    "b:4:5",
    "d:6:8"
]

# 生成如下列表
c = [
    "a:1:2:3",
    "b:2:3:4:5",
    "c:5:7",
    "d:6:8"
]
"""

a = [
    "a:1",
    "b:2:3",
    "c:5:7"]
b = [
    "a:2:3",
    "b:4:5",
    "d:6:8"]
dic_a = {x[0]: x[1:] for x in a}
dic_b = {x[0]: x[1:] for x in b}
c = list()
for k, v in dic_a.items():
    if k in dic_b:
        c.append(k + v + dic_b[k])
    else:
        c.append(k + v)
for k, v in dic_b.items():
    if k not in dic_a:
        c.append(k + v)
print(c)



