# reverse a string using while loop

"""name = input("enter string")
print('original string is', name)

reverse_str = ''
count = len(name)

while count>0:
    reverse_str = reverse_str + name[count-1]
    count = count-1
print('reverse_string is' , reverse_str)"""

# using forloop

str = input('enter string')
print('original string' , str)
r_name = ''

for char in str:
    r_name = char + r_name
    
print('reverse string is ', r_name)    