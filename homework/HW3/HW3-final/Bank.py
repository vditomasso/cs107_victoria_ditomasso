#!/usr/bin/env python3

from enum import Enum

# Not sure that this should be here:
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
            new_bal = self.balance + deposit
            self.balance = new_bal

    def __str__(self):
        return "Account owner: {}, Type of account: {}".format(self.owner, AccountType(self.accountType).name)
    
    def __len__(self):
        return(int(self.balance))

