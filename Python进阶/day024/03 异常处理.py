#  异常类
# 异常（Exception）-在程序执行过程中发生的影响程序正常执行的事件

# raise 语句显式的抛出异常（一个对象）
# Python解释器自己检测到异常并引发它

# 内存
# 栈区：用来存放变量（可变的数据）引用-先入先出
# 堆区：用来存放对象（不可变的）


# 异常处理
# 用特定代码来捕捉异常（与当前程序逻辑无关）

# 方式1  if 影响程序的可读性

# 方法2
# try:
#     # 被检测的代码块
# except 异常类型: #发生异常后接收
#     接收异常后的处理方式

# 使用

# a = [1,2,3]
# try:
#     print(a[5])
# except ZeroDivisionError:
#     print("0不能作为除数")
# print("后续语句")



# ZeroDivisionError
# a = [1,2,3]
# try:
#     print(1/0)  #捕获到异常就抛出
#     print(a[5])
# except ZeroDivisionError:
#     print("除0错误")
# except IndexError: #多分支，不同异常不同处理方式
#     print("索引错误")
# print("后续语句")

# try:
#     # print(1/0)  #捕获到异常就抛出
#     print(a[5])
# except Exception as e: #万能异常-处理方式是一样的
#     print(e)
#
# print("后续语句")




# dic = {1: "login",2: "register",3: "dariy",4: "article",5: "comment"}
# print('''欢迎访问博客园系统： 1，登录 2，注册 3，访问日记页面 4，访问文章页面 5，访问评论页面''')
# try:
#     choice = int(input('请输入：'))
#     print(dic[choice])
# except ValueError:
#     print('请输入数字....')
# except KeyError:
#     print('您输入的选项超出范围...')
# except Exception as e:
#     print(e)









# finally-一般收尾工作
# a = [1,2,3]
# try:
#     print(1/1)
#     print(a[9])
# except ZeroDivisionError:
#     print("除0错误")
# else:#else try后面的语句，没有任何异常，执行else后的内容
#     print("else")
# finally:#没捕获到也一定会执行
#     print("肯定执行finally")
# print("后续语句")

# finally会在return之前执行
# def func():
#     try:
#         return 1
#     finally:
#         print('finally')
# func()

# while 1:
#     try:
#         break
#     finally:
#         print('finally')



# assert 断言
# name = "小明"
# print("1")
# print("1")
# assert name == "小明1" #若为False后面不再执行
# print("1")
# print("1")
# print("1")

class Wodingyideyichang(Exception):
    value = "你中了我定义的异常"
try:
    if 1 < 2:
        raise Wodingyideyichang()
except Wodingyideyichang as e:
    print(e.value)
