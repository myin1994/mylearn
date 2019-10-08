# 类和对象

# 类（包含属性和方法）-封装
    #对象的抽象，一类事物的总称

# 对象（可通过类实现）
    #类的具象，一个具体的事物

# 先有类，通过类可以创建对象

# 创建一个类
# 类命名规则：首字母大写
# 类中包含属性和方法
# class GirlFriend(object):
# class GirlFriend:
#     sex = "女"
#     age = 18
#     height = 180
#     weigh = 180
#     money = 100000000
#     l1 = [1,2,3,4,5,6]
#
#     def __init__(self):
#         self.eye_color = "red"
#
#     def chui_tui(self,num):  #在类里叫方法，self接收的是调用者
#         print(f"捶腿{num}次")
#
#     def get_money(self):
#         print("给100元")

# xiaoli = GirlFriend()
#
# print(xiaoli.sex)
# xiaoli.chui_tui(20)
# 引用计数为0时会被垃圾回收机制回收

# xiaoli1 = GirlFriend()
# print(xiaoli1.sex)
# xiaoli1.chui_tui(20)

# print(GirlFriend.__dict__) #查看类中内容

# 添加新属性(添加到当前)
# xiaoli1.face_value = -5
# print(xiaoli1.face_value)

# 添加新方法
# import types
# def eat(self):
#     print("chi")


# class GirlFriend:
#     num_eyes = 2  #类属性
#
#     def __init__(self,color,height):  #实例属性
#         self.eye_color = color
#         self.height = height  #一般重名使用
#
#     def chui_tui(self, num):  # 在类里叫方法，self接收的是调用者
#         print(f"捶腿{num}次")
#         self.abc = 50
#
#     def get_money(self):
#         print("给100元")
#
# xiaoli = GirlFriend("白色",180)
# print(xiaoli.eye_color)
# print(xiaoli.height)
#
# xiaoli.weight = 120
# print(xiaoli.weight)
#
# xiaoli.num_eyes = 3  #添加的是实例属性
# print(xiaoli.num_eyes)
# 访问属性的优先级：实例属性-类属性

# print(GirlFriend.num_eyes)  #通过类名来访问类属性
# 类属性，实例（对象）属性

# 类属性来存放当前类所有对象所共有的特征，一般通过类名访问和修改（所有类的对象都会改变），用对象名也能访问，但不能修改

# 实例属性：存放每个对象各自的特征，只能通过对象去访问，类名无法访问,可在对象内及其它对象内进行修改

# 实例变量和类变量同名时会有限访问实例对象（通过对象调用时）
# list()

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

class Dogs:
    def __init__(self,name,color,breed,age,sex):
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age
        self.sex = sex

    def info(self):
        print(f"我叫{self.name}，{self.color}色，属于{self.breed}，"
              f"今年{self.age}岁，是{self.sex}狗")

    def shout(self):
        print("汪汪汪！")

    def look_house(self):
        print("有人来了！")
        self.shout()


dog1 = Dogs("张飞","红","藏獒","3","公")

dog1.info()
dog1.look_house()