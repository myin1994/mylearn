"""
s_26_day06 大作业
"""

"""
1.有如下
v1 = {'郭宝元','alex','海绵','王二麻子'}
v2 = {'alex','王二麻子'}
请得到 v1 和 v2 的交集并输出
请得到 v1 和 v2 的并集并输出
请得到 v1 和 v2 的 差集并输出
请得到 v2 和 v1 的 差集并输出
"""
# v1 = {'郭宝元','alex','海绵','王二麻子'}
# v2 = {'alex','王二麻子'}
# print(v1 & v2) #交集
# print(v1 | v2) #并集
# print(v1 - v2) #差集
# print(v2 - v1) #差集

"""
2.循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环）
"""
# lst = []
# while True:
#     content = input("请输入：")
#     if content.upper() == "N":
#         break
#     lst.append(content)
# print(lst)

"""
3.写代码实现
v1 = {'alex','武sir','黑哥'}
v2 = []
​
循环提示用户输入，如果输入的内容在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
"""
# v1 = {'alex','武sir','黑哥'}
# v2 = []
# while True:
#     content = input("请输入：")
#     if content.upper() == "N":
#         break
#     if content in v1:
#         v2.append(content)
#     else:
#         v1.add(content)
# print(v1,v2)

"""
4.通过观察判断以下值那个能做字典的key？那个能做集合的元素？
1 #可做字典key，可做集合value
-1 #k,v
"" #k,v
None #k,v
[1,2] #都不可以
(1,) #k,v
{11,22,33,4} #都不可以
{'name':'wupeiq','age':18} #都不可以
"""

"""
5.is 和 == 的区别？

is 是判断两边内容的地址是否相同
== 是判断两边的内容是否相同
"""

"""
6.type使用方式及作用？

使用type()查看数据的数据类型
"""

"""
7.id的使用方式及作用？

使用id()查看数据的内存地址
"""

"""
8.看代码写结果并解释原因

v1 = {'k1':'v1','k2':[1,2,3]}
v2 = {'k1':'v1','k2':[1,2,3]}
​
result1 = v1 == v2 #从右向左运算，v1 == v2返回True 则result1 = True
result2 = v1 is v2  #从右向左运算，v1v2内存地址不同，v1 is v2返回False 则result1 = False
print(result1) #True
print(result2) #False
验证正确
"""

"""
9.看代码写结果并解释原因

v1 = {'k1':'v1','k2':[1,2,3]}
v2 = v1
​
result1 = v1 == v2 
result2 = v1 is v2 #两变量指向相同的内存地址
print(result1) #True
print(result2) #True
验证正确
"""

"""
10.看代码写结果并解释原因

v1 = {'k1':'v1','k2':[1,2,3]}
v2 = v1
​
v1['k1'] = 'meet' #可变数据类型原地修改
print(v2) #{'k1':'meet','k2':[1,2,3]}
验证正确
"""

"""
11.看代码写结果并解释原因

v1 = '人生苦短，我用Python'
v2 = [1,2,3,4,v1]
v1 = "人生苦短，用毛线Python" #字符串是不可变数据类型，修改时新开辟空间
print(v2) #[1,2,3,4,'人生苦短，我用Python']
验证正确
"""

"""
12.看代码写结果并解释原因

info = [1,2,3]
userinfo = {'account':info, 'num':info, 'money':info}
​
info.append(9) #可变数据类型原地修改
print(userinfo) #{'account':[1,2,3,9], 'num':[1,2,3,9], 'money':[1,2,3,9]}
​
info = "题怎么这么多" #数据类型改变，新开辟空间，新的指向，原来的数据保持不变
print(userinfo) #{'account':[1,2,3,9], 'num':[1,2,3,9], 'money':[1,2,3,9]}
验证正确
"""

"""
13.看代码写结果并解释原因

info = [1,2,3]
userinfo = [info,info,info,info,info]

info[0] = '不仅多，还特么难呢' #可变数据类型，原地修改
print(info,userinfo) #[不仅多，还特么难呢',2,3] [[不仅多，还特么难呢',2,3],[不仅多，还特么难呢',2,3],[不仅多，还特么难呢',2,3],[不仅多，还特么难呢',2,3],[不仅多，还特么难呢',2,3]]
验证正确
"""

"""
14.看代码写结果并解释原因

info = [1,2,3]
userinfo = [info,info,info,info,info]

userinfo[2][0] = '闭嘴' #可变数据原地修改，共用一个内存地址则同步进行修改
print(info,userinfo) #info = [闭嘴',2,3] [[闭嘴',2,3],[闭嘴',2,3],[闭嘴',2,3],[闭嘴',2,3],[闭嘴',2,3]]
"""

"""
15.看代码写结果并解释原因

info = [1,2,3]
user_list = []
for item in range(10): #0-9 共10次
    user_list.append(info)
#user_list = [info,info,info,info,info,info,info,info,info,info]
info[1] = "是谁说Python好学的？" #所有info列表同步修改为[1,"是谁说Python好学的？",3]

print(user_list) #[[1,"是谁说Python好学的？",3],[1,"是谁说Python好学的？",3],……共10个]
验证正确
"""

"""
16.看代码写结果并解释原因

data = {}
for i in range(10):#0-9 共10次
    data['user'] = i#第一次增加，后面持续覆盖
print(data) #{'user':9}
验证正确
"""

"""
17.看代码写结果并解释原因

data_list = []
data = {}
for i in range(10):#0-9 共10次
    data['user'] = i#第一次增加，后面持续覆盖,最后为9
    data_list.append(data)#每次追加data字典，共10次，可变数据类型每次原地修改
print(data_list) #[{'user':9},{'user':9},……10次]
验证正确
"""

