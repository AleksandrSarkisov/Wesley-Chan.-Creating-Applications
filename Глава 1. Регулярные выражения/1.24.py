#Извлечение только имен входа и имен доменов (и имени основного доме-
#на, и имени домена высокого уровня вместе взятых) из адреса электронной почты.

import re

patt = "(\w+)@(\w+\.\w+)"
with open('redata.txt','r') as f:
    for i in f.readlines():
        if(re.search(patt,i) is not None):
            print(re.search(patt,i).groups())
