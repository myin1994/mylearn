# Djongo
from socket import *
server = socket()
server.bind(("",8001))
server.listen()
while True:
    conn, addr = server.accept()

    message_from_client = conn.recv(1024)
    print(message_from_client.decode())
    print(message_from_client)
    conn.send(b"HTTP/1.1 200 ok\r\n")
    conn.send(b"charset:gbk\r\n\r\n")
    with open("login.html","rb") as f:
        data = f.read()
    conn.send(data)
    conn.send(b"success!")
    conn.close()
server.close()

