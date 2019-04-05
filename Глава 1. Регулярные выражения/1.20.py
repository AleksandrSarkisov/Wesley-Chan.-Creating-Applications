#Извлечение полного адреса электронной почты из каждой строки.

import re

patt = "(\w+@\w+\.\w+)"
with open('redata.txt','r') as f:
    for i in f.readlines():
        if re.search(patt, i) is not None:
            print(re.search(patt, i).group(1))
