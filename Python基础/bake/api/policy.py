
name = "policy"
def f1():
    print("is policy")

# import version  #坑
# print(version.name)  #做到了在policy执行时导入

# 方法1-绝对路径
# from bake.api.version import *
# print(name) #sys.path(api)

# 方法2-加路径
# import sys
# import os
# sys.path.append(os.path.dirname(__file__))
# import version
# print(version.name)