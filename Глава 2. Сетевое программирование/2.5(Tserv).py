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
#Дополнительное задание. Сервер должен принимать команду ls dir и возвращать листинг файлов, полученный с помощью dir.

import socket
from time import ctime
from os import name, listdir, curdir
import re

HOST = ''
PORT = 50009
BUFSIZ = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by:', addr)
        while True:
            data = conn.recv(BUFSIZ).decode()
            if not data: break
            if data == 'date': conn.sendall(ctime().encode())
            if data == 'os': conn.sendall(name.encode())
            if data == 'ls': conn.sendall(str(listdir(curdir)).encode())
            if re.match('ls\s(\w+)', data) is not None: conn.sendall(str(listdir(re.match('ls\s(\w+)', data).group(1))).encode())
