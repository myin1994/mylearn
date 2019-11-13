# lst1 = [1,3,4,5,6]
#
# lst2 = [2,3,4,7,8]
#
# def merge(lst1,lst2):
#     lst3 = []
#     i1 = i2 = 0
#     l1 = len(lst1)
#     l2 = len(lst2)
#     while i1 < l1 and i2 < l2:
#         if lst1[i1] < lst2[i2]:
#             lst3.append(lst1[i1])
#             i1 += 1
#         else:
#             lst3.append(lst2[i2])
#             i2 += 1
#     if i1 < l1:
#         lst3.extend(lst1[i1:])
#     if i2 < l2:
#         lst3.extend(lst2[i2:])
#     return lst3
#
#
# print(merge(lst1, lst2))


# lst1 = [1,3,4,5,6]
# lst2 = [2,3,4,7,8]
def merge(lst1,lst2):

    i1 = i2 = i3 = 0
    l1 = len(lst1)
    l2 = len(lst2)
    lst3 = [""]*(l1+l2)
    while i1 < l1 and i2 < l2: #每次找到一个最小值填充到第三个列表中
        if lst1[i1] < lst2[i2]:
            lst3[i3] = lst1[i1]
            i1 += 1
        else:
            lst3[i3] = lst2[i2]
            i2 += 1
        i3 += 1
    while i1 < l1:#若剩余全为lst1则全部按顺序添加即可
        lst3[i3] = lst1[i1]
        i1 += 1
        i3 += 1
    while i2 < l2:#若剩余全为lst2则全部按顺序添加即可
        lst3[i3] = lst2[i2]
        i2 += 1
        i3 += 1
    return lst3

# print(merge([6], [7,8]))
# print(merge(lst1, lst2))
lst = [6,8,7]
def mergesort(lst):
    length = len(lst)
    if length <= 1:
        return lst
    else:
        half = length // 2
        lst1, lst2 = lst[:half], lst[half:]
        # return merge(mergesort(lst1),mergesort(lst2))
        lst1 = mergesort(lst1)
        lst2 = mergesort(lst2)
        return merge(lst1,lst2)

print(mergesort(lst))
# print(lst)
#