# sometimes you want to have the original values unchanged and only modify the new values

# there are two methods in python or copies ,,, deep copy or shallow copy

# we have a copy module


# Shallow copy

import copy

mylist = [[1,2,3] , [4,5,6],[7,8,'a']]
print(f"id of mylist is {id(mylist)}")

newlist = copy.copy(mylist)
print(f"id of newlist is {id(newlist)}")


# deepcopy

list1 = [[1,2,3],[4,5,6],[7,8,'a']]
print(f"id of list1 is{id(list1)}")


list2 = copy.deepcopy(list1)
print(f"id is list2 is {id(list2)}")

list2[2][2] = 9

print(list1)
print(list2)