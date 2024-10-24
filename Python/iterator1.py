"""  program for checking whether a object is iterable or iterator"""

object1 = eval(input("Enter object "))

object_dir = dir(object1)

if '__iter__' in object_dir and '__next__' in object_dir:
    print("Iteration operation will be applied")

elif '__iter__' in object_dir:
    print("iterable operation will be applied")

else:
 print("Not supported")


"""now if we apply iter function  in object1 then it will show the iteration operation will be applied"""

object2 = iter(eval(input("Enter object ")))

object_dir = dir(object2)

if '__iter__' in object_dir and '__next__' in object_dir:
    print("Iteration operation will be applied")

elif '__iter__' in object_dir:
    print("iterable operation will be applied")

else:
 print("Not supported")

