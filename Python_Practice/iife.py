# immedatiely invoked function expression

# iska mtlab h ke ekdum function create krte vkt , call krna

result = (lambda x,y : x+y)(3,2)
print(result)



outcome = (lambda num: num + 1)(int(input("Enter number")))
print(outcome)


# first class objects in python 

# first class object is a programming

# they are the objects of some classes

# there values are stored in the data structure

# can be assigned to be variable

# can be perform operations

# can be passed as a arguments to the functions

# funtion as a agrument 

def get_name():
    nm = input("Enter your first name")
    last_name = input('Enter your last name')
    return nm + " " + last_name

def display(func):
    print(func())
    
display(get_name)    