# constructor is automatically called when  object is invoked

""" all classes have a function callled init function that is excuted when a class is intialized"""

"""class Student:
    name = "Parveen yadav"
    def __init__(self):
        print("addding new student in the database")

s1 = Student()
print(s1.name)"""

# we can take the paramter in the constructor , and then it is called paramterized constructor

"""class Parveen:
    def __init__(self , fullname):
        self.fullname = fullname
        print("I am the hero of my life")

p1 = Parveen("karan")
print(p1.fullname)"""


# we can use any keyword other than self
# data stored in the class and objects are called variables


class Record:
    def __init__(self , name = None  , marks = None):
        if(name is None and marks is None):
            print("Default Constructor is  Called")

        else:
            self.name = name
            self.marks = marks
            print("Parameter Constructor")


r1 = Record()

r2 = Record("Karan" , 97)
print(r2.name , r2.marks)

