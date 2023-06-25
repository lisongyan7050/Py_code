import os,re
import shutil

path=input('输入 路径')

#print(os.listdir(r''+path))# 秒

# 建立正则表达式
regex=re.compile('''^(.*?)#匹配日期前面的任意字符
                    ((0|1)?\d)-# 匹配 月份
                    ((0|1|2|3)?\d)- # 匹配 日期
                    ((19|20)\d\d)# 匹配 19几几年,到 20几几年
                    (.*?)$ # 匹配 日期后面所有 字符
                    ''',re.VERBOSE)

for filename in os.listdir(r''+path):

    newname = ''
    result=regex.search(filename)
    if result!=None:
        newname=result.group(1)+result.group(4)+'-'+result.group(2)+'-'+result.group(6)+result.group(8)
        print(os.path.join(path, newname))
        shutil.move(os.path.join(path,filename),os.path.join(path,newname))