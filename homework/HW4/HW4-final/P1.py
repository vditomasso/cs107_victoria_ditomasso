#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size':14})

def numerical_diff(f, h):
    '''
    Inputs
    ---
    f: function
    h: derivative stepsize, int or float
    
    Returns
    ---
    diff_at_point: function (input: x, returns: derivative of f with stepsize h at x)'''
    
    def diff_at_point(x):
        f_prime_at_x = (f(x+h)-f(x))/h
        return(f_prime_at_x)
        
    return(diff_at_point)

### Part B ###

def f(x):
    '''For Q1 PB, ln(x)'''
    return(np.log(x))
    
def f_prime(x):
    '''For Q1 PB, explicitly calculate the derivative of ln (x), i.e. 1/x'''
    return(1/x)
    
x = np.linspace(0.2,0.4,200)
hs = [1e-1,1e-7,1e-15]

f_FD_primes = []
for h in hs:
    f_FD_primes.append(numerical_diff(f,h))
names = [r'$h = 1\times10^{-1}$',r'$h = 1\times10^{-7}$',r'$h = 1\times10^{-15}$']

for f_FD_prime, name in zip(f_FD_primes,names):
    plt.plot(x, f_FD_prime(x), label=name)

plt.plot(x, f_prime(x), label='Exact derivative',linestyle=':',linewidth=5,alpha=0.8,c='purple')
    
plt.xlabel('x')
plt.ylabel(r'$f^\prime_{FD}(x)$')
plt.legend()
    
plt.show()
plt.savefig('P1_fig.png')
