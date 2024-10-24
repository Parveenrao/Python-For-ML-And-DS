""" short way to create a generator """
"""" write  a program to print the the square of nubers"""

# 1 using list comphresion
n = int(input("Enter your number"))
L = [i*i for i in range(1,n)]

print(L)

# 2 . using generator technique
# if we remove the square brackets then it will be become the generator

n= int(input("Enter Number"))

G = (i*i for i in  range(1, n))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
