# there is better way for opening and reading file in python bys using with keyword

with open("demo.txt" , "r") as f:
    print(f.read())

# if we using with keyword , no need to close the file , bezoc with kyword automatically close the file


with open("demo.txt" , "w") as f:
    f.write('can I earn 25lpa as data scientest')
