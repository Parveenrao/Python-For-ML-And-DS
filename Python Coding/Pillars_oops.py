# pillars of OOPs
# abstraction , encapsulation , inheritance  , polymorphism

""" abstracation---> abstracton means hiding the implementation details and showing essential feature to the user"""

from abc import ABC , abstractmethod

class BankApp(ABC):
    def database(self):
        print("Connecting to Database")

    @abstractmethod
    def security(self):
        pass

class MobileApp(BankApp):
    def mobile_log(self):
        print("Log in to the mobile")

    def security(self):
        print("mobile security")

mob = MobileApp()
mob.security()


# we cant make a object of abstract classs