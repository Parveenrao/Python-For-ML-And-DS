# method overloading 

class ADD:
    def add(self, num1 = None, num2 = None, num3 = None):
        if num1!= None and num2!= None and num3!= None:
            print(f"Addition is :{num1+num2+num3}")
            
        elif num1!= None and num2!= None:
            print(f"Addition is {num1+num2}")
            
        else:
            print(f"Invalid parameters are passed")
            
            
a = ADD()


a.add(10, 20)
a.add(10 ,20 ,30)
            