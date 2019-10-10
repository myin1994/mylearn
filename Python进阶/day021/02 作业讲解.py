# 3.
# class KeChuan:
#     def __init__(self,fdj,ct,jb,cc):
#         self.fdj = fdj
#         self.ct = ct
#         self.jb = jb
#         self.cc = cc
# class HuoChuan:
#     pass
#
# class YouChuan:
#     pass
#
# class FDJ:
#     pass
#
# class CT:
#     pass
#
# class JB:
#     pass
#
# class CC:
#     pass
#
# f = FDJ()
# c = CT()
# j = JB()
# cc = CC()
#
# kechuan = KeChuan(f,c,j,cc)

# 4
class Solider:
    def __init__(self, name, gun = None):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun:
            self.gun.shoot()
        else:
            print("没有枪")

class Gun:
    def __init__(self, model, bullet_count):
        self.model = model
        self.bullet_count = bullet_count

    def shoot(self):
        if self.bullet_count > 0:
            print("biubiu")
            self.bullet_count -= 1
        else:
            print("请换弹夹")

    def add(self,num):
        self.bullet_count += num


ak = Gun("ak47", 5)
so1 = Solider("大卫", ak)
so1.fire()
