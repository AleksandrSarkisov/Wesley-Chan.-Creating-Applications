#Извлечение только значений месяцев из отметок времени.

import re

patt = "(\s\w{3})"
with open('redata.txt','r') as f:
    for i in f.readlines():
        if(re.search(patt,i) is not None):
            print(re.search(patt,i).group(1))
