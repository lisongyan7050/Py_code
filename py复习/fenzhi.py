
# 定义  由于 py 没有 指针, 那么字典 存储结果即可, 定义 字典key 0 的value 为最小值, key 1 的value 是最大值

def fen(a,left,rigth,result):
    if left==rigth:
        result[0]=a[left]
        result[1]=a[rigth]
        return
    if left+1==rigth:
        if a[left]>a[rigth]:
            result[0]=a[rigth]
            result[1]=a[left]
        if a[left]<a[rigth]:
            result[0]=a[left]
            result[1]=a[rigth]
        return

    lresult={}
    fen(a,left,(left+rigth)//2,lresult)

    rresult={}
    fen(a,(left+rigth)//2,rigth,rresult)
    if lresult[1]>=rresult[1]:
        result[1]=lresult[1]
    else:
        result[1]=rresult[1]
    if lresult[0]<=rresult[0]:
        result[0]=lresult[0]
    else:
        result[0]=rresult[0]


a=[-1111111, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 181111111, 19, 20, 21, 22, 23, 24666666666666666666666666666666666, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]


result={}

fen(a,0,99,result)


print('最小值是:'+str(result[0]))
print('最大值是:'+str(result[1]))

