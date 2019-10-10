# 关联关系
# 一对多
# 一个类的属性中包含了多个其他类的对象
# class Boy:
#     def __init__(self, name):
#         self.name = name
#         self.girl_list = []   #通用性
#
#     def baMei(self,girl):
#         self.girl_list.append(girl)
#
#     def happy(self):
#         for i in self.girl_list:
#             i.play()
#
# class Girl:
#     def __init__(self, name):
#         self.name = name
#
#     def play(self):
#         print(f"{self.name}和你一起玩")
#
# bao = Boy("大卫")
# friend1 = Girl("张三")
# friend2 = Girl("李四")
# friend3 = Girl("王五")
# bao.baMei(friend1)
# bao.baMei(friend2)
# bao.baMei(friend3)
# bao.happy()


# class Boy:
#     def __init__(self, name):
#         self.name = name
#         self.girl_lst = []
#
#     def py(self, *args):
#         self.girl_lst.extend(args)
#
#     def happy(self):
#         if self.girl_lst:
#             for i in self.girl_lst:
#                 i.play()
#         else:
#             print("自己玩自己")
#
#
# class Girl:
#     def __init__(self, name):
#         self.name = name
#
#     def play(self):
#         print(f"{self.name}陪你玩")
#
#
# girl1 = Girl("小丽")
# girl2 = Girl("小红")
# girl3 = Girl("小花")
# boy1 = Boy("小刚")
# boy1.py(girl1, girl2)
# boy1.py(girl3)
# boy1.happy()

"""
老师和学生模型(老师对学生是一对多,学生对老师是一对一)
创建教师类和学生类
教师类有姓名和学生列表两个属性
教师类有添加学生的方法（添加的学生是具体对象）
教师类有显示对应学生姓名和学号的方法
学生类有学号/姓名/教师姓名三个属性
创建多个学生，并添加到某位教师的学生列表中
打印该教师的学生
"""


# class Teachers:
#     def __init__(self, name):
#         self.name = name
#         self.student_lst = []
#
#     def add_student(self, *student):
#         self.student_lst.extend(student)
#
#     def students_info(self):
#         for i in self.student_lst:
#             print(f"学生姓名：{i.name} 学号：{i.number}")
#
#
# class Students:
#     def __init__(self, name, number, teacher=None):
#         self.name = name
#         self.number = number
#         self.teacher = teacher
#
#     def add_teacher(self, teacher_name):
#         self.teacher = teacher_name
#
#     def teacher_info(self):
#         print(f"{self.name}的教师名字：{self.teacher.name}")
#
#
# student1 = Students("张三", 1)
# student2 = Students("李四", 2)
# student3 = Students("王五", 3)
#
# teacher1 = Teachers("宝元")
# teacher1.add_student(student1, student2, student3)
#
# teacher1.students_info()
# student1.add_teacher(teacher1)
# student2.add_teacher(teacher1)
# student3.add_teacher(teacher1)
# student1.teacher_info()
# student2.teacher_info()
# student3.teacher_info()

"""
• 在前面英雄反派互殴的练习中加入一个武器类
• 武器类有名称和伤害加成两个属性
• 双方都可以选择拿取武器（添加一个拿武器的方法）
• 拿取武器后伤害会变高
"""


