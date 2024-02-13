l = [1, 2, 3, 4, 5]
output = [item if item < 3 else 0 for item in l]
print(output)

import numpy as np

myarray = np.random.randint(100, size=(5, 5))
print('\n')
print(myarray)
myarray[myarray % 2 == 0] = 0  # Even ==> 0
myarray[myarray % 2 == 1] = 1  # Odd ==> 1
print(myarray)

arr = np.random.randint(20, size=(5, 5))
print(arr)
arr = np.where(arr % 2, 1, 0)
print(arr)
