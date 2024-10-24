# add  , update , remove, pop , clear method in set


w_days = {'monday' , 'friday' , 'saturday'}
w_days.add('sunday')     #--------> add method add element in random position
w_days.update(['tuesday' , 'thrusday'])    # ---> update method add multiple elements in the set

w_days.remove('monday')    # ---> remove method will remove single element from the set

w_days.discard('thrusday')



# the basic difference between remove and discard is that remove element will throw error while we remove the already removed element
# discard method will not throw an error 

# pop method in set will remove any random element in the set

w_days.pop()


# clear method will clear all the elements in the set , while maintain the structure of the set

w_days.clear()
print(w_days) 