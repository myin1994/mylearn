# 冒泡排序

"""
冒泡排序要对一个列表多次重复遍历。
它要比较相邻的两项，并且交换顺序排错的项。
每对列表实行一次遍历，就有一个最大项排在了正确的位置。
大体上讲，列表的每一个数据项都会在其相应的位置 “冒泡”。
如果列表有 n 项，第一次遍历就要比较 n-1 对数据。
需要注意，一旦列表中最大(按照规定的原则定义大小)的数据是所比较的数据对中的一个，它就会沿着列表一直后移，直到这次遍历结束。
"""
# 冒泡排序
# def bubbleSort(alist):
#     n = len(alist)
#     for i in range(n-1, 0, -1):
#         for j in range(0, i):
#             if alist[j] > alist[j+1]:#判断前者是否需要与后者调换位置
#                 alist[j], alist[j+1] = alist[j+1], alist[j]
#     return alist
#
# a = [1,2,4,5,9,8,6,4,3]
# bubbleSort(a)
# print(a)

# 优化
def bubbleSort(alist):
    n = len(alist)
    flag = False
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if alist[j] > alist[j+1]:#判断前者是否需要与后者调换位置
                alist[j], alist[j+1] = alist[j+1], alist[j]

    return alist

a = [1,2,4,5,9,8,6,4,3]
bubbleSort(a)
print(a)