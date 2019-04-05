#Извлечение полной отметки времени из каждой строки.

import re

patt = "\w{3}\s\w{3}\s{1,2}\d{1,2}\s(\d{2}:\d{2}:\d{2})"
with open("redata.txt", "r") as f:
    for i in f.readlines():
        if (re.match(patt,i) is not None):
            print(re.match(patt,i).group(1))
