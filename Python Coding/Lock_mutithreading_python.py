from threading import Thread , Lock
from time import sleep
def task(mylock , msg):
    mylock.acquire()
    for i in range(4):
        print(msg)
        sleep(3)
    mylock.release()

mylock = Lock()
t1 = Thread(target=task, args=(mylock, "hello world",))
t2 = Thread(target=task, args=(mylock, "Parveen",))
t1.start()
t2.start()

# we cannot release and acquire multiple times using lock method

# this can be solved by using R -lock method