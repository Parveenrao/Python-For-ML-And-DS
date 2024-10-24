# multilevel inheritance 

class HumanBeing(object):
    def __init__(self):
        print(f"Parent Class Constructor Called")
        self.name = input("Enter Your Name")
        
class Employee(HumanBeing):
    def __init__(self):
        super().__init__()
        print(f"Child Class Constructor Called")
        self.salary = float(input("Enter Your Salary"))
        

class Manager(Employee):
    def __init__(self):
        super().__init__()
        print(f"Grand Child Constructor Called")
        self.bouns = float(input("Enter Your Bonus"))
        
m = Manager()

   
                
        