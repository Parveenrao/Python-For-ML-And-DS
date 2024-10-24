""" IN concurrent programming , sometimes we need to co-ordinate the threads

    Thread communicate with each other via signals """

# Three ways
""" By creating event object 
    By creating conditon object
    By using queue module """
#---------------------------------------------------------------
"""1) Using Event , by this ways we can communicate between two threds """

"""" Thread1-----------flag = flase------------------------Thread2"""
# both threads maintain their flag variable false
# after wait() method thread 1 sent signal to thread2

#---------------------------------------------------------------------------

#steps  first we have to creata an event object

# create two threds which will communicate

# put Thread2 in waitingn state using wait() method

# use set() method in/after t1 thread code

#------------------------------------------------------
"""1) set() method -- set internal value of flag to True 
    if flag = true waiting thread start awakened"""
""" 2) Reset-----> reset the internal flag to false   other thread will wait """
"""" 3) is_set()----> return ture if and only if internal flag is ture"""

"""4) wait[timeout) ---- calling this function keep other thread on wait until flag is true"""