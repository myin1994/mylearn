from mytools.mytools import *
import random

def get_min_pos(li):
    min_pos = 0
    for i in range(1,len(li)):
        if li[i] < min_pos:
            min_pos = i
    return min_pos

@cal_time
def select_sort(li):
    for i in range(len(li)-1):#n或者n-1趟
        min_pos = i #第i趟无序区范围i~最后
        for j in range(i+1,len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
        li[i],li[min_pos] = li[min_pos],li[i]

li = list(range(10000))
random.shuffle(li)
select_sort(li)
print(li)