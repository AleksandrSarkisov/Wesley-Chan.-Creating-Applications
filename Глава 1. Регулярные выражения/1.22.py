#Извлечение только значений лет из отметок времени.

import re

patt = "(\d{4})"
with open('redata.txt','r') as f:
    for i in f.readlines():
        if(re.search(patt,i) is not None):
            print(re.search(patt,i).group(1))
