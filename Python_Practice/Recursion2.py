# a recursive function for factorial of a number

def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)


print(fact(1))

# fibonacci series

def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-2) + fibo(n-1)



n = int(input("Enter no. of terms"))

print(fibo(n))