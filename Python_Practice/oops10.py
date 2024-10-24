# multiple inheritence

class Dog:
    def dog(self):
        print(f"dog barks")
 
class Cat:
    def cat(self):
        print(f"cat meow")


class Animal(Dog, Cat):
    pass


a = Animal()
a.cat()
a.dog()              
        