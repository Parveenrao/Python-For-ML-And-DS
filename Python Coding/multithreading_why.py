# lets understand through an example why multithreading is important

# we make a function of square and cube with multithreading or without multithreading

"""from threading import  Thread
from time import sleep

def square(num):
    print("Finding sqaure")
    sleep(1)
    print(f"square of {num} is", num * num)

def cube(num):
    print("Finding Cube")
    sleep(1)
    print(f"Cube of {num} is" , num*num*num)
begin = time.time()
t1 = Thread(target=square , args=(3,))
t2 = Thread(target=cube , args=(2,))
t1.start()
t1.join()
t2.start()
t2.join()

print('Total time taken in calculation is' ,time.time()-begin)""" # 2 sec
import time
# without multithreading

from threading import  Thread
from time import sleep

def square(num):
    print("Finding sqaure")
    sleep(1)
    print(f"square of {num} is", num * num)

def cube(num):
    print("Finding Cube")
    sleep(1)
    print(f"Cube of {num} is" , num*num*num)

begin = time.time()
square(3)
cube(2)
print("total time" , time.time()-begin)




