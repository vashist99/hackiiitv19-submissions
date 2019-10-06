import socket
import json
import _thread
# HOST = '10.42.0.1'
# PORT = 8005

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
s1.connect((main_ip, 8055))


def send(s):
    while 1:
        mess = input()
        s.send(mess.encode('utf-8'))
        print('message sent')

def rec(s):
    while 1:
        data = s.recv(1024)
        print(data.decode('utf-8'))


#protocol
message = input()
m = message.encode('utf-8')
s1.sendall(m)
carData = s1.recv(1024)
#receiving driver list
data = json.loads(carData.decode('utf-8'))
print(data)

_thread.start_new_thread(send,(s,))
_thread.start_new_thread(rec,(s,))

s1.close()