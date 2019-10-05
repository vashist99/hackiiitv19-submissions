import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '10.42.0.1'
HOST1 = '10.42.0.243'
PORT = 8005

s.bind((HOST,PORT))
s.listen(5)



while 1:
    c,addr = s.accept()
    mess = c.recv(1024)
    string = mess.decode('utf-8')
    print(string)
    mess = str(input())
    c.send(mess.encode('utf-8'))
    c.close()



#c.close()
