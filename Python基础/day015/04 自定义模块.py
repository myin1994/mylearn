# 模块的介绍：
# py文件就是一个模块

# 模块的分类：
    #1.内置模块--标准库  200+
    #2.第三方模块
    #3.自定义模块

# 为什么要学习模块
    #开发效率高，内置函数和模块
    #拿来主义：没有必要知道其中原理
    #减少重复代码，分文件管理，有助于修改和维护

# qq.py
# 微信.py 合并成一个文件

# 自定义模块
# py文件就是一个模块
# import 导入 相当于把工具箱拿过来
# 导入时发生的事情：
    #1.将模块存储到当前名称空间中
    #2.以模块的名字命名，并开辟空间
    #3.通过模块名来使用模块中的功能
# import lib  #飘红不代表报错，单独使用要用.操作
# print(globals())
#
# lib.login()
# lib.register()
# a = 10
# print(lib.a)
# print(a)

# from 模块名 import 功能
# 同一模块下可在同一行写
# a = 10
# from lib import login,register,a   #从lib模块下将login函数导入
# login()
# register()
# print(a)

# a = 10
# from lib import a as b  #给模块中的变量临时取别名
# print(a)
# print(b)

# 同一个模块，写多次导入只执行一次
# import lib
# import lib
# import lib
# import lib  #多次只会取一次
# print(globals())

# from lib import a
# from lib import a
# from lib import a
# from lib import a
# print(globals())

# 相对路径：导入

# 绝对路径导入
# 模块导入顺序：内存，内置，sys.path
import sys
# print(sys.modules)  #查看内置模块
# print(sys.path) #获取模块查找路径
# for i in sys.path:
#     print(i)

# sys.path.append(r"C:\Users\24479\Desktop\作业上传\Python基础\day014")
# print(sys.path)
# from lib import a
# print(a)


# 练习
# import sys
# sys.path.insert(0,r"C:\Users\24479\Desktop")
# print(sys.path)
# import zhuomian
# print(zhuomian.a)
# zhuomian.login()

# 模块的两种用法：
# 1.普通模块
# 2.被当做脚本执行（终端下运行）
# import sys
# sys.path.append(r"C:\Users\24479\Desktop\作业上传\Python基础\day014")
# from lib import a
# # print(a)
#
# if __name__ == "__name__":
#     pass
# 在当前文件中执行__main__获取的值是"__name__"
# 当前文件被当做模块导入时，__name__获取的是当前文件名


# 一个以后要避免的问题：
# 循环导入（变成环）


# import 和 from 的对比
# import 全部对比
# from 指定功能导入

# import和from都支持as

# from会将之前定义的同名的变量覆盖
# from 可以一行导入多个功能
# from lib import * 将lib下所有的功能全部导入
# import 建议一行导入一个模块

# 推荐使用from

# 自定义模块导入的顺序：内存-内置-sys.path
# sys.path.append() 添加一个模块查找路径


# __all__=['name','read1'] #这样在另外一个文件中用from spam import *就只能导入列表中规定的两个名字