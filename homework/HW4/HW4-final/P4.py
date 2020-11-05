#!/usr/bin/env python3

class AutoDiffToy():

    def __init__(self,val=0,der=1):
        self.val = val
        self.der = der
        
    def __add__(self, other):
    # try as if other is an AutoDiffToy object
        try:
            return(AutoDiffToy(self.val+other.val, self.der+other.der))
        except AttributeError:
            pass
    # try as if other is an int or float
        try:
            return(AutoDiffToy(self.val+other, self.der))
        except TypeError:
            print('Other must be an AutoDiff object, int or float')

    def __radd__(self, other):
        return(self.__add__(other))
        
    def __mul__(self,other):
    # self*other, self*other.der+other*self.der
        try:
            return(AutoDiffToy(self.val*other.val, self.val*other.der+other.val*self.der))
        except AttributeError:
            pass
        # if other is an int or float, derivative = other*self.der
        try:
            return(AutoDiffToy(self.val*other, other*self.der))
        except TypeError:
            print('Other must be an AutoDiff object, int or float')
            
    def __rmul__(self,other):
        return(self.__mul__(other))

### Testing ###

a = 2.0 # Value to evaluate at
x = AutoDiffToy(a)

alpha = 2.0
beta = 3.0

f = alpha * x + beta
print(f.val,f.der)

f = alpha * x + beta
print(f.val,f.der)

f = x * alpha + beta
print(f.val,f.der)

f = beta + alpha * x
print(f.val,f.der)

f = beta + x * alpha
print(f.val,f.der)
