class Account:
    def __init__(self,bal,acc):
        self.balance= bal
        self.account_no= acc
        
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited from Ac",self.account_no)
        print("total balance =",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited.")
        print("total balance =",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1= Account(50000, 147258)
acc1.debit(27000)
acc1.credit(1000)
acc1.credit(2400)

acc2 = Account(100000,147369)
acc2.debit(75000)
acc2.credit(125000)