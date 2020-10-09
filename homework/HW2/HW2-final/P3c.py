#!/usr/bin/env python3

def make_withdrawal(balance):

    def withdraw(withdrawal_amount):
        nonlocal balance
        if withdrawal_amount > balance:
            print('Insufficient funds')
        else:
            new_bal = balance - withdrawal_amount
            balance=new_bal
            print(new_bal)
            return(new_bal)
        
    return(withdraw)

# Demo the function
init_balance = 100
withdrawal_amount = 10
new_withdrawal_amount = 15

wd = make_withdrawal(init_balance)
wd(withdrawal_amount)
wd(new_withdrawal_amount)
