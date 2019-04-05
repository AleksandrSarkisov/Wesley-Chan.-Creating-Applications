#Определите, сколько раз каждый день недели поя вляется во вновь созданном
#файле redata . txt после каждого вызова сценария. (Еще одна проверка
#может состоять в подсчете того, сколько раз был случайным образом выбран
#каждый месяц года.)

import re

days = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
months = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"
days_count = {'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0, 'Sun': 0}
months_count = {'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'May': 0, 'Jun': 0, 'Jul': 0, 'Aug': 0, 'Sep': 0, 'Oct': 0, 'Nov': 0, 'Dec': 0}

with open("redata.txt","r") as f:
    for i in f.readlines():

        print(i)
        day = re.search(days, i).group()
        month = re.search(months, i).group()

        if day is not None:
            days_count[day] += 1

        if month is not None:
            months_count[month] += 1

print(days_count, "\n", months_count)