# class Hero:
#     def __init__(self, name, hp, mp, atk, weapon=[]):
#         self.name = name
#         self.hp = hp
#         self.mp = mp
#         self.atk = atk
#         self.weapon = weapon
#
#     def skill(self, tools):
#         print(f"{self.name}当前攻击力{self.atk}")
#         return tools.skill
#
#     def add_weapon(self, weapon):
#         import random
#         flag = random.randint(1, 10)
#         if flag == 1:
#             self.weapon.append(weapon)
#             self.atk += weapon.atk
#             print(f"{self.name}成功拿起武器{weapon.name} 攻击力增加{weapon.atk}")
#         else:
#             print(f"{self.name}未成功捡起武器")
#
#
# class Enemy:
#     def __init__(self, name, hp, mp, atk, weapon=[]):
#         self.name = name
#         self.hp = hp
#         self.mp = mp
#         self.atk = atk
#         self.weapon = weapon
#
#     def skill(self, tools):
#         print(f"{self.name}当前攻击力{self.atk}")
#         return tools.skill
#
#     def add_weapon(self,weapon):
#         import random
#         flag = random.randint(1,2)
#         if flag == 1:
#             self.weapon.append(weapon)
#             self.atk += weapon.atk
#             print(f"{self.name}成功拿起武器{weapon.name} 攻击力增加{weapon.atk}")
#         else:
#             print(f"{self.name}未成功捡起武器")
#
# class Weapon:
#     def __init__(self, name, atk):
#         self.name = name
#         self.atk = atk
#
#
# class Skills:
#     def skill(self, me, other):
#         other.hp -= me.atk
#         me.mp -= 10
#         print(f"{me.name} 攻击 {other.name} 造成{me.atk}点伤害-{me.name}当前HP:{me.hp} {other.name}当前HP:{other.hp}")
#
#
# mingRen = Hero("鸣人", 1000, 1000, 100)
# zuoZhu = Enemy("佐助", 800, 500, 124)
# skills = Skills()
# a = mingRen
# b = zuoZhu
# while True:
#     a, b = b, a
#     a.add_weapon(Weapon("屠龙刀", 100))
#     a.skill(skills)(a, b)
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
#     print(f"{mingRen.name}存活")
# except NameError:
#     print("鸣人已经死了")
#
# try:
#     print(f"{zuoZhu.name}存活")
# except NameError:
#     print("佐助已经死了")

# 继承：将其他类的属性和方法放在自己的类中
# class Father(object):
#     def __init__(self, name, sex, money):
#         self.name = name
#         self.sex = sex
#         self.money = money
#
#     def live(self):
#         print("花钱")
#
# class Son(Father):
#     pass
#
# xiaoming = Son("小明","男",100) #子类中找不到就去父类中找
# xiaoming.live()

# class Cat(object):  #默认继承object类
#     def run(self):
#         print("跑")
#
# mimi = Cat() #默认调用object的init方法
# mimi.run()


# class Animal:
#     def run(self):
#         print("动物跑")
#
# class Cat(Animal):
#     def run(self):
#         print("猫跑")
#
# mimi = Cat()
# mimi.run()  #自己有就调用自己的，没有就调用父类的



# class Anmial:
#     def __init__(self, color, name, age):
#         self.color = color
#         self.name = name
#         self.age = age
#
#     def jump(self):
#         print("跳")
#
# class Cat(Anmial):
#     def eat(self):
#         print("猫吃鱼")
#
#     def zhualaoshu(self):
#         print("猫抓老鼠")
#
# class Dog(Anmial):
#     def eat(self):
#         print("狗啃骨头")
#
#     def kanmen(self):
#         print("汪汪")
#
# class Pig(Anmial):
#     def eat(self):
#         print("猪吃玉米")
#
#     def sleep(self):
#         print("~zzz")

# 使用目的：减少代码的重复，提高代码重用性（慎用）

# python中，支持单继承和多继承

# class Person:
#     pass
#
# class Driver:
#     pass
#
# class Teacher(Person,Driver):
#     def teach(self):
#         print("教书育人")

# 继承关系
# 实现继承之后，子类将继承父类的属性和方法（包含父类）
# 增加了类的耦合性（不宜多，宜精）
# 减少了重复代码
# 使得代码更加规范化，合理化

# 组合vs继承
# 组合是指在新类里面创建原有类的对象，重复利用已有类的功能 “has-a”关系
# 而继承允许设计人员根据其它类的实现来定义一个类的实现 “is-a”关系

# 注意
# 不要轻易地使用继承，除非两个类之间是“ is -a”的关系
    #不要单纯地为了实现代码的重用而使用继承，因为过多地使用继承会破坏代码 的可维护性，当父类被修改的时候，会影响到所有继承自它的子类，从而增加 程序的维护难度与成本

# 总结：组装的时候用组合，扩展的是时候用继承

# python3中使⽤的都是新式类，如果一个类谁都不继承，那这个类会默认继承object类

# 单继承：
# • 子类可以继承父类的属性和方法（猫狗都是动物），修改父类，所有子类都会 受影响

# isinstance()及issubclass()
#  Python与其他语言不同，当我们定义一个 class 的时候，我们实际上就定义了 一种数据类型

#  我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两 样

#  Python 有两个判断继承的函数
    #isinstance() 用于检查实例类型:isinstance(对象,类型)
    # issubclass() 用于检查类继承：issubclass(子类,父类)

