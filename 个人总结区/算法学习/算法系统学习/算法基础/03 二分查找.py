#列表为顺序结构
import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper
@cal_time
def bin_search(li,val):
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high) // 2
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# li = list(range(0,20000000))
# print(bin_search(li,37777))

import sys
sys.setrecursionlimit(20000)
def recursion_bin_search(li,val,low,high):
    if low <= high:
        mid = (low+high)//2
        print(mid)
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            return recursion_bin_search(li,val,mid+1,high)
        else:
            return recursion_bin_search(li, val, low, mid-1)
    else:
        return -1
@cal_time
def run(li, val, low, high):
    return recursion_bin_search(li, val, low, high)

# li = list(range(0,200))
# print(run(li,2000,0,len(li)-1))

def twoSum(nums, target):
    for i in nums:
        try:
            j = nums.index(target - i)
            print(i, j)
            # if nums.index(i) != j:
            return [nums.index(i), j]
        except:
            continue


# print(twoSum([2, 7, 11, 15], 9))