""" in this program we write two decorator program in which first function is convert our name into
    full name  decor1 = PARVEEN YADAV"""

""" decor2 = ['PARVEEN' , 'YADAV']"""

def decor1(func):
    def inner():
     return func.upper()
    return inner

def decor2(func):
    def inner():
        return func().split()
    return inner



@decor2
def get_name():
     name = input("Enter your name")
     sirname = input("Enter your sirname")
     full_name = name + sirname
     return full_name

"""get_name = decor1(get_name())
print(get_name())

get_name = decor2(decor1(get_name))"""
print(get_name())