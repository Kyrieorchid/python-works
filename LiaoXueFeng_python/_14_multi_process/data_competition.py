import os, time
import threading
from threading import Thread

'''进程间有隔离, 使用thread, 共享内存'''

lck = threading.Lock()
TIMES = 1000000

# 变量++ TIMES 次
def operate_num(num: list):
    for i in range(TIMES):
        # lck.acquire()
        # try:
        #     num[0] += int(1)
        # finally:
        #     lck.release()
        with lck:
            num[0] += int(1)


if __name__ == "__main__":
    num = [0]
    # 启动两个进程 变量++ 2*TIMES次
    t1 = Thread(target=operate_num, args=(num,))
    t2 = Thread(target = operate_num, args = (num,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"expected num[0]={TIMES * 2}")
    print(f"actual {num[0]=}")
    