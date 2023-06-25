import requests
from selenium import webdriver
brower=webdriver.Edge('C:\安装包\msedgedriver.exe')
brower.get('http://mh.dettop.cn:88/mhread.php?mhid=845&ji_no=5')
elem=brower.find_element_by_link_text('下一章')
elem.click()