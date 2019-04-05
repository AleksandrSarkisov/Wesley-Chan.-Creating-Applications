#Сервер имен. Спроектируйте и реализуйте сервер имен. Такой сервер отвечает
#за сопровождение базы данных с парами значений "имя хоста-номер порта",
#к которым могут прилагаться строковые описания служб, предоставляемых
#соответствующими серверами. Возьмите за основу один или
#несколько существующих серверов и обеспечьте регистрацию их служб в
#подготовленном вами сервере имен. (Обратите внимание на то, что в данном
#случае эти серверы становятся клиентами сервера имен.)
#Каждый запускаемый клиент не имеет сведений о том, где находится его
#искомый сервер. Эти клиенты, будучи также клиентами сервера имен,
#должны отправлять запрос на сервер имен с указанием того, какого рода
#обслуживание им требуется. Сервер имен в ответ возвращает клиенту пару
#значений "имя хоста-номер порта", чтобы клиент мог затем подключиться
#к соответствующему серверу для обработки своего запроса.
#Дополнительные задания
#1) Предусмотрите на сервере имен кеширование для ускорения формирования
#ответов на часто встречающиеся запросы.
#2) Обеспечьте возможность ведения журналов на сервере имен, чтобы можно
#было следить за тем, какие серверы зарегистрированы и какие службы
#запрашиваются клиентами.
#3) Сервер имен должен периодически выполнять эхо-тестирование зарегистрированных
#хостов по их соответствующим номерам портов для проверки
#того, что данная служба действительно работает. В случае неоднократных
#неудачных проверок сервер должен быть исключен из списка служб.
#Можно реализовать реальные службы на серверах, которые регистрируются
#в службе имен, или просто использовать фиктивные серверы (лишь подтверждающие
#получение запросов).

import socketserver, re, time, threading, os

HOST, PORT, servers = '', 5050, []              #ХОСТ, ПОРТ, Список всех серверов
cash = []                                       #Кэш серверов

try:
    os.remove('Server.log')                #Удаление файла, содержащего информацию о зарегистрированных серверах
    os.remove('Client.log')                #Удаление файла, содержащего информацию о службах, запрашиваемых клиентами
except:
    pass

class Service:
    # Класс описывающий сервер

    def __init__(self, serviceName, ip, port, description=''):
        self.serviceName = serviceName
        self.ip = ip
        self.port = port
        self.count = 0
        self.description = description

    def add(self):
        self.count += 1

def count(service):                             #Функция для sorted()
    return service.count

class RequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).decode('utf-8')
        if re.search('I am (\w*\s*\w*) server', self.data):
            print('{} connect'.format(re.search('I am (\w*\s*\w* server)', self.data).group(1)))
            self.service = Service(re.search('I am (\w*\s*\w* server)', self.data).group(1), re.search('((\d{1,3}.?){4})-(\d{1,5})', self.data).group(1), re.search('((\d{1,3}.?){4})-(\d{1,5})', self.data).group(3), re.search('-\d{1,5}. (.*)', self.data).group(1))
            if self.service.serviceName not in [i.serviceName for i in servers]:
                servers.append(self.service)                                    #Добавляем в список servers, если его там нет
                with open('Server.log', 'a') as serverLog:               #Добавляем запись о сервере в файле, если ее там нет
                    serverLog.write('Registretion service :: {} :: {}-{} :: {} :: {}\n'.format(time.ctime(), self.service.ip, self.service.port, self.service.serviceName, self.service.description))
        else:
            print('[{}] :: Client {} connect. {}'.format(time.ctime(), self.client_address, self.data))
            self.cash = sorted(servers, key=count, reverse=True)                #Кэшируем список servers
            self.listCashServiceName = [i.serviceName for i in self.cash]
            if self.data in self.listCashServiceName:                           #Поиск запрошенный сервис в кэше
                i = self.listCashServiceName.index(self.data)
                self.sendMessage = self.cash[i].ip + '-' + str(self.cash[i].port)
                print('Send Message => {}'.format(self.sendMessage))
                self.cash[i].add()
                self.request.sendall(self.sendMessage.encode('utf-8'))
            else:                                                               #Поиск запрошенный сервис в списке серверов
                self.listServersServiceName = [i.serviceName for i in servers]
                if self.data in self.listServersServiceName:
                    i = self.listServersServiceName.index(self.data)
                    self.sendMessage = servers[i].ip + '-' + str(servers[i].port)
                    self.request.sendall(self.sendMessage.encode('utf-8'))
                else:
                    self.request.sendall('None server not found'.encode('utf-8'))
            print(self.listCashServiceName)

if __name__ == '__main__':
    with socketserver.ThreadingTCPServer((HOST, PORT), RequestHandler) as server:
        print('nameServer run')
        server.serve_forever()
