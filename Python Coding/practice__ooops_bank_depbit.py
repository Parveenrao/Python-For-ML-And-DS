class Bank:
    def __init__(self , bal , acc):
        self.account = acc
        self.balance = bal

    def debit(self, amount):
        self.balance -= amount
        print("Rs",amount, "was Debited form your acc")

    def credit(self , amount):
        self.balance += amount
        print("Rs" , amount , "is credited into Your account")


    def total(self):
        print("Total balance is ", self.balance)


bob  = Bank(1000 , 123343545)

print(bob.balance)
print(bob.account)

bob.debit(1000)
bob.credit(2000)
bob.total()
