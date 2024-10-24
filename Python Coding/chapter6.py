"""nums = [1, 4, 9, 16, 25]
for val in nums:
    print(val)"""

# important note that , if are working on stopping condition or increment and decrement a variable then we use
# while loops
# if we want to traverse the elements then we use for loops


"""str = "My Name Is Parveen Yadav"

for char in str:
    if(char == 'Z'):
        print("y found")
        break
    else:
        print(char)"""

# write a program to traverse the element in the list and trace its index using for lopp

"""num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 49
index = 0


for element in num:
    if(element == x):
     print("element fount at index", index)
    index+=1"""

# range retrun sequence of numbers

"""for i in range(5): # stopping condition
    print(i)"""

"""for i in range(2, 10): # range(start , stop)
    print(i)"""

"""for i in range(2, 10 ,2): #range(start stop gap)
    print(i)"""

# print all the even number  1 to 100

"""for i in range(2 ,100 ,2):
    print(i)"""

"""for i in range(100, 1 , -1):
    print(i)"""

# print tabel of any number using for loop

"""number = int(input("Enter number"))
for i in range(1, 11):
    print(number * i)"""

# pass statement  , when we want that we dont want any work on loop so we simply use pass statement

for i in range(6):
    pass
print("Helllo parveeen")

