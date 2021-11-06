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
        print("Interest Yield:", self.balance * self.int_rate)
        return self

class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate=0.04, balance=0)
    def make_withdrawl(self):
        self.account.withdraw()
    def make_deposit(self):
        self.account.deposit()
    def display_user_balance(self):
        print("User:", self.name + ",", "Balance:", self.account.balance)

# Accounts
jesse = User("Jesse")

# Transaction Examples
jesse.account.deposit(13700).withdraw(1020).deposit(365)
jesse.display_user_balance()

# With Interest Yield
jesse.account.yield_interest()
