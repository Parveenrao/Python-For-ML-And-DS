# Recusrion ---> a function call itself is called recursion

"""def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)"""

"""def fact(n):
    if(n == 0 or n == 1):
        return 1

    return fact(n-1) * n

print(fact(4))"""


def sum(n):
    if(n == 0):
        return 0
    else:
     return n + sum(n-1)

print(sum(5))