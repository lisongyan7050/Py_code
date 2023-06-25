import threading,time

# x=10
# def run():
#     global x
#     while x>0:
#         # print('当前%s'%x)
#         time.sleep(2)
#         # x-=1#  这里直接这么写会报错, 因为 当前使用的是外部变量,在 局部是不能修改 外部变量的, 需要 使用global
#         print('当前%s' % x)
#         x-=1
# threads=threading.Thread(target=run)
# threads1=threading.Thread(target=run)
# threads2=threading.Thread(target=run)
# threads.start()
# threads1.start()
# threads2.start()


threading.Thread(target=print,args=(1,2,3,45),kwargs={'sep': ' & '}).start()
threading.Thread(target=print,args=(1,2,3,45),kwargs={'sep': ' & '}).start()
threading.Thread(target=print,args=(1,2,3,45),kwargs={'sep': ' & '}).start()
threading.Thread(target=print,args=(1,2,3,45),kwargs={'sep': ' & '}).start()