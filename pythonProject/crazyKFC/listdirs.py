import re,os
path=input("请输入路径")
listfile=os.listdir(path)
text=''
for x in len(listfile):
    # 判断当前名字是不是一个文件, 并且 判断后缀是不是 txt
    if os.path.isfile(os.path.join(path,listfile[x])) and os.path.splitext(listfile[x])[1]=='.txt':
        with open(os.path.join(path,listfile[x]),'r') as f:
            text+=f.read()

regex=re.compile(r'\d+')# 匹配里面任意长度的数字
result=regex.findall(text)
print(result)
