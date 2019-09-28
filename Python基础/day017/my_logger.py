import logging
def my_logger():
    logger = logging.getLogger() #创建一个空架子，与logging独立
    fh = logging.FileHandler("test1.log","a",encoding="utf-8")  #创建一个文件句柄用来记录日志（文件流）
    ch = logging.StreamHandler()  #创建一个屏幕流（打印记录的内容）
    formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)s %(message)s") #定义一个记录文件的格式



    fh.setFormatter(formater)  #给文件句柄设置记录内容的格式
    ch.setFormatter(formater) #给中控台设置打印内容的格式

    logger.addHandler(fh)  #将文件句柄添加到logger对象中
    logger.addHandler(ch)  #将中控台添加到logger对象中

    logger.level = 10  #设置警告级别
    return logger

logger = my_logger()