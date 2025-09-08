import os

'''print('process %s start' % (os.getpid()))

#fork()调用后创建了子进程，在子进程和父进程中分别返回，子进程永远返回0，父进程返回子进程pid
pid = os.fork()
if pid == 0:
    print('child process: %s, parent process: %s' % (os.getpid(), os.getppid()))
else:
    print('process %s created a child precess %s' % (os.getpid(), pid))
'''

#fork()仅适用类Unix，multiprocessing模块提供跨平台的多进程
from multiprocessing import Process

def run_process(name):
    print('now %s is running' % name)

if __name__ == '__main__':
    print('Ppid: %s' % os.getpid())
    p = Process(target=run_process, args=('test',)) #创建运行函数的进程
    p.start()
    p.join() #等待子进程结束，用于进程间同步
    print('child process end')