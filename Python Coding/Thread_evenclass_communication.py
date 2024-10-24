import threading
from time import sleep
e = threading.Event()

""" task():
    print("Game is Started")
    sleep(3)
    e.set()
def end():
    e.wait()
    if e.is_set():
        print("Code for destroying sessoion")



t1 = threading.Thread(target=task())
t2 = threading.Thread(target=end())
t1.start()
t2.start()"""

import threading
from time import sleep

e = threading.Event()

def traffic_switch():
    while True:
        print("Light is green")
        e.set()
        sleep(3)
        print("Light is Red")
        e.clear()
        sleep(3)
        e.set()

def traffic_message():
    e.wait()
    while e.is_set():
        print("you can go")
        sleep(3)
        e.wait()



t1 = threading.Thread(target=traffic_switch)
t2 = threading.Thread(target=traffic_message)

t1.start()
t2.start()
