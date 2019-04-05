#Обеспечить сопоставление с множеством всех допустимых адресов электронной почты
#(начните с наименее ограничительного реrулярного выражения,
#а затем попьrrайтесь сделать его настолько строгим, насколько сможете,
#но все еще предоставляющим требуемые функциональные возможности).

import re

dnsMail = ["mail", "gmail", "rambler", "yandex", "yahoo", "xcorp"]
rigMail = ["ru", "com", "edu", "su"]
data = ["sark1996@mail.ru", "u1114@xcorp.su", "sevostyanova_F@yahoo.com", "12ewq@mail.ru"]

for i in data:
    print(re.match("\w+@({0})\.({1})".format("|".join(dnsMail), "|".join(rigMail)), i).group())
