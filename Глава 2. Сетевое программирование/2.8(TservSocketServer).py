#Дуплексная интерактивная переписка. Доработайте свое решение предыдущего
#упражнения таким образом, чтобы служба интерактивной переписки
#стала дуплексной; это означает, что в этой службе оба абонента моrут и передавать,
#и получать сообщения независимо друг от друга.


import socketserver, threading, time

def receive(name, sock):
    sock.recv = sock.rfile.readline().strip()
    print('{} :: [{}] :: Message => {}'.format(sock.client_address[0], time.ctime(), sock.recv.decode('utf-8')))

class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print('Client {} connection'.format(self.client_address[0]))
        recvThread = threading.Thread(target=receive, args=('RecvThread', self))
        recvThread.start()
        recvThread.join()
        while True:
            self.message = input('> ')
            self.wfile.write(self.message).encode('utf-8')
            
if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print("Server Up")
        server.serve_forever()
