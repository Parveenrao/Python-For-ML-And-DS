#dictionary will be in key value pair

#lets make a program calculate the square of the number

"""nums = [1, 2, 3, 4, 6]
my_dict = {}

for num in nums:
    my_dict[num] = num*2
print(my_dict)
print("_"*50)
# lets make this code into dictionary comphrension

print({num:num*2 for num in nums})"""

# print square when number is even

nums = [1, 2, 3, 4, 6]
my_dict = {}

for num in nums:
    if num %2==0:
        my_dict[num] = num*2
print(my_dict)

print({num:num*2 for num in nums if num%2==0})
