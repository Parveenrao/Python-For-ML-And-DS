# in this chapter we learn about how to creat thread from class method
from threading import Thread

class Example:
    def display(self , n):
        for i in range(n):
            print("hello")

# now in  this class method we want to creat object of class method
e1 = Example()

t1 = Thread(target= e1.display , args=(4,))
t1.start()
for i  in range(4):
    print("Welcome Parveen")

# we can use @classmethod so we dont use to create the object of class method
# and also we can use the @staticmethod , so we dont use the self keyword in the class method
