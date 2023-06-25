import csv
file=open('examply.csv')
csvob=csv.reader(file)
for row in csvob:
    print(csvob.line_num)# line_num 就是获取当前读取的行数