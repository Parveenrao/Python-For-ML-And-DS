# polymorphism means a function can have more than one form

class Complex:
    def __init__(self , real , imag):
        self.real = real
        self.imag = imag


    def show(self):
        print(self.real,"i +",self.imag,"j")


    def __add__(self  , num2):       #---------> dunder function
         newReal = self.real + num2.real
         newImag = self.imag + num2.imag
         return complex(newReal , newImag)






com = Complex(10 ,12)
com.show()

com2 = Complex(12 , 15)
com2.show()

com3 = com + com2