# class Driver:
#     pass
#
# class Teacher(Driver):
#     def teach(self):
#         print("教书育人")
#
# xiaoming = Teacher()
# a = isinstance(10.5,int) #判断是否是该数据类型
# print(a) #False
# b = isinstance(xiaoming,Teacher)  #判断是否是类的对象
# print(b) #True
# #
# c = issubclass(Teacher,Driver) #判断是否是类的子类
# print(c)

# 类的重构-方法重写
# （子类重写父类方法-方法的查找顺序）
# class Father(object):
#     def __init__(self, name, sex, money):
#         self.name = name
#         self.sex = sex
#         self.money = money
#
#     def live(self):
#         print("打人")
#
# class Son(Father):
#     def live(self):
#         print("打妹妹")
#
# xiaoming = Son("小明","男",100)
# xiaoming.live()

# super()关键字：修改实例属性
# class Father(object):
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#
#     def live(self):
#         print("打人")
#
# class Son(Father):
#     def __init__(self, name, age, sex):
#         #Father.__init__(self, name, age)
#         super().__init__(name, age)
#         self.sex = sex
#
#     def live(self):
#         print("打妹妹")
#
# xiaoming = Son("小明",18,"男")
# xiaoming.live()

# 多重继承：包含多个间接父类
# 多继承-少用
# class Men:
#     def __init__(self,sex):
#         self.sex = sex
#     def smoke(self):
#         print("抽烟")
#
#     def run(self):
#         print(111)
#
# class Women:
#     def __init__(self, age):
#         self.age = age
#     def taoBao(self):
#         print("买买买")
#
#     def run(self):
#         print(222)
#
# class NvHanZi(Men, Women): #优先继承前者的属性和方法
#     def __init__(self, name, sex, age):
#         self.name = name
#         Men.__init__(self,name)
#         Women.__init__(self,age)
#         # super(NvHanZi,self).__init__(sex)
#         # super(Men,self).__init__(age)
#
#
# print(NvHanZi.mro())
# xiaoli = NvHanZi(1,2,3)
# print(xiaoli.name)
# print(xiaoli.sex)
# print(xiaoli.age)

# xiaoli.run()
# xiaoli.smoke()
# xiaoli.taoBao()

# super
# 钻石继承会出现问题：爷爷类初始化两遍
# class YeYe:
#     def __init__(self):
#         print("初始化爷爷")
# class Qinba(YeYe):
#     def __init__(self):
#         print("进入亲爸类")
#         YeYe.__init__(self)
#         print("初始化亲爸")
# class GanDie(YeYe):
#     def __init__(self):
#         print("进入干爹类")
#         YeYe.__init__(self)
#         print("初始化干爹")
# class ErZi(Qinba,GanDie):
#     def __init__(self):
#         Qinba.__init__(self)
#         GanDie.__init__(self)
#         print("初始化儿子")
# bigB = ErZi()


# 使用supper mro方法：返回的是一个类的方法解析顺序表，按照表的顺序查找
# class YeYe:
#     def __init__(self):
#         print("初始化爷爷")
# class Qinba(YeYe):
#     def __init__(self): #self 接收的是儿子对象
#         super().__init__()
#         print("初始化亲爸")
# class GanDie(YeYe):
#     def __init__(self):
#         super().__init__()
#         print("初始化干爹")
#
#
# class ErZi(Qinba,GanDie):
#     def __init__(self):
#         super().__init__() #去上一层进行 查找（树中的左右左）
#         print("初始化儿子")
#
#
# bigB = ErZi()
# print(ErZi.mro()) #查找顺序


class YeYe:
    def __init__(self):
        print("初始化爷爷")
class Qinba(YeYe):
    def __init__(self, age):
        self.age = age
        print("进入亲爸类")
        # super(Qinba, self).__init__()
        print("初始化亲爸")
class GanDie(YeYe):
    def __init__(self, sex):
        self.sex  = sex
        print("进入干爹类")
        super(GanDie, self).__init__()
        print("初始化干爹")
class ErZi(Qinba,GanDie):
    def __init__(self, name,age,sex):
        self.name = name
        super(ErZi, self).__init__(age)
        super(Qinba, self).__init__(sex)
        print("初始化儿子")
bigB = ErZi("小明",2,"男")
print(ErZi.mro())
print(bigB.age)
print(bigB.sex)