"""
s_26 day07作业
"""

"""
1.看代码写结果

v1 = [1,2,3,4,5]
v2 = [v1,v1,v1]
v1.append(6)
print(v1)  #[1,2,3,4,5,6]
print(v2)  #[[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
验证正确
"""

"""
2.看代码写结果

v1 = [1,2,3,4,5]
v2 = [v1,v1,v1]
v2[1][0] = 111
v2[2][0] = 222
print(v1)  #[222,2,3,4,5]
print(v2)  #[[222,2,3,4,5],[222,2,3,4,5],[222,2,3,4,5]]
验证正确
"""

"""
3.看代码写结果，并解释每一步的流程。

v1 = [1,2,3,4,5,6,7,8,9]
v2 = {}
for item in v1: #遍历v1中每个元素
    if item < 6:
        continue #小于6的元素重新开始循环
    if 'k1' in v2:
        v2['k1'].append(item)  #"k1"是v2的键，则对键的值-列表追加v1元素
    else:
        v2['k1'] = [item ] #第一次大于等于6的元素添加键值对{"k1":6}
print(v2) #{"k1":[6,7,8,9]}
验证正确
"""

"""
4.简述赋值和深浅拷贝？

赋值：多个变量名指向相同的内存地址（修改时，不可变数据类型开辟新空间；可变数据类型原地修改）

浅拷贝：只拷贝第一次内存地址，可变不可变数据共用内存地址（里面的可变数据类型仍会同步变化）

深拷贝：不可变数据类型共用内存地址，可变数据类型开辟新空间（互不影响）
"""

"""
5.看代码写结果

import copy
v1 = "alex"
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
print(v1 is v2) #浅拷贝元素不可变数据类型共用内存地址，True
print(v1 is v3) #深拷贝元素不可变数据类型共用内存地址，True
一开始忽略了元素类型是不可变数据类型，对不可变数据类型而言深浅拷贝都是共用内存地址的
"""

"""
6.看代码写结果

import copy
v1 = [1,2,3,4,5]
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
print(v1 is v2) #False 可变数据类型新开空间（第一层）
print(v1 is v3) #False 可变数据类型新开空间
验证正确
"""

"""
7.看代码写结果

import copy
v1 = [1,2,3,4,5]
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
​
print(v1[0] is v2[0]) #True 不可变数据类型共用内存地址
print(v1[0] is v3[0]) #True
print(v2[0] is v3[0]) #True
验证正确
"""

"""
8.看代码写结果

import copy
​
v1 = [1,2,3,4,[11,22]]
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
​
print(v1[-1] is v2[-1]) #True 浅拷贝只拷贝第一层，第二层可变数据类型共用内存地址
print(v1[-1] is v3[-1]) #False 深拷贝可变数据类型均新开内存地址
print(v2[-1] is v3[-1]) #False
验证正确
"""

"""
9.看代码写结果

import copy
​
v1 = [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]
v2 = copy.copy(v1)
​
print(v1 is v2) #False
​
print(v1[0] is v2[0]) #True
print(v1[3] is v2[3]) #True
​
print(v1[3]['name'] is v2[3]['name']) #True
print(v1[3]['numbers'] is v2[3]['numbers']) #True
print(v1[3]['numbers'][1] is v2[3]['numbers'][1]) #True
验证正确
"""

"""
10.看代码写结果

import copy
v1 = [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]
v2 = copy.deepcopy(v1)
print(v1 is v2) #False
print(v1[0] is v2[0]) #True
print(v1[3] is v2[3]) #False

print(v1[3]['name'] is v2[3]['name']) #True
print(v1[3]['numbers'] is v2[3]['numbers']) #False
print(v1[3]['numbers'][1] is v2[3]['numbers'][1]) #True
验证正确
"""

"""
11.请说出下面a,b,c三个变量的数据类型。
a = ('太白金星') #str
b = (1,) #tuple
c = ({'name': 'barry'}) #dict
验证正确
"""

"""
12.按照需求为列表排序：
l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]

"""
# l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]
# 从大到小排序
# l1.sort()
# print(l1)
# 从小到大排序
# l1.sort(reverse=True)
# print(l1)
# 反转l1列表
# l1.reverse()
# print(l1)

"""
13.利用python代码构建一个这样的列表(升级题)：

[['_','_','_'],['_','_','_'],['_','_','_']]
"""
# lst = [["_"] * 3] * 3
# print(lst)

"""
14.看代码写结果：

l1 = [1,2,]
l1 += [3,4]
print(l1)  #[1,2,3,4] 迭代增加
"""

"""
15.看代码写结果：

dic = dict.fromkeys('abc',[])
dic['a'].append(666)
dic['b'].append(111)
print(dic) #{"a":[666,111],"b":[666,111],"c":[666,111]}
验证正确
"""

"""
16.l1 = [11, 22, 33, 44, 55]，请把索引为奇数对应的元素删除
"""
# l1 = [11, 22, 33, 44, 55]

#第一种
# del l1[1::2]
# print(l1)

#第二种
# tu = tuple(l1)
# for i in tu:
#     if tu.index(i) % 2 != 0:
#         l1.remove(i)
# print(l1)

"""
17.dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18} 请将字典中所有键带k元素的键值对删除.
"""
# dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18}
# lst = list(dic)
# for i in lst:
#     if "k" in i:
#         del dic[i]
# print(dic)

"""
18.完成下列需求：
s1 = '宝元'
将s1转换成utf-8的bytes类型。
将s1转化成gbk的bytes类型。
b = b'\xe5\xae\x9d\xe5\x85\x83\xe6\x9c\x80\xe5\xb8\x85'
b为utf-8的bytes类型，请转换成gbk的bytes类型。
"""
# s1 = '宝元'
# s2 = s1.encode("utf-8")
# s3 = s1.encode("gbk")
# print(s2)
# print(s3)
# b = b'\xe5\xae\x9d\xe5\x85\x83\xe6\x9c\x80\xe5\xb8\x85'
# s4 = b.decode("utf-8")
# print(s4)
# s5 = s4.encode("gbk")
# print(s5)

"""
19.用户输入一个数字，判断一个数是否是水仙花数。
水仙花数是一个三位数, 三位数的每一位的三次方的和还等于这个数. 那这个数就是一个水仙花数,
例如: 153 = 1**3 + 5**3 + 3**3
"""
# content = input("请输入一个数字：")
# if not content.isdecimal():
#     print("输入错误")
# elif len(content) > 3:
#     print("不是水仙数")
# elif int(content) == (int(content[0]) ** 3 + int(content[1]) ** 3 + int(content[2]) ** 3):
#     print("是水仙数")
# else:
#     print("不是水仙数")

"""
20.把列表中所有姓周的⼈的信息删掉(此题有坑, 请慎重):
lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
结果: lst = ['麻花藤']
"""
# lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
# tu = tuple(lst)
# for i in tu:
#     if "周" in i:
#         lst.remove(i)
# print(lst)

"""
21.车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量. (选做题)
cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
locals = {'沪':'上海', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南'}
结果: {'⿊⻰江':2, '⼭东': 2, '上海': 1}
"""
# cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
# locals = {'沪':'上海', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南'}
# result1 = {}
# result2 = []
# for i in cars:
#     if i[0] in result2:
#         result1[locals[i[0]]] += 1
#     elif i[0] in locals:
#         result1[locals[i[0]]] = 1
#         result2.append(i[0])
# print(result1)