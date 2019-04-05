#Извлечение значений месяцев, дней и лет из отметок времени и вывод их
#в формате "месяц, число, год", лишь с однократной итерацией по каждой
#строке.

import re

patt = "(\w+)\s+(\d{1,2})\s+[\w:]+\s(\d{4})"
with open('redata.txt','r') as f:
    for i in f.readlines():
        if(re.search(patt,i) is not None):
            print(re.search(patt,i).groups())
