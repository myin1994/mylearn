from socket import *
server = socket()
server.bind(("",8001))
server.listen()
def html(path):
    if request_path == "day46":
        with open("home.html","rb") as f:
            return f.read()
    try:
        with open(path, "rb") as f:
            return f.read()
    except:
        print("没有",path)
        return b"no"
while True:
    conn, addr = server.accept()
    message_from_client = conn.recv(1024).decode()
    request_path = message_from_client.split(" ")[1].replace("/C:/Users/24479/Desktop/%E4%BD%9C%E4%B8%9A%E4%B8%8A%E4%BC%A0/Python%E6%A1%86%E6%9E%B6/","")
    # print(request_path)
    conn.send(b"HTTP/1.1 200 ok\r\n\r\n")
    data = html(request_path)
    conn.send(data)
    conn.close()
server.close()