import os,zipfile
# zipob=zipfile.ZipFile(r'C:\Users\10756\Desktop\ehmatthes-pcc-v1.0.0-12-gf555082.zip')
# print(zipob.namelist())
# zip_info=zipob.getinfo('ehmatthes-pcc-f555082/chapter_12/restore_points/restore_point_2_fires_bullets/game_functions.py')
# print(zip_info.file_size)

zipob=zipfile.ZipFile(r'C:\Users\10756\Desktop\快递.zip')
print(zipob.namelist())
info=zipob.getinfo('express.java')
print(info)
# zipob.extractall(r'C:\Users\10756\Desktop\test')
# zipob.close()
zipob.extract('express.java',r'C:\Users\10756\Desktop\bbbb')
zipob.close()