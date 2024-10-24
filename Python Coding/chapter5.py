# while loop

# let write a program that print hello parveen 5 times

"""count = 1

while count<=5:
    print('Hello Parveen')
    count = count+1"""


"""i = 1

while i <= 1000000:
    print("Rao Sabh", i)
    i = i+1"""


# write a program to print number 1 to 100

"""i = 1
while i <= 100:
    print(i)
    i+=1"""

# write  a program to print number 100 to 1

"""i = 100
while i > 1:
    print(i)
    i-=1"""

# write a program to print the table of number n

"""number = int(input('Enter your number'))

i = 1

while i <=10:
    print(number * i)
    i+=1"""

# write a program that print the list using loops

"""list = [1, 4, 9, 16, 25, 36, 49, 81, 100]

index = 0

while index <len(list):
    print(list[index])
    index+=1"""

# write a program to check whether a number present in the tuple or not

"""num = (1, 4, 9, 16, 25, 36, 49, 81, 100)
x = 36

i = 0
while i < len(num):
    if(num[i] == x):
        print("number found at index", i)
        i += 1"""


# break statement is used to terminate a condition

# like a simple program where we print number 1 to 5

i = 1
while i < 5:
    print(i)
    if(i==4):
        break
    i+=1

# another statement called continue , which skip the particular element whom continue statement is applied

i = 0
while i <= 5:
    if(i == 3):
        i+=1
        continue
        print(i)
        i+=1
