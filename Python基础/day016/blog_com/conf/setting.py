import os
BASE_PATH = os.path.dirname(os.getcwd()) #获取当前工作目录
userinfo_PATH = os.path.join(BASE_PATH,'db','userinfo.txt')  #拼接成有效路径
userlog_PATH = os.path.join(BASE_PATH,'log','userlog.txt')
userlog2_PATH = os.path.join(BASE_PATH,'log','userlog2.txt')
userlog3_PATH = os.path.join(BASE_PATH,'log','userlog3.txt')