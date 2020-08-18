import time
import datetime
import os
now = datetime.datetime.now()
print(now)
print(type(now))

for day in range(5,0,-1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))

day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))
'''
while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)
'''
ret = os.getcwd()
print(ret, type(ret))


import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)