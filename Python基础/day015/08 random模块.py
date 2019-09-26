# random随机数
import random
# print(random.random())  #0~1之间的小数
# print(int(random.random() * 10))

# print(random.randint(1,5))  #随机范围整数，包含边界

# print(random.randrange(0,10,2)) #随机偶数
# print(random.randrange(1,11,2)) #随机奇数

# print(random.choice([1,2,"ww",22,33]))  #从可迭代对象随机一个元素
# print(random.choice("12345"))  #从可迭代对象随机一个元素



# print(random.choices([1,2,"ww",22,33],k=2)) #随机多个，会出现重复元素
# print(random.sample([1,2,3,4,5,6,7],k=2))  #随机多个不重复，不会出现重复元素

# lst = [1,2,3,4,5,6,7,8,3]
# lst.sort()
# print(lst)
# random.shuffle(lst) #打乱顺序
# print(lst)


# 使用随机数实现一个5位数的验证码（字母，数字）

# 1.ASCII码表
# 65-90是大写字母，通过chr()获取对应的内容
# 97-122是小写字母，通过chr()获取对应的内容
# 2.使用for循环执行5圈，将获取的内容累加起来，最后输出
# a = chr(random.randint(65,90))
# b = chr(random.randint(97,122))
# c = random.randint(0,9)
# # d = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122)),random.randint(0,9)])
# import random
# s = ""
# for i in range(5):
#     s += str(random.choice([chr(random.randint(65,90)),chr(random.randint(97,122)),random.randint(0,9)]))
# print(s)



# lst = list()
# lst.extend(list(range(65, 91)))
# lst.extend(list(range(48, 58)))
# lst.extend(list(range(97, 123)))
# s = ""
# for i in range(5):
#     s = s + str(chr(random.choice(lst)))
# print(s)

# import random
# print("".join(random.choices([chr(i) for i in range(122) if chr(i).isalnum()],k=5)))