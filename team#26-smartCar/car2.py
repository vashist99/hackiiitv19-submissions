import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 8000

s.connect((HOST,PORT))
message = 'hello'
m = message.encode('utf-8')
s.send(m)
s.close()