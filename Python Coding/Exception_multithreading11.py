# what will happen when exception occur in one thread ? will it impact other threads also

import threading
from time import sleep

def custom_hook(args):
    print("Exception occurred in thread")
    print(args[0])
    print(args[1])
    print(args[2])


def display():
    for i in range(4):
        sleep(0.3)
        print("Hello" + 10)

def show():
    for i in range(4):
        sleep(0.4)
        print("Parveen")

threading.excepthook = custom_hook
t1 = threading.Thread(target=display)
t2 = threading.Thread(target=show)
t1.start()
t2.start()