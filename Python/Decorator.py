""" Decorators in python is powerfull tool which can modify the  behaviour of class and function"""
""" is function which take a function  as input , add functionality in it and return its"""

"""def decor(func):
    def inner():
        func()
        print("hello world")

        return inner


def printer():
        print("hello world")
        print("hello world")

printer()"""

# decoarator function to add two number


def decor(addtion):
    def inner():
        result = addition() # existing functionality

        # now we add to new functinality like addition of three numbers

        num3 = int(input("Enter third number"))
        result = result + num3

        return result
    return inner




def addition():
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    result = num1 + num2
    return result

""" now we call decor function which take the exisiting fucntion as input"""


addtion = decor(addition)
print(addtion())