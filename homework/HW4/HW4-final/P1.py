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
names = [r'$f^\prime_{FD}(x)$ for $h = 1\times10^{-1}$',r'$f^\prime_{FD}(x)$ for $h = 1\times10^{-7}$',r'$f^\prime_{FD}(x)$ for $h = 1\times10^{-15}$']

for f_FD_prime, name in zip(f_FD_primes,names):
    plt.plot(x, f_FD_prime(x), label=name)

plt.plot(x, f_prime(x), label='Analytical derivative',linestyle=':',linewidth=5,alpha=0.8,c='purple')
    
plt.xlabel('x')
plt.ylabel(r'$f^\prime(x)$')
plt.legend()

print('Answer to Q-a: When h=1e-7, the finite difference derivative most closely matches the true derivative. When the h value is too large, the differential is not fine enough to accurately probe the function\'s rate of change. When the h value is too small, the subtraction will have a large rounding error and the derivative will become numerically unstable.')
print('Answer to Q-b: Automatic differentiaion bypasses both of these issues by breaking the input function into composite functions, finding the derivatives of those functions and combining them using the chain rule. In this way, AD calculates the true derivative to machine-precision.')

plt.savefig('P1_fig.png')
plt.show()
