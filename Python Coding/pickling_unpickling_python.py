"""import pickle
data = ['Parveen', 'yadav', 'john', 98, 99]

byte = pickle.dumps(data)
print(byte) #this is called


# unpickling
data = pickle.loads(byte)
print(data)"""


# now we learn to convert python objects into bytes in file

import pickle
data = ['Parveen', 'Rao', 'John', 'Lonely']
f = open('data.json' , 'wb')
pickle.dump(data , f)

