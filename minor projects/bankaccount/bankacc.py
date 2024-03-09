class Bankaccount:

    def __init__(self,name,balance = 0):
        self.name = name 
        self.balance = balance

  

    def get_balance(self):
        print(f"\n\nthe nomine is : {self.name}   and the \n\n\n current balance is :  {self.balance}")


    def deposit(self,amount):
        self.balance +=amount

        print('\n\nHolder name is ',self.name ,'\n\nyour balance is ',self.balance)


    def transaction(self, amount):
        if self.balance>=  amount:
            return
        else:
            raise Exception
        

    def withdraw(self,amount):
        try:
            self.transaction(amount)
            self.balance = self.balance - amount

            print("withdraw complete.")


        except Exception as error:
            print(f"\n withdraw interrput \n because of not sufficient balance")
            
        
    def transfer(self,account,amount):
        try:
            print('\n____________\n\n Beginnning transfer ')
            self.transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f'transfer completed successfully \n\n')
        except Exception as error:
            print(f'\n transfer interrupted {error}')

class InterestRewardAccct(Bankaccount):

    def deposit(self,amount):
        self.balance = self.balance + (amount*(1.05))
        print("\n Deposite complete.")
        self.get_balance()



class SavingsAcct(InterestRewardAccct):

    def __init__(self,acctName,initialAmount):

        super().__init__(acctName,initialAmount)
        
        self.fee = 10


    def withdraw(self,amount):
        try :
            self.transaction(amount + self.fee)
            self.balance = self.balance - (amount +self.fee)
            print("\n withdraw completed.")
            self.get_balance()
        
        except Exception as error:
            print(f"\nWithdraw interrupted : {error}")


        