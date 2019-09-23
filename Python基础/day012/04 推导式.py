# 1.推导式：做一些有规律的数据结构


# 列表推导式（可变）
# lst = [i for i in range(1,51)]
# print(lst)

# 功能：
#     普通循环
# [变量 for循环]
# print([i for i in range(1,51)])
# print([f"python{i}" for i in range(1,51)])
# print([i for i in range(1,51,2)])
#     筛选模式
# [加工后的变量 for循环  加工条件]
# print([i for i in range(1,51) if i > 25])

# lst = []
# for i in range(2):
#     for j in range(2):
#         lst.append(i+j)
# print(lst)
#
# print([i+j for i in range(2) for j in range(2)])  #推导式最多建议使用三层

# 字典
#普通循环
# {变量:变量 for循环}
# print({i:i+1 for i in range(3)})
# print({f"python{i}":i+1 for i in range(3)})

# 筛选模式
# {加工后的变量:加工后的变量 for循环 加工条件}
# print({i:i+1 for i in range(3) if i > 1})

# 集合推导式（参考列表推导式）

# 生成器表达式(推导式)

# 普通模式
# g = (i for i in range(3))
# i相当于yield返回值
# print(next(g))
# print(next(g))
# print(next(g))
# 筛选模式
# g = (i for i in range(3) if i+1 ==2)
# print(next(g))

# 推导式的使用
# 简化代码，提高可读性
# 生成一些有规律的数据
# 生成的数据较大时使用生成器推导式

# s = "alex,meet"
# print([i for i in range(len(s)) if s[i] == "e"])
# lst = []
# for i in range(len(s)):
#     if s[i] == "e":
#         lst.append(i)
# print(lst)

# 推导式理解
# 【对象1 for 对象2 in 对象3】
# 外壳决定推导结果：[]--列表 {}--字典或集合  ()--生成器
# 【】内部：对象1--推导结果  对象2--for循环固定结构（可用于外部使用的变量）
#          对象3--推导目标，决定步长及数据来源





def add(a, b):
    return a + b

def test():
    for r_i in range(4):#0 1 2 3
        yield r_i

g = test()

for n in [2, 10]:
    g = (add(n, i) for i in g) #[2,3,4,5]  [10,11,12,13]

print(list(g)) #[20,21,22,23]

