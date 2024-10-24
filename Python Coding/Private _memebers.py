# if we want that we do not want any class member to be public  we make it private

# by __ we can clss member private

class Bank:
    def __init__(self , acc_no , acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass    # private member

    def reset_pass(self):
        print(f"account passs is : {self.__acc_pass}")


b1 = Bank("12335" , "3454")
print(b1.acc_no)
print(b1.reset_pass())   # it shows an error  we cant directly accesss private memebers


# here we cannot access private member outside the classs

# so we made a method to  access the private member of the class inside the bank class.