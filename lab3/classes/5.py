class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}  Account balance:{self.balance}'

    def deposit(self, deposite):
        self.balance += deposite
        print('Deposit Accepted')

    def withdraw(self,withd):
        if self.balance >= withd:
            self.balance -= withd
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!!!')
    # pass