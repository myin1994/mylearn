# os -- 与操作系统做交互
import os
# 1.文件
# os.rename("旧名字","新名字")  #重名名 ***
# os.remove("要删除的文件名") #删除文件-慎用-回不来 ***

# 2.文件夹
# os.makedirs("a/b/c/d/e") #递归创建文件夹 ***
# os.removedirs("a/b/c/d/e") #递归删除文件夹 ***
# os.mkdir("a") #单独创建文件夹 ***
# os.rmdir("a")  #单独删除文件夹 ***
# print(os.listdir(r"C:\Users\24479\Desktop\作业上传"))  #查看当前路径下所有的文件 **


# 3.路径
# print(os.getcwd())  #获取当前工作路径 ***

# os.chdir(r"C:\Users\24479\Desktop\作业上传\Python基础\day014") #改变当前脚本工作目录，相当于终端里的cd **
# print(os.getcwd())

# print(os.path.abspath("lib"))  #获取到当前文件的绝对路径
# print(os.path.split(r"C:\Users\24479\Desktop\作业上传\一些git命令.md"))  #路径分割从右往左只切一刀，以元组的形式保存
# print(os.path.dirname(r"C:\Users\24479\Desktop\作业上传"))  #获取父级目录  ***
# print(os.path.basename(r"C:\Users\24479\Desktop\作业上传")) #获取文件名 **

# is系列
# print(os.path.exists(r"C:\Users\24479\Desktop\作业上传"))  #判断路径是否存在 **
# print(os.path.exists(r"C:\Users\24479\Desktop\作业上传1"))  #判断路径是否存在 **

# print(os.path.isabs(r"C:\Users\24479\Desktop\作业上传"))  #判断是否绝对路径 **
# print(os.path.isabs("lib1"))  #判断是否绝对路径 **

# print(os.path.isfile(r"C:\Users\24479\Desktop\作业上传\一些git命令.md")) #判断是否是一个文件 ***
# print(os.path.isfile(r"C:\Users\24479\Desktop\作业上传\lib1.py")) #判断是否是一个文件 ***

# print(os.path.isdir(r"C:\Users\24479\Desktop\作业上传"))  #判断目录是否存在
# print(os.path.isdir(r"C:\Users\24479\Desktop\作业上传\一些git命令.md"))


# 重要

# print(os.path.join("l1","l2","C:\\Users","24479","Desktop","作业上传","一些git命令.md"))  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略 ***

# print(os.path.getsize(r"C:\Users\24479\Desktop\作业上传\一些git命令.md"))  #返回path的大小

# 4.其他(了解)
# os.system("dir")

# print(os.popen("dir").read())  #给终端发送指令  **
# print(os.environ)  #获取系统环境变量  **

# 必会：
# os.getcwd()
# os.makedirs()
# os.removedirs()
# os.mkdir()
# os.rmdir()
# os.rename()
# os.remove()
#
# os.path.abspath()
# os.path.dirname()
# os.path.basename()
# os.path.join()
# os.path.isfile()
# os.path.isdir()
# os.path.getsize()

# sys模块 与python解释器做交互
import sys
# sys.path  #***

# print(sys.platform)  #查看操作系统平台 win-win32  mac-darwin

# print(sys.argv) #命令行参数List，第一个元素是程序本身路径
# sys.argv.append(input("请输入:"))
# print(sys.argv)

# print(sys.version) #获取python版本

# sys.exit()   #退出程序，正常退出时exit(0),错误退出sys.exit(1)

print(sys.modules)  #获取所有模块