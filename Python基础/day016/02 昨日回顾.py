# 1.自定义模块
# 导入：
# import 模块名
# 模块名.功能
# 起别名
# from 模块名 import 功能as
# 模块的查找顺序：内存-内置-sys.path
# sys.path.append("路径")

# 模块导入多次只执行一次
# from 会覆盖原有变量名
# from xx import *
# __all__ = ["控制导入的模块"]

# if __name__ == "__main__":模块的两种用法
# 1.当做模块导入
# 2.脚本

# import 和from 的区别
# import 全部导入
# from 指定功能导入

# 推荐使用from

# 2.time
# import time
# time.time()
# time.sleep()
# time.localtime()
# time.strftime()
# time.strptime()
# time.mktime()
# %Y %m %d %H %M %S

# 3.datetime
# from datetime import datetime
# datetime.now()
# datetime(2019,11,11,11,11,11)

# 4.os
# import os
# os.rename()
# os.remove()
# os.getcwd()
# os.mkdir()
# os.rmdir()
# os.makedirs()
# os.removedirs()
# os.path.join()
# os.path.join()
# os.path.isfile()
# os.path.isdir()
# os.path.getsize()


# 5.sys
# import sys
# sys.path
# sys.argv
# sys.platform
# sys.modules
# sys.version

# 6.random
# import random
# random.random()
# random.randint()
# random.randrange()
# random.choice()
# random.choices()
# random.shuffle()