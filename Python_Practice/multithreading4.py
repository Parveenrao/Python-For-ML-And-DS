# join method is multithreading

from threading import Thread

def display():
    for i in range(5):
        print("Parveen You are Great AI ")
 
def show():
    for i in range(5):
        print("developer")
        
        
        
        
t1 = Thread(target=display)
t2 = Thread(target=show)

t1.start()
t1.join() 

t2.start()
t2.join()               


       
for i in range(5):
    print("u are brave parveen") 