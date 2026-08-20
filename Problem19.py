#Q19 — Bank Account
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


account = BankAccount("Bushra", 50000)

account.deposit(10000)
account.withdraw(15000)

account.show_balance()