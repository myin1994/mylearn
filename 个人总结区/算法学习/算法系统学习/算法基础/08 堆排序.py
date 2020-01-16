from mytools.mytools import *
import sys
import random

sys.setrecursionlimit(10000)


def sift(li, low, high):
    # li表示数，low表示树根节点，high表示树最后一个节点的位置(作用是看边界)
    tmp = li[low]
    i = low  # i指向空位
    j = 2 * i + 1  # j初始指向左孩子
    while j <= high:  # 循环退出的第二种情况：j>high，说明空位i没有孩子
        if j + 1 <= high and li[j] < li[j + 1]:  # 如果右孩子存在并且比左孩子大，指向右孩子
            j += 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:  # 循环退出的第一种情况：j位置的值比tmp小，说明两个孩子都比tmp小
            break
    li[i] = tmp


@cal_time
def heap_sort(li):
    n = len(li)
    # 1. 构造堆
    for low in range(n // 2 - 1, -1, -1):
        sift(li, low, n - 1)
    # 2. 挨个出数
    for high in range(n - 1, -1, -1):
        li[0], li[high] = li[high], li[0]  # 退休棋子
        sift(li, 0, high - 1)  # 调整堆


# li = list(range(100000))
# random.shuffle(li)
# heap_sort(li)
# print(li)

import heapq

li = [9, 8, 2, 7, 3, 4, 2, 1]
heapq.heapify(li)
print(li)

import heapq
def heapsort(li):
    h = []
    for value in li:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]
