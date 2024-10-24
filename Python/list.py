list1  = [1, "My", 2, "Name", 3, "is", 4, "Parveen", 5, "Yadav"]

print(len(list1))

print(type(list1))

print(list1[2:5])

print(list1[2:])

print(list1[-5:-1])

if "Parveen" in list1:
    print("Yes  ,Parveen is present in list1")

list1[0] = 0
print(list1)

list1[1:3] = ["Golden, bird"]

list1.insert(9, "John")

print(list1)


list1.append("Golden")
print(list1)

print(len(list1))


#extend method add any data type to list

cars = ["ferrari", "Merecedes", "lamborghini"]
oldcare = ["maruti", "alto", "santro"]

cars.extend(oldcare)

print(cars)

cars.remove("alto")
print(cars)

cars.pop()  #pop remove last element if index is not specified
print(cars)

del cars #completely delete the list

oldcare.clear()   #clear method complete the element of list

print(oldcare)

for b in list1:
    print(b)





fruits = ["apple", "banana", "cheery"]

newlist = [x for x in fruits if 'a' in "x"]
print(newlist)