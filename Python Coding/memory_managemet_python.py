# memory management in important because it is essentail for efficiently written code

# there are two concept in memory management
#---> memory allocation---> allocate memory to objects
#---->memory deallocation----> object which are not used , so remove these objects


# memory management is python is automatically
# two scripts are required
# python memory manager---> allocate
# python garbage collector---> deallocate

# there are two types of memory

# 1 stack memory---> static memory(slow and can be directly accessible)
# 2 heap memory ----> dynamic memory(fast and cant be accessed directly  , access by using refernce variable)


# global reference and function and names memory are allocated in  stack

# all values and object are allocated in heap memory

# stack memory ---->allocate by compiler
# heap memory----> allocate by interpreter

# lets understand through an example

num1 = 100
num2 = 200

def add(x ,y):
    result = x +y
    return result

result = add(num1, num2)

# in stack memory ----> num1 , num2 , addd() , x, y, result
# in heap memory ----> 100 ,200 ,300(x+y)