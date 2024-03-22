from decimal import Decimal


class Account:
    def __init__(self, name, balance):
        if balance < Decimal('0.00'):
            raise ValueError('Inital balance must be >= to 0.00.')
        
        self.name = name 
        self.balance = balance 

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("amount must be positive.")
        else:
            self.balance += amount
            
    def withdraw(self, amount):
        if amount >= self.balance:
           raise ValueError("You do not have enough money")
        elif amount < Decimal(0.00):
            raise ValueError("Must be positive.")
        else:
            self.balance -= amount 
        
account1 = Account("jadon lama", Decimal(50.00))

print(f"Name: {account1.name}\nBalance: ${account1.balance}")

account1.deposit(Decimal(74.24))

print(f"Name: {account1.name}\nBalance: ${account1.balance:.2f}")

account1.deposit(Decimal(-200))
print(account1.balance)