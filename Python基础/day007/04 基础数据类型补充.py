# int
# a = 10 #1010
# a = 15 #1111
# a = 25 #11001
# print(a.bit_length())    #求最大位数
# print(0b11111111)

# str
# s = "alsx hahah"
# s1 = s.capitalize()  #首字母大写
# print(s1)

# s1 = s.title()  #每个单词首字母大写（可用空格，逗号等分割字符串）
# print(s1)

# s1 = s.index("h")  #通过元素查找索引，查找不到时会报错
# print(s1)
# s1 = s.find("x")  #通过元素查找索引，查找不到时返回-1

# s1 = "".join(列表，元组) #将列表转换成字符串
# s.split()  #列表转换字符串

# s1 = s.center(20)  #居中，一共20个
# print(s1)
# s1 = s.center(20,"-")  #居中，填充，一共20个,可用符号代替空格
# print(s1)

# s = "alsx{}ha{}hah"
# s1 = s.format("11","222")  #按照位置格式化

# s = "alsx{1}ha{0}hah"
# s1 = s.format("11","222")  #按照索引格式化

# s = "alsx{a}ha{b}hah"
# s1 = s.format(b = "11",a = "222")  #按照关键字格式化
# print(s1)

# s = "alsx haHah"
# s1 = s.swapcase()   #大小写转换
# print(s1)

# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)
# print(trantab)
# str1 = "this is string example....wow!!!"
# print(str1.translate(trantab))


# list---列表
# lst = [1,2,3,5,6,4]
# # 反向列表
# print(lst[::-1])  #新开辟一个列表
# lst.reverse()  #原地修改
# print(lst)

# lst.sort()  #排序 默认升序
# lst.sort(reverse=True)  #排序 降序
# print(lst)

# lst1 = [1,2,3,[4]]
# print(lst1,id(lst1))
# lst2 = [4,5,6]
# lst1 = lst1 + lst2
# print(lst1,id(lst1))
# print(lst1 + lst2)  #新开辟空间

# lst1 = [1,2,3,[4]]
# lst3 = lst1 * 3
# print(id(lst3[3]),id(lst3[7]))
# #列表和元组进行乘法时元素都是共用的

# lst = [1,2,[]]
# lst1 = lst * 2
# lst[-1].append(8)
# print(lst1)
# print(lst)

# lst = []
# lst1 = list()  #等同于上面
# print(lst,lst1)
# print(str())
# print(bool())
# print(dict())
# print(set())

# 元组
# tu = (10)  #int
# tu = (10,) #tuple
# tu = () #tuple

# 字典
# dic = {}
# dic = {}.fromkeys("abc",12)  #快速创建键值对 参数一：键（可迭代） 参数2：值（共用）
# dic = dict.fromkeys("abc",12)
# print(dic)

# dic = dict.fromkeys("abc",[])
# dic["c"].append(1) #全部变化
# dic["c"] = [67] #用新列表替换
# print(dic)

# 字典的定义
# dic = {}
# dic  = dict()
# dic = dict(k1 = 1,k2 = 2,k3 = 3)
# dic = dict(([1,2],[4,5],[6,7]))
# print(dic)

# 类型转换
# False  只要为空就是False
# print(bool(0))
# print(bool())
# print(bool(None))
# print(bool(""))
# print(bool([]))
# print(bool(()))
# print(bool({}))
# print(bool(set()))

# 列表元组可互转
# tuple(list)
# list(tuple)
# set(list)
# set(tuple)
# list(set)  试一试
# tuple(set)  试一试

s1 = {1:2,3:4}
print(set(s1))


# int(str) #阿拉伯数字
#
# str(int)
# str(dict)
# str(list)
# str(tuple)
# str(set)
# str(bool)


# 基础数据类型总结
# int：有序（不支持索引），不可变，不可迭代，直接查看
# bool：不可变，不可迭代，直接查看
# str：有序，不可变，可迭代，索引
# list：有序，可变，可迭代，索引
# tuple：有序，不可变，可迭代，索引
# dict：无序，可变，可迭代，键
# set：无序，可变，可迭代，直接查看

