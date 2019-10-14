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
        self.origin_level = 0
        self.__hero_exp = 0
        self.__hero_level_dic = {i: i * 100 for i in range(1, 99)}
        self.__weapon_lst = []
        self.__weapon_atk = 0

        
    @property
    def name(self):
        return self.__name

    @property
    def career(self):
        import random
        if self.__hero_career == None:
            self.__hero_career = random.choice(["战士","刺客","法师"])
        return self.__hero_career

    @property
    def hp(self):
        import random
        if self.__hero_hp == 0:
            if self.__hero_career == "战士":
                self.__hero_hp = random.randint(1000,2000)
            if self.__hero_career == "刺客" or self.__hero_career == "法师":
                self.__hero_hp = random.randint(500,1000)
            self.__hero_origin_hp = self.__hero_hp
        return self.__hero_hp

    @hp.setter
    def hp(self, num):
        self.__hero_hp = num

    @property
    def mp(self):
        import random
        if self.__hero_mp == 0:
            if self.__hero_career == "战士":
                self.__hero_mp = random.randint(200,500)
            if self.__hero_career == "刺客":
                self.__hero_mp = random.randint(300,700)
            if self.__hero_career == "法师":
                self.__hero_mp = random.randint(600,1000)
        return self.__hero_mp

    @mp.setter
    def mp(self, num):
        self.__hero_mp = num

    @property
    def atk(self):
        import random
        if self.__hero_atk == 0:
            if self.__hero_career == "战士":
                self.__hero_atk = random.randint(150,200)
            if self.__hero_career == "刺客":
                self.__hero_atk = random.randint(190,250)
            if self.__hero_career == "法师":
                self.__hero_atk = random.randint(180,240)
        return self.__hero_atk

    @atk.setter
    def atk(self, num):
        self.__hero_atk = num

    @property
    def level(self):
        return self.__hero_level

    @level.setter
    def level(self, num):
        self.__hero_level = num

    def lv_up(self):
        self.origin_level = self.__hero_level
        for k, v in self.__hero_level_dic.items():
            if self.__hero_exp >= v:
                self.__hero_level = k
        if self.__hero_level > self.origin_level:
            self.__hero_hp = self.__hero_origin_hp + 100
            self.__hero_origin_hp = self.__hero_hp
            self.__hero_mp += 50
            self.__hero_atk += 10
            print("您的头发掉了！您变强了！")
            print("血量增加100，法力值增加50，英雄攻击力增加10")

    def add_exp(self,num):
        self.__hero_exp += num
        return self.lv_up()

    def fight(self, other):
        other.hp -= self.atk + self.__weapon_atk
        print(f"英雄攻击怪物，英雄当前血量：{self.hp} 怪物当前血量{other.hp}")

    def get_weapon(self, *args):
        self.__weapon_lst.extend(args)
        for i in args:
            self.__weapon_atk += i.atk
            print(f"您获得了{i.level}级{i.name},攻击力增加{i.atk}")

    # def init(self):
    #     return self.career,self.hp, self.mp,self.atk,self.level

    @property
    def heroInfo(self,):
        return f"""
    英雄姓名:{self.name}
    英雄等级lv：{self.level}
    英雄经验值：{self.__hero_exp}/{self.__hero_level_dic[self.level+1]}
    英雄职业:{self.career}
    英雄血量:{self.hp}
    英雄法力值：{self.mp}
    英雄攻击力(武器增幅：{self.__weapon_atk})：{self.atk + self.__weapon_atk}"""
    # 当前武器列表:{'-'.join(self.__weapon_lst)}

class Monster:
    def __init__(self):
        import random
        self.__name = f"{random.randint(1,99)}号怪物"
        self.__hp = random.randint(1300,1500)
        self.__origin_hp = self.__hp
        self.__mp = random.randint(1000,1500)
        self.__atk = random.randint(60,80)

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
    def hp(self,num):
        self.__hp = num

    @property
    def origin_hp(self):
        return self.__origin_hp

    @property
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self, num):
        self.__mp = num

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, num):
        self.__atk = num

    def fight(self, other):
        other.hp -= self.atk
        print(f"怪物攻击英雄，怪物当前血量：{self.hp} 英雄当前血量{other.hp}")

    # def init(self):
    #     return self.hp, self.mp, self.atk

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
        self.name = f"{random.choice([chr(i) for i in range(65,91)])}系列武器"
        self.level = random.randint(1,6)
        self.atk = self.level + 5

hero = Hero(input("请输入英雄姓名："))
while True:
    print(hero.heroInfo)
    flag = input("是否开始游戏？（任意键开始游戏/N-退出）")
    if flag.upper() == "N":
        print(hero.heroInfo)
        exit()
    # hero.init()
    monster = Monster()
    monster.evolve()
    print("遭遇怪物")
    print(monster.monsterInfo)
    # monster.init()
    while monster.hp > 0:
        hero.fight(monster)
        if monster.hp < 0:
            print("怪物死了")
            print(f"您的经验值增加{int(monster.origin_hp*0.05)}")
            hero.add_exp(int(monster.origin_hp*0.05))
            hero.get_weapon(Weapon())
            break
        else:
            monster.fight(hero)
            if hero.hp < 0:
                print("您死了！游戏结束！")
                print(hero.heroInfo)
                exit()



