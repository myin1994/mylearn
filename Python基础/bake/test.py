# import day017.bake.policy as p
# print(bake.api.policy.name)

import os
print(os.getcwd())

# from bake.cmd.manage import name
# print(name)

# from bake.cmd.manage import *
# print(name)
# f()
# foo()

# from bake.api import *
# print(policy.name)
# print(version.name)
# policy.func()

# from bake import *
# # print(policy.name)
# # print(version.name)
# print(manage.name)
# print(models.name)


# from bake import *
# print(policy.name)
# policy.func()


from bake.api.policy import *
print(name)#test中运行时，sys.path中第一个存的是back