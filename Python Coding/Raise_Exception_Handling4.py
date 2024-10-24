try:
    age = int(input('Ennter your age :'))
    if age<0:
     raise ValueError
    print(f"your age is {age}")

except ValueError:
    print("Enter valid age")