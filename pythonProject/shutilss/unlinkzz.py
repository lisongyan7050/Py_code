import os,send2trash

import send2trash as send2trash


# for name in os.listdir(r'C:\Users\10756\Documents\pythonProject\venv\day3\TEST'):
#     if name.endswith('.txt'):
#         print(name)
#         os.unlink(os.path.join(r'C:\Users\10756\Documents\pythonProject\venv\day3\TEST',name))
#
# # 改变 工作环境到TEST 目录下
# os.chdir(r'C:\Users\10756\Documents\pythonProject\venv\day3\TEST')
# print(os.getcwd())
# for name in os.listdir():
#     if name.endswith('.txt'):
#         print(name)
#         os.unlink(name)
send2trash.send2trash('crazyKFC')