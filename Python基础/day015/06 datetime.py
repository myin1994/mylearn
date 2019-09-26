from datetime import datetime
# print(datetime.now())  #获取到当前时间，对象
# print(str(datetime.now()))  #获取到当前时间，对象
# print(type(datetime.now()))  #获取到当前时间，对象

# print(datetime(2016,11,22,13,25,2,2))  #指定时间

# 时间戳转对象
import time
# print(datetime.fromtimestamp(time.time()))

#将对象转换成时间戳
# print(datetime.timestamp(datetime.now()))

#对象转换成字符串
# print(datetime.strftime(datetime.now(),"%Y-%m-%d  %H:%M:%S"))

#字符串转换为对象
# print(datetime.strptime("2019/10/14","%Y/%m/%d"))
# print(datetime.strptime("2019/10/14 13:25:26","%Y/%m/%d %H:%M:%S"))

# print(datetime.now() - datetime(2019,9,1,12,13))  #计算时间

# from datetime import datetime,timedelta
# print(datetime.now()-timedelta(days=365)) #加减时间间隔
# print(datetime.now()+timedelta(days=365))