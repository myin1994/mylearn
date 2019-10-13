# 约束（对类的约束）
# 在一些重要的逻辑，与用户数据相关等核心部分，要建立一种约束，避免发生此类错误
#保护程序内部的核心代码完整

# 类的约束有两种解决方式：
# 1.通过继承，在父类建立一种约束（通过抛出异常）
# 2.引入抽象类的概念

# 解决方式一：
# • 提取⽗类，在⽗类中定义好⽅法，在这个⽅法中抛⼀个异常。
# 这样所有的⼦类都必须重写这个⽅法.否则.访问的时候就会报错
# class Fpay:
#     def pay(self):
#         raise Exception("子类必须重新pay方法")
#
#
# class QQpay(Fpay):
#
#     def pay(self):
#         print(f"QQpay")
#
#
# class Alipay(Fpay):
#     def pay(self):
#         print("Alipay")
#
#
# class WXpay(Fpay):
#     def pay1(self):
#         print("微信支付")
#
#
# def pay(pay_func):  # 归一化设计
#     pay_func.pay()
#
#
# q = QQpay()
# a = Alipay()
# w = WXpay()
# pay(q)
# pay(w)

# 解决方式二：
# • 用抽象类(制定一种规范)的概念,建立一种约束 （从多个类中再抽象出类）
# • 基类如下设置,子类如果没有定义pay方法,在实例化对象时就会报错

from abc import ABCMeta,abstractmethod #导入元类，抽象方法
class Payment(metaclass=ABCMeta):#修改了元类，该元类可以创建抽象类
    @abstractmethod #声明抽象方法，只定义，不实现具体功能（但要求子类必须实现同名方法）
    def pay(self):
        pass

# 设置一个类的metaclass（元类）是ABCMeta
# 那么这个类就变成了一个抽象类(接口类)
# 这个类的功能就是建立一个规范
# 由于该⽅案来源是java和c#. 所以不常用

#  Python本身不提供抽象类和接口机制，要想实现抽象类，可以借助abc模块。ABC是 Abstract Base Class（抽象父类）的缩写
# abc.ABCMeta是用来生成抽象基础类的元类。由它生成的类可以被直接继承，但是 抽象类不能直接创建对象（只能被继承）
# @abstractmethod表明抽象方法，如果子类不具备@abstractmethod的方法，那么就 会抛出异常

class QQpay(Payment):

    def pay(self):
        print(f"QQpay")

class Alipay(Payment):

    def pay(self):
        print("Alipay")

class WXpay(Payment):

    def pay1(self):  #定义时就报错
        print("微信支付")

def pay(pay_func):  # 归一化设计
    pay_func.pay()

q = QQpay()
a = Alipay()
w = WXpay()
pay(q)
