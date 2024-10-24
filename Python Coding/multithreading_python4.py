# how to create threads
""" there are two ways of creatig threads
    one is thread class present in threading module
    by extneded thread class"""

# step 1 import thread class

from threading import Thread , current_thread

# step 2 create a function to be executed paralley

def display(n , msg):
    print("t1 thread details", current_thread().name)   # if it is running outside then it is executed my  main thread
    for i  in range(n):
        print(msg)

# step 3 create new thread  object of thread

t1 = Thread(target= display , kwargs={'n': 4 , 'msg': 'hello'})

# step 4 start thread

t1.start()

# now run parallely another function

for i in range(4):                        #  this function is run paralley and is executed by main thread
    print("Welcome Parveen")
