import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))
# Input values (example)
x = np.array([1.5, 2.0, 3.0])
# Layer 1 weights (3 hidden neurons, 3 inputs each)
W1 = np.array([
[0.2, 0.2, 0.2], # weights for h1
[0.4, 0.4, 0.4], # weights for h2
[0.6, 0.6, 0.6] # weights for h3
])
b1 = np.array([0.8, 0.8, 0.8]) # biases for hidden layer

# Layer 2 weights (output layer)
W2 = np.array([0.5, 0.5, 0.5]) # weights for output
b2 = 0.2 # output bias# Forward propagation
# Hidden layer
z2 = np.dot(W1, x) + b1
h2 = sigmoid(z2)
# Output layer
z3 = np.dot(W2, h2) + b2
output = sigmoid(z3)
print(f"Hidden layer outputs: {h2}")
print(f"Final output: {output:.4f}")