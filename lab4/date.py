# Exercise 1
from datetime import date, timedelta

subtract = date.today() - timedelta(5)

print(subtract)

# Exercise 2

from datetime import date, timedelta

today = date.today()
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)

print(tomorrow)
print(today)
print(yesterday)

# Exersice 3

import datetime
date = datetime.datetime.today().replace(microsecond=0)
print(date)

# Exercise 4

from datetime import datetime as d

def Dif_Time(dt2,dt1):

    delta_time = dt2 - dt1

    return delta_time.days * 24 * 3600 + delta_time.seconds


data1 = d.strptime('2022-11-14 14:32:30','%Y-%m-%d %H:%M:%S')

data2 = d.now()

print(Dif_Time(data2,data1))

