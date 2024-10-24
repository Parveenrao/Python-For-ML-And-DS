# Lets take example of student marks and his average marks .


"""class Student:
    def __init__(self , phy , chem , maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.average = str((self.phy + self.chem + self.maths) / 3)

    def calculate(self):
            self.average = str((self.phy + self.chem + self.maths) / 3)    # this is method to change average


stu = Student(20 , 20 , 20)
print(stu.average)

# now we realized that our phyics marks are wrong , take phy = 50

stu.phy = 50
print(stu.phy)
print(stu.calculate())
print(stu.average)   # but the average doesnot change"""


# so there is an another method called property decorator , so that we do not write the method agian and again


# here is the example

class Student:
    def __init__(self , phy , chem , maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property
    def average(self):
       return str((self.phy + self.chem + self.maths) / 3)


stu = Student(20 , 20, 20)
print(stu.average)

stu.phy = 50
print(stu.phy)
print(stu.average)