# character class in python ---> refer to set of character that you can define using regular expression
"""import re
pattern = r"[0-9]"
data = " The Price is $100"

match_iter = re.finditer(pattern , data)

for match in match_iter:
    print(match)

# finditer return iteration and findall() method return list of number


import re
pattern = r"[0-9]"
data = " The Price is $100"

match_list = re.findall(pattern , data)
print(match_list)

# if not match then it will return a empty list

import re
pattern = r"[a-z]"
data = " The Price is $100"

match_list = re.findall(pattern , data)
print(match_list)

# return all the character present in the data

import re
pattern = r"[A-Z]"
data = " The Price is $100"

match_list = re.findall(pattern , data)
print(match_list)"""


import re
pattern = r'[^a-z0-9]'  # ^exculde all the character
data = " The Price is $100"

match_list = re.findall(pattern, data)
print(match_list)

