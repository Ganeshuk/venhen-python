class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return("deposit")
    def withdraw(self,amount):
        if(self.balance<amount):
            return(False)
        else:
            return(True)
    def getBalance(self):
        return(self.balance)
b=BankAccount(12312,"ganesh",1000)
print(b.deposit(50))
print(b.withdraw(2000))