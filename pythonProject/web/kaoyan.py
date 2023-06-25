import os,requests,bs4

x=1
"""下载漫画"""
url='https://www.at0566.com/chapter/270'
res=requests.get(url)


soup=bs4.BeautifulSoup(res.text)
elems=soup.select('.clearfix img')
print(len(elems))
for elem in elems:
    if elem.get('data-original')!= None:
        res=requests.get(elem.get('data-original'))

        # 创建一个文件
        f=open(os.path.join('漫画','%s.png'%x),'wb')# 以二进制方式打开
        for byte in res.iter_content(10000):
            f.write(byte)
        f.close()
        x+=1

print('完成')
