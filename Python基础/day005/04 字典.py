# 字典 --Python中的数据类型之一
# 唯一一种 键 值 对的数据
# dict

# 作用
# 存储大量的数据  比列表存储的数据还要大
# 将数据和数据之间进行关联
# name_list = ["新力","孙","海绵","秀"]
# id_list = [18,9,25,50]

# 定义：可变数据类型
# dic = {"键":"值"}
# dic = {"新力":["开车","唱"],"孙":9,25:"海绵",True:"秀",(1,2,3):"大圣"}
# 通过键可以准确的找到值
# print(dic)
# 哈希：
# 可变数据类型不可哈希
# 不可变数据类型可哈希

# 字典的键：
#   不可变数据类型（可哈希）
#   唯一（重名则覆盖）
# 字典的值：任意

# 字典的增
# dic = {"key":1}
# dic["键"] = "值"
# dic["sss"] = 89
# dic[666] = "sss"
# print(dic)

# dic.setdefault("meet",18) #参数1：key 参数2：value  直接对字典增加，有返回值
# dic.setdefault("key",18) #字典中不存在时添加，存在时不进行添加（无加有不加，理解为设定默认值）
# print(dic)

# setdefault ：先查找，再添加
    # 先通过键去字典中查找，返回值是None，才会执行第二步
    # 将键和值添加到字典中

# dic = {"key":1}
# print(dic.setdefault("key",2)) #键存在时返回键对应的值(忽略设置的新值)
# print(dic.setdefault("meet")) #键不存在且值不存在时返回None，且将键值对添加到字典
# print(dic.setdefault("meet",12)) #键不存在时有值返回对应值
# print(dic) #键不存在时返回None

# 字典的删除
# dic = {"key":1,"dd":"sss"}
# dic.clear()  #清空 -- 空字典
# print(dic)

# print(dic.pop("key") ) #发黄需要参数,有返回值，返回的是被删除的键对应的值
# print(dic)

# print(dic.popitem())  #随机删除 python3默认删除最后一个,返回的是键值对-元组
# print(dic)

# 字典中没有remove
# del dic #删除整个字典
# del dic["键"]
# del dic["dd"]
# print(dic)

# 字典所有的操作都是针对键

# 字典的修改：
# dic = {"key":1,"dd":"sss"}
# dic["键"] = "值" #暴力增加 当键在字典中存在就修改，不存在就增加
# dic["dd"] = "666" #修改
# dic["ss"] = "666" #增加
# print(dic)

# dic.update(字典)  #update中的字典级别高于点前面的字典
# dic.update({"key":2,"meet":"sss"}) #相当于字典合并
# print(dic)

# 字典的查询：

# dic = {"key":1,"dd":"sss"}
# setdefault 通过返回值查询
# print(dic.setdefault("key"))
# print(dic.setdefault("key1"))

# print(dic["dd"]) #通过键查找值，暴力，键存在时返回对应的值
# print(dic["cdd"]) #通过键查找值，键不存在时报错

# print(dic.get("dd")) #通过键查找值,键存在时返回对应的值
# print(dic.get("cdd")) #通过键查找值,键不存在时返回None
# print(dic.get("cdd","找不到")) #通过键查找值,键不存在时可返回自定义内容

# 获取字典的键
# print(dic.keys())  #高仿列表，可迭代,不支持索引
# print(list(dic.keys())[0]) #转为列表后可索引

# 获取字典的值
# print(dic.values())
dic = {"key":1,"dd":"sss"}
print(dic.items())
for i in dic.items():
    print(i)