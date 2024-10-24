# iterate over string 
name = "Parveen"
for i in name:
    print(i)
    

print('-'*50)

# len of strin without using len function 

"""str = input("enter string")
counter=0
for char in str:
    counter+=1
    print('length of given string is ' , counter)"""
    
# membership operator in python 

name = 'parveen'  

print('cd' in name)  

print('pa' not in name)


print('-'*50)

# check whether the vowel present in the given string or not 

str = input('Enter the string')
vowels = ['a', 'i', 'e', 'o', 'u']
counter=0

for char in str:
    if char in vowels:
        counter+=1
print('number of vowels', counter)            
    
    
    
  