from mytools.mytools import *
import random

@cal_time
def bubble_sort(li):
    flag = True
    for i in range(len(li)-1): #i表示第n趟 一共n或者n-1趟
        for j in range(len(li)-i-1):#第i趟 无序区[0,n-i-1] j表示箭头0~n-i-2
            if li[j]<li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                flag = False
        if flag:
            return li
    return li


li = list(range(10000))
random.shuffle(li)
bubble_sort(li)
print(li)
