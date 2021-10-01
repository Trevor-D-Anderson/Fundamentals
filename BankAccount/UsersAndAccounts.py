class BankAccount:
# don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance<amount:
            print(f"Insufficient Funds: Charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Your Balance is: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance = self.balance + (self.balance*self.int_rate)
        return self
    @classmethod
    def fullAccount(cls):
        sum = 0
        for account in cls.all_accounts:
            print(account.balance, account.int_rate)
            sum+=1

class User:
    def __init__(self, firstName, lastName, interest, balance, type = "savings"):
        self.firstName = firstName
        self.lastName = lastName
        if type == "checking":
            self.checking = BankAccount(interest,balance)
        else:
            self.savings = BankAccount(interest, balance)
# Deposit
    def depositChecking(self, amount):
        self.checking += amount
        print(f"You have deposited ${amount}")
        return self
# Withdrawl
    def withdrawlChecking(self, amount):
        self.checking -= amount
        print(f"you have withdrawn ${amount}")
        return self
# Transfer checking to Savings
    def transferCheckingToSavings(self, amount):
        self.checking -= amount
        self.savings += amount
        print(f"{self.firstName} has ${self.checking} in Checking and ${self.savings} in Savings.")
        return self
# Display Balance
    def displayBalance(self):
        print(f"You have in Checking: ${self.checking}")
        print(f"You have in Savings: ${self.savings}")
        return self
# User Transfer
    def userTransfer(self, user, amount):
        self.checking -= amount
        user.checking += amount
        print(f"{self.firstName} has transferred ${amount} to {user.firstName}")
        return self