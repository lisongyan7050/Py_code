import datetime,time
today=datetime.datetime.now()
print(today.year)

print(today.time())

print(time.time())
print(datetime.datetime.fromtimestamp(time.time()))
