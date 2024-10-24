# filter is high order function

# a function is called high order function if it is contain either properties 
# 1. it contain other function as parameters 
# 2. return function as an output for further processing


# filter function take two argument function_name and iterbale 

# functio_name ---> a function that test if each element of a function is true or not..... consist of logic filtering
# iterbale ---> list tuple , set from which we have to filter elemetns 

"""seq = ['g' , 'e' , 'h ' , 'a' , 'i' , 'k' , 'l' , 'o' , 't' , 'u']

def fun(variables):
    letters = ['a' , 'e' , 'i' , 'o' , 'u']
    if (variables in letters):
        return True
    else:
        return False
    
filtered = filter(fun , seq)   


for elements in filtered:
    print(elements)
    
    
    
# filter out odd no.add even no

data = [1 ,2, 3, 4, 5 ,6, 7, 7, 8, 9, 10]

def no(num):
    if num%2 == 0:
        return True
    else:
        False
        
 
filter_no = filter(no , data) 

for nums in filter_no:
    print(nums , end=" ")"""
           
        
# filter function using lambda expressions


        
data = [2, 5 ,3, 4,9, 0, 4, 9, 10 ,12]

filtered = filter(lambda x: x%2==0 , data)

for elements in filtered:
    print(elements ,end=' ')
    