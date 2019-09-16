# lst = [11,22,33,44,55]
# 列表删除时会自动补位，使用range或复制一份
# for循环 删除列表元素
# for i in range(len(lst)):  #第一种
#     lst.pop()
# print(lst)

# lst1 = lst.copy()  #第二种
# for i in lst1:
#     lst.remove(i)
# print(lst)

# 字典和集合
# 大小说的是字典的长度，长度就是键值对的个数
#字典和集合在循环（迭代）中不可删除键值对，但可修改键的值
# dic = {"key":1,"key2":2}
# for i in dic:   #报错
#     del dic[i]
# print(dic)

# dic1 = dic.copy()
# for i in dic1:
#     del dic[i]
# print(dic) #{}

# s = {1,2,3,4,5,6}
# for i in list(s):
#     s.remove(i)
# print(s)

# lst = [11,22,33,44,55,66]
#
# tu = tuple(lst)
# for i in range(len(tu)):
#     if i % 2 != 0:
#         lst.remove(tu[i])
# print(lst)
#
# print(lst[::2])
#
# del lst[1::2]
# print(lst)