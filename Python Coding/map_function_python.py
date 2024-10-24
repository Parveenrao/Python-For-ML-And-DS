# syntax -----> mapped_object = map(function_name , iterable)

#function_name ---> a function that process every result and return result

# iterable ---> sequence like string , list , tuple from which we have to  iterate elements

# lets undertand throuh a example we make a function that return the length of character

"""num = ['parveen' , 'shruti' , 'nirmala']

def name_char(name):
    return len(name)

mapped_object = map(name_char , num)

print(mapped_object)
print(type(mapped_object))
print(list(mapped_object))

# now again print the elements
print(list(mapped_object))

#it will provide an empty list because it work like filter function , we can use map function one time,
# after it will exhaust"""

# we can use map function with lambda expression

"""num = [1, 2, 3, 4, 5]

mapped_object  = map(lambda x: x**2 , num)
print(list(mapped_object))"""

num =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""def square(n):
    if n %2!=0:
        return n**2

mapped_object = map(square, num)

for ele in mapped_object:
    print(ele)"""

# we have two list we add two list using map function

"""num1 = [10, 20, 30, 40, 50]
num2 = [10, 30, 50, 70, 90]

def add(n1, n2):
    return n1 + n2

mapped = map(add, num1, num2)

print(list(mapped))"""


# we can pass multiple iterables into the ma function

marks = [10, 20, 30, 40]
bonus = [20, 30, 40]
bonus1 = [40, 50, 60]

def logic(arg1, arg2, arg3):
    return arg1 + arg2 +arg3

mapped = map(logic, marks , bonus , bonus1)

for ele in mapped:
    print(ele)