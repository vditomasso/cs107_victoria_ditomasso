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
        if amount > self.balance:
            raise Exception('Insufficient funds')
        elif amount<0:
            raise Exception('Cannot withdraw a negative amount')
        else:
            new_bal = self.balance - amount
            self.balance = new_bal

    def deposit(self, amount):
        if amount<0:
            raise Exception('Cannot deposit a negative amount')
        else:
            new_bal = self.balance + amount
            self.balance = new_bal

    def __str__(self):
        return "Account owner: {}, Type of account: {}".format(self.owner, AccountType(self.accountType).name)
    
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
        owner_info = "{} ".format(self.owner)
        if self.savingsAccount!=None:
            savings_info = "has a savings account, balance: {} ".format(self.savingsAccount.balance)
        else:
            savings_info = "has no savings account "
        if self.checkingAccount != None:
            checking_info = "and a checking account, balance: {} ".format(self.checkingAccount.balance)
        else:
            checking_info = "and no checking account"
        return(owner_info + savings_info + checking_info)
