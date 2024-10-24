# comphresnsion-----> is a way to write compact code in python

# expample we have an example of four lines

"""lst = []

for i in range(1,4):
    for j in range(5, 7):
        lst.append(i*j)
        print(lst)"""

# syntax of list comphresion
# [expression for variable in iterable

# write a program which calculate the square of number and append im the list

"""nums = [2, 3, 4, 5, 6, 7, 8]"""
"""square = []
for num in nums:
    square.append(num*num)
    print(square)"""

# we can do this in one line code using list comprension

"""print([num * num for num in nums])"""

"""nums = [1, 2, 3, 4, 5, 6, 7]
sq = []
for num in nums:
    if num%2==0:
        sq.append(num*num)
print(sq)"""


"""print([num*num for num in nums if num%2==0])"""

#
