from mytools.mytools import *
import sys
import random
sys.setrecursionlimit(10000)
def quick_sort(li,left,right):
    if left<right:#待排序的元素至少有两个元素
        mid = random_partition(li,left,right)
        # mid = partition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)


def partition(li,left,right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left

def random_partition(li,left,right):

    tmp = li[random.randint(left,right)]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left
@cal_time
def run(li,left,right):
    return quick_sort(li,left,right)
# li = list(range(5000,0,-1))
# # random.shuffle(li)
# run(li,0,len(li)-1)
# print(li)


def quick_sort2(li):
    if len(li) < 2:
        return li
    tmp = li[0]
    left = [v for v in li[1:] if v<=tmp]
    right = [v for v in li[1:] if v>tmp]
    left = quick_sort2(left)
    right = quick_sort2(right)
    return left + [tmp] +right
@cal_time
def run2(li):
    return quick_sort2(li)

# li = list(range(10000))
# random.shuffle(li)
# print(run2(li))