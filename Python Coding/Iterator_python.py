# Iteration ---> process of taking each element of something one after another is called iteration
# Ex -> whenever you use loops for visiting every item of a sequence

# Iterator ---> An iteration is a pyhton object which allow programmers to travel through the sequene of data
# iteration possuble ho pta h intertor ke help se

# Iterable ---> Iterable hota h jske uper hm iteration krte h

# container of multiple classs

"""L = [10, 20, 30, 40]   # --->  Iterable jiske uper process ho rha h

for ele in L:    # ----> Iteration
    print(ele)"""
import sys

# how to create iteration

# for makin iteration python provie us an in built function called iter

L = [10, 20, 30, 40, 50]
iter_list = iter(L)
"""print(iter_list)

# by next function we can fetch the element of list
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))   # ---> give stop iteration error because cant fetech next item ,"""

# iterator (next) function remeber its last item

# how to check whether a object is interable or itertor
 # for checking a object is iterbale is ornot , use for loop

 # Every itertor is iterable

 # __iter__  ---> iterable
 # __iter__ __next___ -----> iterator

"""print(dir(L))
print(dir(iter_list))"""

"""L = [10, 20, 30, 40, 50, 60, 70, 80]

iter_list = iter(L)
print(iter_list.__next__())"""


"""object = eval(input('Enter object'))
object_dir = dir(object)

if "__iter__" in object_dir and "__next__" in object:
    print("Iterator Supported")

elif "__iter__" in  object_dir:
    print("Iterable Supported")

else:
    print("Not supported")"""

"""object1 = iter(eval(input("Enter Object")))
object_dir = dir(object1)

if "__iter__" in object_dir and "__next__" in object_dir:
    print("iterator  Supported")

elif '__iter__' in object_dir:
    print("Iterable Supported")

else:
    print("Not Supported")"""

L = [10, 20, 30, 40, 50]

def mine_loop(iterable):
    iterator = iter(iterable)

    try:
        while True:
            print(next(iterator))

    except StopIteration:
        pass


mine_loop(L)


# biggest advantage of iterator is it saves memeory
# write a program to calculate the sqaure of first ten number

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for ele in L:
    print(ele **2)

print("L" , sys.getsizeof(L))

a = range(1, 11)
for ele in a:
    print(ele ** 2)

print(sys.getsizeof(a))


b = range(1, 1500000)
for ele in b:
    print(ele ** 2)

print(sys.getsizeof(b))

# in range method the memory storage remains samme

# actually range function uses iterators

# working of range function ----> range function first store 1 element and then vanish it , again store 2nd
# element and vanish it and so on

# iterators are lazy evalutaion