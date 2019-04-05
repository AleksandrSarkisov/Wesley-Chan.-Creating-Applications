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

import socket, threading, time

HOST, PORT = '127.0.0.1', 45557
description = 'I am waiting mode server. I listening {}-{}. I call time.sleep() function on the host.'.format(HOST, PORT)

def sleepClnt(name, sock):
    try:
        while True:
            recvTime = sock.recv(1024).decode('utf-8')
            print('{} :: Ухожу в сон на {} секунды'.format(name, recvTime))
            time.sleep(int(recvTime))
            print('Function done')
            sock.sendall('Function done'.encode('utf-8'))
        sock.close()
    except:
        print('Client disconnect')

def clientSocket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
        try:
            c.connect(('localhost', 5050))
            print('Connect with Name Server done')
            c.sendall(description.encode('utf-8'))
            try:
                print(c.recv(1024).decode('utf-8'))
                print('Coonection with Name Server success')
            except:
                print('Connection with Name Server denide')
        except:
            print('Name Server not access')

def serverSocket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
            s.listen()
            print('Server run')
            while True:
                clnt, addr = s.accept()
                print('Connect with {}'.format(addr))
                clntThread = threading.Thread(target=sleepClnt, args=('sleepClnt', clnt))
                clntThread.start()
        except:
            print('This PORT are already in use')

if __name__ == '__main__':
    nameServer = threading.Thread(target=clientSocket)
    sleepServer = threading.Thread(target=serverSocket)
    nameServer.start()
    sleepServer.start()
