# destructor in python 

class Employee:
    def __init__(self, name , sal):
        self.name = name 
        self.sal = sal
        
    def display(self):
        print(f"Name is {self.name} and salary is {self.sal}")
        
      
    def __del__(self):
        print("Destructor called")
        
        
ob  = Employee('Parveen' , 1200)
ob.display()        

del ob