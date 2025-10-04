class BankAccount:
    def __init__(self,initial_balance: float=0.0):
        self.account_balance=float(initial_balance)
    
    def deposit(self,amount:float):
        self.account_balance+=float(amount)
    
    def withdraw(self,amount:float):
        amount=float(amount)
        if amount<=self.account_balance:
            self.account_balance-=amount
            return True
        return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
