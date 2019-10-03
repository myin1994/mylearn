# 包：具有__init__.py的文件夹

# 包的目的：管理模块

# 包的本质就是模块  模块可以导入  包也可以导入

# python2中 使用import一个包时，包中没有__init__.py会报错
# python3中 使用import一个包时，包中没有__init__.py不报错

# 在导入时发现使用点操作就是在导入包
# 导入时，点前面必须是一个包

# 路径：
# 绝对路径：import bake.api.policy  从最外层的包开始查找
# 相对路径：from 可以使用相对路径 取决于在哪个文件中运行

# import bao.bao.模块
# import bao.bao.模块  as v

# from bao.bao.mokuai import hanshu,变量，*

from bake import *
# 1.先在bake的__init__.py中导入bake下所有的包
# 2.在bake下所有的包中的__init__.py导入每个包下的模块

# 按照软件开发规范创建包 ，包中存放模块

