# Raise keyword and statement 

# an exception can be raised forcefully  by using raise clause

# raise statement is used when we want to thwor exception for particular conditon 


try:
    age = int(input("Enter your age"))
    if age<0:
        raise ValueError
    print(f"Your age is {age}")
    
except ValueError:
    print("Enter valid age")
    
print("rest of the code")    


# user definded exception 


class SevenDivisionError(Exception):
    'this is the exception class called when the SevenDivisonError occur'
    def __init__(self):
        print("Cannot divide by 7")
        
    pass


try:
    n1 = int(input("Enter first number :"))
    n2 = int(input("Enter second number :"))
    
    if n2 == 7:
        raise SevenDivisionError
    
    div = n1/n2
    print(f"Division is {div}")

except SevenDivisionError as var:
    print(var)
            
    