""" generator function in python is liike a normal function but when it need to generate value
     it does it with yield keyword"""

""" Generators are simply function that return the iterator using yiedl keyword"""

def my_gen():
    yield "Hello world"
    yield "Parveen here"
    yield "Coding with Parveen"

g = my_gen()
print(g)      # it will not print any statement


print(next(g))

print("------------------")
for ele in g:
    print(ele)