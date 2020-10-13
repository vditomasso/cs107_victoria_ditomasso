#!/usr/bin/env python3

from Bank import BankUser
from Bank import AccountType

def test_over_withdrawal(): #this test function should throw an Exception or Error
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 10);
    try:
        user.withdraw(AccountType.SAVINGS, 1000); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption

def test_deposit_neg(): #this test function should throw an Exception or Error
    user = BankUser("Joe");
    user.addAccount(AccountType.CHECKING);
    try:
        user.deposit(AccountType.CHECKING, -10);
    except Exception as e:
        print(e);

def test_getBalance_noAccount():
    user = BankUser("Joe");
    try:
        user.getBalance(AccountType.CHECKING);
    except Exception as e:
        print(e);
        
def test_deposit_noAccount():
    user = BankUser("Joe");
    try:
        user.getBalance(AccountType.SAVINGS);
    except Exception as e:
        print(e);
        
def test_withdraw_noAccount():
    user = BankUser("Joe");
    try:
        user.withdraw(AccountType.CHECKING, 10);
    except Exception as e:
        print(e);

test_over_withdrawal()
test_deposit_neg()
test_getBalance_noAccount()
test_deposit_noAccount()
test_withdraw_noAccount()
