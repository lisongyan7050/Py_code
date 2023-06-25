import traceback
def diveson_2():
    while True:
        a=input("\n输入第一个数字:")
        if a=='q':
            break
        b=input("\n输入第二个数字:")
        if b=='q':
            break
        try:
            answer=int(a)/int(b)
        except ZeroDivisionError as zero:
            print("不能除以0")
            print(traceback.format_exc())
        else:# 依赖于try 代码块成功执行后产生的数据再做进一步执行的代码, 都应当放在 else里面
            print(answer)

diveson_2()