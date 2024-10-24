f = open("demo.txt", "r")

data = f.read()
print(data)
print(type(data))
f.close()

# if we are open a file and , we cant set any mode of the file so its default mode is read mode

# and in deafult read mode we cant do an other option  just only read file

# "w"---> this mode is used for write , firts turncate the file and overwrite

# "t"---> this mode  is used for open text files

# "b"----> this mode is used for open binary file

# "+" ----> this mode is used for updating , is we want both operation at same time(read and write ,, r+ ,w+)

# "x"----> this mode is used for create new file and open for wriiting

# read and text mode( r, t)  are default mode


