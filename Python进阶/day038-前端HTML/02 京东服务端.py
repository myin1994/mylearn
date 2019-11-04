from socket import *

jd_server = socket()

jd_server.bind(("",8989))
jd_server.listen(5)
conn,client_addr = jd_server.accept()

from_clinent_msg = conn.recv(1024).decode()

print(from_clinent_msg)
conn.send("HTTP1.1 200 OK\r\n\r\n".encode())
# conn.send("<h1>hahaha</h1>".encode())

with open("01test.html","rb") as f:
    data = f.read()
conn.send(data)

conn.close()
jd_server.close()