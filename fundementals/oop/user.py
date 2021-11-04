class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def make_withdrawl(self, amount):
        self.balance -= amount
    def make_deposit(self, amount):
        self.balance += amount
    def display_user_balance(self):
        print("User:", self.name, self.balance)

jesse = User("Jesse")
frank = User("Frank")
jenny = User("Jenny")

# first User
jesse.make_deposit(100)
jesse.make_deposit(50)
jesse.make_deposit(30)
jesse.make_withdrawl(150)
jesse.display_user_balance()

# second User
frank.make_deposit(20)
frank.make_deposit(30)
frank.make_withdrawl(10)
frank.make_withdrawl(5)
frank.display_user_balance()

# third User
jenny.make_deposit(500)
jenny.make_withdrawl(50)
jenny.make_withdrawl(200)
jenny.make_withdrawl(40)
jenny.display_user_balance()