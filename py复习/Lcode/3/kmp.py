import time

input('回车')
print("开始")
starttime = time.time()
lastTime = starttime  # 上一次点击的时间

lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)  # 计算出 距离上一次点击的时间间隔
        time.sleep(100000)
        totaltime = round(time.time() - starttime, 2)  # 当前用的总时间
        print('lap#%s:%s (%s)' % (lapNum, totaltime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    pass

print('完成')