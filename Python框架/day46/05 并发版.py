from socket import *
from threading import *
server = socket()
server.bind(("",8001))
server.listen()
def html(path):
    if path == "":
        with open("home.html","rb") as f:
            return f.read()
    try:
        with open(path, "rb") as f:
            return f.read()
    except:
        print("没有", path)
        return b"no exit"
def func(message_from_client,conn):
    request_path = message_from_client.split(" ")[1].replace("/","")
    conn.send(b"HTTP/1.1 200 ok\r\n\r\n")
    data = html(request_path)
    conn.send(data)
    conn.close()
if __name__ == '__main__':
    while True:
        conn, addr = server.accept()
        message_from_client = conn.recv(1024).decode()
        t1 = Thread(target=func,args=(message_from_client,conn))
        t1.start()