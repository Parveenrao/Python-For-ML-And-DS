"""import sys

def format_traceback(exc_type , exc_value , exc_traceback):
    print("Something went wrong")
    print(exc_type)
    print(exc_value)
    print(exc_traceback)

sys.excepthook = format_traceback

def display():
    print(1 + "hello")   #----> this function cals excepthook

display()"""

# exception handling for taking input

def square():
    try:
     num = int(input('Enter the number'))
     print(f"the square is {num**2}")

    except Exception as e:
        print(e)

    square()


square()
