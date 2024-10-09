# Design a Class to Represent a Bank Account
# Create a BankAccount class that supports operations like depositing, withdrawing, and checking the balance.

class BankAccount:
    def __init__(self, account_holder, balance = 0.0):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit{amount}, New balance{self.balance}")
        else:
            print("Invalid deposit amount")
            
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw{amount}, New Balance{self.balance}")
        else:
            print("Insufficient balance")
            
    def check_balance(self):
        print(f"Account holder: {self.account_holder}, Balance: {self.balance}")
        
account = BankAccount("Mrinmohy", 20000)
account.deposit(5000)
account.withdraw(2500)
account.check_balance()