"""
18.看代码写结果并解释原因

data_list = []
for i in range(10):#0-9 共10次
    data = {}#每次重置为空字典，新的定义新的地址
    data['user'] = i #值1-9
    data_list.append(data)   #每次追加新的data字典，共10次
print(data_list) #[{'user':0},{'user':1},……,{'user':9}]
验证正确（第一次忽略了重新赋值地址改变）
"""

"""
19.使用循环打印出一下效果：
格式一

* 
** 
*** 
**** 
***** 
格式二

**** 
***
** 
*
格式三

* 
*** 
***** 
******* 
*********
"""
# 格式一
# for i in range(1,6):
#     print("*" * i)

# 格式二
# for i in range(4,0,-1):
#     print("*" * i)

# 格式三
# for i in range(6):
#     print("*" * (2 * i + 1))

"""
20.敲七游戏. 从1开始数数. 遇到7或者7的倍数（不包含17,27,这种数）要在桌上敲⼀下. 
编程来完成敲七. 
给出⼀个任意的数字n. 从1开始数. 数到n结束. 
把每个数字都放在列表中, 在数的过程中出现7或 者7的倍数（不包含17,27,这种数）.则向列表中添加⼀个'咣'
例如, 输⼊10. lst = [1, 2, 3, 4, 5, 6, '咣', 8, 9, 10]
"""
# lst = []
# for i in range(1,int(input("请输入数字："))+1):
#     if i % 7 == 0:
#         lst.append("咣")
#         continue
#     lst.append(i)
# print(lst)

"""
21.模拟购物车

要求:
1,用户先给自己的账户充钱：比如先充3000元。
2,有如下的一个格式:

goods = [{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},]
3,页面显示 序号 + 商品名称 + 商品价格，如：
1 电脑 1999
2 鼠标 10
…

4,用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车(自己定义购物车)，用户还可继续添加商品。

5,如果用户输入的商品序号有误，则提示输入有误，并重新输入。

6,用户输入N为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。

7,用户输入Q或者q退出程序。

8,退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少，并将购买信息显示。
"""
goods = [{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},]
shop_cart = {}
shop_cart_sum = {}
cost_sum = 0
flag = 1
while flag:
    account = input("请给账户充值:")
    if account.replace(".","",1).isdecimal() and float(account) > 0: #判断充值金额是否正确，大于0的数字（可为小数）
        account = float(account)
        print("充值成功！")
        flag = 0
    else:
        print("充值金额错误！")
while True:
    for i in goods:
        if goods.index(i) == 0:
            print("序号  商品名称 商品价格")
            print("---------------------")
        print(goods.index(i)+1,"   ",i["name"],"   ",i["price"])
    good_select = input("请输入购买商品序号（N-结算，Q-退出）：")
    if good_select.upper() == "Q": #判断是否退出
        print("退出成功！")
        break
    if good_select.upper() == "N": #判断是否结算
        settle1 = 1
        while True:
            if settle1 == 1:
                print("开始结算购物车")
            settle1 += 1
            cost = 0
            settle2 = 1
            for k,v in shop_cart.items():
                if settle2 == 1:
                    print("序号  商品名称 数量 单价")
                    print("---------------------")
                settle2 += 1
                print(v[0],"   ",k,"   ",v[1]," ",v[2])
                cost += v[1] * v[2]
                if settle2 == len(shop_cart.keys()) + 1:
                    print(f"商品总价：{cost}元")
                    print(f"账户余额：{account}元")
            if cost > account:
                goods_del = input("余额不足，请输入删除商品序号：")
                if goods_del.isdecimal():
                    if goods[int(goods_del)-1]["name"] in shop_cart:
                        if shop_cart[goods[int(goods_del) - 1]["name"]][1] > 1: #商品数量大于一则删除一个商品
                            shop_cart[goods[int(goods_del) - 1]["name"]][1] -= 1
                        else:
                            del shop_cart[goods[int(goods_del) - 1]["name"]] #商品数量等于一则删除商品键
                    else:
                        print("输入有误，请重新输入！")
                else:
                    print("输入有误，请重新输入！")
            elif cost == 0:
                print("当前购物车为空！请添加商品！")
                break
            else:
                for k,v in shop_cart.items():#可进行结算时将购物车添加进总购买记录字典，每次结算更新
                    if k not in shop_cart_sum:
                        shop_cart_sum[k] = v
                    else:
                        shop_cart_sum[k][1] += 1
                account -= cost
                cost_sum += cost
                print(f"结算成功！当前余额{account}")
                shop_cart = {} #结算成功后清空当前购物车
                break
        continue
    if good_select.isdecimal():
        if int(good_select) in list(range(1,len(goods) + 1)):
            print("当前商品 单价 \n-----------")
            print(goods[int(good_select)-1]["name"],"  ",goods[int(good_select)-1]["price"])
            if goods[int(good_select)-1]["name"] not in shop_cart.keys():#购物车中无商品添加新的键
                shop_cart[goods[int(good_select)-1]["name"]] = [int(good_select),1,goods[int(good_select)-1]["price"]]
            else:#购物车中已有商品数量+1
                shop_cart[goods[int(good_select) - 1]["name"]][1] += 1
        else:
            print("输入有误，请重新输入！")
    else:
        print("输入有误，请重新输入！")
settle3 = 1
for k, v in shop_cart_sum.items():
    if settle3 == 1:
        print("序号  商品名称 数量 单价")
        print("---------------------")
    settle3 += 1
    print(v[0], "   ", k, "   ", v[1], " ", v[2])
print(f"总消费：{cost_sum}元")
print(f"账户余额：{account}元")