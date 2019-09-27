# 路径等不变的变量
import os
BASE_PATH = os.path.dirname(os.getcwd())
userinfo_path = os.path.join(BASE_PATH,'db','userinfo.txt')
userlog_path = os.path.join(BASE_PATH,'log','userlog.txt')
userlog2_path = os.path.join(BASE_PATH,'log','userlog2.txt')