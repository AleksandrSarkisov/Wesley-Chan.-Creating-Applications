#Убедитесь в том, что данные в файле redata.txt строго соответствуют форма
#ту, путем проверки совпадения первой цифры целочисленного поля с
#отметкой времени, заданной в начале каждой выходной строки.

import re

patt = "[\w.]+\s+[\w.]+\s+[\d.]+ ([0-2])"
flag = True

with open("redata.txt", "r") as f:
    for i in f.readlines():
        print(re.match(patt,i))
        if re.match(patt,i) == None:
            flag = False

print(flag)
