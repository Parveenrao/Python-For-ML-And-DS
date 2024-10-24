from threading import Thread,current_thread
class Bus:
    def __int__(self , name , available_seats):
        self.available_seats = available_seats
    def reserve(self , need_seats):
        print("Available seats are ", self.available_seats)
        if self.available_seats>= need_seats:
            nm = current_thread().name
            print(f"{need_seats}are allocated to {nm}")
            self.available_seats-= need_seats
        else:
            print("sorry! , seats are not available")


b1 = Bus("Mahalakshmi Travels" , 2)
t1 = Thread(target = b1.reserve, args=(1,), name = "Raj")
t2 = Thread(target = b1.reserve, args=(2,), name = "Jay")
t1.start()
t2.start()


"""it is bug generated when you do multiprocessing. it Occur becuase two or more threds update the same result
   ans return unreliable output"""

""" a common approach to protect the critical section of the code(prevent concurrency"""