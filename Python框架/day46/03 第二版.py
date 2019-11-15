from socket import *
server = socket()
server.bind(("",8001))
server.listen()
while True:
    conn, addr = server.accept()
    message_from_client = conn.recv(1024).decode()
    request_path = message_from_client.split(" ")[1].replace("/","")
    print(request_path)
    conn.send(b"HTTP/1.1 200 ok\r\n\r\n")
    if request_path == "":
        with open("home.html","rb") as f:
            data = f.read()
        conn.send(data)
        conn.close()
    if request_path == "home.css":
        with open("home.css","rb") as f:
            data = f.read()
        conn.send(data)
        conn.close()
    if request_path == "home.js":
        with open("home.js","rb") as f:
            data = f.read()
        conn.send(data)
        conn.close()
server.close()