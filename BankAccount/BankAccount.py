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

trevor = BankAccount(balance=1500)
hannah = BankAccount()

trevor.deposit(1500).deposit(800).deposit(600).withdraw(2200).yield_interest().display_account_info()
hannah.deposit(700).deposit(5000).withdraw(4000).withdraw(1000).withdraw(400).withdraw(350).yield_interest().display_account_info()

BankAccount.fullAccount()