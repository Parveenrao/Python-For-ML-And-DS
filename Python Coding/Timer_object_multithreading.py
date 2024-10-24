import threading
from threading import *
from time import sleep

def task():
    for i in range(5):
        print("Hello Mr. Parveen")


timer = threading.Timer(10 ,task)
timer.start()


for i in range(5):
    print('Welcome')