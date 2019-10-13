# class Person:
#     def __run(self):
#         print("人会跑")
#
# class Boy(Person):
#     def __run(self): #不一样
#         print("我会跑")
class Single(object):
    ans = False
    def __new__(cls, *args, **kwargs):
        if not cls.ans:
            cls.ans = object.__new__(cls)
        return cls.ans
class Mather(Single):

    def __init__(self, nmae):
        self.name = nmae
    def cook(self):
        print(f"妈妈叫{self.name}，会炒山药")

m1 = Mather("小丽")
m2 = Mather("小红")
print(m1.name)