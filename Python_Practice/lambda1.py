# lambda is a single line anonymns function 

addd = lambda x ,y : x+y

print(addd(10 ,20))

# important note that we can not return multiple values by lambda,  but it can be creating  a tuple 

add = lambda x, y: (x+y , x-y)

print(add(10 ,5))

# lambda function to increment a number 

no = lambda n : n+1
print(no(1))

# lambda function for finding power of a number 

power = lambda x : x**2
print(power(3))

# lambda function for convertining string to upper case

upper = lambda str : str.upper()

print(upper('parveen'))


# lambda functon for converting celsuis to farenheit

temp = lambda c: c*9/5 + 32

print(temp(30))


# ques is why we use lambda functions 


# 1 -----> lambda function is for useful for small expression and less code required
# 2------> lambda function mostly used in high order function 


# if -else in lambda function 

hi = lambda n1, n2: n1 if n1>n2 else n2
print(hi(2 ,1))


# list comphrension and lambda expressions 

arr = [2, 3, 4 ,5 ,6, 7]

print([i*i for i in arr])

# using lambda functin 

my = lambda data:[i*i for i in arr]
print(my(arr))