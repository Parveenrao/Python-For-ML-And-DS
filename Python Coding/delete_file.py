# we cant directly remove the file , we need a module callled os

"""import os

os.remove("demo.txt")"""


# practice ques

"""with open("practice.txt" , "w") as f:
    f.write("Hi everyone\n we are learning File I/o\n")
    f.write("using python\n I am using python\n")"""

# write a program that replace occuurrences of python with java

"""with open("practice.txt" , "r") as f:
    data = f.read()

new_data = data.replace("python" , "Java")
print(new_data)


with open("practice.txt" , "w") as f:
    f.write(new_data)"""


 # write a function if a particular word is in the file or not

def check_word(word):
    word = "learning"
    with open("practice.txt" , "r") as f:
        data = f.read()
        if (data.find(word) != -1):
            print("Found")
        else:
            print("Not found")


check_word("learnning")