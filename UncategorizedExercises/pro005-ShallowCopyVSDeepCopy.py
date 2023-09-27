# Shallow copy and deep Copy

# importing copy module
import copy

# initializing list 1
li1 = [[1, 2, 3], [[4, 5], [6, 7]], [8, 9]]

print(f'Original list: {li1}  \t  id= {id(li1)}')
# using copy for shallow copy
li2 = copy.copy(li1)

# using deepcopy for deepcopy
li3 = copy.deepcopy(li1)

li4 = li1

li1[1][0].append(10)
li1[1][0][0] += 1000

print(f'Shallowcopy: {li2}  \t  id= {id(li2)}')
print(f'DeepCopy: {li3}  \t  id= {id(li3)}')
print(f"list4=originallist: {li4}  \t  id= {id(li4)}")
