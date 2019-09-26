"""
s_26 day15 作业
"""

"""
2.写函数：用户输入某年某月，判断这是这一年的第几天（需要用Python的结构化时间）。
结构化时间可以通过这样取值：

import time
ret = time.localtime()
print(ret)  # time.struct_time(tm_year=2019, tm_mon=6, tm_mday=28, tm_hour=15, tm_min=50, tm_sec=47, tm_wday=4, tm_yday=179, tm_isdst=0)
print(ret.tm_year)  # 2019
"""
# import time
# def day():
#     user_year = input("请输入年份:")
#     user_month = input("请输入月份:")
#     user_day = input("请输入日期:")
#     user_time = time.strptime(f"{user_year}-{user_month}-{user_day}","%Y-%m-%d")
#     print(f"这是这一年的第{user_time.tm_yday}天")
# day()
"""
3.用户输入一个"2019-7-26 20:30:30"和当前时间相比,一共过去了多少年多少月多少天到少小时多少分钟
"""
# import time
# user_time = input("请输入一个时间：")
# user_time = time.strptime(user_time ,"%Y-%m-%d  %H:%M:%S")
# local_time = time.localtime()
# print(user_time)
# print(local_time)
# print(f"和当前时间相比已经过去了{local_time.tm_year-user_time.tm_year}年"
#       f"{local_time.tm_mon-user_time.tm_mon}月"
#       f"{local_time.tm_mday-user_time.tm_mday}天"
#       f"{local_time.tm_hour-user_time.tm_hour}小时"
#       f"{local_time.tm_min-user_time.tm_min}分钟")

"""
4.写函数，生成一个4位随机验证码（包含数字大小写字母)
"""
# import random
# def random_code(n):
#     s = ""
#     for i in range(n):
#         s += str(random.choice([chr(random.randint(65,90)),chr(random.randint(97,122)),random.randint(0,9)]))
#     print(s)
# random_code(4)
