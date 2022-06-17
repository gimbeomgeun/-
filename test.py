import socket
import time
host=""
port=4444
BUF=4096
s=socket.socket()
s.bind((host,port))
s.listen(1)

conn,adress=s.accept()

while(1):
    text=input()
    t=time.time()
    tm=time.localtime(t)
    conn.send(text)
    data=conn.recv(BUF).decode('utf-8')
    print(data)
