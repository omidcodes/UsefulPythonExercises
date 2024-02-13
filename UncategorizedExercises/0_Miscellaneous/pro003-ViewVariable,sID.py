x = [1,2,3]
y= x.copy()     #Copying
x.pop()
print(x)
print(y)

print(id(x))
print(id(y))