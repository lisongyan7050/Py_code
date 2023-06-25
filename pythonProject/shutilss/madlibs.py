import bs4
result=open(r'C:\Users\10756\Desktop\管理员页面-毕业设计系统.html')

doc=bs4.BeautifulSoup(result)
print(doc.text)