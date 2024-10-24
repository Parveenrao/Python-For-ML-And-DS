# destructor in python is done by del keyword

class Bank:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Destructor is called")

b1 = Bank("parveen")
print(b1.name)

del b1
print(b1.name)