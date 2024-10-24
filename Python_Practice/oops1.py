# classs

# class is collectiion of objects 
# class is collection of attributes and items 
# Technically class is a user-defined data type


class Employee:
    def __init__(self):
        self.salary = 12000
        self.age = 21
        
e1 = Employee()
print(e1.salary ,e1.age)        
        
        
# constructor  ---> sepcial method used for intializing objects with attributes 
# it is __init__ method
#first agrument is self

# consntructor has three types ----> non parameterize , parameterize and default constructor 



# parameterize constructor 

class Personal:
    def __init__(self , salary , name ,age):
        self.name = name
        self.age = age
        self.salary = salary
        
    def display(self):
        print(f"salary is {self.salary} and name is {self.name} and age is {self.age}")
            
        
s1 =   Personal(12000 , 'Parveen' , 21)

s1.display()