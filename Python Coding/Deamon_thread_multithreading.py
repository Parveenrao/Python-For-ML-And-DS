# there are two types of threads
"""daemon thread (supportive thread ) --- is a thread which continuously run in the background and provide suppor to
   non daemon thread
   daemon threads are used for task such as monitoring ,  background services or cleaup operation """

# non - daemon thread(non - supportive threads)


# checking daemon nature of main thread

from threading import current_thread , Thread

def display():
    print("This is display function")

t1 = Thread(target=display)
print("Daemon nature of thread is" , t1.daemon)
t1.daemon = True
t1.start()

# the nature is false beacuse t1 parent thread is main thread , and by default main thread nature is false

# to change nature

print("Daemon nature of thread is" , t1.daemon)
