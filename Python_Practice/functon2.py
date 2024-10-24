# there are two types of variable in function one is local variable and gloabal varaible ,,, 

# varible that are inside the function and the parameters defined in the function are callled local variables

def display(name):    # --> name is local variable
    age = 22          # ---> age is also a local variable 
    print(f"name is {name} and age is {age}")



# global variables -----> those variables that are not defined inside an function and class are called global variblaes 

country = 'India'
def show():
    name = "Parveen"
    print(name)    
    
    
    
# what if we have same local and global varible    