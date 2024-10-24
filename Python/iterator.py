
""" iterator is  an object which allows programmer to traverse the  sequence of data without storing them
    in memory """

""" iteration  =  process of taking each element one after another , example like for loop"""

""" iterable =  whom iteration is performed , container of multiple items"""

data  = [10, 20, 30] # iterable
for ele in data:
    print(ele)       # iteration

""" for iterator , python provide us a built in function clled iter 
          in which pass the parameter and for fetching element we have next function"""

data1 = [10, 20, 30, 40]
iter_obj =  iter(data1)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

""" we also use the.__iter__method"""

data2 = [50, 60, 70, 80]
iter_obj = data2.__iter__()
print(iter_obj.__next__())

