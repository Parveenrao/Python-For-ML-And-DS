#sets are represented using {} (curly brackets) and sets are unchangeable ordered and do not allow duplicates
import setuptools.config

thisset = {"Parveen", "Yadav", "Hello", "john"}

#duplicates are not allowed in sets like true or  1 considered as same value in set

#and false and 0 are also considered as same value

print(len(thisset))

print(type(thisset))

# we cannot access set items using index or some key

#we can print set value using for loop

for x in thisset:
    print(x)

# we cant change the items of set but we can add items in set using  add() methd

thisset.add("Rao")

print(thisset)

# we can add two sets also using the update() method

set1 = {"car", "bike", "aeroplane", "helicopter" }

set2 = {"ship", "supercar", "hypercar"}

set1.update(set2)
print(set1)

# usin update() method we can add any other data types also like dict and tuples and list

list1 = ["Hello", "Parveen"]

set1.update(list1)

print(set1)

# for removing items in set we have two methods discard() and remove()

set1.discard("Parveen")

set1.remove("hypercar")

print(set1)

# pop() method will remove random item from the set

set1.pop()
print(set1)

#del keyword will completey delete the set

"""del thisset

print(thisset)"""

# where as clear() method will  clear the items present in the set

set1.clear()
print(set1)

# union() method will joins two set and return a new set with both elements present in the two sets

set3 = {"Savita", "Nirmala", "Priyanka"}

set4 = {"Parveen", "Jaiparkash"}

set5 =  set3.union(set4)

print(set5)

#intersection() method will retun the items the items that will present in both the sets

set6 = {1, 3,5, 6, 7, 8}

set7 = {1, 3, 5, 9, 10, 11}

set8 = set6.intersection(set7)
print(set8)