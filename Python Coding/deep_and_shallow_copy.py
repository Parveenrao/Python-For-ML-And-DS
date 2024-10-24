# sometime you want to have the the original value unchanged and only modify new values or vice vera

# there are two method deep copy and shallow copy

# first we have to use copy module

# best method for copy is deep copy

# copy in one list dont reflect the other list also

# memory addresses are also same in deep copy

import copy

my_list = [[1, 2, 3] , [4, 5, 6] , [7, 8,'a']]

print("id of my_list is " , id(my_list))
print("id of first  my_list is " , id(my_list[0]))
print("id of second my_list is " , id(my_list[1]))
print("id of third  my_list is " , id(my_list[2]))
new_list = copy.deepcopy(my_list)
print("-"*50)

print("id of my_list is " , id(new_list))
print("id of first  new_list is " , id(new_list[0]))
print("id of second new_list is " , id(new_list[1]))
print("id of third  new_list is " , id(new_list[2]))

new_list[2][2] = 'hello'
print(new_list)
print(my_list)