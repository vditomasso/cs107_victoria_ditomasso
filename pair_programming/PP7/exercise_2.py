#Coder: Pawel Nawrocki, Diego Zertuche, Victoria DiTomasso,Matheus C. Fernandes
Sharer: Matheus C. Fernandes

class my_pow():
    def __init__(self, x):
        self.x=x
        self.d=1
    
    def __pow__(self, r):
        return(self.x**r, r*self.x**(r-1)*self.d)
        
if __name__ == "__main__":
    v=my_pow(3)
    print(v**4)
