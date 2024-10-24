# regex stands for regular expression

# special search pattern to find and manipulate txt

# Uses of rege
# 1 mobile validation --> should contain 10 digit
# 2 email validation

# to create translators ---> compilers , interpretor and assemblers

# for syntax and lexical analysis

# data extraction

# data cleaning and formatting data

# wrb scrapping


# basic search function in Regex

# 1 search() function ---> re.search(pattern , data)
"""import re
pattern = "python"  # pattern to be searched
data = "python is very powerful and python has lots of features" # data to be search in

match = re.search(pattern , data)
print(match)
print(type(match))

pattern = "xyz"
data = "python is very powerfull and python has lots of features"

match = re.search(pattern , data)
print(match)        # return none

# if we write python in uppercasse then it will return none ,

pattern = "python"
data = "PYTHON is a very powerfull and it has a lots of features"

match = re.search(pattern , data , re.IGNORECASE)    # we write ignorecse
print(match)

if match:
    print("Found" , match.group())
else:
    print("Not Found")"""
import re

# search() and match() ---> in search pattern is found anywhere , but in match() , pattern found at very begining

"""pattern = "python"
data = "Hello i am learning python"

match = re.match(pattern , data )
print(match)                        # return none because python is not found at beginning"""

# Regular expresssion object can be created in two ways first is simple string and second one is regular expression object
# using compile() method

pattern = re.compile("python") # in case of flags we use insdie compile method

data = "python is a very powerfull language"

match = re.match(pattern , data)
print(match)

print(type(pattern))