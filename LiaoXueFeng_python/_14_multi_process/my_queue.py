'''进程间通信——queue'''

from multiprocessing import Process, Queue
import os, time, random

def write_q(q:Queue):
    print(f"this is the write queue proc {os.getpid()}.")
    for each in "ABC":
        q.put(each)
        time.sleep(random.random())

def read_q(q:Queue):
    print(f"this is the read queue proc {os.getpid()}.")
    while(True):
        info = q.get()
        print(f"info get from queue: {info}.")

if __name__ == "__main__":
    print(f"this is the main proc {os.getpid()}")
    q = Queue()
    pw = Process(target=write_q, args=(q,))
    pr = Process(target=read_q, args=(q,))
    pw.start()
    pr.start()
    time.sleep(random.random())
    pw.join()   #等待写完
    pr.terminate()  #主动关闭读进程
