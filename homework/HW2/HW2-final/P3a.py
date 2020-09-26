#!/usr/bin/env python3

def make_withdrawal(balance):

    def withdraw(withdrawal_amount):
        if withdrawal_amount > balance:
            print('Insufficient funds')
        else:
            new_bal = balance - withdrawal_amount
            return(new_bal)
        
    return(withdraw)

# Demo the function
init_balance = 100
withdrawal_amount = 10
new_withdrawal_amount = 15

wd = make_withdrawal(init_balance)
wd(withdrawal_amount)
wd(new_withdrawal_amount)

print('This does not perform two consecutive withdrawals because I am not reassigning the initial balance. Executing wd with a different withdrawal amount will simply return the initial input balance minus the new withdrawal amount; the function wd has no way of knowing about the output of the previous execution of wd.')
