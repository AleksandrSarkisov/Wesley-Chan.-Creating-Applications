#Обеспечить сопоставление с множеством всех допустимых адресов веб-сайта
#(URL) (начните с наименее ограничительного реrулярного выражения, а
#затем попытайтесь сделать его настолько строгим, насколько сможете, но
#все еще предоставляющим требуемые функциональные возможности).

import re

patt = "https://(\w+)\.(ru|com|edu|io)(/\w*)*"
data = ["https://google.com", "https://yandex.ru/job", "https://sfedu.ru"]

for i in data:
    print(re.match(patt,i).group())
