from selenium import webdriver
import requests
x=1
browser = webdriver.Edge("C:\安装包\msedgedriver.exe")
browser.get("http://mh.dettop.cn:88/mhread.php?mhid=845&ji_no=5")
try:
    elems=browser.find_elements_by_tag_name('img')
    for elem in elems:
        f=open('imag\%s.jpg'%x,'wb')
        res=requests.get(elem.get_attribute('src'))
        for byte in res.iter_content(100000):
            f.write(byte)
        f.close()
        x+=1
except:
    print('发生了意外')
