#Извлечение только значений времени (НН:ММ:SS) из отметок времени.

import re

patt = "(\d{2}:\d{2}:\d{2})"
with open('redata.txt','r') as f:
    for i in f.readlines():
        if(re.search(patt,i) is not None):
            print(re.search(patt,i).group(1))
