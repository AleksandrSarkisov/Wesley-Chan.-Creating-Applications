#Дуплексная интерактивная переписка. Доработайте свое решение предыдущего
#упражнения таким образом, чтобы служба интерактивной переписки
#стала дуплексной; это означает, что в этой службе оба абонента моrут и передавать,
#и получать сообщения независимо друг от друга.

from socket import *
import threading

HOST = 'localhost'
PORT = 9999

def receive(name, sock):
    while True:
        data = sock.recv(1024).decode('utf-8')
        if data != '': print('Server response: {}'.format(data))

while True:
    data = input('')
    if not data: break
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print('Connection success')
        s.sendall(data.encode())
        recvThread = threading.Thread(target=receive, args=('RecvThread', s))
        recvThread.start()
        recvThread.join()
