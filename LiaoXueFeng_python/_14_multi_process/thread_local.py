import threading
from threading import Thread

local_school = threading.local()

def process_student():
    print(f"student {local_school.student} in thread {threading.current_thread().name}")

def process_thread(name):
    #每个线程绑定自己的name
    local_school.student = name
    #同一线程里调用的函数可以访问到该线程的local
    process_student()

if __name__ == "__main__":
    t1 = Thread(target=process_thread, args=("Akker",), name="Thread_A")
    t2 = Thread(target=process_thread, args=("Bubble",), name="Thread_B")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    