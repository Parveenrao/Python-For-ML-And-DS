from functools import reduce
list1 = [10, 20, 30, 40, 50, 60, 70, 80]

sum = reduce(lambda x,y:x+y , list1)
print(sum)

mul = reduce(lambda x,y: x*y, list1 )
print(mul)