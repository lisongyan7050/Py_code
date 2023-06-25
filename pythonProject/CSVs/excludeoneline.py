import os,csv
"""总的来说，该程序必须做到以下几点：

找出当前工作目录中的所有CSV文件。
读取每个文件的全部内容。
跳过第一行，将内容写入一个新的CSV文件。"""

# C:\Users\10756\Documents\pythonProject\CSVs



path = input("输入路径")# 改变当前工作环境到.
os.chdir(path)
os.makedirs('headerRemoved',exist_ok=True)

for filename in os.listdir():# 获取当前 工作环境的下的所有文件并返回一个列表
    if not filename.endswith('csv'):
        continue
    print('移除第一行从: '+filename)

    bufferdata=[]
    # 读取这个csv
    file=open(os.path.join(path,filename))
    csvob=csv.reader(file)
    for row in csvob:
        if csvob.line_num==1:
            continue
        bufferdata.append(row)
    file.close()
    # 写入 csv
    filecopy=open(os.path.join(path,'headerRemoved',filename),'w',newline='')
    mywriter=csv.writer(filecopy)

    for row in bufferdata:
        mywriter.writerow(row)
    filecopy.close()