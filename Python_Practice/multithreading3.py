# to check whether thread is alive or not 

from threading import Thread

def show():
    for i in range(3):
        print("Parveen Dont ")


def run():
    for i in range(3):
        print("Give up")
        

t1 = Thread(target=show)
print("Before" , t1.is_alive()) 

t1.start()
print("After" , t1.is_alive())               


t2 = Thread(target=run)
t2.start()