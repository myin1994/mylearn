import sys
import os
base_path = os.path.dirname(os.path.dirname(__file__)) #获取当前目录--获取当前目录的父级目录
sys.path.append(base_path) #将父级目录添加到sys路径下
from core import src
src.run()