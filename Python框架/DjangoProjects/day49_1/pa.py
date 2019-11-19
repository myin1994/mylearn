import requests

ret = requests.post("http://127.0.0.1:8000/login/",data={"uname":"123","pwd":"123"})
print(ret.content.decode())