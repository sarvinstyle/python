class BalanceException(Exception):
    pass

class BankAccount :
    def __init__(self , initalAmount , actName):
        self.balance = initalAmount
        self.name = actName
        print(f"\nAccount {self.name} created.\nBalance = {self.balance:.2f}")

    def getBalance (self):
        print(f"\nAccount {self.name} balance = {self.balance:.2f}")

    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getBalance()

    def checkTransaction(self, amount):
        if self.balance >= amount :
            return
        else:
            raise BalanceException(f"Sorry account {self.name} only has balance of ${self.balance}")


    def withdraw (self , amount):
        try:
            self.checkTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw is completed")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw is intrrupted: {error}")


    def transfer (self , amount , accName):
        try:
            print("\n********\nTransfer started")
            self.checkTransaction(amount)
            self.withdraw(amount)
            accName.deposit(amount)
            print("\n********* \nTransfer comleted")
        

        except BalanceException as error:
            print(f"\Transfer is intrrupted: {error}")


class IntrestRewardAccount(BankAccount):
    def deposit(self, amount):
        self.balance +=( amount * 1.05)
        print("\nDeposit completed.")
        self.getBalance()


class SavingAccount(IntrestRewardAccount):
    def __init__(self , initalAmount , actName ):
        super().__init__(initalAmount , actName)
        self.fee = 5

    def transfer(self, amount, accName):
        try:
            print("\n********\nTransfer started")            
            self.checkTransaction(amount + self.fee)
            self.withdraw(amount + self.fee)
            accName.deposit(amount)
            print("\n********\nTransfer started")            
        except BalanceException as error:
            print(f"\nTransfer intrrupted : {error}")
            