# if elif else in list comphresnion
"""num = int(input("Enter number"))
if num>0:
    print("Positive")

elif num<0:
    print("Negative")

else:
    print("Zero")"""

#if-eilif-else in list comphrension is given by

"""print(["Positive" if num>0  else "Negative"   if num<0  else "zero"])"""

# this is called chaining

# every code cannot be converted into list comphrension


# let take an another example


"""nums = [90 , 0, -33, 34, -21, 20]
status = []
for num in nums:
    if num>0:
        status.append("Positive")
    elif num<0:
        status.append("Negative")
    else:
        status.append("Zero")
print(status)

print("-"*50)

print(["Positive" if num>0 else "Negative" if num<0 else "zero" for num in nums])"""

print("-"*50)


checkup_fee = []
ages = [23, 78, 16, 41, 43, 21, 17, 12, 48]
for age in ages:
    if age<18:
        checkup_fee.append(100.0)
    elif age<30 and age>18:
        checkup_fee.append(500.0)
    elif age <48 and age>31:
        checkup_fee.append(700.0)
    else:
        checkup_fee.append(150.0)

print(checkup_fee)

print("-"*50)

print([100.0 if age>18 else 500.0 if age<30 and age>18 else 700.0 if age<48 and age>31 else 150.0 for age in ages])

