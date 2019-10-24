from socketserver import *
class Mysever(BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            print("-->",data.decode())
            self.request.send(data.decode().upp().encode)
TCPServer.allow_reuse_address = True
sever = ThreadingTCPServer(("192.168.34.170",7878),Mysever)
sever.serve_forever()