#Обеспечить сопоставление с множеством строковых представлений всех чисел с плавающей точкой, поддерживаемых языком Python.

import re

patt = "\d+\.\d+"
data = ["23.123", "2.3", "3.14"]

for i in data:
    print(re.match(patt, i).group())
