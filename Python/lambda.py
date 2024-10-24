# lambda is a anoynomus function which can take any type of any argument and return only one statement

x = lambda x, y,z: x+y+z

print(x(5, 6, 7))

#lambda function is used without any name and without def keyword.

add = lambda x: x+100
print(add(200))

mul = lambda x, y: x*y
print(mul(3 , 15))

product = lambda x , y ,z : x*y*z
print(product(3,3,3))

#we can also use *args parameter to define many arguments

addtion = lambda *args: sum(args)
print(addtion(20 ,200, 2000,))

# for find if a susstring is in a string or not

sub_string = lambda string: string in "Welcome to the pycharm community"

print(sub_string("Parveen"))

print(sub_string("Welcome"))


