num = [10 , 20 , 30 , 40 , 5 , 6 ,90 , 8 ,100]
max_list = list(filter(lambda num : num>30 , num))
print(max_list)

# double the no

list2 = [10, 20, 30, 40,50]

list3 = list(map(lambda x: x*2 , list2))
print(list3)

#power of a no. using pow()

list5 = [1, 2, 3, 4, 5]

list6 = list(map(lambda x:pow(x, 3), list5))

print(list6)