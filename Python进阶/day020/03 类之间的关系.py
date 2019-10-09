# 1.依赖关系（关联）-使用别的类的方法实现自己的功能
    #将一个类的对象或者类名传到另一个类的方法使用（在某个方法中调用其他类的方法）
    #此时关系是最轻的，随时可以更换其他对象
# class Person:
#     def play(self,tools):
#         print("准备打游戏")
#         tools.run()
#
# class Computer:
#     def run(self):
#         print("电脑游戏：LOL")
#
# class Phone:
#     def run(self):
#         print("手机游戏:王者荣耀")
#
# xiaoMing = Person()
#
# iPhone = Phone()
#
# lxComputer = Computer()
#
# xiaoMing.play(iPhone)
# xiaoMing.play(lxComputer)

"""
定义一个英雄类和一个反派类
• 两个类都包含名字、血量，攻击力（ATK），和一个技能（skill）
• 两派对象互殴
• 血量为0死亡，删除对象（del 对象名）
"""
# class Heros:
#     def __init__(self,name,hp,mp,ATK):
#         self.name = name
#         self.hp = hp
#         self.mp = mp
#         self.ATK = ATK
#
#     def skill(self,tools):
#         tools.hp -= self.ATK
#         self.mp -= 10
#         print(f"{self.name} 攻击 {tools.name} 造成{self.ATK}点伤害-{self.name}当前HP:{self.hp} {tools.name}当前HP:{tools.hp}")
#
# class Enemys:
#     def __init__(self, name, hp, mp, ATK):
#         self.name = name
#         self.hp = hp
#         self.mp = mp
#         self.ATK = ATK
#
#     def skill(self, tools):
#         tools.hp -= self.ATK
#         self.mp -= 10
#         print(f"{self.name} 攻击 {tools.name} 造成{self.ATK}点伤害-{self.name}当前HP:{self.hp} {tools.name}当前HP:{tools.hp}")
#
# mingRen = Heros("鸣人",1000,1000,100)
# zuoZhu = Enemys("佐助",800,500,124)
# a = mingRen
# b = zuoZhu
# while True:
#     a, b = b, a
#     a.skill(b)
#     if mingRen.hp <= 0:
#         print(f"{mingRen.name}死了")
#         del mingRen
#         break
#     elif zuoZhu.hp <= 0:
#         print(f"{zuoZhu.name}死了")
#         del zuoZhu
#         break
#
# try:
#     print(mingRen.name)
# except NameError:
#     print("鸣人已经死了")
#
# try:
#     print(zuoZhu.name)
# except NameError:
#     print("佐助已经死了")


# class heros:
#     def __init__(self,name,hp,mp,ATK):
#         self.name = name
#         self.hp = hp
#         self.mp = mp
#         self.ATK = ATK
#
#     def skill(self,tools):
#         return tools.skill
#
# class enemys:
#     def __init__(self, name, hp, mp, ATK):
#         self.name = name
#         self.hp = hp
#         self.mp = mp
#         self.ATK = ATK
#     def skill(self,tools):
#         return tools.skill
#
# class Skills:
#     def skill(self, me,other):
#         other.hp -= me.ATK
#         me.mp -= 10
#         print(f"{me.name} 攻击 {other.name} 造成{me.ATK}点伤害-{me.name}当前HP:{me.hp} {other.name}当前HP:{other.hp}")
#
#
# mingRen = heros("鸣人",1000,1000,100)
# zuoZhu = enemys("佐助",800,500,124)
# skills = Skills()
# a = mingRen
# b = zuoZhu
# while True:
#     a, b = b, a
#     a.skill(skills)(a,b)
#     if mingRen.hp <= 0:
#         print(f"{mingRen.name}死了")
#         del mingRen
#         break
#     elif zuoZhu.hp <= 0:
#         print(f"{zuoZhu.name}死了")
#         del zuoZhu
#         break
#
# try:
#     print(mingRen.name)
# except NameError:
#     print("鸣人已经死了")
#
# try:
#     print(zuoZhu.name)
# except NameError:
#     print("佐助已经死了")

# 老师版
# class Hero:
#     def __init__(self, name, hp, atk):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#
#     def skill(self, bos):
#         print(f"{self.name} 对{bos.name}使出了千年杀")
#         bos.hp -= self.atk
#
#
# class Boss:
#     def __init__(self, name, hp, atk):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#
#     def skill(self, bos):
#         print(f"{self.name} 对{bos.name}使出了吐口水")
#         bos.hp -= self.atk
#
#
# bigB = Hero("宝元",100,30)
# alex = Boss("alex",60,50)
#
# while True:
#     if bigB.hp > 0 and alex.hp > 0:
#         bigB.skill(alex)
#         alex.skill(bigB)
#     else:
#         print("战斗结束")
#         break


# class Person:
#     def __init__(self):
#         self.name = "xiaoli"
#         self.age = 20

# xiaoming = Person()
# print(xiaoming.name)
# del xiaoming #删除对象
# print(xiaoming)
# del xiaoming.name #删除属性
# del xiaoming.age #删除属性
# print(xiaoming)

# 删除属性
# delattr(对象名,"属性名")

# delattr只针对实例对象，
# del del可通过类名删除类属性

# class Boy:
#     a = 1
#     def __init__(self):
#         self.name = "张三"
#
#     def func(self):
#         print(22)
#
# boy1 = Boy()
# # print(boy1.name)
# # delattr(boy1,"name")
# # print(boy1.name)
#
#
# print(boy1.name)
# del Boy.self.name
# print(boy1.name)


# print(boy1.name)
# del boy1.name
# print(boy1.name)

# del Boy
# print(boy1.name)
# print(boy1.a)
# boy2 = Boy()
# print(boy2.name)
# 2.组合关系（聚合）-使用多个类
# 在对象里面包含对象
    #将一个类的对象封装到另一个类的对象的属性中
    #一对一关系
    #一对多关系

# class Person:
#     def __init__(self,friend):
#         self.friend = friend
#
# class Women:
#     def __init__(self):
#         self.name = "xiaoli"
#
# xiaoli = Women()
# xiaoming = Person(xiaoli)
# print(xiaoming.friend.name)

# 一对一
# class BigB:
#     def __init__(self,name,friend = None):
#         self.name = name
#         self.friend = friend
#
#     def eat(self):
#         if self.friend:
#             print(f"{self.name}带着{self.friend.name}去吃饭")
#         else:
#             print("吃狗粮")
#
# class Girl:
#     def __init__(self,name):
#         self.name = name
#
# xiaoli = Girl("唐艺昕")
# baoyuan = BigB("宝元",xiaoli)
# baoyuan2 = BigB("宝元")
# baoyuan.eat()
# baoyuan2.eat()


# 一对多
class Boy:
    def __init__(self):
        self.girl_list = []

    def baMei(self,girl):
        self.girl_list.append(girl)

    def happy(self):
        for i in self.girl_list:
            i.play()

class Girl:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name}和你一起玩")

bao = Boy()
friend1 = Girl("张三")
friend2 = Girl("李四")
friend3 = Girl("王五")
bao.baMei(friend1)
bao.baMei(friend2)
bao.baMei(friend3)
bao.happy()

# 3.继承关系（实现）-cv一下

# 类之间的关系要做到 高内聚（封装），低耦合（有必要的时候才建立联系）

