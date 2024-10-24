## methods are the function that belong to the object

"""class Student:
    def __init__(self,  name , marks):
        self.name = name
        self.marks = marks

    def greetigs(self):
        print("Welcome Students " , self.name)


    def get_marks(self):
        return self.marks

s1 = Student("karan" , 97)

s1.greetigs()

print(s1.get_marks())"""


# Practice Question

""" write a student class that takes name and marks of  three subjects  in constructor,  create a method to take the
     average"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        avg = sum / len(self.marks)
        print("Hi", self.name, "your avg score is", avg)

s1 = Student("Lonely", [98, 97, 95])
s1.get_avg()

s1.name = "parveen"
s1.get_avg()