import traceback

try:
    raise Exception('This is the error message.')
except:
    with open('error.txt','w') as f:
        f.write(traceback.format_exc())
else:
    print('成功')