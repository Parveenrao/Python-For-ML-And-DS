# genrator function does not take any input like decorator but return genrator object

# generator object is like iterator which generate next term

def my_gen():
    yield "hello world"  # use yield keyword instead of return
    yield "Parveen Yadav"
    yield "Lonely"

g = my_gen()  # for print the value inside the function use next keyword
print(next(g))
print("--------")
for ele in my_gen():
    print(ele)

# like iteraton , generator function remember last word , and print next word.
# it also dont store word in memory , when we call any particular value then the value be saved .

import time

def cout_down(num):
    print('Countdown Starting')
    while num >0:
        yield num
        num = num-1

c = cout_down(5)

for ele in c:
    print(ele)