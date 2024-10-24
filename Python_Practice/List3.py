# maximum element in the list/array unsing inbuilt function and using by our own logic

"""l1 = [10, 20 ,30 ,40 ,50 ,60]
print(max(l1))"""

# now using own logic 
def largest(arr , n):
    max = arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max = arr[i]
        
    return max

arr = [10, 324, 123232, 90 , 9488] 
n = len(arr)

ans = largest(arr , n)    
print(ans)


#minimum element in the array 

def minimum(arr ):
    mini = arr[0]
    for num in arr:
        if num < mini:
            mini = num
    return mini


arr = [10 ,4, 20 ,50 ,1]

ans = minimum(arr)

print(ans)        

       
    