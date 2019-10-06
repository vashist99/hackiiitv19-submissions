import socket
import _thread
import sys
import json


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 8055

# s.bind((HOST,PORT))
# s.listen(5)


def send(conn):
    conn.send(b'mess')
    print('message sent')

def rec(conn):
    while 1:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        carNo = data[:len(data)-1]
        mess = data[-1:]
        d[d1[carNo]].send(mess.encode('utf-8'))
        if not data:
            break
    
    conn.close()

d1 = {}
def clientThread(conn,addr):
    #receives car no
    no = conn.recv(1024)
    d1.update({no:addr})
    carData = json.dumps(d1)
    conn.send(carData.encode('utf-8'))
    #while 1:
    _thread.start_new_thread(send,(conn,))
    _thread.start_new_thread(rec,(conn,))

d = {}
while 1:
    s.bind((HOST,PORT))
    s.listen(5)
    c,addr = s.accept()
    
    #write code to create thread to connect
    _thread.start_new_thread(clientThread,(c,addr))
    d.update({addr[0]:c})
    #mess = c.recv(1024)
    #string = mess.decode('utf-8')
    #print(string)
    #mess = str(input())
    #c.send(mess.encode('utf-8'))
    #c.close()



#c.close()
