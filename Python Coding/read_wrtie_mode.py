
# ""r+" ----> mode read and write file , but when we write it overwrite at the beginning

"""f = open("database.txt" , "r+")
f.write("Hello")
print(f.read())
f.close()"""

# "w+"----> this mode is writing and reading , first it turncate the whole file

f = open("database.txt" , "w+")
f.write("Hello")
print(f.read())
f.close()
