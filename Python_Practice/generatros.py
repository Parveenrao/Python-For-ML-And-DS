# A Generator is a python function that return the iterator using yield keyword.

def my_gen():
    yield "Parveen Yadav"
    
my_gen()    

#for i in my_gen():
    #print(i)
    
    
    
def gen():
    yield "Parveen"
    yield "Rao"    
    yield "Lonely"
    
g = gen()

print(next(g))
print(next(g))
print(next(g))
    