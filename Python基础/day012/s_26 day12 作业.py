"""
s_26 day12 作业
"""

"""
2.用列表推导式做下列小题
lst = ["alex","wusir","太白","宝元"]
过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
"""
# lst = ["alex","wusir","太白","宝元"]
# print([i.upper() for i in lst if len(i) > 2])

"""
3.求[{x:y}]其中x是0-5之间的偶数组成的元组的，y是0-5之间的奇数组成的元组
"""
# print([{tuple([x for x in range(0,6,2)]):tuple([x for x in range(1,6,2)])}])

"""
4.求3,6,9 组成的列表结果: M = [[1,2,3],[4,5,6],[7,8,9]]
"""
# print([[x-2,x-1,x] for x in [3,6,9]])

"""
5.求出50以内能被3整除的数的平方，并放入到一个列表中。
"""
# print([x**2 for x in range(51) if x % 3 ==0])

"""
6.构建一个列表：['python1期', 'python2期', 'python3期', 'python4期', 'python6期', 'python7期', 'python8期', 'python9期', 'python10期']
"""
# print([f"python{i}期" for i in range(1,11)])

"""
7.构建一个列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
"""
# print([(x,x+1) for x in range(6)])

"""
8.构建一个列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
"""
# print([i for i in range(0,19,2)])

"""
9.有一个列表l1 = ['alex', 'WuSir', '老男孩', '太白']将其构造成这种列表
['alex0', 'WuSir1', '老男孩2', '太白3']
"""
# l1 = ['alex', 'WuSir', '老男孩', '太白']
# print([v + str(k) for k,v in enumerate(l1)])

"""
10.有以下数据类型：
x = {
'name':'alex',
'Values':[{'timestamp':1517991992.94,
'values':100,},
{'timestamp': 1517992000.94,
'values': 200,},
{'timestamp': 1517992014.94,
'values': 300,},
{'timestamp': 1517992744.94,
'values': 350},
{'timestamp': 1517992800.94,
'values': 280}
],}
a.将上面的数据通过列表推导式转换成下面的类型：
[[1517991992.94, 100], [1517992000.94, 200], [1517992014.94, 300], [1517992744.94, 350], [1517992800.94, 280]]
"""
# x = {
# 'name':'alex',
# 'Values':[{'timestamp':1517991992.94,
# 'values':100,},
# {'timestamp': 1517992000.94,
# 'values': 200,},
# {'timestamp': 1517992014.94,
# 'values': 300,},
# {'timestamp': 1517992744.94,
# 'values': 350},
# {'timestamp': 1517992800.94,
# 'values': 280}
# ]}
# print([[v['timestamp'],v['values']] for v in x["Values"]])

"""
11.构建一个列表，列表里面是三种不同尺寸的T恤衫，每个尺寸都有两个颜色（列表里面的元素为元组类型）。
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
"""
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# print([(x,colors) for x in sizes])

"""
12.构建一个列表,列表里面的元素是扑克牌除去大小王以后，所有的牌类（列表里面的元素为元组类型）。
l1 = [('A','spades'),('A','diamonds'), ('A','clubs'), ('A','hearts')......('K','spades'),('K','diamonds'), ('K','clubs'), ('K','hearts') ]
"""
# lst1 = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
# lst2 = ['spades','diamonds','clubs','hearts']
# print([(x,y) for x in lst1 for y in lst2])

"""
13.看代码求结果（面试题）：
v = [i % 2 for i in range(10)]
print(v)#[0,1,0,1,0,1,0,1,0,1]

v = (i % 2 for i in range(10))#生成器
print(v)#生成器地址
验证正确
"""
