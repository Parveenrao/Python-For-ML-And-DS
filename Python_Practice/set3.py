# union in set 
set1 = {20, 30, 40, 50, 60}
set2 = {20, 40, 50, 50}

set1|set2 
u = set1.union(set2)
#print(set1)

#print(set1&set2)
i = set1.intersection(set2)

# difference between two sets in python 

A = {10, 20, 30, 50, 70}
B = {10, 20, 30, 60 ,80}

c = A - B

d = A^B     #---> symmetric difference (uncommon elements) 
print(d)