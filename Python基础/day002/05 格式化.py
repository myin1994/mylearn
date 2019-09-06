# msg = """
# ------infor------
# name：姓名
# age：18
# sex：男
# hobby：女
# --------end------
# """


# %s 占位（字符串）：%s可以填充字符串也可以填充数字
# %d/%i 占位（整型）：必须填充数字
# name = input("name：")
# age = int(input("age："))
# sex = input("sex：")
# hobby = input("hobby：")
#
# msg = """
# ------infor------
# name：%s
# age：%d
# sex：%s
# hobby：%s
# --------end------
# """
# print(msg%(name,age,sex,hobby)) #按位置顺序补位，占位数据类型要和变量类型保持一致

# %% 转义：变成普通的%
# msg = "目前的学习进度为%s%%"
# print(msg%(2))
# msg = "%s,%d,%%"%(name,age)
# msg = "my name is %s I'm %s years old"
# print(msg%(input("name:"),input("age:")))

# f-strings python3.6版本及以上才能使用
# f."{name},{age},{{}}%"
# {{  }}重复使用转义
# msg = f"my name is {input('name:')} I'm {input('age:')} years old"
# print(msg)