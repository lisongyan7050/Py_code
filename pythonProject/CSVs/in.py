import csv
file=open('examply.csv','a',newline='')
mywriter=csv.writer(file)
mywriter.writerow([1,2,3,4,5,6])