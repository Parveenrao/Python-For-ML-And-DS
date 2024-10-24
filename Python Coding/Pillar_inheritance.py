""" when one child clsss inherit the properties of another parent class is called inheritance"""

# Single Inheritance
"""class Car:       # Parent class
    @staticmethod
    def start():
        print("Car Started")

        @staticmethod
        def stop():
            print("Car stop")


class Toyota(Car):
    def __init__(self , name):
        self.name = name


car1 = Car()
car2 = Toyota("nexus")

print(car2.name)

car2.start()"""

# Multilevel Inheritance ----> base class ---derived classs ---derived classs

"""class Animal:   # ----> Parent classs(Base)
    @staticmethod
    def Roar():
        print("Animal Sound")

class Dog(Animal):      # ----> child CLass(Derived Class)
    @staticmethod
    def barks():
        print("Dog barks")

class Puppy(Dog):    # ------> Derived classs
    @staticmethod
    def speak():
        print("Puppy yaps")


puppy = Puppy()
puppy.speak()

puppy1 = Puppy()
puppy1.barks()

puppy2 = Puppy()
puppy2.Roar()"""


# Mulitple Inheritance

# multiple inheitance allows you to inherit subclass form more than one super class

"""class Animal:
    def Roard(self):
        print("Animal sound")

class Bird:
    def Flying(self):
        print("Birds flying")

class FlyingDog(Animal , Bird):
    def Brak(self):
        print("Flying Dog Barks")

fly = FlyingDog()

fly.Roard()
fly.Flying()"""

# Super method  is used to call the constructor or method of parent class in the subclass.

class Animal:
    def __init__(self , name):
        self.name = name

    def Roar(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   #----> call the constructor of parent class
        self.name = name
        self.breed = breed

    def speak(self):
        print(f"{self.name} of {self.breed} barks")


dog  = Dog("Buddy" , "German")
dog.Roar()

# Hierarchical Inheritance

class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Dog barks
print(cat.speak())  # Output: Cat meows

# Hybrid Inheritance

class Animal:
    def speak(self):
        return "Animal sound"

class Mammal(Animal):
    def has_fur(self):
        return True

class Bird(Animal):
    def fly(self):
        return "Bird is flying"

class Bat(Mammal, Bird):
    def speak(self):
        return "Bat screeches"

bat = Bat()
print(bat.speak())  # Output: Bat screeches
print(bat.fly())    # Output: Bird is flying
print(bat.has_fur())  # Output: True