#!/usr/bin/env python3

from enum import Enum

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():
    
    def __init__(self, owner, accountType, balance=0):
        self.owner = owner
        self.accountType = accountType
        self.balance = balance
    
    def withdraw(self, amount):
        if int(amount) > self.balance:
            raise Exception('Insufficient funds')
        elif int(amount)<0:
            raise Exception('Cannot withdraw a negative amount')
        else:
            new_bal = self.balance - int(amount)
            self.balance = new_bal

    def deposit(self, amount):
        if int(amount)<0:
            raise Exception('Cannot deposit a negative amount')
        else:
            new_bal = self.balance + int(amount)
            self.balance = new_bal

    def __str__(self):
        return 'Account owner: {}, Type of account: {}'.format(self.owner, AccountType(self.accountType).name)
    
    def __len__(self):
        return(int(self.balance))

class BankUser():
    
    def __init__(self, owner):
        self.owner = owner
        self.savingsAccount = None
        self.checkingAccount = None
    
    def addAccount(self, accountType):
        if accountType == AccountType.SAVINGS:
            if self.savingsAccount == None:
                self.savingsAccount = BankAccount(self.owner, accountType)
            else:
                raise Exception('This owner already has a savings account')
        if accountType == AccountType.CHECKING:
            if self.checkingAccount == None:
                self.checkingAccount = BankAccount(self.owner, accountType)
            else:
                raise Exception('This owner already has a checking account')
        
    def getBalance(self, accountType):
        if accountType == AccountType.SAVINGS:
            if self.savingsAccount == None:
                raise Exception('Cannot get balance: This owner does not have a savings account')
            else:
                return(self.savingsAccount.balance)
        if accountType == AccountType.CHECKING:
            if self.checkingAccount == None:
                raise Exception('Cannot get balance: This owner does not have a checking account')
            else:
                return(self.checkingAccount.balance)
    
    def deposit(self, accountType, amount):
        if accountType == AccountType.SAVINGS:
            if self.savingsAccount == None:
                raise Exception('Cannot make a deposit: This owner does not have a savings account')
            else:
                self.savingsAccount.deposit(amount)
        if accountType == AccountType.CHECKING:
            if self.checkingAccount == None:
                raise Exception('Cannot make a deposit: This owner does not have a checking account')
            else:
                self.checkingAccount.deposit(amount)

    def withdraw(self, accountType, amount):
        if accountType == AccountType.SAVINGS:
            if self.savingsAccount == None:
                raise Exception('Cannot withdraw funds: This owner does not have a savings account')
            else:
                self.savingsAccount.withdraw(amount)
        if accountType == AccountType.CHECKING:
            if self.checkingAccount == None:
                raise Exception('Cannot withdraw funds: This owner does not have a checking account')
            else:
                self.checkingAccount.withdraw(amount)

    def __str__(self):
        owner_info = '{} '.format(self.owner)
        if self.savingsAccount!=None:
            savings_info = 'has a savings account, balance: {} '.format(self.savingsAccount.balance)
        else:
            savings_info = 'has no savings account '
        if self.checkingAccount != None:
            checking_info = 'and a checking account, balance: {} '.format(self.checkingAccount.balance)
        else:
            checking_info = 'and no checking account'
        return(owner_info + savings_info + checking_info)

### ATM Closure Function ###
def ATMSession(bankUser):
    def Interface():
        prompt1=input('Enter Options: \n1)Exit \n2)Create Account \n3)Check Balance \n4)Deposit \n5)Withdraw \n')
        
        if prompt1=='1':
            return
        
        elif prompt1=='2': # Create an account
            prompt2=input('Enter Options: \n1)Checking \n2)Savings \n')
            if prompt2=='1': # Checking
                bankUser.addAccount(AccountType.CHECKING)
                print('You have created a checking account for {}.'.format(bankUser.owner))
                Interface()
            elif prompt2=='2': # Savings
                bankUser.addAccount(AccountType.SAVINGS)
                print('You have created a savings account for {}.'.format(bankUser.owner))
                Interface()
            else:
                print('\"{}\" is not an acceptable input. Please try again, or press 1 to Exit.'.format(prompt2))
                Interface()
                
        elif prompt1=='3': # Check balance
            prompt2=input('Enter Options: \n1)Checking \n2)Savings \n')
            if prompt2=='1': # Checking
                print('{}\'s checking account balance is: ${}'.format(bankUser.owner,bankUser.getBalance(AccountType.CHECKING)))
                Interface()
            elif prompt2=='2': # Savings
                print('{}\'s savings account balance is: ${}'.format(bankUser.owner,bankUser.getBalance(AccountType.SAVINGS)))
                Interface()
            else:
                print('\"{}\" is not an acceptable input. Please try again, or press 1 to Exit.'.format(prompt2))
                Interface()

        elif prompt1=='4': # Deposit
            prompt2=input('Enter Options: \n1)Checking \n2)Savings \n')
            if prompt2=='1': # Checking
                amount=input('Enter Integer Amount, Cannot Be Negative: \n')
                bankUser.deposit(AccountType.CHECKING, amount)
                print('You have deposited ${} into {}\'s checking account.'.format(amount, bankUser.owner))
                Interface()
            elif prompt2=='2': # Savings
                amount=input('Enter Integer Amount, Cannot Be Negative: \n')
                bankUser.deposit(AccountType.SAVINGS, amount)
                print('You have deposited ${} into {}\'s savings account.'.format(amount, bankUser.owner))
                Interface()
            else:
                print('\"{}\" is not an acceptable input. Please try again, or press 1 to Exit.'.format(prompt2))
                Interface()

        elif prompt1=='5': # Withdraw
            prompt2=input('Enter Options: \n1)Checking \n2)Savings \n')
            if prompt2=='1': # Checking
                amount=input('Enter Integer Amount, Cannot Be Negative: \n')
                bankUser.withdraw(AccountType.CHECKING, amount)
                print('You have withdrawn ${} from {}\'s checking account.'.format(amount, bankUser.owner))
                Interface()
            elif prompt2=='2': # Savings
                amount=input('Enter Integer Amount, Cannot Be Negative: \n')
                bankUser.withdraw(AccountType.SAVINGS, amount)
                print('You have withdrawn ${} from {}\'s savings account.'.format(amount, bankUser.owner))
                Interface()
            else:
                print('\"{}\" is not an acceptable input. Please try again, or press 1 to Exit.'.format(prompt2))
                Interface()
       
        else:
            print('\"{}\" is not an acceptable input. Please try again, or press 1 to Exit.'.format(prompt1))
            Interface()
       
    return Interface

