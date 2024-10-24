#hierarchical inheritance

class Person:
    def __init__(self,name , age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, salary):
        self.salary = salary


class Student(Person):
    def __init__(self, name, age , marks):
        super().__init__(name, age)
        self.marks = marks


s = Student("Parveen" , 22 , 90)
print(s.__dict__)                
        
        