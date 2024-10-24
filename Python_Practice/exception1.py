# an exception is an event which occurs during the execution of the program that disrupts the normal flow of program
# lead to sudden termination of the program 
# corrupt data 
# can block application 

num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))

try:
    div = num1/num2
    print(div)

except ZeroDivisionError:
    print("divide by zero is not possible")
    

print("rest of code")    
    
    

num3 = int(input("Enter number 3 :"))
num4 = int(input("Enter number 4 :"))

try:
    div = num3/num4
    print(div) 

except (ZeroDivisionError , NameError) as obj:
    print(obj) 
    
          