class BankAccount:
    def __init__(self, balance=0) -> None:
        self.__account_balance = balance  # Encapsulated attribute

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def display_balance(self):
        print(f"Current balance: ${self.__account_balance}")
