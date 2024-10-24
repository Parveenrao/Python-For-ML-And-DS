f = open('hello.txt')
f.close
# when we close the file , the file content is no longer accessible , when we try to open it again
f.read()

# what happen when do not close the file ----> after program execution the python garbage collector will automatically destroy the file 
# Note ---> do not rely on garbage collector ---> lets assume that we perform some operation the file and we forgot to close the file 
# so in this way garbage collector will remove the content of the file 

with open('database.txt' , 'w') as f:
    f.write("I am a great data scientist and i want to earn around 25 lpa")