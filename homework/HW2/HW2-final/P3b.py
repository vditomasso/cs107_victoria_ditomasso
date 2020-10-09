#!/usr/bin/env python3

def make_withdrawal(balance):

    def withdraw(withdrawal_amount):
        if withdrawal_amount > balance:
            print('Insufficient funds')
        else:
            new_bal = balance - withdrawal_amount
            balance=new_bal
            print(new_bal)
            return(new_bal)
        
    return(withdraw)

# Explain why this won't work
print('Trying to assign the variable balance within the inner function means that Python will treat balance as a variable that is local to the inner function. In order for this code to run, balance needs to remain a nonlocal variable (in the case, an input argument to the outer function).')

# Demo the function
init_balance = 100
withdrawal_amount = 10
new_withdrawal_amount = 15

wd = make_withdrawal(init_balance)
wd(withdrawal_amount)
wd(new_withdrawal_amount)
