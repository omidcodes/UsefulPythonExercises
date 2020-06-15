import numpy as np

raw_data = [[1,2,3,2,1,1],
     [2,4,4,3,2,2],
     [5,5,5,5,4,4],
     [6,6,7,6,5,5]
     ]

a = np.array(raw_data)

result = all([np.all(a[i] < a[i+1], axis=0) for i in range(len(a)-1)])  # all is like AND
print(result)
