from socket import *
from threading import *
import pymysql
from jinja2 import Template
import time
server = socket()
server.bind(("",8001))
server.listen()
def html(path):
    dic = {"name":"张三","hobby":[1,2,3,4]}
    current_time = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime())
    if path == "":
        with open("home.html","r",encoding="utf-8") as f:
            data = f.read()
            data = data.replace("%xxoo%",current_time)
            tem = Template(data)
            return tem.render(dic).encode()

    try:
        with open(path, "rb") as f:
            return f.read()
    except:
        print(path,"不存在,看看要不要添加")
        with open("404_页面不存在.html", "rb") as f:
            return f.read()

def judge(username,password):
    conn = pymysql.connect(host="127.0.0.1", user="root", password="77963333", database="day36")
    cur = conn.cursor()
    sql = "select * from userinfo where username = %s and password =%s"
    ret = cur.execute(sql, (username, password))
    if ret:
        return html("successpage.html")
    else:
        return html("failedpage.html")



def main(message_from_client,conn):
    if message_from_client == "":
        pass
    else:
        try:
            request_path = message_from_client.split(" ")[1].replace("/","")
            username = re.findall("username=(.*)&password",message_from_client)
            password = re.findall("&password=(.*)",message_from_client)
            if username and password:
                data = judge(username,password)
            else:
                data = html(request_path)
            conn.send(b"HTTP/1.1 200 ok\r\n\r\n")
            conn.send(data)
            conn.close()
        except Exception as e:
            print(e)
            pass
if __name__ == '__main__':
    import re
    while True:
        conn, addr = server.accept()
        message_from_client = conn.recv(1024).decode()
        t1 = Thread(target=main,args=(message_from_client,conn))
        t1.start()