import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

y = sigmoid(x)

plt.plot(x, y, label="Sigmoid Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Sigmoid Activation Function")
plt.grid()
plt.legend()
plt.show()