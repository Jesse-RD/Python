class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def make_withdrawl(self, amount):
        self.balance -= amount
        return self
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def display_user_balance(self):
        print("User:", self.name, self.balance)

jesse = User("Jesse")
frank = User("Frank")
jenny = User("Jenny")

# first User
jesse.make_deposit(100).make_deposit(50).make_deposit(30).make_withdrawl(150).display_user_balance()

# second User
frank.make_deposit(20).make_deposit(30).make_withdrawl(10).make_withdrawl(5).display_user_balance()

# third User
jenny.make_deposit(500).make_withdrawl(50).make_withdrawl(200).make_withdrawl(40).display_user_balance()