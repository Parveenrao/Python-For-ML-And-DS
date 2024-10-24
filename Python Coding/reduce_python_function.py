# built in higer order function defined in functools module

# syntax
#import functools
#reduce_object = reduce(funtion_name , iterables)

# it doesnt return an another value , but it returns a reduce varailbes

import functools
num = [10, 5, 15, 20, 30, 20]

"""def function(a ,b):  # previous value + current value
    return  a +b

print(functools.reduce(function , num))
print(functools.reduce(function , num))  """

# we can use this by lambda expression

"""print(functools.reduce(lambda x ,y: x+y , num))"""

def max(a ,b):
    if a > b:
        return a
    else:
        return b

print(functools.reduce(max , num))