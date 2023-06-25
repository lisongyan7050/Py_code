import bs4,requests
"""使用BeautifulSoup"""

example=open('example.html')
noStarchSoup=bs4.BeautifulSoup(example)


# res=requests.get('http://nostarch.com')
# res.raise_for_status()
# noStarchSoup=bs4.BeautifulSoup(res.text)# 获取 bs4对象
#有了BeautifulSoup对象之后，就可以利用它的方法，定位HTML文档中的特定部分。

# elems=noStarchSoup.select('#author')
elems=noStarchSoup.select('p a')
print(type(elems))
print(len(elems))
print(elems[0])
print(elems[0].text)
print(elems[0].attrs)
print(elems[0].get('href'))
