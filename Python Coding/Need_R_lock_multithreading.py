from threading import *
l = Lock()

def get_first_line():
    l.acquire()
    print("Code for fetching first line")
    l.release()

def get_second_line():
    l.acquire()
    print("Code for fetching second line")
    l.release()

def main():
    l.acquire()
    get_second_line()
    get_second_line()
    l.release()

t1 = Thread(target=main)
t1.start()

# now our program stuck , so  instead of lock  used r lock for multiple lock and r lock

# use  = RLock