# Pair Programming Week 4

# Coder: Gayatri
# Listener: Benjamin
# Sharer: Victoria

import numpy as np

# layer function
def layer(shape, actv):
    # This is the outer enclosing function

    def layer_inner(inputs, weights, bias):
        h = actv(np.dot(inputs, weights) + bias)
        # print("inside inner function")

        return h

    return layer_inner  # returns the nested function



########### TEST
# code to test our function
t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network

shape1 = [np.size(t),4]
shape2 = [4,1]


layer1 = layer(shape1, np.tanh) # Define layer 1
layer2 = layer(shape2, np.tanh) # Define layer 2

# Initialize weights and biases
w1 = np.random.uniform(-1,1, size = shape1)
w2 = np.random.uniform(-1,1, size = shape2)
b1 = 0.05
b2 = 0.08

# Run through the network
h1 = layer1(t, w1, b1) # First layer
h2 = layer2(h1, w2, b2) # Last layer

#print(h1)
#print(h2)
