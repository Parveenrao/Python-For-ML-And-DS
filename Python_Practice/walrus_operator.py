"""data = [10,20,30,40,50,60]
n = len(data)
i=0
while i<=n:
    print(data[i])
    i = i+1"""
    
    
# using walrus_operator
data = [10, 20, 30, 40, 50, 60]
i= -1
while (i:=i+1)<(n:=len(data)):
    print(data[i])   