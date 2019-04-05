#Обновите код сценария gendata . py так, чтобы данные записывались непосредственно
#в файл reda ta . txt, а не выводились на экран.

from sys import maxsize
from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime

tlds = ['com', 'edu', 'net', 'org', 'gov']
with open("redata.txt", "w") as f:
    for i in range(randrange(5,11)):
        dtint = randrange(int(maxsize*0.000000001)) # Выборка даты
        dtstr = ctime(dtint) # Строка даты
        llen = randrange(4,8) # Имя входа короче
        login = ''.join(choice(lc) for i in range(llen))
        dlen = randrange(llen, 13) # Имя домена длинее
        dom = ''.join(choice(lc) for i in range(dlen))
        f.write('{0}::{1}@{2}.{3}::{4}-{5}-{6}\n'.format(dtstr, login, dom, choice(tlds),dtint,llen,dlen))
