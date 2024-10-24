# property decorator

class Name:
    def __init__(self,first ,last):
        self.firstname = first
        self.lastname = last
    @property    
    def mail(self):
        return f'{self.firstname}{self.lastname}@gmail.com'
    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'
    
    
    
e = Name('Parveen' , "Yadav")

print(e.mail)
print(e.fullname)   