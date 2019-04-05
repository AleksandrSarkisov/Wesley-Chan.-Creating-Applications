import re

patt = "w{3}\.\w+\.\w+"
data = ["www.google.com", "www.yandex.ru", "www.yahoo.com", "www.foothil.edu"]

print(re.match(patt, data[3]).group())
