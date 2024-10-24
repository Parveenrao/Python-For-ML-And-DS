# pthonn provide 4 keywords
# try  --> exception code
# exception --> code to handle exception
# else  ---> code executed if no exception occured
# finally  ---> always execution

# else and finally block are optional

"""num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))

try:
    div = num1 / num2
    print(div)

except ZeroDivisionError:
       print("Divide by zero is not possible")"""


# handle multiple Exception

"""num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

try:
    div = num1 / num2
    print(di)          # name error

except ZeroDivisionError:
    print("Divide by zero is not possible")

except NameError:
    print("Variable name is wrong")

print("Rest of code")"""

# syntax of multiple exception is

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

try:
    div = num1 / num2
    print(div)          # name error

except (ZeroDivisionError , NameError) as obj:
    print(obj)

else:
    print("Exception didnt Occur")

finally:
    print("always executed")

# if exception is occur or  not occur finally block is always executed
# else block executed when exceptin didnt occur