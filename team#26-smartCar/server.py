import socket
import threading
import sys
import json


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '10.42.0.1'
PORT = 8065

# s.bind((HOST,PORT))
# s.listen(5)


def sends(conn):
    mess = str(input())
    conn.send(mess.encode('utf-8'))
    print('message sent')

def rec(conn):
    while 1:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        carNo = data[:len(data)-1]
        print(data)
        mess = data[-1:]
        if carNo in d1.keys():
            print(carNo)
            d[d1[carNo]].send(mess.encode('utf-8'))
        else:
            print(mess.encode('utf-8'))
        if not data:
            break
    
    conn.close()

d1 = {}
def clientThread(conn,addr):
    #receives car no
    no = conn.recv(1024)
    d1.update({no.decode('utf-8'):addr[0]})
    carData = json.dumps(d1)
    conn.send(carData.encode('utf-8'))
    print(carData)
    #while 1:
    t2 = threading.Thread(target = sends,args=(conn,))
    t3 = threading.Thread(target = rec,args = (conn,))
    t2.start()
    t3.start()

d = {}
s.bind((HOST,PORT))
s.listen(5)
while 1:
    # s.bind((HOST,PORT))
    # s.listen(5)
    c,addr = s.accept()
    
    #write code to create thread to connect
    t1 = threading.Thread(target = clientThread,args = (c,addr))
    t1.start()
    d.update({addr[0]:c})
    
    #mess = c.recv(1024)
    #string = mess.decode('utf-8')
    #print(string)
    #mess = str(input())
    #c.send(mess.encode('utf-8'))
    #c.close()



#c.close()
