# This is a simple implementation of a BankAccount class in Python.
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, balance)

account.show_balance()
 
deposit = float(input("Enter deposit amount: "))
account.deposit(deposit)

withdraw = float(input("Enter withdrawal amount: "))
account.withdraw(withdraw)

account.show_balance()