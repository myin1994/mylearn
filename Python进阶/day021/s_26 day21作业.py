"""
s_26 day21作业
"""

"""
1 定义宠物类（ Pet ），猫类（Cat）和狗类（Dog）
宠物都有属性姓名（name）和年龄(age)
宠物都有吃（eat）、喝（drink）、叫（shout）的方法
猫除了具有宠物类的方法，还有爬树（ climbTree ）的方法
狗除了具有宠物类的方法，还有警戒（ police）的方法
"""
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(f"{self.name}吃")
#
#     def drink(self):
#         print(f"{self.name}喝")
#
#     def shout(self):
#         print(f"{self.name}叫")
#
# class Cat(Pet):
#     def climbTree(self):
#         print("爬树")
#
# class Dog(Pet):
#     def police(self):
#         print("狂叫")
#
# xiaoHua = Cat("小花",2)
# gouDan = Dog("狗蛋",3)
# xiaoHua.eat()
# gouDan.shout()
# xiaoHua.climbTree()

"""
2 建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等属性，至少要求 汽车能够加速 减速 停车。
再定义一个小汽车类CarAuto 继承Auto 并添加空调、CD属性，并且重新实现方法覆盖加速、减速的方法
"""
# class Auto:
#     def __init__(self, tyre_num, color, weight, speed=0):
#         self.tyre_num = tyre_num
#         self.color = color
#         self.weight = weight
#         self.speed = speed
#
#     def speed_up(self):
#         self.speed += 60
#         print("汽车加速")
#
#     def speed_down(self):
#         self.speed -= 5
#         print("汽车减速")
#
#     def stop(self):
#         print("停车")
#         self.speed -= self.speed
#
# class CarAuto(Auto):
#     def __init__(self, air, cd, tyre_num, color, weight, speed=0):
#         self.air = air
#         self.cd = cd
#         super().__init__(tyre_num, color, weight, speed)
#
#     def speed_up(self):
#         self.speed += 60
#         print("小汽车加速")
#
#     def speed_down(self):
#         self.speed -= 5
#         print("小汽车减速")
#
# little_car = CarAuto("空调","cd",4,"red","6000kg")
# little_car.speed_up()
# print(little_car.speed)
# little_car.speed_down()
# print(little_car.speed)
# little_car.stop()
# print(little_car.speed)


"""
3 银行卡类（BankCard）有余额（balance）属性和存款（deposit）取款（draw）的方法，只要取款金额小于余额即可完成取款操作
信用卡类（CreditCard）继承自银行卡类，信用卡多了透支额度（overdraft）属性，如果卡中余额和透支额度的和大于取款金额即可完成取款。
如果透支，显示透支金额
"""
# class BankCard:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def deposit(self,num):
#         self.balance += num
#
#     def draw(self,num):
#         if self.balance >= num:
#             self.balance -= num
#             print(f"成功取款{num}元，当前余额{self.balance}")
#         else:
#             print(f"当前余额不足{num}元，取款失败！")
#
# class CreditCard(BankCard):
#     def __init__(self, balance, overdraft):
#         self.overdraft = overdraft
#         super().__init__(balance)
#
#     def draw(self,num):
#         if self.balance + self.overdraft >= num:
#             if self.balance >= num:
#                 self.balance -= num
#                 print(f"成功取款{num}元，当前余额{self.balance}")
#             else:
#                 touZhi = num-self.balance
#                 self.overdraft -= touZhi
#                 self.balance = 0
#                 print(f"成功取款{num}元，当前余额{self.balance}元,透支{touZhi}元，透支额度剩余{self.overdraft}元")
#         else:
#             print(f"当前余额不足{num}元，取款失败！")
#
# my_card = CreditCard(1000,5000)
# my_card.draw(1999)


"""
4 编写程序, A 继承了 B, 两个类都实现了 handle 方法, 在 A 中的 handle 方法中调用 B 的 handle 方法
"""


# class B:
#     def handle(self):
#         print("B的handle")
#
#
# class A(B):
#     def handle(self):
#         super().handle()
#
#
# a = A()
# a.handle()