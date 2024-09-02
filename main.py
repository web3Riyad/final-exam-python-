from Users import Account_holder,Admin
from banks import Bank

amer_bank=Bank("Amer_bank")
def admin():
    ad_min=Admin()
    while True:
        print("\n----------- Admin Panel ---------")
        print("1.Create an Account")
        print("2.Delete an Account")
        print("3.All account list")
        print("4.Total balance of the bank")
        print("5.Total loan ot the bank")
        print("6.Control the loan feature")
        print("7.Exit")
    
        choice = int(input("Enter Your choice : "))
        if choice == 1:
            name=input("Enter your name : ")
            email=input("Enter your Email : ")
            address=input("Enter your Address : ")
            account_type=input("Enter your type : ")
            account=Account_holder(name=name,email=email,address=address,account_type=account_type)
            ad_min.create_account(amer_bank,account)

        elif choice == 2 :
            email_id=input("Enter your email ID : ")
            ad_min.delete_account(amer_bank,email_id)

        elif choice == 3 :
            ad_min.account_list(amer_bank)

        elif choice == 4 :
            ad_min.total_bank_balance(amer_bank)

        elif choice == 5 :
            ad_min.check_loan_amount(amer_bank)

        elif choice == 6 :
            ad_min.controll_loan_feature(amer_bank)

        elif choice == 7 :
            break

        else:
            print("Invalid choice")


def User():
    while True:
        print("\n---------- Account Holder Panel --------")
        print("1.Create an account")
        print("2.Deposit Money")
        print("3.Wihtdraw Money")
        print("4.Available balance")
        print("5.Transaction History")
        print("6.Take loan")
        print("7.Transfer Money")
        print("8.Exit")


        choice = int(input("Enter Your choice : "))
        if choice == 1:
            name=input("Enter your name : ")
            email=input("Enter your Email : ")
            address=input("Enter your Address : ")
            account_type=input("Enter your type : ")
            account=Account_holder(name=name,email=email,address=address,account_type=account_type)
            amer_bank.add_holder(account)

        elif choice == 2 :
            amount=int(input("Enter deposit amount : "))
            account.deposit(amer_bank,amount)
            
        elif choice == 3 :
            amount=int(input("Enter withdraw money : "))
            account.withdraw(amer_bank,amount)

        elif choice == 4 :
            account.check_balance()

        elif choice == 5 :
            account.check_history()

        elif choice == 6 :
            amount=int(input("Enter loan amount : "))
            account.take_loan(amer_bank,amount)

        elif choice == 7 :
            email=input("Enter reciver email : ")
            amount =int(input("Enter amount : "))
            account.transfer_money(amer_bank,email,amount)

        elif choice == 8 :
            break

        else:
            print("Invalid choice")

def main():

    while(True):
        print("\n-------- HOME -----------")
        print("1.Admin")
        print("2.Account Holder")
        print("3.Exit")
   
        choice=int(input("Enter your choice : "))
        if choice == 1:
            admin()

        elif choice == 2:
            User()

        elif choice == 3:
            break
        
        else:
            print("Invalid Choice")

if __name__=="__main__":
    main()
