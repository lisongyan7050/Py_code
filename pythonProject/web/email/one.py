from selenium import webdriver
brower=webdriver.Edge("C:\安装包\msedgedriver.exe")
brower.get('https://18comic.vip/photo/335258')
confir=brower.find_element_by_id('chk_cover')
confir.click()
nexturlk=''
# while True:
imagelem=brower.find_elements_by_class_name('center scramble-page')
print(len(imagelem))

