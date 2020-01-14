from mytools.mytools import *
import random
@cal_time
def insert_sort(li):
    for i in range(1,len(li)):#i表示摸到的牌的下标
        tmp = li[i] #摸到的牌
        j = i - 1
        while j>=0 and li[j] > tmp:
        #只要往后挪就循环 2个条件都要满足
        #如果 j=-1停止挪 如果li[j]小了停止挪
            li[j+1] = li[j]
            j -= 1
        # j位置在循环结束时，要么是-1，要么是一个比tmp小的值
        li[j+1] = tmp

li = list(range(10000))
random.shuffle(li)
insert_sort(li)
print(li)