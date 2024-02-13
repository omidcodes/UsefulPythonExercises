import random

import matplotlib.pyplot as plt
import numpy as np

x_list = []
y_list = []

color_choices = \
    ["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown", "gray", "cyan", "magenta"]

colors = []

length = 30

for i in range(length):
    for j in range(length):
        x_list.append(i)
        y_list.append(j)

        colors.append(random.choice(color_choices))

x = np.array(x_list)
y = np.array(y_list)
colors = np.array(colors)

plt.scatter(x, y, c=colors, linewidths=9)

plt.show()

# plt.savefig('/tmp/omidHashemzadeh.png', dpi=400)
