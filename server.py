from socket import *

s = socket(AF_INET,SOCK_STREAM)
print('socket 생성')

s.bind(("localhost",7777))
s.listen(5)
print('서버가 연결을 기다리고 있습니다.')

while True:
    csock,addr = s.accept()
    text = csock.recv(512).decode() 
    print('메세지',addr,text)
    csock.send(bytes('메세지가 성공적으로 전송되었습니다','utf-8'))
