from Bank_account import *

Ali = BankAccount(1000, "Ali")
Sara = BankAccount(1500 , "Sara")

Ali.getBalance()
Sara.getBalance()

Ali.deposit(500)

Ali.withdraw(10000)

Ali.withdraw(100)

Ali.transfer(500 , Sara)

Mina = IntrestRewardAccount(1000 , "Mina")
Mina.getBalance()
Mina.deposit(100)

Kian = SavingAccount(1000 , "Kian")
Kian.transfer(1000 , Ali)
Kian.transfer(100 , Ali)
