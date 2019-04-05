# Обеспечить сопоставление с любой парой слов, разделенной одним пробелом, такой как имя и фамилия.

import re

patt = "[A-Za-z]+ [A-Za-z]+"
data = '''Jade Jones
        John Jones
        Alex Perol'''

print(re.findall(patt,data))
