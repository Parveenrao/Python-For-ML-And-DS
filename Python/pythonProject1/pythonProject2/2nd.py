class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

        def show_details(self):
            print("Hey my name is ", self.name)
            print("Hey my age is ", self.age)
            print("Hey my salary is ", self.salary)
            print("Hey my gender is ", self.gender)

            emp = Employee("Parveen", 22, 90000, "Male")
            emp.show_details()
