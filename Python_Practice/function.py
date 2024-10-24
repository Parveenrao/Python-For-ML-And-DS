# function is an organizable code of reusable code 
# functions can be called any no of times

# function contain set of instruction which perform special task 

# for example , write a function to calculate simple interest 

def interest(principle , rate , year):
    principle = float(input('Enter amount'))
    rate = float(input("Enter the rate on interest"))
    year = float(input("Enter year "))
    
    si = (principle * rate * year)/100
    
    print(f"Simple interest is {si}")
    
    
interest()   