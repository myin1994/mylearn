"""
选择排序提高了冒泡排序的性能，它每遍历一次列表只交换一次数据，即进行一次遍历时找到最大的项，完成遍历后，再把它换到正确的位置。
和冒泡排序一样，第一次遍历后，最大的数据项就已归位，第二次遍历使次大项归位。
这个过程持续进行，一共需要 n-1 次遍历来排好 n 个数 据，因为最后一个数据必须在第 n-1 次遍历之后才能归位。
"""
# def selectionSort(alist):
#     n = len(alist)
#
#     for i in range(n - 1):
#         # 寻找[i,n]区间里的最小值
#         min_index = i
#         for j in range(i+1, n):
#             if alist[j] < alist[min_index]:
#                 min_index = j
#         alist[i], alist[min_index] = alist[min_index], alist[i]
#     return alist
#
# print(selectionSort([1,2,4,5,9,8,6,4,3,1]))

def selectionSort(alist):
    n = len(alist)

    for i in range(n-1,0,-1):
        max_index = i
        for j in range(i-1,0,-1):
            if alist[j] > alist[max_index]:
                max_index = j
        alist[i], alist[max_index] = alist[max_index], alist[i]
    return alist

print(selectionSort([1,2,4,5,9,8,6,4,3,1]))