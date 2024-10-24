num = int(input('Enter the number'))
while True:
    for i in range(1,11):
        print(f"{num}*{i} = {num*i}")
        
    ans = input('Do you want to continue(y/n):')
    if ans!= 'y':
        break