import os
path=r'C:\Users\10756\Documents\pythonProject\web\漫画'
filelist=os.listdir(r''+path)
for file in filelist:
    if os.path.isfile(os.path.join(path,file)):
        os.unlink(os.path.join(path,file))