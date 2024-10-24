# if we not know which excetion will occur ,

# and ZeroDivisionError is a class

"""num1 = int(input("enter first number :"))
num2 = int(input("Enter Second number :"))

try:
    div = num1 / num21
    print(div)

except Exception as var:      # ----> if we did not know which exception will occur
    print(var.__class__)"""



# another method is sys module

import sys
num1 = int(input("enter first number :"))
num2 = int(input("Enter Second number :"))

try:
    div = num1 / num2
    print(div)

except:
    print(sys.exc_info()[0])   # ----> return exception information
    print(sys.exc_info()[1])   # ----> return exception name
