import datetime

today=datetime.datetime.now()
print(today.time())
extra=datetime.timedelta(days=1000,minutes=9,seconds=8)
newday=today+extra
print(newday)

print(extra.seconds)

print(newday>today)