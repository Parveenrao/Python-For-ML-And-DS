""" dividing program using decorator """

def smart_Divider(func):
    def inner(num1, num2):
        if num2 == 0:
            print("Cannot divided by zero")
            return (
                func(num1, num2))
        return inner

@smart_Divider
def division(num1, num2):
    print("Division is ", num1/num2)

    print(division(10,0))
