# Race condition in multithreading
""" below are the steps performed while doing  operation
    1) read the current value of the thread
    2) Calculate new value of the thread
    3) write a new value for the variable """

# lets understand through an example
x = 100
t1  = x +10    # x value wiil be updated to 110 (t1 thread)
t2 = x-20      # x value will be updated to 90  (t2 thread)

# we expect that x value will be 90 , but this is not ture because both the threads are running parallely
# so there will be an different value

from threading import Thread

def add(x):
    print(x+10)

def subtract(x):
    print(x-20)

t1 = Thread(target=add , args=(100,))
t2 = Thread(target=subtract ,args=(100,))
t1.start()
t2.start()
