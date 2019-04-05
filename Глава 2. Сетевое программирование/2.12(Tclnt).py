#Сервер ждущего режима. Создайте сервер ждущего режима. Клиент отправляет
#запрос для перевода его в состояние ожидания на указанное количество
#секунд. Сервер выдает команду от имени клиента, затем возвращает
#клиенту сообщения, указывающее на успешное завершение. Клиент должен
#переходить в состояние ожидания или простаивать в точном соответствии
#с указанным временем. Это простая реализация удаленного вызова процедур,
#при котором запрос клиента вызывает команды на другом компьютере
#по сети.

import socket, time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
        client.connect(('localhost', 9090))
        print('Connection success')
        data = input('> ')
        client.send(data.encode('utf-8'))
        time.sleep(int(data))
        print(client.recv(1024).decode('utf-8'))
    except:
        print('Connection unavailable')
