# 解构
# dic = {"key":1,"key1":2}
# print(dic.items())
# print(list(dic.items()))
# 字典是无序的，显示时按照定义的顺序显示（python3.6版本以上）

# dic = {"key1":1,"key2":2,"key3":3}
# for i in dic.items():
#     print(i[0],i[1])

# a,b = 10,20
# print(a)
# print(b)

# a,b,c = "你好啊"
# print(a)
# print(b)

# a,b,c = [1,2,3]
# print(a)
# print(b)

# a,b,c = {"key1":1,"key2":2,"key3":3}
# print(a)
# print(b)

# a,b,a = 10,20,30
# print(a)
# print(b)

# a,b,*c = [1,2,3,4,5,6]  # *聚合，将多余的数据打包为列表（无论多少）
# print(a,b,c)


# dic = {"key1":1,"key2":2,"key3":3}

# for i in dic.items():
#     k,v = i
#     print(k,v)

# for k,v in dic.items():
#     print(k,v)

# for i in [1,2,3,4]:
#a,b,c,d = [1,2,3,4]

# keys 获取所有的键
# values 获取所有的值
# items 获取所有的键和值

# 字典的嵌套：
# house = {
#     101:{1:{"pp":{"mou":["xiao","cdd"],"zzz":["xingda","er"]},
#          2:{"ll":["moya"]}}},
#     102:{},
#     103:{},
#     104:{},
#     105:{},
#     106:{},
# }
# print(house)

# 字典和列表的区别：
    # 字典查找内容时方便
    # 字典查找速度快
# 键：可哈希
# dic = {"key1":"cccc"}
# print(hash("666"))

#如果你对这个变量不关心，或者以后也不会用到那么就用_
#比如说我要取出列表的头尾，对其他我并不关心是什么
# a=[23,3,4,2,5,5,31,6,4,77,8]
# h,*_,t=a
# print(h)
# print(_)
# print(t)
# #输出
#
#
# #比如在用for循环，我不会用到比如说i这个用来迭代下标的变量，那么我也可以使用_
# for _ in range(10):
#     print ("欢迎你10次")
# print(_)
