# reduce function , reduce into a single values


from functools import reduce

data = [2, 5, 9, 11]

def func(a ,b):
    return a + b

red = reduce(func , data)

print(red)
    
    
# using lambda expression 

my_data = reduce(lambda x ,y : x +y , data)

print(my_data)    