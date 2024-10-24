# class method , which works on the class varaible 

# made by using class decorator @ 

class Personal:
    personal_name = 'moni'
    def __init__(self, name ,age):
        self.name = name 
        self.age = age
    @classmethod   
    def display_personal_name(cls):
        print(cls.personal_name)
        
p1 = Personal('Parveen',22)             
Personal.display_personal_name()        
        
        
# setter and getter method 

class Name:
    def setName(self ,nm):
        self.name = nm
        
    def getName(self):
        print(f"The name is {self.name}")
        
        
n1 = Name()
n2 = Name()

n1.setName(input("Enter the name you want to set"))
n2.setName(input("Enter the name you want to set"))

print(f"n1 object is {n1.__dict__}")
print(f"n2 object is {n2.__dict__}")

n1.getName()
n2.getName()            
                