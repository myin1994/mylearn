# 作用
#     后期开发代码时避免出现问题，不知道原因
#     面试几乎必问
#         什么是赋值
#         什么是浅拷贝
#         什么是深拷贝

# 赋值：多个变量名指向同一个内存地址
# a = 10 #不可变数据类型
# b = a # a,b 都指向10的内存地址
# a = 11
# print(a,b)
# print(id(a),id(b))

# lst =[1,2,3] #可变数据类型
# lst1 = lst #lst,lst1 都指向列表的内存地址
# print(lst,lst1)
# lst.append(4)
# lst = [1,2,3,4]
# print(lst,lst1)
# print(id(lst),id(lst1))

# lst =[1,2,3] #可变数据类型
# lst1 = lst #lst,lst1 都指向列表的内存地址
# lst = lst.append(4)  #返回值为None
# print(lst,lst1)

# dic = {"key":11,"key2":[1,2,3]}
# dic1 = dic #dic,dic1都指向字典的内存地址，理解为新的引用
# dic["key2"].append(5)
# del dic["key"]
# print(dic,dic1)
# print(id(dic) , id(dic1))

# 总结：多个变量指向同一个内存地址，如果这个内存地址的数据类型是
# 不可变的数据类型的时候，会新开空间（字符串，数字）
# 可变的数据类型时，会在原地进行修改


# 浅拷贝：
# lst = [1,2,3]
# lst1 = lst.copy()  #复制,新的列表
# print(lst,lst1)
# lst1.append(4)
# print(lst,lst1)
# print(id(lst),id(lst1))
# print(id(lst[0]),id(lst1[0]),id(1))

# lst = [1,2,[3,4]]
# lst1 = lst[:] #只拷贝第一层
# print(id(lst),id(lst1))
# print(id(lst[-1]),id(lst1[-1]))
# lst1[-1].append(5)
# print(lst,lst1)
# print(id(lst[-1]),id(lst1[-1]))

# lst = [1,2,[3,4]]
# lst1 = lst.copy()
# lst[0] = 5
# lst[-1] = 8
# # lst[-1].append(8)
# print(id(lst[-1]),id(lst1[-1]))
# print(lst,lst1)

# lst = [2,3,[4,5],257]
# lst1 = lst
# lst2 = lst[:]
# lst2[2].append(257)
# print(lst)
# print(lst1)
# print(lst2)
# print(id(lst[2][-1]),id(lst[-1]))  #再看看地址
# print(id(lst1[2][-1]),id(lst1[-1]))
# print(id(lst2[2][-1]),id(lst2[-1]))
# print(id(257))
# lst = [2,3,[4,5],6]
# lst1 = lst
# lst2 = lst[:]
# lst2[-1] = [8,9]
# lst1[-1].append([0]) #报错

# 深拷贝
# import copy  #导入copy模块
# lst = [-111,-111,[3,4]]
# lst1 = copy.deepcopy(lst)  #深拷贝
# print(id(lst),id(lst1)) #外壳不一样
# print(id(lst[0]),id(lst1[0]))   #不可变数据  --共用
# print(id(lst[1]),id(lst1[1]))   #不可变数据  --共用，开始定义过是不同地址，复制出来的是用相同地址
# print(id(lst[-1]),id(lst1[-1]))  #可变数据--新开辟空间
# print(id(lst[-1][-1]),id(lst1[-1][-1]))  #里面的不可变数据  --共用

# 总结：
# 赋值:多个变量名指向同一个内存地址
# 浅拷贝：只拷贝第一层的内存地址，可变和不可变的数据都是共用的，能看到是因为通过内存地址去查找值然后显示的
# 深拷贝：不可变数据，元素共用内存地址；可变数据类型开辟新的空间，不管嵌套多少层都是这样的原理（理解为互相不会影响）
