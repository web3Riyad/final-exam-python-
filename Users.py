from random import randint

class Users:
    def __init__(self,name,email,address,account_type) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        
class Account_holder(Users):
    def __init__(self, name, email, address, account_type) -> None:
        super().__init__(name, email, address, account_type)
        self.account_num=randint(50000,100000)
        self.amount=0    
        self.loan_count=0   
        self.transaction_history=[]

    def deposit(self,bank,amount):
        self.amount+= amount
        bank.bank_balance += amount
        self.transaction_history.append(f'Deposited : {amount}')
        print(f"Successfully deposited {amount} taka and current amount is {self.amount}")

    def withdraw(self,bank,amount):
        if bank.bank_balance >amount:
            if amount > self.amount:
                print('Withdrawal amount exceeded')
                print(f"Your current is {self.amount}\nBut you want to withdraw {amount}")
            else:
                self.amount -=amount
                bank.bank_balance -=amount
                self.transaction_history.append(f'withdraw : {amount}')
                print(f'withdrawal money : {amount} is successful and current balance is {self.amount}')
        else:
            print(f"The {bank} is bankrupt")

    def check_balance(self):
        print(f"Current account balance is {self.amount} taka")

    def check_history(self):
        print(f"-------------Transaction History-------------------")
        for history in self.transaction_history:
            print(history)

    def take_loan(self,bank,amount):
        if bank.loan_feature:
            if self.loan_count <= 2:
                self.amount += amount
                bank.bank_balance -+amount
                bank.total_loan_amount+=amount
                self.loan_count+=1
                self.transaction_history.append(f'Loan : {amount}')
                print(f"Successfully took {amount} taka as a loan and current balance is {self.amount}")
            else:
                print("You are unable to take loan")
        else:
            print("Loan featurn is unable, NOw")


    def transfer_money(self,bank,reciver_email,amount):
        reciver= bank.find_account(reciver_email)
        if self.amount < amount:
            print('Transfer amount exceede')
        elif reciver:
            self.amount -=amount
            reciver.amount += amount
            self.transaction_history.append(f"Transfered money to {reciver_email}")
            reciver.transaction_history.append(f"Recieve money from {self.email}")
            print(f"Successfull transfered money from {self.email} to {reciver.email}")


class Admin:
    def __init__(self) -> None:
        pass

    def create_account(self,bank,account):
        bank.add_holder(account)
    
    def delete_account(self,bank,email):
        bank.remove_account(email)

    def account_list(self,bank):
        bank.view_holder_list()

    def total_bank_balance(self,bank):
        bank.check_bank_balance() 

    def check_loan_amount(self,bank):
        bank.loan_amount()

    def controll_loan_feature(self, bank):
        bank.loan_feature = not bank.loan_feature
        if bank.loan_feature:
            state="Enabled"
        else :
            state="disabled"
        print(f"Loan feature is now {state}")






        

    


    
        
        