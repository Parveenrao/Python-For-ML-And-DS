class FiveDivisionError(Exception):
    "this is the exception class called when five divsion happens"
    def __int__(self):
        print("Cant divide by 5")


try:
    num1 = int(input("Enter number1 :"))
    num2 = int(input("Enter number2 :" ))
    if num2 == 5:
        raise FiveDivisionError
    div = num1/num2
    print(f"Division is {div}")

except(FiveDivisionError ,ZeroDivisionError) as var:
    print(var, end = "")


# write a program for five divsion error 

