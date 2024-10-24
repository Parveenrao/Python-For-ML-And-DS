"""num = int(input("Enter your number:"))

if num>0:
    print(f"{num} is positive number")
elif num<0:
    print(f"{num} is negative number")
else:
    print("zero")"""
    
    
# using list comphrension

#print(['Postivite' if num>0 else 'Negative' if num<0 else "Zero"])


ages = [23, 78, 16 , 43, 21, 17 ,12, 48]

print([100 if ages<18 else 500 if ages<30 and ages>18 else 700 if ages<45 and ages>31 else 200 for ages in ages])