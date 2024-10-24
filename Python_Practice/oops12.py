# Polymorphism means more than one  from 

# polymorphism in python is an ability of python to takae many forms

# lets understand through inheritance 

class Veh:
    def __init__(self , name , color, price):
        self.price = price
        self.name = name 
        self.color = color 
         
    def get(self):
        print(f"Name of vehicle is {self.name} , color of vehicle is {self.color} , price of vehicle is {self.price}")
        
    def max_speed(self):
        print(f"maximum speed is 100") 
        
    def gear(self):
        print(f"gear change is 6")
        
        
class Car(Veh):
    def max_speed(self):
        print(f"maximum speed for car is 140")
        
    def gear(self):
        print(f"gear change is 7")
        
        
        
v1 = Veh("Truck" , "Green" , "1000000")
c1 = Car("Ferrari" , "Green" , 200000000)

v1.max_speed()
c1.max_speed()            
                        