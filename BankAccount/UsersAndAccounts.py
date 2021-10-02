class BankAccount:
# don't forget to add some default values for these parameters!
    all_checkings = []
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_checkings.append(self)


    @classmethod
    def fullchecking(cls):
        sum = 0
        for checking in cls.all_checkings:
            print(checking.balance, checking.int_rate)
            sum+=1

class User:
    def __init__(self, firstName, lastName, checkingBalance = 0, savingsBalance = 0):
        self.firstName = firstName
        self.lastName = lastName
        self.checking = BankAccount(0.01, checkingBalance)
        self.savings = BankAccount(0.05, savingsBalance)
# Deposit
    def depositChecking(self, amount):
        self.checking.balance += amount
        print(f"You have deposited ${amount}")
        return self
# Withdrawl
    def withdrawSavings(self, amount):
        if self.savings.balance<amount:
            print(f"Insufficient Funds: Charging a $5 fee.")
            self.savings.balance -= 5
        else:
            self.savings.balance -= amount
        return self
    def withdrawlChecking(self, amount):
        if self.checking.balance<amount:
            print(f"Insufficient Funds: Charging a $5 fee.")
            self.checking.balance -= 5
        else:
            self.checking.balance -= amount
        return self
# Transfer checking to Savings
    def transferCheckingToSavings(self, amount):
        self.checking.balance -= amount
        self.savings.balance += amount
        print(f"{self.firstName} has ${self.checking.balance} in Checking and ${self.savings.balance} in Savings.")
        return self
# Display Balance
    def displayBalance(self):
        print(f"You have in Checking: ${self.checking.balance}")
        print(f"You have in Savings: ${self.savings.balance}")
        return self
# User Transfer
    def userTransfer(self, user, amount):
        self.checking.balance -= amount
        user.checking.balance += amount
        print(f"{self.firstName} has transferred ${amount} to {user.firstName}")
        return self
# Interest Yield
    def yield_interest(self, account):
        if account == "checking":
            if self.checking.balance>0:
                self.checking.balance = self.checking.balance + (self.checking.balance*self.checking.int_rate)
            return self
        elif account == "savings":
            if self.savings.balance>0:
                self.savings.balance = self.savings.balance + (self.savings.balance*self.savings.int_rate)
            return self


trevor = User("Trevor", "Anderson", 500, 10000)
hannah = User("Hannah", "Anderson")
trevor.displayBalance().yield_interest("savings").displayBalance()
BankAccount.fullchecking()