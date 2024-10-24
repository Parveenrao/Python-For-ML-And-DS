name = input("Enter your name").lower()
list = ['parveen' , 'shruti', 'yadav', 'savita']
if name in list:
    print(f'{name} is present in the list')
else:
    print(f'{name} is not present in the list')
    
    
# length of list ----> 
l1 = [12 , 14, 15, 'hello', [1, 2, 3]]

print(len(l1))
    
count = 0
for i in l1:
    count = count+1
print('length of list is ' , count)
        
    
    