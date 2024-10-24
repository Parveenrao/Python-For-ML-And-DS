# wrapping up a single data  in a classs is called encapsulation ,

# encapsulation restrict the modification of the data outside the class

# encapsulation is also callled data hiding 
# so there are three access modifiers public , private , protected


class Finance:
    def __init__(self):
        self.__revenue = 10000   # private data
        self.__name = "Parveen"  # protected data
        
    def display(self):
        print(f"revenue is {self.__revenue} and name is {self.__name}")    
        

f  = Finance() 
f.display()      

# in python pure encapsulation in not exist 
# another method to access prviate members are


print(f._Finance__revenue)