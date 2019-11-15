# Djongo
from socket import *
server = socket()
server.bind(("",8001))
server.listen()
conn, addr = server.accept()

message_from_client = conn.recv(1024)
print(message_from_client.decode())
conn.send(b"HTTP/1.1 200 ok\r\n\r\n")

with open("home.html","rb") as f:
    data = f.read()
conn.send(data)
conn.close()
server.close()