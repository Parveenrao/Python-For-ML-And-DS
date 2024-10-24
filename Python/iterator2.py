""" so we have  a question to , iterate the loop without using  built in for loop
     so in this case we have to make our own loop and using iterator"""

"""we have a list of certain elements """
L = [10, 20, 30, 40]

def my_own_loop(iterable):

    iterator = iter(iterable)

    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

            my_own_loop(L)





my_own_loop(L)







