# map is also an high order function .

# map function return a map object which is an iterator 

names = ['Parveen' , 'Savita' , 'Nirmala']

def get_length(name):
    return len(name)

mapped = map(get_length , names)
print(list(mapped))

# using lambda expressions

ob = map(lambda str : len(str), names)

print(list(ob))