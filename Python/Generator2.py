"""" program for fibonacci series with generator technique"""

def fib():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second

g = fib()
"""print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))"""

# we can print the elements of the  fibonaaci series using generator

for i in g:
    if i >= 100:
     break

     print(i)
