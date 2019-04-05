#Сервер ждущего режима. Создайте сервер ждущего режима. Клиент отправляет
#запрос для перевода его в состояние ожидания на указанное количество
#секунд. Сервер выдает команду от имени клиента, затем возвращает
#клиенту сообщения, указывающее на успешное завершение. Клиент должен
#переходить в состояние ожидания или простаивать в точном соответствии
#с указанным временем. Это простая реализация удаленного вызова процедур,
#при котором запрос клиента вызывает команды на другом компьютере
#по сети.

import socketserver, time

class MyRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('Connection with {} success'.format(self.client_address[0]))
        self.data = self.request.recv(1024)
        print('Request receive')
        try:
            time.sleep(int(self.data.decode('utf-8')))
            self.request.sendall('OK'.encode('utf-8'))
            print('Request Success')
        except:
            self.request.sendall('Type of data not int'.encode('utf-8'))
            print('Request Wrong')

with socketserver.TCPServer(('', 9090), MyRequestHandler) as server:
    print('Server Run')
    server.serve_forever()
