#Полудуплексная интерактивная переписка. Создайте простую, полудуплексную
#программу интерактивной переписки. Под полудуплексной подразумевается
#то, что после создания соединения и начала работы службы только
#один из участников переписки может вводить свое сообщение. Другой
#участник должен ожидать поступления сообщения, поскольку лишь после
#этого перед ним появится приглашение к вводу сообщения. После отправки
#сообщения отправитель должен ожидать ответа для получения возможности
#отправить следующее сообщение. Один из участников будет находиться
#на стороне сервера, а второй - на стороне клиента.


import socketserver

class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            self.data = self.rfile.readline().strip()
            print('{} wrote:'.format(self.client_address[0]))
            print(self.data)
            self.receive = input()
            self.wfile.write(bytes(self.receive, 'utf-8'))

if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
