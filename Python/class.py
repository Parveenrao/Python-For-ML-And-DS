class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show(self):
    print("my name is " + self.name)

    p1 = Person("Parveen", 22)
    print(p1.show())


