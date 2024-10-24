# in static method like ----> they cant change or modify the class state and general utility

"""class Person:
    name = "Parveen"

    def change_name(self , name):
        self.name = name


p1 = Person()
p1.change_name("Parveen Yadav")
print(p1.name)

print(Person.name)  #  ----> the name of the person cant be changed  """

# Class method

#a class method is bound to the class and recieve the class implict first argument

class Person:
    name = "Parveen"

    @classmethod
    def change_name(cls, name):
        cls.name = name

p1 = Person()
print(p1.change_name("Parveen Yadav"))
print(p1.name)
print(Person.name)
