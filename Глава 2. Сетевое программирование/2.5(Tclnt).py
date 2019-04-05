#Организация сетей и сокеты. Реализуйте примеры програм м клиентов и
#серверов ТСР, приведенные в документации справочного руководства по
#библиотеке Python для модуля socket, и заставьте их работать. Установите
#сервер, а затем клиент. По следующему адресу можно также получить готовую версию этого исходного кода:
#http://docs.python.org/library/socket#example
#ы нашли, что наш сервер слишком примитивен. Внесите изменения в программу
#сервера так, чтобы он мог выполнять гораздо больше действий, в частности, распознавал следующие команды:
#date. Сервер возвращает свою текущую отметку даты/времени, т.е. результат вызова time.ctirne().
#os. Получение информации об операционной системе (os . name).
#ls. Получение л и стинга текущего каталога . (Подсказка. Вызов
#os.listdir() обеспечи вает получение листинга каталога, а os.curdir возвращает текущий каталог.)
#Дополнительное задание. Сервер должен прини мать команду ls dir и возвращать листинг файлов, полученный с помощью dir.

import socket

HOST = '127.0.0.1'
PORT = 50009
BUFSIZ = 1024
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = input('> ')
        if not data: break
        s.sendall(data.encode())
        data = s.recv(BUFSIZ).decode()
        print('Received\n', data)
