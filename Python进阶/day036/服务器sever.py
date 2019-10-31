from socket import *
import pymysql
s = socket()
s.bind(("192.168.34.170",7788))
s.listen(5)

conn = pymysql.connect(host="127.0.0.1",user="root",password="77963333",database="day36")
cur = conn.cursor()
s1,addr = s.accept()
while True:
    action = s1.recv(1024).decode()
    if action == "注册":
        s1.send("请输入（用户名:密码）".encode())
        accountinfo = s1.recv(1024).decode()
        username, password = accountinfo.split(":")
        sql = "insert into userinfo values (%s,%s)"
        print(1)
        try:
            ret = cur.execute(sql,(username,password))
            print(ret)
            if ret:
                s1.send("注册成功！".encode())
                conn.commit()
            else:
                s1.send("注册失败！".encode())
        except:
            s1.send("输入有误，注册失败".encode())
    elif action == "登录":
        s1.send("请输入（用户名:密码）".encode())
        accountinfo = s1.recv(1024).decode()
        username, password = accountinfo.split(":")
        sql = "select * from userinfo where username = %s and password =%s"
        try:
            ret = cur.execute(sql, (username, password))
            if ret:
                s1.send("登录成功！".encode())
            else:
                s1.send("登录失败！".encode())
        except:
            s1.send("输入有误，登录失败".encode())
    else:
        s1.send("输入有误，请重新输入！".encode())

