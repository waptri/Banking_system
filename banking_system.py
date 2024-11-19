from os import system
from platform import node
import random

class Account:
    def __init__(self, owner, initial_balance=0):
        self.account_number = f"AC-{random.randint(1000, 9999)}"
        self.owner = owner
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Invalid deposit amount.")
            
    def withdraw(self, amount):
        if amount > self.balance:
         print("Insufficient funds for this transaction!")   
        elif amount <= 0 :
            print("Invalid Withdrawal amount!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
            
    def display_account_info(self):
        print(f"\nAccount Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")        
        print(f"Account Balance: ${self.balance}\n")
        
class savings_account(Account):
    def __init__(self, owner, initial_balance=0, interest_rate=2.5):
        super().__init__(owner, initial_balance )
        self.interest_rate = interest_rate
        
    def calculate_interest(self):
        interest = (self.balance * self.interest_rate) / 100 
        print(f"Yearly interest earned: {interest}")
        return interest
    
class current_account(Account):
    def __init__(self, owner, initial_balance=0, overdraft_limit=1000):
        super().__init__(owner, initial_balance)
        self.overdraft_limit = overdraft_limit
        self.overdraft_balance = 0
        
    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("overdraft limit exceeded!")
        elif amount <= 0:
            print("Invalid Withdrawal amount!")
        else:
            self.balance -= amount
            print("Withdrawal successfull! current balance: {self.balance}")
            
class bankingsystem:
    def __init__(self):
        self.accounts = {}
        
    def create_account(self, accounts):
        account_number = len(self.accounts) + 1
        print("\n---Create New Account---")
        owner = input("Enter Account owner's name: ")
        account_type = input("Choose account type (savings/current) ").strip().lower()
        initial_deposit = float(input("Enter Initial deposit Amount:"))
        
        if account_type == "savings":
         new_account = savings_account(owner, initial_deposit)
        elif account_type == "current":
            new_account = current_account(owner, initial_deposit)
        else:
            print("Invalid account type. please try again")
            return
        self.accounts[account_number] = new_account
        print(f"Account created successfully! Account number: {account_number}")
        
    def find_account(self, account_number):
        for accounts in self.accounts:
            if accounts.account_number == account_number:
                return accounts
            print("Account not found!")
            return node
        
    def deposit_to_account(self):
        account_number = input("Enter Account number:")
        account = self.find_account(account_number)
        if account :
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
            
    def withdrawal_from_account(self):
        account_number = input("Enter account number")
        account = self.find_account_number(account_number)
        if account:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
            
    def display_account_info(self):
        account_number = input("Enter account number:")
        account = self.find_account(account_number)
        if account:
            account.display_account_info()
            
    def calculate_savings_interest(self):
        account_number = input("Enter savings account number:")
        account = self.find_account(account_number)
        if isinstance(account, savings_account) :
            account.calculate_interest()
        else:
            print("This is not a savings account.")
    
    def menu(self):
        while True:
             print("\n--- Banking System Menu ---")
             print("1. Create Account")
             print("2. Deposit Money")
             print("3. Withdraw Money")
             print("4. Display Account info")
             print("5. Calculate Savings Interest")
             print("6. Exit")
             
             choice = input("Enter your choice:")     
        
             if choice == "1":
              self.create_account(Account)
             elif choice == "2":
                 self.deposit_to_account()
             elif choice == "3":
                 self.withdrawal_from_account()
             elif choice == "4":
                 self.display_account_info()
             elif choice == "5":
                 self.calculate_savings_interest()
             elif choice == "6":
                 print("Thank you for using the Banking System. Goodbye!")
                 break
             else:
                 print("Invalid choice. Please choose again.")
                 
if  __name__ == "__main__":
 system = bankingsystem()
system.menu()

                  
             
                       
                
                
             
             
        
            
            
                
                    
            
            
    
           
            
            
        