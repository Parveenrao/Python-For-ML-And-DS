# inheritance in python

class Employee:
    bonus_emp = 10000
    def display(self):
        print(f"This is a employee class method")
    
class Manager(Employee):
    bonus = 20000
    def show(self):
        print(f"This is a manager class method")
        


m = Manager()
m.show()   
m.display()
print(m.bonus_emp)      