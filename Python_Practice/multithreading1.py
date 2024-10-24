# how to creat thread in python 

from threading import Thread

def display():
    for i in range(4):
        print("Parveen you are good person")


t1  = Thread(target=display) 
t1.start()       
        
        

for i in range(5):
    print("You are a great data scientist")   # this was create by main thread 
    
            