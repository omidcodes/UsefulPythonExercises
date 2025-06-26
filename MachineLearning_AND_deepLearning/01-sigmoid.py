import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.linspace(-10 , 10 , 100)


y = sigmoid(x)


plt.plot(x,y)
plt.title("Sigmoid function")
plt.xlabel("x")
plt.ylabel("sigmoid(x)")
plt.grid(True)
plt.axhline(0.5, color="red" , linestyle="--", label='y=0.5')
plt.legend()
plt.show()

