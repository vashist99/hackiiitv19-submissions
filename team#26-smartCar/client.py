import socket
import json
import _thread
import threading
# HOST = '10.42.0.1'
# PORT = 8005


def sends(s1):
    print("sending...")
    while 1:
        mess = str(input())
        s1.send(mess.encode('utf-8'))
        print('message sent')

def rec(s1):
    print("recieving...")
    while 1:
        data = s1.recv(1024)
        print(data.decode('utf-8'))



s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()
s.close()
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#gathering host IP:
ip2 = "0.1"
ip1 = ""
cnt = 0
for c in range(len(ip[0])):
    if ip[0][c] == '.':
        cnt += 1
    if cnt == 2:
        ip1 = ip[0][0:c+1]
        break
main_ip = ip1 + ip2
#print(main_ip)
s1.connect((main_ip, 8065))


#protocol
message = input()
m = message.encode('utf-8')
s1.sendall(m)
carData = s1.recv(1024)
#receiving driver list
data = json.loads(carData.decode('utf-8'))
print(data)


if s1:
    print("ok")
    t1 = threading.Thread(target= sends, args=(s1, ))
    t2 = threading.Thread(target=rec, args=(s1,))
    t1.start()
    t2.start()

# s1.close()