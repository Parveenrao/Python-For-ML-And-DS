# a function  without name is called lambda function
#  single line , anonmyns function
# written using lambda name
# lambda function can take any no. of arguments and return only one statements

additon = lambda a : a+12

print(additon(4))

X = lambda x ,y : x * y
print(X(2 ,3))

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_new_list = list(filter(lambda x : x % 2 == 0 , num))
odd_new_list = list(filter(lambda x : x % 2 != 0 , num))

print(even_new_list)
print(odd_new_list)


f = lambda x: x if x % 2 == 0 else None
result = f(6)
print(result)

greet = lambda: "Hello, World!"
result = greet()
print(result)

students = ['Alice', 'Bob', 'Charlie', 'David']
sorted_students = sorted(students, key=lambda x: len(x))
print(sorted_students)
