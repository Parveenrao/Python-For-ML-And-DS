class Base1:  
    def __init__(self):  
  
        
        self._p = 78  
  

class Derived1(Base1):  
    def __init__(self):  
  
        Base1.__init__(self)  
        print ("We will call the protected member of base class: ",  
            self._p)  
  

        self._p = 433  
        print ("we will call the modified protected member outside the class: ",  
            self._p)  
  
  
obj_1 = Derived1()  
  
obj_2 = Base1()  
  
 
print ("Access the protected member of obj_1: ", obj_1._p)  
  

print ("Access the protected member of obj_2: ", obj_2._p)  