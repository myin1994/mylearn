"""
s_26 day20 作业
"""

"""
1.有一个男人类和一个女人类
创建男女朋友之间互相关联的关系
例如男人类的对象调用看电影的方法时，需要用到女人类的对象，女人类的对象调用逛街的方法时也需要用到男人类的对象（相互关联）
"""

# class Men:
#     def __init__(self, name, girl_fridend = None):
#         self.name = name
#         self.girl_friend = girl_fridend
#
#     def watch_films(self):
#         if self.girl_friend:
#             print(f"和{self.girl_friend.name}一起看电影")
#         else:
#             print(f"{self.name}一个人看电影")
#
# class Women:
#     def __init__(self, name, boy_fridend=None):
#         self.name = name
#         self.boy_friend = boy_fridend
#
#     def shopping(self):
#         if self.boy_friend:
#             print(f"和{self.boy_friend.name}一起逛街")
#         else:
#             print(f"{self.name}一个人逛街")


# xiaoMing = Men("小明")
# xiaoHong = Women("小红",xiaoMing)
# xiaoHong.shopping()
# xiaoMing.watch_films()
# xiaoMing.girl_friend = xiaoHong
# xiaoMing.watch_films()


"""
2.创建一个学生类和一个背包类，将背包类的对象组合到学生类中
"""
# class Students:
#     def __init__(self, name):
#         self.goods_lst = []
#         self.name = name
#
#     def take_in(self,goods):
#         self.goods_lst.append(goods)
#         print(f"{self.name}将{goods.goods}放入书包")
#
#     def take_out(self):
#         for i in self.goods_lst:
#             print(f"{self.name}拿出了{i.goods}")
#
#
# class Bags:
#     def __init__(self, goods):
#         self.goods = goods
#
# xiaoMing = Students("小明")
# goods1 = Bags("语文书")
# goods2 = Bags("数学书")
# goods3 = Bags("英语书")
# goods4 = Bags("游戏机")
#
# xiaoMing.take_in(goods1)
# xiaoMing.take_in(goods2)
# xiaoMing.take_in(goods3)
# xiaoMing.take_in(goods4)
# xiaoMing.take_out()


"""
3.创建客船类/货船类和油船类，三个类都需要组合发动机类/船体类/甲板类/船舱类对象engine hull deck cabin
"""
# class PassengerShip:
#     def __init__(self, name, engine, hull, deck, cabin):
#         self.name = name
#         self.engine = engine
#         self.hull = hull
#         self.deck = deck
#         self.cabin = cabin
#
#     def info(self):
#         print(f"船名：{self.name} 发动机：{self.engine.engine_name} 船体：{self.hull.hull_name} "
#               f"甲板：{self.deck.deck_name} 船舱：{self.cabin.cabin_name}")
#
# class CargoShip:
#     def __init__(self, name, engine, hull, deck, cabin):
#         self.name = name
#         self.engine = engine
#         self.hull = hull
#         self.deck = deck
#         self.cabin = cabin
#
#     def info(self):
#         print(f"船名：{self.name} 发动机：{self.engine.engine_name} 船体：{self.hull.hull_name} "
#               f"甲板：{self.deck.deck_name} 船舱：{self.cabin.cabin_name}")
#
# class TankShip:
#     def __init__(self, name, engine, hull, deck, cabin):
#         self.name = name
#         self.engine = engine
#         self.hull = hull
#         self.deck = deck
#         self.cabin = cabin
#
#     def info(self):
#         print(f"船名：{self.name} 发动机：{self.engine.engine_name} 船体：{self.hull.hull_name} "
#               f"甲板：{self.deck.deck_name} 船舱：{self.cabin.cabin_name}")
#
# class Engine:
#     def __init__(self,engine_name):
#         self.engine_name = engine_name
#
# class Hull:
#     def __init__(self,hull_name):
#         self.hull_name = hull_name
#
# class Deck:
#     def __init__(self,deck_name):
#         self.deck_name = deck_name
#
# class Cabin:
#     def __init__(self,cabin_name):
#         self.cabin_name = cabin_name
#
# engine1 = Engine("超级发动机")
# hull1 = Hull("钢铁船体")
# deck1 = Deck("钛合金甲板")
# carbin1 = Cabin("无限空间船舱")
#
# ship1 = PassengerShip("长江一号客船",engine1,hull1,deck1,carbin1)
# ship2 = CargoShip("长江一号货船",engine1,hull1,deck1,carbin1)
# ship3 = TankShip("长江一号油船",engine1,hull1,deck1,carbin1)
# ship1.info()
# ship2.info()
# ship3.info()

"""
4.士兵类（Soldier）具有名字，和枪支（gun）两个属性
枪支属性默认为None值
士兵可以使用枪支开火(fire)，如果没有获得枪则提示“还没有枪”
枪类（Gun）有型号(model)和子弹数量（bullet_count）属性
枪能够发射子弹(shoot)，也可以装填子弹(add_bullet)，如果子弹数为0则不能继续发射
"""
# class Soldier:
#     def __init__(self, name, gun = None):
#         self.name = name
#         self.gun = gun
#
#     def fire(self):
#         if self.gun:
#             self.gun.shoot()
#         else:
#             print("还没有枪")
#
# class Gun:
#     def __init__(self, model, bullet_count = 0):
#         self.model = model
#         self.bullet_count = bullet_count
#
#     def shoot(self):
#         if self.bullet_count > 0:
#             self.bullet_count -= 1
#             print(f"爆头！剩余子弹{self.bullet_count}")
#         else:
#             print("当前弹夹为空")
#
#
#     def add_bullet(self):
#         self.bullet_count += 10
#         print(f"填充了10颗子弹")
#
# soldier1 = Soldier("张飞")
# soldier1.fire()
# gun1 = Gun("98K")
# soldier1.gun = gun1
# soldier1.fire()
# gun1.add_bullet()
# while True:
#     if gun1.bullet_count > 0:
#         soldier1.fire()
#     else:
#         soldier1.fire()
#         break