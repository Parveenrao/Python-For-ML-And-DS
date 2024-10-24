"""dictionary are used to store elements in key value pair , which are ordered and changeable"""

thisdict = {

    "brand": "ford",
    "name" : "endaver",
    "year" : 2000,
}

print(type(thisdict))

print(len(thisdict))

print(thisdict["brand"])

print(thisdict.get("year"))   # get method is used to return elements

print(thisdict.keys())    # keys method return all keys present in the dictionary

print(thisdict.values())  # values method return all values present in the dictionary



thisdict["name"] = "Parveen"

print(thisdict)

thisdict["color"] = "red"

print(thisdict)

# item method is used to return all element in the tuple form

print(thisdict.items())

#update method is used to update key value pair in the dictionar

thisdict.update({"color": "yellow"})

print(thisdict)

print(thisdict.pop("name")) # pop method delete item with sepcified key
print(thisdict)

thisdict.popitem()  #popitem remove the last inserted item
print(thisdict)

#del thisdict  # completely remove the dictionary

#thisdict.clear()     # clear method clear the contents of the dictionay

#print(thisdict)


for x in thisdict:
    print(x)

# values method is also used to return values throght loops

for x in thisdict.values():

    print(x)

# same key method is used to return keys through loops

for x in thisdict.keys():
    print(x)

# we can also return all the items using loops

for x ,y in thisdict.items():
    print(x, y)