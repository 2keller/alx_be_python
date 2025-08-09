class bankaccount:
    def __init__(self, balance=0) -> None:
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds")
        else:
            self.account_balance -= amount

    def display_balance(self):
        print(f"Current balance: {self.account_balance}")