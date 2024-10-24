# traditonal language like c , c++ are not this type of operator 

# Need of this operator 
# they are usually used with sequence like string

# there are two types of special operators called membership operators and identity operator 

str = 'Parveen'

print('shruti' in str)

numbers = [10,20,30 ,40 ,50]
print(50 in numbers)


group = ['parveen', 'shruti', 'john']
name = input("Enter your name")

if name in group:
    print(f"{name} is present")
else:
    print(f"{name}is not found")
   
# identity operator which checks the identity of the opertor 

a = 100
print(id(a))
b = 100 
print(id(b))    

print(a is b)
    
