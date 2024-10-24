# all method we are used are non - static method
# for non_static method we use self parameter
# static method allows to not use self parameter

# they work at class level , they do not work at classs level


# they are called decorator , they used to change the behaviour of the function
# simply wrap another function to change the behavoir of the wrapped function without permanently modifying it


class Record:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def greeting():
        print("Hello ")


r1 = Record("Parveen" , 98)

r1.greeting()

