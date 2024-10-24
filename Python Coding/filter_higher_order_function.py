# python provide three main  higher order function filter map and reduce which used in the projects

# syntax ---- filtered_object = filter(function_name , iterbale)

#  function_name ---> test each element of sequence if it is true or not

# iterable ---> sequence like tuple , list and strings

# so if we have a list of data that contain number we have to filter out the even number and odd number
# so our functon return true if num is even or else false

# let understand through an example

data = [23, 22, 36, 54, 59, 90]

"""def even(num):
    if num % 2 == 0:
        return True
    else:
        return False


filtered_object = filter(even , data)
print(filtered_object)
print(type(filtered_object))

# so for printing the elements of filter function  we have to run a loop becuse it is an iterable function


for ele in filtered_object:
    print(ele)

# another method for printing filter element is list method
print(list(filtered_object))
print(list(filtered_object))"""


# importat note ---> filter function used only once , after they used once they will exhausted , only give empty list

# we can use lambda expression in the filter method


filter_obj = filter(lambda num: num % 2== 0 , data)
print(list(filter_obj))

# any value in python other than 0 is considered as true

print(bool(4))
print(bool("parveen"))