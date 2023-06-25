import os,shutil
"""把 jpg和png结尾的文件移动到其他目录下"""
path=input('输入目录')
for foldercurrent,subfolders, filenames in os.walk(r''+path):
    # print(filename)
    print("当前文件夹是"+ foldercurrent)
    for sub in subfolders:
        print("包含的子文件夹有"+sub)
    for name in filenames:
        if name.endswith('.jpg') or name.endswith('.png'):
            #print(os.path.join(foldercurrent,name))
            shutil.move(os.path.join(foldercurrent,name),r"C:\Users\10756\Desktop\to")

