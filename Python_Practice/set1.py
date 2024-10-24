# set is an unordered collection of items of different types enclosed in curly braces

set = {'hello', 10 , 30 ,'parveen' , 1.50}
#print(type(set))


# duplicates items are not allowed in the set 

set2 = {10, 20, 30, 40 ,50, 60, 70, 10, 20, 30}

#print(set2)


# indexing and slicin are not allowed in set 

# set is mutable data types 

# we can add item in the set ---> using addd ---> the element will be add to any particular location 

set2.add(100)
#print(set2)


# elements inside the set are aslo immuatble --> means the if we add list inside an set it will throw an eror:


#set3 = {10, 20, 30, 40, [10, 20, 40,]} #---> here list is a mutable data type

#print(set3)


# we cannot make a empty set using {} this , only method is this that we can make a empty set is by using set function

s = set()
print(type(s))