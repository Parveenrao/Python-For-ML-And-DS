class Vehicle:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost
        
        def show_details(self):
            print("Mileage of vehicle is ", self.mileage)
            print("Cost of the vehicle is " , self.cost)
            print("I am Parveen")
            
            v2 = Vehicle(36 , 120000)
            v2.show_details() 
            
            
            class car(Vehicle):         #child class which take the value of parent value .
                
             def show_car_details(self):
                 print("hey i am car")
                 
                 c1 = car(300 ,50)
                 c1.show_car_details()
        
  