
dic = {1:"name",2:"sex",4:"hobby"}
# 删:
# dic.clear()
# print(dic.pop(1))
# print(dic.popitem())
# del dic[1]
# del dic

# 改：
# dic[1] = "name1"
# dic.update({1:"name1",2:"sex1",4:"hobby"})

# 查：
# print(dic.setdefault(1))
# print(dic[1])
# print(dic.get(1))
# print(dic.get(4,"没有"))
# for i in dic.values():
#     print(i)
# for i in dic.keys():
#     print(i)
# print(list(dic.keys()))
# print(list(dic.values()))
# print(dic.get(1))
# print(dic.get(5,"meiy"))
# print(dic)
# for k,v in enumerate(dic):
#     print(k,v)







goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]

dic = {}

for i in range(len(goods)):
    goods[i]["index"] = i
    print(goods[i]["index"] + 1, goods[i]["name"], goods[i]["price"])
    dic[goods[i]["index"] + 1] = [goods[i]["name"], goods[i]["price"]]

# print(dic)
while True:
    seq = input("请输入商品序号(按Q退出)：")
    if seq.upper() == "Q":
        break
    elif int(seq) in dic:
        print(dic[int(seq)])
    else:
        print("输入有误，请重新输入！")