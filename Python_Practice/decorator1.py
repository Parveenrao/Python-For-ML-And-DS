# decorator is a python function which takes another function as an argument add additionla functionality and return it 

# implemetn a decor function in which a normal function take two no and add then , i want to modify the function to take another third no and modify it


def decor(addition):
    def inner():
        result = addition()
        # modify the function 
        num3 = float(input("Enter 3rd number"))
        result = result + num3
        return result
    
    return inner





@decor
def addition():
    num1 = float(input('Enter Ist number'))
    num2 = float(input('Enter 2nd number'))
    result = num1 + num2
    return result


print(addition())