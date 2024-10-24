laptop = {'dell' : 40000 , 'hp' : 50000 , 'mac' : 60000 , 'asus' : 70000}

budget = int(input("Enter your laptop  budget"))

def logic(ele):
    if laptop[ele] <=budget:
        return True

    else:
        return False

filtered = filter(logic , laptop)

print(list(filtered))