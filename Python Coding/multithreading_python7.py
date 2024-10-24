# how to print and change name in thread

from threading import Thread , current_thread

def display():
    for i in range(4):
        print("hello")

def show():
    for i in range(3):
        print('Parveen')

t1 = Thread(target=display())
t2 = Thread(target=show())
t1.start()
t2.start()

# name of thread
print(t1.name)
print(t2.name)

# also we can change the name of the thread by assigning the name to the thread

t1.name = "Parveen"
print(t1.name)

print(current_thread().name)

# we can change the name of main thread(current)thread)

current_thread().name = "hello"
print(current_thread().name)

print("-"*50)

# thread have two identity thread id and native id
# and one pid (process id)

print(t1.ident)
print(t1.native_id)

# for pid we have to call os module

import os
print(os.getpid())    #---> it is the id of the program