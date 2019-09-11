"""
s_26 day05 作业
"""
"""
1.请将列表中的每个元素通过 "_" 链接起来。
users = ['西游记','红楼梦','三国演义']
"""
# users = ['西游记','红楼梦','三国演义']
# print("_".join(users))

"""
2.请将列表中的每个元素通过 "_" 链接起来。
users = ['秀色可餐','岳新力',666,'孙一帆']
"""
users = ['秀色可餐','岳新力',666,'孙一帆']
# print("_".join(list(map(str,users))))  #map函数

# st1 = ""  #遍历
# for i in users:
#     st1 += str(i) + "_"
# print(st1[:-1])

"""
3.请将元组 v1 = (11,22,33) 中的所有元素追加到列表 v2 = [44,55,66] 中。
"""
# v1 = (11,22,33)
# v2 = [44,55,66]
# v2 += v1
# print(v2)

"""
4.请将元组 v1 = (11,22,33,44,55,66,77,88,99) 中的所有偶数索引位置的元素 追加到列表
v3 = [44,55,66] 中。
"""
# v1 = (11,22,33,44,55,66,77,88,99)
# v3 = [44,55,66]
# for i in range(0,len(v1),2):
#     v3.append(v1[i])
# print(v3)

"""
5.将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
key_list = []
value_list = []
info = {'k1':'v1','k2':'v2','k3':'v3'}
"""
# key_list = []
# value_list = []
# info = {'k1':'v1','k2':'v2','k3':'v3'}
# for k,v in info.items():
#     key_list.append(k)
#     value_list.append(v)
# print(key_list,value_list)

"""
6.字典dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}

"""
# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# a. 请循环输出所有的key
# for k in dic.keys():
#     print(k)

# b. 请循环输出所有的value
# for v in dic.values():
#     print(v)

# c. 请循环输出所有的key和value
# for k,v in dic.items():
#     print(k,v)

# d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic.setdefault("k4","v4")
# print(dic)

# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic["k1"] = "alex"
# print(dic)

# f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic["k3"].append(44)
# print(dic)

# g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic["k3"].insert(0,18)
# print(dic)

"""
7.有如下字典,请按照一下的需求对字典进行操作
"""
# av_catalog = {
# "欧美":{
# "www.宝元.com": ["很多免费的,世界最大的","质量一般"],
# "www.alex.com": ["很多免费的,也很大","质量挺好"],
# "oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
# "hao222.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
# },
# "日韩":{
# "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
# },
# "大陆":{
# "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
# }
# }
# a.给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个 元素：'量很大'。
# av_catalog["欧美"]["www.宝元.com"].insert(1,"量很大")
# print(av_catalog)

# b.将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# av_catalog["欧美"]["hao222.com"].remove("全部收费,屌丝请绕过")
# print(av_catalog)

# c.将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# av_catalog["日韩"]["tokyo-hot"][-1] = av_catalog["日韩"]["tokyo-hot"][-1].upper()
# print(av_catalog)

# d.给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# av_catalog["大陆"].setdefault("1048",['一天就封了'])
# print(av_catalog)

# e.删除这个键值对："oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]
# av_catalog["欧美"].pop("oldboy.com")
# print(av_catalog)

# f.给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素对应的字符串，加上一句话：'可以爬下来'
# av_catalog["大陆"]["1024"][0] = av_catalog["大陆"]["1024"][0] + "可以爬下来"
# print(av_catalog)

"""
8.请循环打印k2对应的值中的每个元素。
"""
# info = {
# 'k1':'v1',
# 'k2':[('alex'),('wupeiqi'),('oldboy')],
# }
# for i in info.values(): #打印值
#     print(i)

# for i in info.values():#每个元素
#     if type(i) == str:
#         print(i)
#     else:
#         for j in i:
#             print(j)

"""
9.有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2,'k3':4}
写代码
"""
# str1 = "k: 1|k1:2|k2:3 |k3 :4"
# dic = {}
# str2 = str1.replace(" ","").split("|")
# for i in range(len(str2)):
#     str2[i] = str2[i].split(":")
# for k,v in str2:
#     if  k == "k2":
#         continue
#     dic[k] = v
# print(dic)

"""
10.有如下值 li= [11,22,33,44,55,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
result = {'k1':[],'k2':[]}
"""
# li= [11,22,33,44,55,77,88,99,90]
# result = {'k1':[],'k2':[]}
# for i in li:
#     if i > 66:
#         result["k1"].append(i)
#     else:
#         result["k2"].append(i)
# print(result)

"""
11.看代码写结果

v = {}
for index in range(10):
    v['users'] = index
print(v)
"""
# {"user":9} 验证正确

"""
12.输出商品列表，用户输入序号，显示用户选中的商品

商品列表：
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}
]
要求:
1：页面显示 序号 + 商品名称 + 商品价格，如：
1 电脑 1999
2 鼠标 10
...
2：用户输入选择的商品序号，然后打印商品名称及商品价格
3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4：用户输入Q或者q，退出程序。
"""
# goods = [
# {"name": "电脑", "price": 1999},
# {"name": "鼠标", "price": 10},
# {"name": "游艇", "price": 20},
# {"name": "美女", "price": 998}
# ]
# for i in range(len(goods)):
#     print(i + 1, goods[i]["name"], goods[i]["price"])
# while True:
#     goods_select = input("请输入序号(输入Q/q退出)：")
#     if goods_select.upper() == "Q":
#         print("退出程序")
#         break
#     elif goods_select.isdecimal():
#         if int(goods_select) <= len(goods):
#             print(goods[int(goods_select)-1]["name"],goods[int(goods_select)-1]["price"])
#         else:
#             print("输入有误，请重新输入")
#     else:
#         print("输入有误，请重新输入")