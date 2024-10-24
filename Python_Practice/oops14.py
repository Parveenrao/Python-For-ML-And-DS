# polymorphism in function and objects

class BMW:
    def fuel_type(self):
        print(f"Petrol")
        
    def max_speed(self):
        print(f"BMW max speed is 200")
        
class Ferrari:
    def fuel_type(self):
        print(f"Diesel")
        
    def max_speed(self):
        print(f"Ferrari max speed is 300")
        
b = BMW()
f = Ferrari()
        
def get_details(obj):
    obj.fuel_type()
    obj.max_speed()                      
    
    
    
get_details(b)
print('------------')
get_details(f)    