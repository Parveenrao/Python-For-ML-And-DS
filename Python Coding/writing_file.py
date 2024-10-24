
# "w"----> mode is used to write file

f = open("demo.txt" , "w")

f.write("I want to learn , generative artifical intelligence")
f.close()

f = open("demo.txt" , 'r')
data = f.read()
print(data)

f.close()
# so we can cleary see that write "W" mode completely delete the old file and overwrite it







