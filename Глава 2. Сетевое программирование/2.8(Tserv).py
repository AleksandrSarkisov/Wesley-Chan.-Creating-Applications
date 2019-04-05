#Дуплексная интерактивная переписка. Доработайте свое решение предыдущего
#упражнения таким образом, чтобы служба интерактивной переписки
#стала дуплексной; это означает, что в этой службе оба абонента моrут и передавать,
#и получать сообщения независимо друг от друга.

import socket, threading, time

def receive(name, sock):
    while True:
        try:
            data = sock.recv(1024)
            addr = socket.gethostbyname(socket.gethostname())
            if data != '': print(data.decode('utf-8'))
            time.sleep(0.2)
        except:
            pass

HOST, PORT = '', 9090

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)


    print("[ Server Up ]")

    conn, addr = server.accept()
    with conn:
        print("Connected by:", addr)
        recvThread = threading.Thread(target = receive, args = ('RecvThread', conn))
        recvThread.start()

        while True:
            message = input('')

            if message != '':
                conn.sendall(message.encode('utf-8'))
            time.sleep(0.2)
    recvThread.join()
