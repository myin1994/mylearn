import random
import sys
sys.setrecursionlimit(100000)
li = list(range(10000))
#二分查找
#通过每次对比中间值与查找值的大小对半缩小范围
def bin_search(li,val):
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high) // 2
        if li[mid] == val:
            return mid
        if li[mid] < val:
            low = mid + 1
        else:
            high = high - 1
    return -1

# print(bin_search(li,9999))
#递归版二分查找
def recursion_bin_search(li,val,low,high):
    if low <= high:
        mid = (low + high) // 2
        if li[mid] == val:
            return mid
        if li[mid] < val:
            return recursion_bin_search(li,val,mid+1,high)
        else:
            return recursion_bin_search(li,val,low,mid-1)

# print(recursion_bin_search(li,9999,0,len(li)-1))

#冒泡排序
#总体思想，每次循环将待排序数据与相邻数据比较，冒泡到应有位置
def pubble_sort(li):
    flag= True
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j]<li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                flag = False
        if flag:
            return
random.shuffle(li)
# pubble_sort(li)
# print(li)

#选择排序，每次循环找出最大或最小值的索引，最后再最大最小值放在应有位置

def select_sort(li):
    for i in range(len(li)-1):
        min_pos = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
        li[i],li[min_pos] = li[min_pos],li[i]


# select_sort(li)
# print(li)

#插入排序，把第一个数据当做有序，每次取一个数据进行插入

def insert_sort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i-1
        while j >= 0 and li[j]>tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp

# insert_sort(li)
# print(li)

def replace_kuoh(s):
    while 1:
        length1 = len(s)
        s = s.replace('()', "").replace('[]', "").replace('{}', "")
        length2 = len(s)
        if length1 == length2:
            return False if length2 else True
            # if not length2:
            #     return True
            # else:
            #     return False
print(replace_kuoh("]{[}"))