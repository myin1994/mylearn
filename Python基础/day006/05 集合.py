# 集合：python数据类型
# 集合：去重，集合关系
# 关键字：set
# 定义：
# 空集合：set()
# s = {1,2,3,4}
# print(type(s))
#
# lst = [1,2,1]
# print(list(set(lst)))

# 集合：就是一个没有值的字典
# 括号：{}
# 键不可变--集合的元素是不可变的（可哈希的）
# 具有唯一特性才能做到去重
# 无序，可变，可迭代

# dic = {1:2,2:2,3:2,[1,2,3]:2}
# s = {1,2,3,[1,2,3]}

# s = {1,2,3,"4",5,6,7,8,9}
# print(s)

# 容器：能够存储数据的就是容器
# list,tuple,dict,set

# 可变：
# 增
# s = set()
# s.update("alex") #迭代添加
# s.add("alex") #添加
# print(s)

# 删
# s = {"0","1","2","3"}
# s.pop() #随机删除 pop具有返回值
# s.remove("0")  #指定元素删除
# s.clear() #清空 后的显示set()
# print(s)

# 改
# 1.先删后加
# 2.转换数据类型进行修改

# 查
#     for循环
#     直接打印

# 集合关系
# python = {"海绵","一帆","心累","大圣"}
# linux = {"海绵","大圣","哈哈哈","嘿嘿嘿"}
# print(python | linux)  #并集  or
# print(python & linux)  #交集  and
# print(python ^ linux)  #补集
# print(python - linux)  #差集
# print(linux - python )  #差集

python = {"海绵","一帆","心累","大圣"}
linux = {"海绵","大圣"}
# # 超集(父集)
print(python > linux) #判断python是不是linux的超集
# # 子集
print(python < linux) #判断python是不是linux的子集