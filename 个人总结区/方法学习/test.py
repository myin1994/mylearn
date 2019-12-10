from functools import partial
# def chunked_file_reader(file, block_size=1024 * 8):
#     """
#     生成器函数：分块读取文件内容，使用 iter 函数
#     @param file: 文件句柄
#     @param block_size: 字节数
#     @return:
#     """
#     # 首先使用 partial(fp.read, block_size) 构造一个新的无需参数的函数
#     # 循环将不断返回 fp.read(block_size) 调用结果，直到其为 '' 时终止
#     for chunk in iter(partial(file.read, block_size), ''):
#         yield chunk

# with open('ajax过csrf验证.md') as f:
#     for chunk in chunked_file_reader(f):
#         print(chunk)

from datetime import datetime,timedelta
def GetNextDay(baseday,n):
    return str((datetime.strptime(str(baseday),'%Y-%m-%d')+timedelta(days=n)).date())
selected_day = '2019-11-11'
print(GetNextDay(selected_day, 1))
print(GetNextDay(selected_day, 2))
print(GetNextDay(selected_day, 6))
print(GetNextDay(selected_day, 13))
print(GetNextDay(selected_day, 29))

nday = partial(GetNextDay,selected_day)
print('>>>>>>>>>>>>>')
print(nday(1))
print(nday(2))
print(nday(6))
print(nday(13))
print(nday(29))