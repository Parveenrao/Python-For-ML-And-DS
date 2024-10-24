# In Lock and R-Lock technique at a time only one thread is allowed to execute

# result website ---> consider 1000 students can enter result to check result and website capacity is 100
# so we make 100 threads allowed to execute at one time

# seamphore can be used to limit the access to the shared resources with limited capacity

from threading import *
from time import sleep

obj = Semaphore(3)

def display(name):
    obj.acquire()
    for i in range(4):
        print("Hello")
        print(name)
        sleep(0.5)
        obj.release()

t1 = Thread(target=display, args=('Thread _1' ,))
t2 = Thread(target=display, args=('Thread _2' ,))
t3 = Thread(target=display, args=('Thread _3' ,))
t4 = Thread(target=display, args=('Thread _4' , ))
t5 = Thread(target=display, args=('Thread _5' , ))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


# if we acquire one time and releasd more time then sometime it will crash our software
# in this case we should use boundedsemaphore

# we can avoid race condition through semaphore if we use its defualt value 1
