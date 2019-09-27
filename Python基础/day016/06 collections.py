# 1.统计
# lst = [11,2,2,11,2,3,4,5,6,7,8,3,2,4,5,6,4,3]
# collections
# dic = {}
# for i in lst:
#     dic[i] = lst.count(i)
# print(dic)

# lst = [11,2,2,11,2,3]
# from collections import Counter
# print(dict(Counter(lst)))
# print(Counter(lst))

# 2.有序字典
# python2  中使用
# from collections import OrderedDict
# a = OrderedDict({"key":1,"key2":2})
# print(a)
# print(a["key"])

# 3.默认字典
# from collections import defaultdict
# dic = defaultdict(lambda :"2")
# dic["key"] += "11"
# dic["key1"]
# print(dic)

# lst = [11,22,33,44,55,77,88,99]
# dic = {}
# for i in lst:
#     if i > 66:
#         dic.setdefault("key2",[]).append(i)
#     else:
#         dic.setdefault("key1",[]).append(i)
# print(dic)

# from collections import defaultdict
# dic = defaultdict(list)
# lst = [11,22,33,44,55,77,88,99]
# for i in lst:
#     if i > 66:
#         dic["key2"].append(i)
#     else:
#         dic["key1"].append(i)
# print(dic)

# 4.双端队列
# 1.队列：先进先出

# lst = []
# lst.append(1)
# lst.append(2)
# lst.append(3)
# lst.append(4)
#
# print(lst)
# lst.pop(0)
# print(lst)


# from collections import deque
# lst = deque([11,22,33,44,55])
# print(lst)
# lst.append(66)
# print(lst)
# lst.appendleft(44)
# print(lst)
# lst.pop()
# print(lst)
# lst.popleft()
# print(lst)

# 2.栈：先进后出
# lst = []
# lst.append(1)
# lst.append(2)
# lst.append(3)
# print(lst)
# lst.pop()
# print(lst)
# lst.pop()
# print(lst)

# 列表，队列，双端队列，单向链表，双向链表

# gc：垃圾回收机制
# 以引用计数为主，标记清除和分带回收为辅

# a = 10
# b = a
# c = a
# d = c

# 5.命名元组
from collections import namedtuple
dg = namedtuple("dg",["jd","wd","gd"])
a = dg(111,222,8888)
print(a)
print(a.jd)
print(a[2])