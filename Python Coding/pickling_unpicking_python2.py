class Student:
    def __init__(self,name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"name is {self.name}\n roll_no is {self.roll_no} \n marks is {self.marks}")

