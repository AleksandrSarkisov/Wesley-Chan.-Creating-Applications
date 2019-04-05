#Служба дневного времени. Используйте функцию socket.getservbyname(),
#чтобы определить номер порта для службы дневного времени, создаваемой
#с применением протокола UDP. Ознакомьтесь с документацией к функции
#getservbyname() для получения точных сведений о синтаксисе ее использования
#(т.е. выполните вызов socket.getservbyname.__doc__). После
#этого напишите приложение, которое отправляет фиктивное сообщение и
#ожидает ответа. Вслед за тем, как будет получен ответ от сервера, его необходимо
#отобразить на экране.

from socket import *

HOST = 'localhost'
PORT = 12032
BUFSIZ = 1024

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = "port number of daytime service"
    s.sendall(data.encode())
    data = s.recv(BUFSIZ).decode()
    print(data)
