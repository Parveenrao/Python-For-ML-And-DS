""" thread synchronization is defined as a mechanism  which ensure that two or more concurrent  thread do
    not simultaneously execute some particular program segment called critical section """

"""" R-Lock is modified version of lock

      by using R-Lock we can acquire() multiple times"""

"""R-lock big advantage is that is contain information of current running method """

# lets understand through an example
from threading import *
from time import sleep
l = RLock()
class Bus:
    def __init__(self,name , available_seats , rlock):
        self.name = name
        self.available_seats = available_seats
        self.rlock = rlock

    def Reserve(self, need_seats):
        self.rlock.acquire()
        self.rlock.acquire()
        print("available_seats are" , self.available_seats)
        if self.available_seats>=need_seats:
            nm = current_thread().name
            print(f"{need_seats} are alloacted to {nm}")
            self.available_seats-= need_seats

        else:
            print("sorry ! no seats are left")
            self.rlock.release()
            self.rlock.release()

b1 = Bus("Mahalakshmi Travels",2,l)
t1 = Thread(target=b1.Reserve , args=(1,) , name = "Raj")
t2 = Thread(target=b1.Reserve , args=(2,) , name = "Jay")
t1.start()
t2.start()
