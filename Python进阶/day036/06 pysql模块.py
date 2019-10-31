import pymysql

conn = pymysql.connect(host="127.0.0.1",user="root",password="77963333",database="day35")

cur = conn.cursor() #游标
# cur.execute("DROP TABLE IF EXISTS test1")
# sql = """CREATE TABLE test1 (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT
#          )"""
#
# cur.execute(sql)

# cur.execute("select * from test1")

# print(cur.fetchone())
# print(cur.fetchall())
# print(cur.fetchmany(2))
# print(cur.rowcount)

# try:
#     cur.execute("insert into test1 values(4,4,4,5)")
#     conn.commit()
# except:
#     conn.rollback()

# cur.execute("update test1 set first_name='张三' where age=4")
# conn.commit()

# cur.execute("delete from test1 where age=3")
# conn.commit()














#
#
# username = input("用户名")
# password = input("密码")
# # sql = f'select * from userinfo where user ="{username}" and password ="{password}"'
# sql = 'select * from userinfo where user =%s and password =%s'
# # print(sql)
# ret = cur.execute(sql,(username,password))
# if ret:
#     print("登录成功")
# else:
#     print("登录失败")

# sql注入






#
# # 查询语句
# cur.execute("select * from book")#陆续获取数据并记录位置
# # print(cur.fetchone())
# # print(cur.fetchone())
# # print(cur.fetchmany())
# print(cur.fetchall())

# 网络带宽限制（一次性最多能够传输的字节数-1500 MTU）

# 插入数据
# cur.execute("insert into book values('天天向上','彭于晏','哈哈出版社',80,'2019-9-9')")
# conn.commit()

# 更新数据
# cur.execute("update book set 价格=45 where 作者='jinxin'") #内存中临时更新
# conn.commit() #生效

# 删除数据
# cur.execute("delete from book where 价格=40")
# conn.commit()

# cur.close()
# conn.close()


# import pymysql
# while True:
#     user = input("请输入账号：")
#     password = input("请输入密码：")
#     database = input("请输入登录的数据库")
#     try:
#         conn = pymysql.connect(host="127.0.0.1", user=user, password=password, database=database)
#         cur = conn.cursor()  # 游标
#         print("登录成功")
#         break
#     except:
#         print("账号或密码错误！")
# while True:
#     order = input("请输入指令：")
#     try:
#         cur.execute(order)
#         if order[:6].strip().lower() == "select":
#             print(cur.fetchall())
#         else:
#             conn.commit()
#             print("操作成功！")
#     except Exception as e:
#         print("指令错误！",e)

# import pymysql
# db = pymysql.connect("localhost", "root", "77963333", "day38")
# cursor = db.cursor()
#
# for i in range(1,3000000):
#     cursor.execute("insert into s1 values(%d,'eva','female','eva%s@oldboy')"%(i,i))  # 执行sql语句
# db.commit()  # 提交到数据库执行
#
# db.close()
