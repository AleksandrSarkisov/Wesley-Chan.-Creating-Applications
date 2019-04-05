#Многопользовательская дуплексная интерактивная переписка. Внесите дополнительные
#обновления в свое решение, чтобы служба интерактивной переписки
#стала многопользовательской.

import socket, threading, time

HOST, PORT = '', 9090
clients = []

def receive(name, clntAddr, sock):
    while True:
        try:
            recvMessage = sock.recv(1024).decode('utf-8')
            if recvMessage != '':
                print('[{}] :: {}  message => {}'.format(time.ctime(), clntAddr, recvMessage))
                for client in clients:
                    if client != sock:
                        client.sendall(recvMessage.encode('utf-8'))
        except:
            print('Client {} disconnect'.format(clntAddr))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    print('Server UP')
    server.listen(5)
    while True:
        clnt, addr = server.accept()
        print('Client {} connect'.format(addr))
        if clnt not in clients: clients.append(clnt)
        clntThread = threading.Thread(target=receive, args=('ClientThread', addr, clnt))
        clntThread.start()
    clntThread.join()
