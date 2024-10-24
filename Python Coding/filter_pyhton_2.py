str = "parveen"

vowel_list = ['a', 'i', 'e', 'o', 'u']

"""def vowel(char):
    if char in vowel_list:
        return True
    else:
        return False


filter_object = filter(vowel , str)
print(list(filter_object))"""

"""filterd_objects = filter(lambda ch: ch in vowel_list , str)
print(list(filterd_objects))"""

data = {'Nitesh': 78 , 'Parveen':98, 'Raj':91, 'Amar': 90 , 'Abhi': 81}

filter_object = filter(lambda students : data[students] >90 , data )

print(list(filter_object))


