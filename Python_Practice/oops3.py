#class varaible in python

class Employee:
    company_name = "Amdocs"
    def __init__(self, name , dept):
        self.name = name
        self.dept = dept
 
 
e1 = Employee("Parveen" , "Software Developer") 
e2 = Employee("John" , "Machine Learning Engineer") 

# acces class varaible using classs instance
print(Employee.company_name)

# access using object 

print(e1.company_name)      
        
# modify class varaible 

Employee.company_name  = "Tower Research"

print(Employee.company_name)        
     
        