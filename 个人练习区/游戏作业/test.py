"""
实现每次开始游戏输入姓名后随即职业与属性

"""


class Single:
    single = None

    def __new__(cls, *args, **kwargs):
        if cls.single == None:
            cls.single = super().__new__(cls)
        return cls.single


class Hero(Single):

    def __init__(self, name):
        self.__name = name
        self.__hero_career = None
        self.__hero_hp = 0
        self.__hero_origin_hp = 0
        self.__hero_mp = 0
        self.__hero_atk = 0
        self.__hero_level = 0
        self.__hero_exp = 0
        self.__hero_level_dic = {i: i * 200 for i in range(1, 99)}
        self.__weapon_lst = []

    @property
    def name(self):
        return self.__name

    @property
    def career(self):
        import random
        if self.__hero_career == None:
            self.__hero_career = random.choice(["战士", "刺客", "法师"])
        return self.__hero_career

    @property
    def hp(self):
        import random
        if self.__hero_hp == 0:
            if self.__hero_career == "战士":
                self.__hero_hp = random.randint(1000, 2000)
            if self.__hero_career == "刺客" or self.__hero_career == "法师":
                self.__hero_hp = random.randint(500, 1000)
        self.__hero_origin_hp = self.__hero_hp
        return self.__hero_hp

    @hp.setter
    def hp(self, num):
        self.hp = num

    @property
    def mp(self):
        import random
        if self.__hero_mp == 0:
            if self.__hero_career == "战士":
                self.__hero_mp = random.randint(200, 500)
            if self.__hero_career == "刺客":
                self.__hero_mp = random.randint(300, 700)
            if self.__hero_career == "法师":
                self.__hero_mp = random.randint(600, 1000)
        return self.__hero_mp

    @mp.setter
    def mp(self, num):
        self.mp = num

    @property
    def atk(self):
        import random
        if self.__hero_atk == 0:
            if self.__hero_career == "战士":
                self.__hero_atk = random.randint(20, 50)
            if self.__hero_career == "刺客":
                self.__hero_atk = random.randint(60, 100)
            if self.__hero_career == "法师":
                self.__hero_atk = random.randint(80, 120)
        return self.__hero_atk

    @atk.setter
    def atk(self, num):
        self.atk = num

    @property
    def level(self):
        return self.__hero_level

    @level.setter
    def level(self, num):
        self.level = num

    def lv_up(self):
        self.origin_level = self.__hero_level
        for k, v in self.__hero_level_dic.items():
            if self.__hero_exp > v:
                self.__hero_level = k
        if self.__hero_level > self.origin_level:
            self.__hero_hp = self.__hero_origin_hp + 100
            self.__hero_origin_hp = self.__hero_hp
            self.__hero_mp += 50
            self.__hero_atk += 10

    def add_exp(self, num):
        self.__hero_exp += num

    def fight(self, other):
        other.hp -= self.atk

    def get_weapon(self, *args):
        self.__weapon_lst.extend(args)
        if self.__weapon_lst != []:
            for i in self.__weapon_lst:
                self.__hero_atk += i.atk

    def init(self):
        return self.career, self.hp, self.mp, self.atk, self.level

    @property
    def heroInfo(self, ):
        return f"""
    英雄姓名:{self.name}
    英雄等级lv：{self.level}
    英雄经验值：{self.__hero_exp}
    英雄职业:{self.career}
    英雄血量:{self.hp}
    英雄法力值：{self.mp}
    英雄攻击力：{self.atk}
    当前武器列表:{'-'.join(self.__weapon_lst)}"""


class Monster:
    def __init__(self):
        import random
        self.__name = f"{random.randint(1, 99)}号怪物"
        self.__hp = random.randint(1500, 2000)
        self.__mp = random.randint(1000, 1500)
        self.__atk = random.randint(15, 20)

    def evolve(self):
        self.__hp += 150
        self.__mp += 100
        self.__atk += 5

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, num):
        self.hp = num

    @property
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self, num):
        self.mp = num

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, num):
        self.atk = num

    def fight(self, other):
        other.hp -= self.atk

    def init(self):
        return self.hp, self.mp, self.atk

    @property
    def monsterInfo(self):
        return f"""
    怪物名:{self.name}
    怪物血量:{self.hp}
    怪物值：{self.mp}
    怪物攻击力：{self.atk}"""


class Weapon:
    def __init__(self):
        import random
        self.__name = f"{random.choice([chr(i) for i in range(65, 91)])}系列武器"
        self.__level = random.randint(1, 6)
        self.__atk = self.__level + 5


while True:
    hero = Hero(input("请输入英雄姓名："))
    hero.init()
    print(hero.heroInfo)
    monster = Monster()
    print(monster.hp)
    hero.fight(monster)
    if monster.hp > 0:
        print(1)

# hero = Hero("123")
# # print(hero.heroInfo)
# mo = Monster()
# hero.init()
# mo.init()
# print(hero.hp)
# print(mo.hp)
# print(hero.hp-mo.atk)
# print(type(hero.hp))
# print(type(hero.atk))
# print(type(mo.hp))
# print(type(mo.atk))

