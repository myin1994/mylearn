# range -- 范围
# 通过range达到循环数字
# 坑
# a = range(0,5)
# print(a)  #打印range本身 python2 [0,1,2,3,4]  python3 range(0,5)

# 字符串转换列表
# a = "alex"
# print(list(a))
# a = [i for i in a]
# print(a)
# b = []
# b.extend(a)
# print(b)

# range() 和咱们的切片很像
# range(起始位置,终止位置,步长) 顾头不顾尾
# lst = list(range(0,5)) #直接打印列表
# print(lst)

# for i in range(0,51,2): #偶数
#     print(i)
# for i in range(1,51,2): #奇数
#     print(i)

# 一般情况可以只写终止位置，使用步长时要添加起始位置
# for i in range(10,2,-1):
#     print(i)
#
# for i in range(100,-1,-1):
#     print(i)

# range() 是可迭代对象