#Распознать следующие строки: "bat", "Ьit ", "but", "hat", "hit" или "hut".

import re

patt = "([bh][aiu]t)"
data = "bat, bit, but, hat, hit, hut"

print(re.findall(patt, data))
