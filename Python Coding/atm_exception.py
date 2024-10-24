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

    pin = int(input("Enter your pin value: "))

    if pin == saved_pin:
        try:
            amt = float(input('Enter amount to withdraw: '))
            if amt > balance - 1000:
                raise BalanceExceptionError("Insufficient Balance")

            balance -= amt
            print("Remaining balance is", balance)

        except BalanceExceptionError as e:
            print(e)

    else:
        attempts += 1
        if attempts >= 4:
            print("Too many attempts, your account is blocked for one hour")
            time.sleep(3600)  # Simulate blocking the account for one hour
            attempts = 1  # Reset attempts after blocking period

        else:
            ans = input("Wrong PIN. Do you want to continue (y/n)? ")

            if ans.lower() == "y":
                withdraw()
            else:
                print("Thank You, Welcome again")

if __name__ == "__main__":
    withdraw()



