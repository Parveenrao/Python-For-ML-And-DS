# circle classs

"""class Circle:
    def  __init__(self , radius):
        self.radius = radius


    def Area(self):
        return 3.14 * self.radius **2

    def Perimeter(self):
        return 2 * 3.14 * self.radius



c1 = Circle(21)
print(c1.Area())
print(c1.Perimeter())"""


# Employe class

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_detail(self):
        print(f"Role is {self.role}")
        print(f"Department is {self.department}")
        print(f"Salary is {self.salary}")

class Engineer(Employee):
    def __int__(self , name , age):
        self.name = name
        self.age = age
        super().__init__("Engineer" , "IT" , "75,000")

e1 = Engineer("Parveen" , "40")
e1.show_detail()