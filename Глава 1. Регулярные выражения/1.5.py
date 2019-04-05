import re

patt = "[\d\w\s-]+[, \d]*"
data  = ["2-nd Kombaynovskaya, 42", "3120 De la Cruz Boulevard"]
print(re.match(patt, data[1]).group())
