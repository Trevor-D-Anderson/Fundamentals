class User:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.checkingBalance = 0
        self.savingsBalance = 0
# Deposit
    def depositChecking(self, amount):
        self.checkingBalance += amount
        print(f"You have deposited ${amount}")
# Withdrawl
    def withdrawlChecking(self, amount):
        self.checkingBalance -= amount
        print(f"you have withdrawn ${amount}")
# Transfer checking to Savings
    def transferCheckingToSavings(self, amount):
        self.checkingBalance -= amount
        self.savingsBalance += amount
        print(f"{self.firstName} has ${self.checkingBalance} in Checking and ${self.savingsBalance} in Savings.")
# Display Balance
    def displayBalance(self):
        print(f"You have in Checking: ${self.checkingBalance}")
        print(f"You have in Savings: ${self.savingsBalance}")
# User Transfer
    def userTransfer(self, user, amount):
        self.checkingBalance -= amount
        user.checkingBalance += amount
        print(f"{self.firstName} has transferred ${amount} to {user.firstName}")

trevor = User("Trevor", "Anderson")
hannah = User("Hannah", "Anderson")
joe = User("Joe", "Young")

trevor.depositChecking(500)
trevor.depositChecking(500)
trevor.depositChecking(1500)
trevor.withdrawlChecking(50)
trevor.displayBalance()
hannah.depositChecking(150)
hannah.depositChecking(150)
hannah.withdrawlChecking(25)
hannah.withdrawlChecking(75)
hannah.displayBalance()
trevor.transferCheckingToSavings(200)
trevor.userTransfer(hannah, 100)
joe.depositChecking(800)
joe.withdrawlChecking(75)
joe.withdrawlChecking(75)
joe.withdrawlChecking(75)
joe.displayBalance()
trevor.displayBalance()
hannah.displayBalance()
