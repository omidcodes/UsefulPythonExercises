#Shallow copy and deep Copy

# importing copy module
import copy

# initializing list 1
li1 = [[1, 2, 3] , [[4,5], [6,7]] , [8,9]]

# using copy for shallow copy
li2 = copy.copy(li1)

# using deepcopy for deepcopy
li3 = copy.deepcopy(li1)

li4 = li1


li1[1][0].append(10)
li1[1][0][0]+= 1000
print('original list:' , li1)
print('Shallowcopy:' , li2)
print('DeepCopy:' , li3)
print(li4)

print(id(li1))
print(id(li2))
print(id(li3))
print(id(li4))