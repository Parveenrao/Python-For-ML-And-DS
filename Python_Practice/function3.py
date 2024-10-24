# how to access global variables  and solve unbound error

num = 10 #---> global variable 

def display():
    global num     #------> resolve unound local error
    num = num + 5
    print('inside' , num)
    
display() 

print('outside' , num)   


# how to return multiple values from the funtion 

def show(a,b):
    add = a + b
    sub = a - b
    return add , sub


print(show(10 ,20))




# parameters and arugmetns 

# parameter ----> paremeters are present in function definition  , varailbes for holding actual values

# arguments ---> arguments are actual values , used in function calling 

# important note is that , when arguments are changed , result will also be changed 



# example 


def Name(name, age):
    print(f"name is {name} and age is {age}")
    
Name(23 , 'jay')   #----->  result is here name is 23 and age is jay    
    
    
    
    
# varible length arguments 


def SUM(*num):
    sum = 0 
    for n  in num:
        sum = sum + n
    return sum     
      
  


print(SUM(10, 20, 30))    