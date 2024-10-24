# tupple is collection of items of different data types 

# tuple is unchangeable , immmutable 

# list can be change (elements can be change , add ,remove and update)
# where elements in the tuple cannot be chnage

# tuple is nearly similar to the list 

tuple = ('parveen' , 1 ,3 ,20.5 , ['Jaiparksh' , 'Savita'])

# tuple can contain duplicates item also 

# packing and unpacking in tuple ----> we can perfrom pack and unpack in iterables like tuple and list 

tuple4 = (101 , 'parveen', 90.2 , 'A+' , 'Yadav')    # packing 
roll_no , name , marks , grade , s_name = tuple4      # unpacking

#print(roll_no)
#print(name)


data = (101 , 'raj' , ('cricket' , 'chess'))    # nested tuples 

# concatenation of tuples 

data1 = ('parveen' , 'savita' )
data2 = ('jaiparkash' , 'nirmala' , 'priyanka')

family = data1 + data2
#print(family)


# deletion of entire tuple 

del data

# membership in tuple 

#info = ("Jaiparkash" , "Savita" , 'Nirmala' , "Parveen" , "Priyanka")
#name = input('Enter name you want to check')


"""if name in info:
    print(f"{name} is present in the info")
else:
    print(f"{name} is not present in the info")"""
    
# iterating in tupel 

#for ele in info:
    #print(ele)    
    
""""index = 0
while index<4:
    print(info[index])
    index = index + 1    """
    
# Important methods in tuple 

info = ("Jaiparkash" , "Savita" , 'Nirmala' , "Parveen" , "Priyanka", "Parveen" , "Parveen")
#print(info.index("Savita"))

# count method --> count the occurences of the element
#print(info.count('Parveen'))


# inbuilt function in tuple min max ans sum

count = (10, 20, 30, 40, 50 ,60, 70,  80, 90)
print(min(count))
print(max(count))
print(sum(count))

print('-'*50)


#paranthesis in tuple in optional , we can create a tuple without paranthesis

t1 = 'hello', 1 ,3, 5, ['parveen' , 'sys']

print(type(t1))

import sys



# tuple is memory efficient , take less memory than list

l1 = [1, 2, 3, 4, 'hello']

print(sys.getsizeof(t1))
print(sys.getsizeof(l1))


# there is no concept comphrension in tuple, where list comphresion is valid 

# list suport pack and not supoort unpack

# tuple support both pack and unpack