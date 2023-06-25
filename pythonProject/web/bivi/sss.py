import requests,os
from selenium import webdriver
brower = webdriver.Edge("C:\安装包\msedgedriver.exe")
brower.get('https://www.google.com/search?sxsrf=ALiCzsajyTwfBL3AL0-w4XIxCRIxgtAlNw:1660187642828&source=univ&tbm=isch&q=%E5%A3%81%E7%BA%B8&fir=R9AyykUij1y-ZM%252CKi3XDKyPeaQpCM%252C_%253BS6A5rTb_LDdpxM%252CdRAG9gL35Z2VjM%252C_%253B0dlZd69zBVkjhM%252C92MM4liDsxsRGM%252C_%253BCXPzlaK0PYtk2M%252CFFblg_4gX-VREM%252C_%253BJPm4KiGS81xPHM%252ChHIrSYMG4ZvMpM%252C_%253B2-pt762XT_1VbM%252C8hyNO8z4HAWu2M%252C_%253B0l3t-d6xIeHB9M%252CokED9fpCbHw2iM%252C_%253BTSN7iWf6Q1MTAM%252CrAXddWWs6Wb8uM%252C_%253B5j-rIUdLoRmqTM%252C1yt2BdDCE_ZjGM%252C_%253BE-zjfpzCmwz2XM%252CEgBcCOrFqZEMXM%252C_%253B7kDAXs8s3pY-pM%252C9iRpT4mlVgRByM%252C_%253B2dVHDEQWTAmXxM%252CSpOHqR7LY8axNM%252C_%253BNGJKj0Uy8DTK6M%252Cgn2VdlYREy1TNM%252C_%253BtZ625DvH0JrpJM%252CrZnDPS8eNcV1fM%252C_&usg=AI4_-kSCipDFfltGKD2SBWRwcNK0xDfoEg&sa=X&ved=2ahUKEwiOgdj16L35AhUPfZQKHWNKCzUQjJkEegQIAxAC&biw=2560&bih=1289&dpr=1')
imags=brower.find_elements_by_class_name('Q4LuWd')
print(len(imags))

x=1
for imag in imags:
    file=open('壁纸\%s.jpg'%x,'wb')
    src=imag.get_attribute('src')
    if src != None and src.startswith('https') :
        res=requests.get(src,verify=False)
        for byte in res.iter_content():
            file.write(byte)
    x+=1
    file.close()

brower.quit()
