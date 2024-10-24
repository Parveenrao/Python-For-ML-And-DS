# a function is called higher order function if it is statify two conditions
# ----> it contain function as a parameter
#           or
#  return an function as an output for further processing

# simply a function which operate on another function is called higher order function

def add(n1, n2):
    return n1 + n2

def display(func):
    print(func(10, 20))

display(add)     # here display function take input the add function so display function is higher order function
