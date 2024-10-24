# static method 

class Bank:
    bank_name = "HDFC"
    rate_of_interest = 12.25
    
    @staticmethod
    def simple_interest(pri , n):
        si = (pri*n*Bank.rate_of_interest)/100
        print(si)
        
pri = float(input("Enter the principle amount"))
n = int(input("Enter the numbers of years"))

Bank.simple_interest(pri , n)