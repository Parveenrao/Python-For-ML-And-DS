name = 'hello , welcome'

print(name.startswith('he'))
print(name.endswith('ome'))

print('-'*50)

# removing characters from the string

#lstrip() -- remove any leading character from  the string

name = input("Enter your name")
print(name)

name = name.lstrip()
print(name)


# strip()--> remove leading and trailing character from the string 