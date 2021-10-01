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
        return self
# Withdrawl
    def withdrawlChecking(self, amount):
        self.checkingBalance -= amount
        print(f"you have withdrawn ${amount}")
        return self
# Transfer checking to Savings
    def transferCheckingToSavings(self, amount):
        self.checkingBalance -= amount
        self.savingsBalance += amount
        print(f"{self.firstName} has ${self.checkingBalance} in Checking and ${self.savingsBalance} in Savings.")
        return self
# Display Balance
    def displayBalance(self):
        print(f"You have in Checking: ${self.checkingBalance}")
        print(f"You have in Savings: ${self.savingsBalance}")
        return self
# User Transfer
    def userTransfer(self, user, amount):
        self.checkingBalance -= amount
        user.checkingBalance += amount
        print(f"{self.firstName} has transferred ${amount} to {user.firstName}")
        return self

trevor = User("Trevor", "Anderson")
hannah = User("Hannah", "Anderson")
joe = User("Joe", "Young")

trevor.depositChecking(500).depositChecking(500).depositChecking(1500).withdrawlChecking(50).displayBalance()
hannah.depositChecking(150).depositChecking(150).withdrawlChecking(25).withdrawlChecking(75).displayBalance()
trevor.transferCheckingToSavings(200).userTransfer(hannah, 100)
joe.depositChecking(800).withdrawlChecking(75).withdrawlChecking(75).withdrawlChecking(75).displayBalance()
trevor.displayBalance()
hannah.displayBalance()
