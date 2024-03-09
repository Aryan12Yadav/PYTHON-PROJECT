from bankacc import *


Lucknow = Bankaccount('Aryan',7899.98)

Kanpur = Bankaccount('Ayush')



Kanpur.get_balance()


Lucknow.deposit(8000)

Kanpur.deposit(5000)

Lucknow.withdraw(7000)

Kanpur.withdraw(80000)
 

sbi = InterestRewardAccct('Rahul',1000)
sbi.get_balance()
sbi.deposit(100)
sbi.transfer(Lucknow,500)

Neeraj  = SavingsAcct('Neeraj',3000)
Neeraj. get_balance()
Neeraj.transfer(Kanpur,1000)