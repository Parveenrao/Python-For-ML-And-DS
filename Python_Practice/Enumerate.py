# keeps a counter to iterable and return it

enu = ['kabbadi' , 'cricket' , 'hockey' , 'shooting']

enu_obj = enumerate(enu , 1)
print(enu_obj)

for i in enu_obj:
    print(i)