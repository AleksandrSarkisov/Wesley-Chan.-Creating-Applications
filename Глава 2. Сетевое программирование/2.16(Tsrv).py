#*Расшрение классов SocketServer. Когда мы рассматривали пример с кодом
#сервера ТСР на основе модуля SocketServer, нам пришлось внести изменения
#в код клиента, отличающие его от исходного базового клиента ТСР,
#поскольку класс SocketServer не поддерживает соединение между запросами.
#а) Создайте подклассы классов TCPServer и StreamRequestHandler и перепроектируйте
#сервер так, чтобы он сопровождал и использовал отдельное
#соединение для каждого клиента (а не создавал соединение для каждого
#запроса).
#б) Объедините свое решение предыдущего упражнения с решением для
#пункта (а) текущего упражнения, чтобы обеспечить параллельное обслуживание
#нескольких клиентов.

import socketserver, socket

class MyRequestHandler(socketserver.StreamRequestHandler):
    pass

class MyServer(socketserver.TCPServer):

    def get_request(self):
        request, client_address = self.socket.accept()
        if client_address not in client_address_list:
            client_address_list.update(client_address: request)
            return request, client_address
        else:
            return client_address_list[client_address], client_address
            
if __name__ == '__main__':
    client_address_list = dict()
    with Myserver(('', 9090), MyRequestHandler) as server:
        server.serve_forever()
