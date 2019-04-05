#Служба дневного времени. Используйте функцию socket.getservbyname(),
#чтобы определить номер порта для службы дневного времени, создаваемой
#с применением протокола UDP. Ознакомьтесь с документацией к функции
#getservbyname() для получения точных сведений о синтаксисе ее использования
#(т.е. выполните вызов socket.getservbyname.__doc__). После
#этого напишите приложение, которое отправляет фиктивное сообщение и
#ожидает ответа. Вслед за тем, как будет получен ответ от сервера, его необходимо
#отобразить на экране.

from socket import *
from datetime import time

HOST = ''
PORT = 12032
BUFSIZ = 1024

service = "daytime"
portNum = getservbyname(service, "udp")

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(BUFSIZ).decode()
            if not data: break
            conn.sendall("The port Number of {} service is {}".format(service, portNum).encode())
