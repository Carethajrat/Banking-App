class Transaction:
    def __init__(self,balance):
        self.balance = balance
        
    @property
    def withdrawal(self):
        amount_withdrawal = input("Enter an amount to withdraw\n")
        try:
            amount_withdrawal = float(amount_withdrawal)
        except ValueError:
            amount_withdrawal = 0
        print("Transaction in process...\n")
        if self.balance >= amount_withdrawal:
            self.balance = self.balance - amount_withdrawal
            detail = f"Transaction Completed Withdrawal of {amount_withdrawal} Rs \n Clear Balance: {self.balance} Rs"
            with open('details.txt','a') as file:
                file.write(detail)
        else:
            print("Not enough balance\n")
        print("Clear Balance: ",self.balance)
    @property
    def deposit(self):
        amount_deposit = input("Enter an amount to deposit\n")
        try:
            amount_deposit = float(amount_deposit)
        except ValueError:
            amount_deposit = 0
        print("Transaction in process...\n")
        self.balance = self.balance + amount_deposit
        detail = f"Transaction Completed Deposit of {amount_deposit} Rs \n Clear Balance: {self.balance} Rs"
        with open('details.txt','a') as file:
                file.write(detail)
        print("Clear Balance: \n",self.balance)

new_transaction = Transaction(98000)

while True:
    try:
        print("Welcome to Carethajrat ATM")
        choice = input("Withdrawal or Deposit\n")
    except KeyboardInterrupt:
        print("\n Leaving the ATM \n")
        break
    choice = choice.lower()
    if choice:
        if choice in ['withdrawal','deposit','w','d']:
            if choice in ['withdrawal','w']:
                new_transaction.withdrawal
            elif choice in ['deposit','d']:
                new_transaction.deposit
        else:
            print("Please Enter a valid option\n")
    else:
        print("The choice field can not be null.Try again.\n")
