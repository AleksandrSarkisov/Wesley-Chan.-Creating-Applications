#Клиенты. Внесите изменения в клиентские програм м ы для ТСР (tsTclnt .
#ру) и UDP (tsUclnt . ру), чтобы имя сервера не было жестко задано в приложении.
#Предоставьте возможность пользователю указывать имя хоста и
#номер порта и используйте значения по умолчанию, только если не заданы
#один или оба параметра.

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpServSock = socket(AF_INET, SOCK_STREAM)
tcpServSock.bind(ADDR)
tcpServSock.listen(5)

while True:
    print('Waiting for connection...')
    tcpCliSock, addr = tcpServSock.accept()
    print('...connected from', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()
        if not data:
            break
        tcpCliSock.send('[{0}] {1}'.format(ctime(), data).encode())
    tcpCliSock.close()
tcpSerSock.close()
