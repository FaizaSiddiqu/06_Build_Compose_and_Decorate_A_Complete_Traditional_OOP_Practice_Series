
# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) 
# that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "HBL Bank"
    
    def __init__(self, account_holder):
        self.account_holder = account_holder
        
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        
    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank Name: {self.bank_name}")
        
account1 = Bank("Alice")
account2 = Bank("John")

account1.display()
account2.display()

Bank.change_bank_name("State bank")

account1.display()
account2.display()
