# logging  -- 日志
# 1.记录程序运行状态
# 时间，哪个文件，报错位置（行数），错误信息
# 2.用户的喜好
    #分析用户的一些喜好，操作
# 3.银行
    #记录账户流水


# 日志的级别：
# 1.debug 调试 --10-- print
# 2.info 信息 --20
# 3.worning 警告--30
# 4.error 错误 --40
# 5.critical 危险 --50

# 基础版
# import logging
# # # 默认从30开始记录
# # # 编码不能修改
# # # 屏幕和文件不能同时有
# logging.basicConfig(
#     level=10,
#     format="%(asctime)s %(name)s %(filename)s %(lineno)s %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
#     # filename="test.log",
#     # filemode="a"
#     )
# logging.debug("这是调试")
# logging.info("这是信息")
# logging.warning("这是警告")
# logging.error("这是错误")
# logging.critical("这是危险")
#
# num = input("请输入数字：")
# try:
#     num = int(num)
#     print(num)
# except Exception:
#     logging.warning("字符串不能转换为数字")


# 进阶版：组装一个日志功能（二次开发实现的）
# import logging
# logger = logging.getLogger() #创建一个空架子，与logging独立
# fh = logging.FileHandler("test1.log","a",encoding="utf-8")  #创建一个文件句柄用来记录日志（文件流）
# ch = logging.StreamHandler()  #创建一个屏幕流（打印记录的内容）
# formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)s %(message)s") #定义一个记录文件的格式
#
#
#
# fh.setFormatter(formater)  #给文件句柄设置记录内容的格式
# ch.setFormatter(formater) #给中控台设置打印内容的格式
#
# logger.addHandler(fh)  #将文件句柄添加到logger对象中
# logger.addHandler(ch)  #将中控台添加到logger对象中
#
# logger.level = 10  #设置警告级别
#
# logger.debug("调试")
# logger.info("信息")
# logger.warning("警告")
# logger.error("错误")
# logger.critical("危险")

from my_logger import logger
logger.debug("调试2")
logger.info("信息2")
logger.warning("警告2")
logger.error("错误2")
logger.critical("危险2")
