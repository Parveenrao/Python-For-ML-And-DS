# append method in list ---> this method adds a single item to the list
# it modify the list , dont create  a new list 

"""l1 = [12, 13, 14, 15, 18, 19]
l1.append(3)
print(l1)"""

# adding multiple items in the list

"""bowlers = []

for i in range(3):
    name = input('Enter name you want to add/n')
    bowlers.append(name)
   
print('bowlers name', bowlers)    """


# append the second list into first list

l1 = ['chemistry' , 'physics', 'biology' , 'maths']
l2 = ['poonam' , 'vinay' , 'monu' , 'rachna']

"""for i in l2:
    l1.append(i)


print(l1)"""


# we can use extend method to add element in the list

l1.extend(l2)
    
print(l1)   
