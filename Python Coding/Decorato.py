# Decorators are powerfull tools in  python that are used to change the behvaiour or moddify the function
# of the class

# adding things more attractive and more presentable through decorator

# Decorator ----> is a function which take function as function and additional functionalities and return it
# Callalbe object ( High order function)


"""def greet(function):
    print("hello Parveen")

def printer():           # ----> this function that decorator as input
    print("Welcome")
    print('Welcome')



greet(printer())"""

# now we want to add functionality in printer function
"""def decor(printer):
    def inner():
        printer()    # ---> existing functionality
        print("Hello World !")
    return inner

@decor
def printer():
    print("Hello World")
    print("Hello World")


printer()"""

"""def decor(addition):
    def inner():
        result = addition()
        num3 = int(input("Enter your third number"))
        result = result + num3
        return result

    return inner
@decor
def addition():
    num1 = int(input("Enter first number"))
    num2 = int(input('Enter Second number'))
    result = num1 + num2
    return result



print(addition())"""

# multiple decorator function

# we make two decorator function first function will print full name like name and sirname

# 1st decorator function will convert this function into uppercase
# 2nd decorator function will split

def decor1(function):
    def inner():
        return function().upper()

    return inner

def decor2(function):
    def inner():
        return function().split()

    return inner

@decor2
@decor1
def get_name():
    name = input('Enter your name')
    sirname = input('Enter your sirname')
    full_name = name + " " + sirname
    return full_name



print(get_name())

