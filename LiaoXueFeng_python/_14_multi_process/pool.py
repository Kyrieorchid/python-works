'''pool启动若干子进程'''

from multiprocessing import Process, Pool
import os, random, time

def x_time_task(name):
    print(f"run task {name} with pid {os.getpid()}.")
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(f"last for {end - start} seconds.")

if __name__ == "__main__":
    print(f"parent pid {os.getpid()}.")
    p = Pool(4)
    for i in range(5):
        p.apply_async(x_time_task, args=(i,))   #机器只有4核，只能同时运行task0~3，task4要等task0完成才启动
    print("all procs running.")
    p.close()   #join之前必须close，close之后不能添加新的procs
    p.join()    #等待所有子进程结束
    print("all procs done")
