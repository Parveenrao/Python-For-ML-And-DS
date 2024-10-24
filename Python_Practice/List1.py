# list is collection of values of items of different types 
# list is ordered collection

list = [20 , 'hello', 20.5,  ]
print(type(list))

# list and array are not same 
# array --> store the item of similar data types 
#list ---> store the itme of differnt data types 

# concetation of list 

arr1 = [20, 30 ,30.5 , 'hello']
arr2 = [30 , 40 , 50 , 'parveen']
arr3 = arr1 + arr2
print(arr3)

#iteration through list

list = [10, 20 ,30 ,40 ,50 ,'hello'] 

for i  in list:
    print(i)   
    
# membershp in list ---> using in operator , if and element found in the list it return true

arr4 = [10 , 'parveen' , 'hello' , 'yadav']
print('parveen' in arr4)    