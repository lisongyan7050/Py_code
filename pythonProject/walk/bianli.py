import os

print(list(os.walk(r'C:\Users\10756\Documents\pythonProject')))
for foldername,subfolders, filenames in os.walk(r'C:\Users\10756\Documents\pythonProject'):
    print("当前文件夹是"+ foldername)
    for subfolder in subfolders:
        print(subfolder)
    for filename in filenames:
        print("这里面的文件有"+filename)