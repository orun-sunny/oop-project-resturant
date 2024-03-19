class Bank:
    def __int__(self,balance):
        self.balance =balance
        self.min_withdraw = 100
        self,max_withdraw = 10000

    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        if amount > 0:
            self.balance +=amount 