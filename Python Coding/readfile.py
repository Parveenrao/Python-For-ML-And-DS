# we have learnt how to open and read file

# now we are learn some more opeation on reading files

# readline ----> this opeartion read file line by line

f = open("demo.txt" , "r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

# if there is no data or line , then the readline operation show empty space

# always rememebr that after open file , close the file

f.close()