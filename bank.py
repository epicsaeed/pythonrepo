#TESTING OOP WITH PYTHON

class BankAccount:
    def __init__(self,name,ID,balance):
        self.balance = balance
        self.name = name
        self.ID = ID

    def setBalance(self,balance):
        self.balance = balance

    def setName(self,name):
        self.name = name

    def setID(self,ID):
        self.ID = ID

    def withdraw(self,amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance-=amount
        return self.balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance
