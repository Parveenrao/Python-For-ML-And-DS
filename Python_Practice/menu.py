while True:
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    print('1.Additon\n2.Subtraction\n3.Multiplication\n4.Divide')
    choice = int(input('choose from above'))
    if choice == 1:
        print('Addition is :' , num1 + num2)
    if choice == 2:
        print('Subtraction is :' , num1-num2)
    if choice == 3:
        print('Multiplication is:', num1*num2)
    if choice == 4:
        print('Divide is :' , num1/num2)
    
    ans = input('DO you want to continue(y/n):')
    ans = ans.lower()
    if ans!='y':
        break        