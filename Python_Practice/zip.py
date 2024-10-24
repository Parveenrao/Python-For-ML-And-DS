#zip function aggregates elements from two or more iterables

students = ['Jaiparkash' , 'Savita' , 'Nirmala' , 'Parveen' , 'Priyanka']
roll_no = [321, 322, 323, 324, 325]
marks = [100 , 90 , 80 , 70 ,60]

items = zip(students , roll_no , marks)
for item in items:
    print(item)


for item in zip(students , roll_no , marks):
    print(item)    