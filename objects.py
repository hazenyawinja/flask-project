from datetime import datetime
today=datetime.today()

class bank_acc:
    def __init__(self,account_number,balance,owner_name,date_opened):
        self.account_number=account_number
        self.balance=balance
        self.owner_name=owner_name
        self.date_opened=date_opened

    def deposit(self,amount):
        if amount <=0:
            print("invalid amount entered")
        else:
            self.balance += amount
            print(f"ksh.{amount} added to {self.account_number} successfully")
            print(f"new balance is:{self.balance}")

    def withdraw(self,amount):
        if amount <=0:
            print("invalid ammount, cannot complete withdrawal")
        else:
            self.balance -= amount
            print(f"{amount} deducted from {self.account_number} successfully")
            print(f"new balance is: {self.balance}")

    def display_info(self):
        print(f"acc:{self.account_number},balance:{self.balance},name:{self.owner_name},date:{self.date_opened}")

bank_acc1=bank_acc(101,20_000,"james")
bank_acc1.deposit(2000)
bank_acc1.display_info()
bank_acc1.withdraw(500)

bank_acc2=bank_acc(102,200_000,"jane")
bank_acc2.display_info()
bank_acc2.deposit(9000)
bank_acc2.withdraw(200)