"""
1.时间模块
2.输入时间
3.转换为时间戳
4.获取当前时间戳
5.当前时间戳减去用户输入的时间戳
6.将差值转为结构化时间

"""
import time
str_time = input("输入时间：")
struct_time = time.strptime(str_time,"%Y-%m-%d %H:%M:%S")
origin_time = time.mktime(struct_time)
gap_time = time.time()-origin_time
gap_time = time.localtime(gap_time)

print(f"过去了：{gap_time.tm_year-1970}年，"
      f"{gap_time.tm_mon-1}月，"
      f"{gap_time.tm_yday-1}天，"
      f"{gap_time.tm_hour-8}时，"
      f"{gap_time.tm_min}分")