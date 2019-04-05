#Замена адреса электронной почты в каждой строке данных произвольно выбранным
#адресом электронной почты

import re
from string import ascii_lowercase
from random import choice

tldc = ['com', 'ru', 'edu', 'org', 'net', 'io', 'gov']

patt = "(\w+@\w+\.\w+)"
with open('redata.txt','r') as f:
    with open('1.26_redata.txt','w') as n_f:
        for i in f.readlines():
            if(re.search(patt,i) is not None):
                n_log = ''.join(choice(ascii_lowercase) for i in range(10))
                n_dom = ''.join(choice(ascii_lowercase) for i in range(15))

                n_f.write(re.sub(patt, "{0}@{1}.{2}".format(n_log, n_dom, choice(tldc)), i))
