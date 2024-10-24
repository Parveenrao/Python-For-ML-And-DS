import time

class BalanceExceptionError(Exception):
    pass

class AttemptExceptionError(Exception):
    pass

attempts = 1

def withdraw():
    global attempts
    saved_pin = 1234
    balance = 10000
    pin = int(input("Enter your pin value"))

    if pin == saved_pin:
        try:
            amt = float(input('Enter amount to withdraw'))
            temp_bal = balance - amt
            if temp_bal < 1000:
                raise BalanceExceptionError("Insufficient Balance")

            balance = balance - amt
            print("Remaining balance is " , balance)

        except Exception as var:
            print(var)


    else:
        ans = input("wrong pin , Do you want to continue (y/n)")

        if ans.lower() == "y":
            attempts+= 1

            try:
                if attempts == 4:
                    raise AttemptExceptionError("Too many attempts , your account is blocked for one hour")

            except Exception as var:
                print(var)
                time.sleep(3600)

            else:
                withdraw()

        else:
            print("Thank You , Welcome again")
            return


