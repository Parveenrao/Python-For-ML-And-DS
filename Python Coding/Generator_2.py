# normaly way to calculate square of numbers between 1 to n

"""n = 11

l =  [i* i for i in range(1, n)]
print(l)

import sys

print(sys.getsizeof(l))"""

# fibbo series using recursion

""""def fibbo():
    first,second = 0, 1
    while True:
        yield first
        first,second = second,first + second

f = fibbo()
for ele in f:
    if ele>=100:
        break
    print(ele)"""

# we have a function who filter out even number first funcction  and second functon calculate square of even
# and third function calculate the sum

def filter(seq):
    for num in seq:
        if num % 2 == 0:
            yield num


def even_sqaure(seq):
    for num in seq:
        yield num ** num

def summation(seq):
    total = 0
    for num in seq:
        total = total + num
        yield total


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
g = filter(numbers)
g1 = even_sqaure(g)
g2 = summation(g1)
for ele in g2:
    print(ele)


# chaining of generators

g = summation(even_sqaure(filter(numbers)))   # ----> chaining

