
class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance:", self.balance)
    def yield_interest(self):
        print("Balance:", self.balance * self.int_rate)
        return self


# Accounts
accountOne = BankAccount(0.04, 500)
accountTwo = BankAccount(0.06, 700)

# Transactions
accountOne.deposit(500).deposit(1000).deposit(200).withdraw(300).yield_interest().display_account_info()
accountTwo.deposit(200).deposit(500).withdraw(100).withdraw(200).withdraw(150).withdraw(270).yield_interest().display_account_info()