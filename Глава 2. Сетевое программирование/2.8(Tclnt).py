#Дуплексная интерактивная переписка. Доработайте свое решение предыдущего
#упражнения таким образом, чтобы служба интерактивной переписки
#стала дуплексной; это означает, что в этой службе оба абонента моrут и передавать,
#и получать сообщения независимо друг от друга.

import socket, threading, time

def receiving(name, sock):
    while True:
        try:
            while True:
                data = sock.recv(1024)
                addr = socket.gethostbyname(socket.gethostname())
                if data != '': print(data.decode('utf-8'))
                time.sleep(0.2)
        except:
            pass

HOST, PORT = 'localhost', 9090

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))
    print('Connected')

    recvThread = threading.Thread(target = receiving, args = ("RecvThread", s))
    recvThread.start()
    while True:
        message = input('')
        if message != '':
            s.sendall(message.encode('utf-8'))
        time.sleep(0.2)
    recvThread.join()
