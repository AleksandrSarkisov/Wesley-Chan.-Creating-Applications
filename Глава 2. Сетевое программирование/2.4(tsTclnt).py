#Клиенты. Внесите изменения в клиентские програм м ы для ТСР (tsTclnt .
#ру) и UDP (tsUclnt . ру), чтобы имя сервера не было жестко задано в приложении.
#Предоставьте возможность пользователю указывать имя хоста и
#номер порта и используйте значения по умолчанию, только если не заданы
#один или оба параметра.

from socket import *
import re

HOST = input("Enter host\n")
PORT = int(input("Enter port\n"))
BUFSIZ = 1024

if not HOST or re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',HOST) is not None:
    HOST = 'localhost'
if not PORT:
    PORT = 21567

ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)
tcpCliSock.close()
