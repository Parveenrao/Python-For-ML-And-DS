# ist function will take complete name as input 

# 2nd function  will capital the name

# 3nd function will split the name 


def decor1(func):
    def inner():
        return func().upper()
    return inner



def decor2(func):
    def inner():
        return func().split()
    return inner

@decor2
@decor1
def get_name():
    name = input("Enter your name")
    sirname = input('Enter your sirname')
    fullname = name + sirname
    return fullname


print(get_name())