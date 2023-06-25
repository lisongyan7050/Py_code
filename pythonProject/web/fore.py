import requests,bs4,webbrowser
key=input('输入 查询的内容')
print('https://cn.bing.com/search?q='+str(key))
res=requests.get('https://cn.bing.com/search?q='+key)
res.raise_for_status()
bs=bs4.BeautifulSoup(res.text)
elems=bs.select('h2 a')
print(len(elems))

numOpen = min(5, len(elems))

for x in range(numOpen):
    webbrowser.open(elems[x].get('href'))


