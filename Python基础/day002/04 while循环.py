# while 循环：不断的重复做某件事情
# while 关键字

#先判断关键字后的条件，满足时执行，执行完最后一个语句返回继续判断，直到条件不成立
# while True: #死循环
#     print("郭德纲")
#     print("于谦")
#     print("小岳岳")
#     print("孙悦")
#     print("五环之歌")
#     print("鸡你太美")
#     print("大面")
# print("造作")

# print("循环开始之前")
# while True: #死循环
#     print("郭德纲")
#     print("于谦")
#     print("小岳岳")
#     print("孙悦")
#     print("五环之歌")
#     print("鸡你太美")
#     print("大面")
# print("造作")

# 循环5次
# break：终止当前循环

# count = 0
# while True:  #死循环
#     print(111)
#     count += 1  #先执行 = 右边的内容
#     if count == 5:
#         print(count)
#         break #有限循环

# continue：跳出本次循环继续下次循环（continue 就是伪装成循环体中最后一行代码）
# count = 0
# while True:  #死循环
#     count += 1  #先执行 = 右边的内容
#     if count == 5:
#         print(111)
#         continue
#     print(count)

# continue 和 break 下方的代码都不会被执行

# 通过条件控制循环次数
# count = 0
# while count <2:
#     print(count)
#     count += 1

# 打印4-67
# count = 4
# while count <68:
#     print(count)
#     count += 1

# 打印100-6
# count = 100
# while count >= 6:
#     print(count)
#     count -= 1

# 1,3,5,7,9
# count = 1
# while count < 10:
#     print(count)
#     count += 2

# while else 与 if else相似,是一体的
# print(111)
# count = 0
# while count < 3:
#     print(count) #若一直死循环，则可能是计算器没有进行计算
#     count += 1
# print(222)

# print(111)
# count = 0
# while count < 3:
#     print(count) #若一直死循环，则可能是计算器没有进行计算
#     count += 1
# else: #理解为while某次次判断不满足条件时执行
#     print(222)

print(111)
count = 0
while count < 3:
    print(count)
    count += 1
    break
else:
    print(222)

# print(111)
# count = 0
# while count < 3:
#     print(count)
#     count += 1
#     continue
# else:
#     print(222)