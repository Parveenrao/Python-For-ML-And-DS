# nested classes

class Outer:
    def __init__(self):
        print('Outer class constructor called')
        
    def display(self):
        print('This is a display method') 
        
        
    class Inner:
        def __init__(self):
            print('Inner class construtor called')
            
        def show(self):
            print("This is show method")
            
            
ob = Outer()                  
inn = ob.Inner()     

inn.show()