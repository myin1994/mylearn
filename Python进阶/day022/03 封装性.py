# 封装（特性）：将抽象得到的数据和行为相结合，形成一个有机的整体
# 抽象得到类的过程

# 数据的封装：元组，列表，字典-通过引用去使用数据
# 算法的封装: 函数

# 封装的目的：简化编程和增强安全性，
    #使用者不必关系如何实现
    #通过接口调用（点）
    #可以设置特定的访问权限
    #明确区分内外
        #类的实现者：内
        #类的使用者：外
# 封装：对内隐藏类内的具体实现，只提供接口，供外界访问（尽量多做封装）
# 使用__创建属性和方法

class Person:
    def __init__(self, name, age):
        self.__name = name  #私有属性,实际上自动变成当前类的类名_Person__name
        self.__age = age

    def __play(self): #私有方法
        print(f"{self.__name}喜欢玩儿手机")
    #提供外界访问的接口
    #类内可以访问私有属性和私有方法
    def get_name(self): #访问私有属性的接口
        return self.__name

    def set_name(self, name):
        self.__name = name
    def set_age(self,num):
        if 0 < num < 150:#对传入的属性设限
            self.__age = num
        else:
            print("输入不合法！")
    def get_play(self):
        self.__play()

# xiaoming = Person("小明",18)
# print(xiaoming.get_name())
# # xiaoming.play()
# xiaoming.set_name("马云")
# print(xiaoming.get_name())
# # print(xiaoming._Person__name)
# xiaoming._Person__name = "张飞"
# print(xiaoming._Person__name)
# print(xiaoming.get_name())
# print(xiaoming.__dict__)

# xiaoming.get_play()

class Boy(Person): #继承的也是相同的方法
    pass

xiaoli = Boy("小刚",20)
print(xiaoli.get_name())
print(xiaoli._Person__name)
print(xiaoli.__dict__)