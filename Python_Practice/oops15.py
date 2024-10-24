#operator overloading

num1 = 10 
num2 = 20

print(num1 + num2)
print(num1.__add__(num2))
print(int.__add__(num1 , num2))


str1 = 'Parveen'
str2 = 'Yadav'
print(str1 + str2)
print(str1.__add__(str2))
print(str.__add__(str1, str2))


# opertor overloading

class Hotel:
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
    
    def __gt__(self , other):
        return self.fare > other.fare
        

h1 = Hotel("The Taj" , 18000)
h2 = Hotel("The Radison Blue" , 20000)

print(h1>h2)         