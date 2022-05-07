from socket import *

while True:
    csock = socket(AF_INET,SOCK_STREAM)
    csock.connect(("localhost",7777))
    
    text = input('>>')
    if len(text) < 1:
        text = ' '
    csock.send(bytes(text, 'utf-8'))
    print(csock.recv(512).decode()) 