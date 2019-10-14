# 魔法方法
# __ 双下划线
# 自动调用

# __new__ 创建对象

# __init__ 构造器，初始化对象的属性

# __del__ 析构器

# class Person:
#     def __new__(cls, *args, **kwargs):
#         print("new创建对象的方法")
#         return object.__new__(cls)
#     def __init__(self):
#         self.name = 1
#         print("用来初始化对象，构造方法或构造器")
#
#     def __del__(self):
#         print("析构器，析构方法，在对象被删除时，自动调用")
#
#     def __len__(self):
#         return 666
#
#     def __str__(self):
#         return "人类对象，有{}{}方法{}{}对象"

# xiaoming = Person()
# del xiaoming



# __len__  通过len(obj)调用，返回值必须设置为长度
# lis = [1,2,3,4,5,6,7,8]
# print(len(lis))
# print(len(xiaoming))

# __hash__ 通过hash(obj) 调用 获取哈希值

# __str__
# print(xiaoming)

# __eq__ 判断两个对象是否相同,设置规则
class A:
    def __init__(self):
        self.name = "xiaoming"
        self.age = 20

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False

class B:
    def __init__(self):
        self.name = "xiaoming"
        self.age = 20
a =A()
b = B()
print(a == b)  #调用前者的eq方法
b.name = 111
print(a == b)