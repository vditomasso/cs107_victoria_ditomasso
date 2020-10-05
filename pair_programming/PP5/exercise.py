# Coder: Victoria DiTomasso
# Listener: Will Wang
# Sharer: Morris Reeves

import numpy as np

class Layer():
    def __init__(self,shape,actv):
        # weights:  length of inputs x number of nodes
        self.weights = np.random.rand(shape[0],shape[1]) 
        self.bias = np.random.rand(1,shape[1])
        self.actv=actv

    def __repr__(self):
        return "class name {}, actv {}, weights {}, bias {}".format(type(self).__name__, self.actv, self.weights.shape, self.bias.shape)

    def __str__(self):
        return "Activation function {}, shape weights {}, shape bias {}".format(self.actv.__name__, self.weights.shape, self.bias.shape)

    def __eq__(self, other):
        return self.actv == other.actv and self.weights.shape == other.weights.shape and self.bias.shape == other.bias.shape
        
    def forward(self, inputs):
        h = self.actv(np.dot(inputs, self.weights) + self.bias)
        return h

inputs = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # e.g. input to the network: (1, 100)
number_of_nodes1 = 5
number_of_nodes2 = 2
len_input = inputs.shape[1] # 100
shape1 = (len_input,number_of_nodes1) # 100,5
shape2 = (number_of_nodes1, number_of_nodes2) # 5,2

actv = np.tanh

layer1 = Layer(shape1, actv)
layer2 = Layer(shape2, actv)

h1 = layer1.forward(inputs) #(1x100)*(100x5)+(1x5) -> (1,5)
h2 = layer2.forward(h1) #(1x5)*(5x2)+(1x2) -> (1x2)
print(h1)
print(h2)

print(layer1)
print(repr(layer1))
print(layer1==layer1, ' should be True')
print(layer2==layer1, ' should be False')

'''
Points of contention/group work documentation:

(1) Pseudocode provided appears to be incorrect?
    Confirmed that should be "layer1.forward(inputs)" rather than layer1(inputs)

(2) Initial debugging (Resolved by changing order of arguments in __init__)
    Traceback (most recent call last):
    File "exercise_1.py", line 34, in <module>
    h1 = layer1.forward(inputs)
    File "exercise_1.py", line 18, in forward
    h = self.actv(np.dot(inputs, self.weights) + self.bias)
    ValueError: operands could not be broadcast together with shapes (1,5) (1,100)
'''