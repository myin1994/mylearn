# time ---  模块
import time
# print(time.time())  #时间戳  浮点数

# print(time.sleep(2))  #秒  进行睡眠 返回None

"""
python中时间日期格式化符号： 
%y 两位数的年份表示（00-99） 
%Y 四位数的年份表示（000-9999） ***
%m 月份（01-12）   ****
%d 月内中的一天（0-31）  ***
%H 24小时制小时数（0-23） ***
%I 12小时制小时数（01-12） 
%M 分钟数（00=59）  ****
%S 秒（00-59）   ****
%a 本地简化星期名称 
%A 本地完整星期名称 
%b 本地简化的月份名称 
%B 本地完整的月份名称 
%c 本地相应的日期表示和时间表示 
%j 年内的一天（001-366） 
%p 本地A.M.或P.M.的等价符 
%U 一年中的星期数（00-53）星期天为星期的开始 
%w 星期（0-6），星期天为星期的开始 
%W 一年中的星期数（00-53）星期一为星期的开始 
%x 本地相应的日期表示 
%X 本地相应的时间表示 
%Z 当前时区的名称 
%% %号本身
"""

# 时间分类:
# 1.时间戳  --用于计算
# 2.结构化时间 ---给程序员查看使用(命名元组)
# 3.字符串时间 --- 给用户看查看

# t = time.time() #时间戳
# print(t)
# print(time.localtime(t))  #时间戳转换结构化时间
# print(time.localtime())  #默认转换当前时间戳为结构化时间

# t = time.localtime()
# print(time.mktime(t))  #将结构化时间转换为时间戳

# t = time.localtime()
# print(time.strftime("%Y-%m-%d  %H:%M:%S",t)) #将结构化时间转换成字符串时间

# str_time = "2019-09-26  12:23:36"
# print(time.strptime(str_time,"%Y-%m-%d  %H:%M:%S"))  #将字符串时间转换为结构化时间

# print(time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime())) #时间戳直接转换字符串时间

# print(time.localtime().tm_year)  #获取当前年份
# print(time.localtime().tm_yday)