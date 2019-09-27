# 软件开发规范：分文件管理

# bin -- 启动文件
# lib -- 公共模块
# core -- 主逻辑
# db -- 相关数据
# log -- 日志，记录程序运行情况
# conf --配置文件(静态文件)
import sys
import os
# base_path = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(base_path)
# print(base_path)

base_path = os.path.dirname(os.getcwd())
log_path = os.path.join(base_path,"day016",'userlog.txt')
print(log_path)