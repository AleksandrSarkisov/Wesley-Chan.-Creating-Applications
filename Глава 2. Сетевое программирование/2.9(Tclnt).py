#Многопользовательская дуплексная интерактивная переписка. Внесите дополнительные
#обновления в свое решение, чтобы служба интерактивной переписки
#стала многопользовательской.

import socket, threading

HOST, PORT = 'localhost', 9090

def receive(name, sock):
    while True:
        try:
            receive = sock.recv(1024).decode('utf-8')
            if receive != '':
                print('{} => {}'.format(sock.getpeername(), receive))
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        recvThread = threading.Thread(target=receive, args=('RecvThread', s))
        recvThread.start()
        while True:
            try:
                data = input()
                if data != '':
                    s.sendall(bytes(data + '\n', 'utf-8'))
            except:
                print('Client socket close')
                break
    except:
        print('Connection down')
        exit(0)
