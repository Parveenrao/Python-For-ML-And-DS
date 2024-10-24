# write a program which calculate the sqaure of those number which is divisible by 2 and 3

""""nums = [1, 2, 3, 4, 5, 6, 7, 8]
sq = []
for num in nums:
    if num%2 == 0:
        if num%3 == 0:
            sq.append(num*num)
print(sq)

# now try this using list comphrension

print([num*num for num in nums if num%2==0 if num%3==0])"""

# if else using list comphrension

"""nums = [1, 2, 3, 4, 5, 6, 7, 8,9]
result = []
for num in nums:
    if num%2==0:
        result.append(num*num)
    else:
        result.append(num*num*num)
print(result)

print("--"*50)

print([num*num if num%2== 0 else num*num*num for num in nums])"""

list= []
for i in range(3,6):
    for j in range(5,7):
        list.append(i*j)
print(list)
print("-"*50)

print([i*j for i in range(3,6) for j in range(5, 7)])



# the big advantage of list comphrension is it make code non readable



