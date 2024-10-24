# constructor overriding ------> child class constructor have more priority than parent class constructor


class Father:
    def __init__(self):
        print("Father class constructor called")
        self.vehicle = 'BMW'
        
class Son(Father):
    def __init__(self):
        print("son classs constructor called")
        self.vehicle = "Ferrari"
        
        
s = Son()
print(s.vehicle)       
        
# super method is used to access the properties of parent classs when constructor is overriding
"""class Computer:
    def __init__(self):
        self.ram = '8GB'
        self.storage = '512GB'
        print(f"Parent class constructor called")
        
class Mobile(Computer):
    def __init__(self):
        super().__init__()
        self.model = "Samsung"
        print(f"son class constructor callled")


app = Mobile()

print(app.__dict__)"""      
                
                