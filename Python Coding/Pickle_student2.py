import pickling_unpicking_python2 , pickle
n = int(input("Enter no. of employess"))
f = open('hello.txt' , 'wb')
for i in range(n):
    marks = float(input("Enter marks "))
    name = input("Enter name")
    roll_no = int(input("Enter roll_no"))
    obj = pickling_unpicking_python2.Student(marks, roll_no, name)
    pickle.dump(obj, f)