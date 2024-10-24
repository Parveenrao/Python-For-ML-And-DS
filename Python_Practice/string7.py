# replace method in python 

"""msg = 'C is a object-oriented language and  C it is very easy'

new_msg = msg.replace('C', 'Python' )
print(new_msg)"""

"""msg = "Parveen"
new = msg.find('r')
print(new)"""

# centre() --> method align the centre to the by filling paddings left and right 

"""msg = "Parveen is a living Legend"

new = msg.center(len(msg)+10, '*')
print(new)"""

msg = 'i want to become a python programmer'

new = msg.split()
print(new)


countries = 'india, america, pakistan, russia, australia , canada, france'
country = countries.split(',')
print(len(country))


for coun in country:
    print(coun)
    
l = ['p','a','r','v','e','e','n']

str = ''.join(l) 
print(str)   