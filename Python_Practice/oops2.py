# built in class methods getatt , 


class Employee:
    def __init__(self, salary , name):
        self.salary = salary
        self.name = name
        
e1 = Employee(12000 , "Parveen")

#print(getattr(e1 , 'name')) 
        
        
print(setattr(e1 , 'name' , 'Savita')) 
#print(e1.name)       

print(delattr(e1 , 'salary'))

print(e1.__dict__)
print(hasattr(e1, 'name'))