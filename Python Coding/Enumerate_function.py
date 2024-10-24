# keeps a counter o iterate and return it

# enumerate(iterable syntax = [0])
import json

sports = ['cricket' , 'hockey' , 'badminton' , 'football']

enum_obj = enumerate(sports)
print(enum_obj)  # returns a object

print(type(enum_obj))

for pos , ele in enumerate(sports , 1):
    print(f"{pos} : {ele}")

# conversion

data = print(dict(list(enumerate(sports ,  1))))

f = open('data.json' , 'w')


json.dump(data,f)

f.close()
