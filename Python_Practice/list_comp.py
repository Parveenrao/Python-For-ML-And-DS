# it is way or writing compact code 

nums = [3, 6, 9, 12, 15]
"""sq = []

for num  in num:
    sq.append(num*num)
    
print(sq)   """


# now try  it with using list comphrension
 
#print([num*num for num in nums])

# now we want to calculate the square of that numbers who are even 

#print([num*num for num in nums if num%2==0 ])


result = []
for num in nums:
    if num%2==0:
        result.append(num*num)
    else:
        result.append(num*num*num)
        
print(result)           


# using list comphresion

print([num*num if num%2==0 else num*num*num for num in nums ])


out = []
for i in range(3,6):
    for j in range(5,7):
        out.append(i*j)

print(out)        


# using list comphrension

print([i*j for i in range(3,6) for j in range(5,7)])