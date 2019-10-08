"""
s_26 day19作业
"""

"""
创建一个英雄类：
• 包含英雄的各项属性：例如血量魔法值等等（注意哪些应该是类属性，哪些应该作
为实例属性）
• 英雄有自残的能力，自残后会掉血
"""
# class Heros:
#     def __init__(self,blood = 100,magic = 100):
#         self.blood = blood
#         self.magic = magic
#
#     def kill_self(self):
#         self.blood -= 1
#         print(f"成功自残，当前血量{self.blood}点")
#
# mingren = Heros(1000,999)
# print(mingren.blood)
# mingren.kill_self()
# print(mingren.blood)

"""
 创建一个狗类：
• 包含名字，颜色，品种，年龄，性别等属性
• 有一个自我介绍的方法，打印自身的属性信息（我叫XXX。。。）
• 狗有看家的能力，狗有叫的能力，在看家方法中调用叫的方法
"""
# class Dogs:
#     def __init__(self,name,color,breed,age,sex):
#         self.name = name
#         self.color = color
#         self.breed = breed
#         self.age = age
#         self.sex = sex
#
#     def info(self):
#         print(f"我叫{self.name}，{self.color}色，属于{self.breed}，"
#               f"今年{self.age}岁，是{self.sex}狗")
#
#     def shout(self):
#         print("汪汪汪！")
#
#     def look_house(self):
#         print("有人来了！")
#         self.shout()
#
#
# dog1 = Dogs("张飞","红","藏獒","3","公")
# dog1.info()
# dog1.look_house()

"""
定义一个学生类。有下面的类属性：
1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:
zm = Student('zhangming',20,[69,88,100])
返回结果：
zhangming
20
100
"""
# class Student:
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def get_course(self):
#         return max(self.score)
#
# zm = Student('zhangming',20,[69,88,100])
# print(zm.get_name())
# print(zm.get_age())
# print(zm.get_course())

"""
定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
"""
# class DictClass:
#     def __init__(self,dic):
#         self.dic = dic
#
#     def del_dict(self,key):
#         del self.dic[key]
#
#     def  get_dict(self,key):
#         if key in self.dic:
#             return key
#         else:
#             return "not found"
#
#     def get_key(self):
#         return [i for i in self.dic]
#
# dic = DictClass({1:"1",2:"2",3:"3"})
# print(dic.dic)
# dic.del_dict(2)
# print(dic.dic)
# print(dic.get_dict(1))
# print(dic.get_dict(2))
# print(dic.get_key())

"""
定义一个列表的操作类：Listinfo
包括的方法:
1 列表元素添加: add_key(keyname) [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	[list:列表类型]
4 删除并且返回最后一个元素：del_key()
list_info = Listinfo([44,222,111,333,454,'sss','333'])
"""
# class Listinfo:
#     def __init__(self,lst):
#         self.lst = lst
#
#     def add_key(self,keyname):
#         if type(keyname) == str or type(keyname) == int:
#             self.lst.append(keyname)
#         else:
#             print("wrong type")
#
#     def get_key(self,num):
#         if type(num) == int and len(self.lst) > num:
#             return self.lst[num]
#         else:
#             return "wrong num"
#
#     def update_list(self,lst2):
#         if type(lst2) == list:
#             self.lst += lst2
#             return self.lst
#         else:
#             return "wrong tpye"
#
#     def del_key(self):
#         value_last = self.lst[-1]
#         del self.lst[-1]
#         return value_last
#
# lst = Listinfo([1,2,3,4,5,6,7,8])
# lst.add_key(99)
# print(lst.lst)
#
# print(lst.get_key(8))
# print(lst.update_list([11,22,33,44]))
# print(lst.del_key())
# print(lst.lst)