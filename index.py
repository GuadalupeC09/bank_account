class BankAccount:
    bank_name= "Dojo Bank"
    def __init__(self, int_rate, balance):
        self.int_rate = 0
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account(self):
        print(f'Balance: ${self.balance}')
        return self
    def add_interest(self):
        self.balance = self.balance * 0.01
        return self


checking1= BankAccount(5, 5000)
checking2= BankAccount(0, 3000)
checking1.deposit(2000).deposit(2000).deposit(2000).withdraw(1000).add_interest().display_account()
checking2.deposit(10000).deposit(10000).withdraw(100).withdraw(100).withdraw(100).withdraw(150).add_interest().display_account()