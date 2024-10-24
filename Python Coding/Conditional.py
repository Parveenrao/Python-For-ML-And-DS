"""age = 21

if(age >=18):
    print("he/she can vote and applied for vote")

else:
    print("he/she cant vote")"""


"""light = 'green'

if(light == 'red'):
    print("stop")

elif(light == 'green'):
    print('go')

elif(light == 'yellow'):
    print('look')

else:
    print("end of code")

# note if-statement always check for the condition
# elif-statement check only when if statement is false"""


"""marks = int(input("Enter Your Marks : "))

if(marks >=90):
    grade = "A"

elif(marks<90 and marks>=80):
    grade = "B"

elif(marks<80 and marks>=70):
    grade = "C"

else:
    grade = "D"

print("The Grade of The Student is", grade)"""


# write a program to check whether a number is entered by user is odd or even

"""number = int(input("Enter Number :"))

if(number%2==0):
    print("Number Entered by user is even")

else:
    print("Number Entered by user is odd")"""


# write a programm to check largest among three numbers

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

if(a>b and a>c):
    print(a, "number is greatest")

elif(b>c):
    print(b, "number id greatest")

else:
    print(c, "number is greatest")