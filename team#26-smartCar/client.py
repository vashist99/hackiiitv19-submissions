import socket

HOST = '10.42.0.1'
PORT = 8005

#while 1:
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
message = input()
m = message.encode('utf-8')
s.sendall(m)
# v = s.recv(1024)
# print(v.decode('utf-8'))
s.close()