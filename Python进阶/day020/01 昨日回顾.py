# 面向过程和面向对象的表述

class Person:
    #命名时：见名知意，驼峰体
    #类属性和实例属性
    eyes = 2

    def __init__(self,name):
        #self.name = "小明"
        self.name = name

    #实例方法
    def run(self):
        print(f"{self.name}在跑")

# 类不能访问实例属性及实例方法
xiaoming = Person("小明")