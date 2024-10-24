from time import sleep
from threading import Thread
videos = ['oop_slybuss' , 'constructor' , 'destructor' , 'file_handling']

class Myclass(Thread):
    def __int__(self):
        print("constructor called")   # for this constructor callled we need to call also the thread constructor
        Thread.__init__(self)
    def run(self):
        for vid in videos:
            print(f"{vid} start uploading")
            sleep(3)
            print(f"{vid} uploaded")


t1 = Myclass()
t1.start()

for i in range(5):
    sleep(0.3)
    print("checking checkpoint")