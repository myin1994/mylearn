from mytools.mytools import *
import sys
import random
def merge_list(li1,li2):
    li = []
    i = 0
    j = 0
    while i<len(li1) and j < len(li2):
        if li1[i] <= li2[j]:
            li.append(li1[i])
            i += 1
        else:
            li.append(li2[j])
            j += 1
    while i < len(li1):
        li.append(li1[i])
        i += 1
    while j < len(li2):
        li.append(li2[j])
        j += 1
    return li


# li1 = [2,5,7,8,9]
# li2 = [1,3,4,6]
# print(merge_list(li1, li2))

def merge(li,low,mid,high):
    #列表两段有序【low，mid】 【mid+1，high】
    i = low
    j = mid + 1
    li_tmp = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            li_tmp.append(li[i])
            i += 1
        else:
            li_tmp.append(li[j])
            j += 1
    while i<= mid:
        li_tmp.append(li[i])
        i += 1
    while j<=high:
        li_tmp.append(li[j])
        j += 1
    for i in range(low,high+1):
        li[i] = li_tmp[i-low]
    # li[low:high+1] = li_tmp

# li = [2,5,7,8,9,1,3,4,6]
# merge(li,0,4,8)
# print(li)

def merge_sort(li,low,high):#排序li的low到high的范围
    if low<high:
        mid = (low+high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)
@cal_time
def run(li,low,high):
    return merge_sort(li,low,high)
li = list(range(100000,-1,-1))
# random.shuffle(li)
run(li,0,len(li)-1)
print(li)