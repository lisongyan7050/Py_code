import os,requests,bs4
import threading

url='http://xkcd.com'
os.makedirs('漫画',exist_ok=True)# 创建一个文件夹


def downloadxkcd(startnum,endnum):
    for urlnumber in range(startnum,endnum):
        print('下载 页面 http://xkcd.com%s'%urlnumber)

        # < a href = "//xkcd.com/1732/" > < img border = "0" src = "//imgs.xkcd.com/s/temperature.png"
        # width = "520" height = "100" alt = "Earth temperature timeline" > < / a >

        res=requests.get('http://xkcd.com/%s'%urlnumber)
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text)

        # 查找 image 的url
        elems=soup.select('#comic img')
        if elems==[]:
            print('没有找到 图片')
        else:
            elemurl='http:'+elems[0].get('src')
            print('下载 图片%s'%elemurl)
            res=requests.get(elemurl)
            res.raise_for_status()
            imagfile=open(os.path.join('漫画',os.path.basename(elemurl)),'wb')
            for byte in res.iter_content(100000):
                imagfile.write(byte)

            imagfile.close()

# 看一下浏览器的 元素,可以发现 这个图片一共有 1700个; 那么可以创建17个线程, 一个线程下载 100个
downloadThreads = []
for start in range(1,1700,10):
    downloadThread =threading.Thread(target=downloadxkcd,args=(start,start+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()


for downloadThread in downloadThreads:
    downloadThread.join()

print('完成')

        # # 获取前一页的链接
        # prelink=soup.select('a[rel="prev"]')[0]
        # url='http://xkcd.com'+prelink.get('href')

### ps  : 这里面的一个页面只有一个图片,,,如果一个页面有多个图片,那么就 加个for即可