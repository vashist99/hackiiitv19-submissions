import socket

# HOST = '10.42.0.1'
# PORT = 8005

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()
s.close()
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
s1.connect(('127.0.0.1', 8055))

message = input()
m = message.encode('utf-8')
s1.sendall(m)
s1.close()