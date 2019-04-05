#Извлечение только и мен входа и имен доменов (имени основного домена и
#имени домена высокого уровня) из адреса электронной почты.

import re

patt = "(\w+)@(\w+)\.(\w+)"
with open('redata.txt','r') as f:
    for i in f.readlines():
        if(re.search(patt,i) is not None):
            print(re.search(patt,i).groups())
