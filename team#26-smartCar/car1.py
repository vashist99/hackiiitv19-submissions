import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = '10.42.0.1'
PORT = 8000

s.bind((HOST,PORT))
s.listen(5)

c,addr = s.accept()

mess = c.recv(1024)

string = mess.decode('utf-8')
print(sting)
c.close()
