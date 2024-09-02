class Bank:
    def __init__(self,Bank_name) -> None:
        self.bank_name=Bank_name
        self.holder_list=[]
        self.bank_balance=1000000000
        self.total_loan_amount = 0
        self.loan_feature = True


    def add_holder(self,account):
        self.holder_list.append(account)
        print(f"The account (name : {account.name}) is created successfully")
    
    def find_account(self,email):
        for account in self.holder_list:
            if account.email.lower() == email.lower():
                return account
        return None
    
    def remove_account(self,email):
        account =self.find_account(email)
        if account:
            self.holder_list.remove(account)
            print(f"account name : {account.name} is deleted")
        else:
            print(f"There are NO account about this {account.name} name")

    def view_holder_list(self):
        print("\n-------------------------Holder List--------------------------")
        print("Account_name\tEmail\t\tAccount_type\tAccount Number\n")
        for account in self.holder_list:
            print(f"{account.name}\t\t{account.email}\t{account.account_type}\t\t{account.account_num}")

    def check_bank_balance(self):
        print(f"Total bank balance is {self.bank_balance}")

    def loan_amount(self):
        print(f"Total loan amount is {self.total_loan_amount}")

    