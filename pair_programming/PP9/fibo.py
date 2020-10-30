# PairProgramming Week 9
# Sharer: Victoria DiTomasso
# Coder: Wenqi Chen
# Listener: Golo Feige
#!/bin/usr python3

class Fibonacci:

    def __init__(self, num): 
        self.num = num
        n1, n2 = 0, 1
        count = 0
        ns = []
        while count < num:
            n3 = n1 + n2
            n1 = n2
            n2 = n3 
            ns.append(n3)
            count += 1

        self.terms = ns

    def __iter__(self):
        return FibonacciIterator(self.terms) # Returns an instance of the iterator


class FibonacciIterator:
    
    def __init__(self, terms): 
        self.terms = terms 
        self.index = 0 # Determines the next word to fetch

    def __next__(self): 
        try:
            term = self.terms[self.index] 
        except IndexError:
            raise StopIteration() 
        self.index += 1
        return term

    def __iter__(self):
        return self


### Demo ###
fib = Fibonacci(10) # Create a Fibonacci iterator called fib that contains 10 terms
print(list(iter(fib)))

