# fpath = './LiaoXueFeng_python/temp.txt'
# with open(fpath, 'a') as f:
#     f.write('hello py\n')
# with open(fpath, 'r') as f:
#     print(f.read().strip())

#利用os模块编写一个能实现dir -l输出的程序
import os
from datetime import datetime

def dir_l(path):
    L = [x for x in os.listdir(path)]
    # flist = [x for x in os.listdir(path) if not os.path.isdir(x)]
    # dlist = [x for x in os.listdir(path) if os.path.isdir(x)]
    for f in L:
        fsize = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime("%Y-%m-%d %H-%M")
        flag = '/' if os.path.isdir(f) else ''
        print("%10d %s %s%s" % (fsize, mtime, f, flag))

# dir_l('.')


